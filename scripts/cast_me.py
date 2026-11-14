#!/usr/bin/env python3
"""Run the cast-me skill through Codex CLI and answer its questions in the terminal.

Usage:
  scripts/cast_me.py IMAGE [IMAGE ...] "request"   start a session in output/<time>/ of this repo
  scripts/cast_me.py                               continue the most recently used session
  scripts/cast_me.py --forget [SESSION]            delete a session's Codex records and input copies
                                                   (SESSION: folder name under output/; default: most recent)
  scripts/cast_me.py --forget --all                the same for every session under output/
Add `--out DIR` to start or continue a session in a specific directory instead.

Each session directory is self-contained: the input photos are copied in as input-N,
results land beside them, and DIR/.cast-me-session holds the Codex session id.
SKILL.md is read when a session starts; references/ is read live.
An empty answer or `q` pauses the session. Generated PNGs are moved out of
$CODEX_HOME/generated_images into DIR and stripped of C2PA/XMP.
"""

import argparse
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from strip_png_c2pa import PngError, strip_png_c2pa

SKILL_DIR = Path(__file__).resolve().parent.parent / "skills" / "cast-me"
CODEX_HOME = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
DEFAULT_ROOT = Path(__file__).resolve().parent.parent / "output"
SESSION_FILE = ".cast-me-session"
SESSION_ID = re.compile(r"[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}")
# Repeated on every turn because these settings are not stored with the session.
CONFIG = [
    "-c", "skills.include_instructions=false",  # keep installed skills out of the run
    "-c", "project_doc_max_bytes=0",  # keep project AGENTS.md files out of the run
    "-c", "memories.use_memories=false",
    "-c", "memories.generate_memories=false",  # photos must not leak into long-term memory
    "-c", 'sandbox_mode="read-only"',
]
MOVED_NOTE = (
    "\n\n[host] This session's files are in {out}/ with unchanged filenames: the input photos "
    "(input-N) and every generated image. Reference them there, not at older paths "
    "or under $CODEX_HOME/generated_images."
)


def instructions():
    return (
        f"You are running the cast-me skill below. Its root is {SKILL_DIR}; "
        "resolve every `references/...` path against it.\n"
        "The user answers in a terminal between turns. Generate with the built-in image_gen tool "
        "and leave the files where it saves them; the host collects them.\n\n"
        + (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    )


def turn(cmd, record=None):
    """Run one codex turn, print its messages, and return its thread id.

    `record` gets the thread id as soon as codex reports it, so an interrupted
    first turn still leaves a session that --forget can delete.
    """
    print("... codex is working", file=sys.stderr, flush=True)
    thread_id = None
    # codex appends piped stdin to the prompt; the user's terminal input belongs to this script
    with tempfile.TemporaryFile("w+") as errors:
        proc = subprocess.Popen(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                stderr=errors, text=True)
        for line in proc.stdout:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            kind = event.get("type")
            if kind == "thread.started":
                thread_id = event["thread_id"]
                if record:
                    record.write_text(thread_id + "\n")
            elif kind == "item.completed" and event["item"].get("type") == "agent_message":
                print(event["item"]["text"] + "\n", flush=True)
            elif kind in ("turn.failed", "error"):
                print(json.dumps(event, ensure_ascii=False), file=sys.stderr)
        if proc.wait():
            errors.seek(0)
            print(f"codex exited {proc.returncode}:\n{errors.read()[-2000:]}", file=sys.stderr)
    return thread_id


def collect(thread_id, out):
    folder = CODEX_HOME / "generated_images" / thread_id
    for src in sorted(folder.glob("*.png")):
        dst = out / src.name
        shutil.move(src, dst)
        try:
            strip_png_c2pa(dst)
            print(f"saved {dst}", flush=True)
        except (OSError, PngError) as error:  # keep the image; only the scrub failed
            print(f"saved {dst} but C2PA removal failed: {error}", file=sys.stderr)
    try:
        folder.rmdir()
    except OSError:
        pass


def session_id(out):
    record = out / SESSION_FILE
    if not record.is_file():
        return None
    thread_id = record.read_text().strip()
    if not SESSION_ID.fullmatch(thread_id):  # the id becomes part of a deleted path
        sys.exit(f"{record} does not hold a session id")
    return thread_id


def forget(thread_id, out):
    """Delete the session's Codex records and input photo copies; keep generated images."""
    proc = subprocess.run(["codex", "delete", "--force", thread_id],
                          stdin=subprocess.DEVNULL, capture_output=True, text=True)
    if proc.returncode:
        print(f"{out}: codex delete failed, session kept:\n{proc.stderr[-2000:]}", file=sys.stderr)
        return False
    shutil.rmtree(CODEX_HOME / "generated_images" / thread_id, ignore_errors=True)
    for photo in out.glob("input-[0-9]*"):
        photo.unlink()
    (out / SESSION_FILE).unlink()
    print(f"cleaned {out}: Codex records and input photos deleted, generated images kept")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Run cast-me through Codex CLI.",
        usage="%(prog)s [--out DIR] [IMAGE ... REQUEST] | --forget [SESSION | --all]",
    )
    parser.add_argument("--out", type=Path,
                        help=f"session directory (default: new or most recent under {DEFAULT_ROOT})")
    parser.add_argument("--forget", nargs="?", const="", metavar="SESSION",
                        help="delete a session's Codex records and input photo copies; SESSION is "
                             "a folder name under output/ or a path (default: most recent)")
    parser.add_argument("--all", action="store_true",
                        help=f"with --forget: every session under {DEFAULT_ROOT}")
    parser.add_argument("inputs", nargs="*", help="person image(s) then the request")
    args = parser.parse_args()
    forgetting = args.forget is not None
    if args.all:
        if args.forget != "" or args.out or args.inputs:
            parser.error("--all only goes with a bare --forget")
        # read every id first so one bad record stops the run before anything is deleted
        sessions = [(out, session_id(out)) for out in
                    sorted(record.parent for record in DEFAULT_ROOT.glob(f"*/{SESSION_FILE}"))]
        if not sessions:
            parser.error(f"no session under {DEFAULT_ROOT}")
        results = [forget(thread_id, out) for out, thread_id in sessions]
        sys.exit(0 if all(results) else 1)
    if args.forget and args.out:
        parser.error("name the session either with --forget SESSION or with --out, not both")
    if args.forget:
        named = Path(args.forget).expanduser()
        out = (named if named.is_dir() else DEFAULT_ROOT / args.forget).resolve()
    elif args.out:
        out = args.out.expanduser().resolve()
    elif args.inputs and not forgetting:
        out = DEFAULT_ROOT / time.strftime("%Y%m%d-%H%M%S")
    else:
        # most recently used: continuing a session touches its record
        records = DEFAULT_ROOT.glob(f"*/{SESSION_FILE}")
        latest = max(records, key=lambda path: path.stat().st_mtime, default=None)
        if not latest:
            parser.error(f"no session under {DEFAULT_ROOT}; start one with IMAGE ... REQUEST")
        out = latest.parent
    record = out / SESSION_FILE

    thread_id = session_id(out)
    if forgetting:
        if not thread_id:
            parser.error(f"no session recorded in {out}")
        sys.exit(0 if forget(thread_id, out) else 1)

    if thread_id:
        if args.inputs:
            parser.error(f"{out} already has a session: run with only --out to continue it, "
                         "or --forget it first")
        record.touch()
        print(f"continuing session in {out}", file=sys.stderr)
    else:
        if len(args.inputs) < 2:
            parser.error("a new session needs IMAGE ... REQUEST")
        *images, request = args.inputs
        images = [Path(image) for image in images]
        for image in images:
            if not image.is_file():
                parser.error(f"not a file: {image}")
        out.mkdir(parents=True, exist_ok=True)
        copies = [out / f"input-{n}{image.suffix.lower()}" for n, image in enumerate(images, 1)]
        for image, copy in zip(images, copies):
            shutil.copy2(image, copy)
        image_args = [arg for copy in copies for arg in ("-i", str(copy))]
        thread_id = turn([
            "codex", "exec", "--json", "--skip-git-repo-check", "-C", str(out),
            # json.dumps output is a valid TOML basic string
            "-c", "developer_instructions=" + json.dumps(instructions(), ensure_ascii=False),
            *CONFIG, *image_args, "--", request,
        ], record)
        if not thread_id:
            sys.exit("codex did not start a session")

    while True:
        collect(thread_id, out)
        try:
            answer = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if answer in ("", "q"):
            break
        turn(["codex", "exec", "resume", "--json", "--skip-git-repo-check", *CONFIG,
              "--", thread_id, answer + MOVED_NOTE.format(out=out)])
    resume = sys.argv[0] if out.parent == DEFAULT_ROOT else f"{sys.argv[0]} --out {shlex.quote(str(out))}"
    print(f"\nsession paused, images in {out}\ncontinue with: {resume}", file=sys.stderr)


if __name__ == "__main__":
    main()
