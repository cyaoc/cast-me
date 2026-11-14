#!/usr/bin/env python3
"""Remove PNG C2PA chunks, PNG XMP chunks, and the matching .c2pa sidecar."""

import argparse
import binascii
import os
import stat
import struct
import sys
import tempfile
from pathlib import Path


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
C2PA_CHUNK = b"caBX"
XMP_KEYWORD = b"XML:com.adobe.xmp"
TEXT_CHUNKS = {b"iTXt", b"tEXt", b"zTXt"}
KNOWN_CRITICAL_CHUNKS = {b"IHDR", b"PLTE", b"IDAT", b"IEND"}
MAX_CHUNK_LENGTH = (1 << 31) - 1
COPY_BUFFER_SIZE = 1024 * 1024


class PngError(ValueError):
    """The input is not a structurally valid PNG."""


def _read_exact(stream, size, description):
    data = stream.read(size)
    if len(data) != size:
        raise PngError(f"truncated PNG while reading {description}")
    return data


def _transfer_data(source, output, length, crc):
    remaining = length
    while remaining:
        data = _read_exact(
            source,
            min(remaining, COPY_BUFFER_SIZE),
            "chunk data",
        )
        crc = binascii.crc32(data, crc)
        if output is not None:
            output.write(data)
        remaining -= len(data)
    return crc


def _validate_ihdr(data):
    width, height, bit_depth, color_type, compression, filtering, interlace = (
        struct.unpack(">IIBBBBB", data)
    )
    valid_depths = {
        0: {1, 2, 4, 8, 16},
        2: {8, 16},
        3: {1, 2, 4, 8},
        4: {8, 16},
        6: {8, 16},
    }
    if not width or not height:
        raise PngError("PNG width and height must be non-zero")
    if bit_depth not in valid_depths.get(color_type, set()):
        raise PngError("invalid PNG color type or bit depth")
    if compression != 0 or filtering != 0 or interlace not in (0, 1):
        raise PngError("unsupported PNG IHDR method")
    return color_type


def _process_png(source, output=None):
    signature = _read_exact(source, len(PNG_SIGNATURE), "signature")
    if signature != PNG_SIGNATURE:
        raise PngError("invalid PNG signature")
    if output is not None:
        output.write(signature)

    chunk_index = 0
    seen_ihdr = False
    seen_plte = False
    seen_idat = False
    idat_closed = False
    color_type = None
    removed_c2pa = 0
    removed_xmp = 0

    while True:
        header = _read_exact(source, 8, "chunk header")
        length = struct.unpack(">I", header[:4])[0]
        kind = header[4:]

        if length > MAX_CHUNK_LENGTH:
            raise PngError(f"{kind!r} chunk exceeds the PNG length limit")
        if not all(65 <= byte <= 90 or 97 <= byte <= 122 for byte in kind):
            raise PngError(f"invalid PNG chunk type {kind!r}")
        if kind[2] & 0x20:
            raise PngError(f"reserved bit is set in PNG chunk type {kind!r}")
        if (kind[0] & 0x20) == 0 and kind not in KNOWN_CRITICAL_CHUNKS:
            raise PngError(f"unknown critical PNG chunk {kind!r}")
        if chunk_index == 0 and kind != b"IHDR":
            raise PngError("IHDR must be the first PNG chunk")
        if chunk_index > 0 and not seen_ihdr:
            raise PngError("PNG is missing IHDR")

        if kind == b"IHDR":
            if seen_ihdr or length != 13 or chunk_index != 0:
                raise PngError("PNG must contain one 13-byte initial IHDR")
            seen_ihdr = True
        elif kind == b"PLTE":
            if seen_plte or seen_idat or not length or length % 3 or length > 768:
                raise PngError("invalid PNG PLTE chunk")
            seen_plte = True
        elif kind == b"IDAT":
            if idat_closed:
                raise PngError("PNG IDAT chunks must be consecutive")
            if color_type == 3 and not seen_plte:
                raise PngError("indexed PNG is missing PLTE before IDAT")
            seen_idat = True
        elif seen_idat:
            idat_closed = True

        if kind == b"IEND":
            if length != 0 or not seen_idat:
                raise PngError("invalid PNG IEND chunk")
            if color_type == 3 and not seen_plte:
                raise PngError("indexed PNG is missing PLTE")
            if color_type in (0, 4) and seen_plte:
                raise PngError("greyscale PNG must not contain PLTE")

        crc = binascii.crc32(kind)
        copy_chunk = kind != C2PA_CHUNK
        prefix = b""

        if kind == b"IHDR":
            data = _read_exact(source, length, "IHDR data")
            crc = binascii.crc32(data, crc)
            color_type = _validate_ihdr(data)
            if output is not None:
                output.write(header)
                output.write(data)
        elif kind in TEXT_CHUNKS:
            keyword_bytes = bytearray()
            for _ in range(min(length, 80)):
                byte = _read_exact(source, 1, "text keyword")
                keyword_bytes += byte
                crc = binascii.crc32(byte, crc)
                if byte == b"\0":
                    break
            if not keyword_bytes or keyword_bytes[-1:] != b"\0":
                raise PngError(f"invalid {kind.decode()} keyword")
            keyword = bytes(keyword_bytes[:-1])
            if not 1 <= len(keyword) <= 79:
                raise PngError(f"invalid {kind.decode()} keyword length")
            prefix = bytes(keyword_bytes)
            if keyword == XMP_KEYWORD:
                copy_chunk = False
            if copy_chunk and output is not None:
                output.write(header)
                output.write(prefix)
            crc = _transfer_data(source, output if copy_chunk else None, length - len(prefix), crc)
        else:
            if copy_chunk and output is not None:
                output.write(header)
            crc = _transfer_data(source, output if copy_chunk else None, length, crc)

        stored_crc_bytes = _read_exact(source, 4, f"{kind!r} CRC")
        stored_crc = struct.unpack(">I", stored_crc_bytes)[0]
        if crc != stored_crc:
            raise PngError(f"CRC mismatch in {kind!r} chunk")
        if copy_chunk and output is not None:
            output.write(stored_crc_bytes)

        if kind == C2PA_CHUNK:
            removed_c2pa += 1
        elif kind in TEXT_CHUNKS and not copy_chunk:
            removed_xmp += 1

        chunk_index += 1
        if kind == b"IEND":
            if source.read(1):
                raise PngError("data follows PNG IEND")
            break

    return removed_c2pa, removed_xmp


def strip_png_c2pa(image_path):
    path = Path(image_path).expanduser().absolute()
    file_stat = path.lstat()
    if stat.S_ISLNK(file_stat.st_mode):
        raise OSError(f"refusing to replace symbolic link: {path}")
    if not stat.S_ISREG(file_stat.st_mode):
        raise OSError(f"not a regular file: {path}")
    if file_stat.st_nlink != 1:
        raise OSError(f"refusing to replace hard-linked file: {path}")
    if path.suffix.lower() == ".c2pa":
        raise OSError("input must be a PNG asset, not a .c2pa sidecar")

    temporary_path = None
    try:
        with path.open("rb") as source, tempfile.NamedTemporaryFile(
            mode="w+b",
            prefix=f".{path.name}.",
            suffix=".tmp",
            dir=str(path.parent),
            delete=False,
        ) as temporary:
            temporary_path = Path(temporary.name)
            os.fchmod(temporary.fileno(), stat.S_IMODE(file_stat.st_mode))
            removed_c2pa, removed_xmp = _process_png(source, temporary)
            temporary.flush()
            os.fsync(temporary.fileno())

        if removed_c2pa or removed_xmp:
            with temporary_path.open("rb") as cleaned:
                if _process_png(cleaned) != (0, 0):
                    raise PngError("post-write audit found remaining C2PA data")
            os.replace(str(temporary_path), str(path))
            temporary_path = None
            with path.open("rb") as cleaned:
                if _process_png(cleaned) != (0, 0):
                    raise PngError("post-replace audit found remaining C2PA data")
        else:
            temporary_path.unlink()
            temporary_path = None

        sidecar = path.with_suffix(".c2pa")
        try:
            sidecar.unlink()
            sidecar_removed = True
        except FileNotFoundError:
            sidecar_removed = False

        return removed_c2pa, removed_xmp, sidecar_removed
    finally:
        if temporary_path is not None:
            try:
                temporary_path.unlink()
            except FileNotFoundError:
                pass


def _scrub_and_report(path):
    try:
        removed_c2pa, removed_xmp, sidecar_removed = strip_png_c2pa(path)
    except (OSError, PngError) as error:
        print(f"{path}: {error}", file=sys.stderr)
        return False

    sidecar_status = "removed" if sidecar_removed else "absent"
    print(
        f"{path}: removed caBX={removed_c2pa}, XMP={removed_xmp}; "
        f"sidecar={sidecar_status}"
    )
    return True


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Remove PNG C2PA manifests, all PNG XMP, and the matching .c2pa sidecar.",
    )
    parser.add_argument("path", help="PNG file or directory to scrub in place")
    args = parser.parse_args(argv)
    target = Path(args.path).expanduser()

    if target.is_dir() and not target.is_symlink():
        try:
            images = sorted(
                path
                for path in target.rglob("*")
                if path.suffix.lower() == ".png"
                and not path.is_symlink()
                and path.is_file()
            )
        except OSError as error:
            print(f"{target}: {error}", file=sys.stderr)
            return 1

        succeeded = sum(_scrub_and_report(path) for path in images)
        failed = len(images) - succeeded
        print(
            f"{target}: processed={len(images)}, "
            f"succeeded={succeeded}, failed={failed}"
        )
        return int(bool(failed))

    return 0 if _scrub_and_report(target) else 1


if __name__ == "__main__":
    raise SystemExit(main())
