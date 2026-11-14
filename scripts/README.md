# 终端脚本

`cast_me.py` 通过本机的 Codex CLI 运行 CastMe skill。skill 的提问在终端里回答，成图保存到本仓库的 `output/` 目录，并去掉 C2PA 元数据。不需要往 Codex 里安装 skill。

## 环境要求

- [Codex CLI](https://github.com/openai/codex)，已用 ChatGPT 账号登录。出图用的是 Codex 内置的图像工具，不需要 `OPENAI_API_KEY`。测试版本为 codex-cli 0.167.2。
- Python 3.9 及以上，无第三方依赖。

## 用法

用一张或多张人物照片加一句需求，开始新会话：

```bash
scripts/cast_me.py photo.jpg "做一张社交头像"
```

Codex 会按 skill 的流程一次问一个问题，在 `>` 后输入回答即可，比如 `A` 或 `A＋采用推荐默认值`。直接回车或输入 `q` 暂停会话。

在任意目录下继续最近用过的会话：

```bash
scripts/cast_me.py
```

改完后清理会话：

```bash
scripts/cast_me.py --forget                    # 最近用过的会话
scripts/cast_me.py --forget 20261114-140847    # 指定会话：output/ 下的目录名，或完整路径
scripts/cast_me.py --forget --all              # output/ 下的所有会话
```

会话名就是 `output/` 下的目录名，用 `ls output/` 查看。

想回到更早的某个会话，传它的目录。之后它就成了「最近用过的」，再运行不用加参数：

```bash
scripts/cast_me.py --out output/20261114-140847
```

新会话也可以加 `--out DIR`，把会话放在指定目录。

## 模型

脚本固定用 `gpt-6.1-sol`、推理强度 `high` 主持会话，不跟随 `~/.codex/config.toml` 的全局设置。出图由 Codex 内置的图像工具完成，不受这个设置影响。

长期更换：改 `cast_me.py` 顶部的 `MODEL` 和 `REASONING_EFFORT`。临时更换：加 `--model` / `--effort`，只对这一次运行有效，继续会话时不加就回到默认值：

```bash
scripts/cast_me.py --model gpt-6-astra --effort xhigh
```

## 会话目录

每个会话在 `output/` 下有自己的目录，会话需要的文件都在里面：

```text
output/20261114-140847/
├── .cast-me-session   Codex 会话 id，目录靠它找到自己的会话
├── input-1.jpg        传入照片的副本
└── exec-….png         生成的图，已去掉 C2PA 和 XMP
```

会话开始后，原始照片可以随意移动或删除，因为 Codex 用的是目录里的副本。整个仓库也可以搬位置，因为每一轮都会告诉 Codex 会话目录现在在哪。

`output/` 已加入 `.gitignore`。里面是个人照片，不能提交。

## 隐私与清理

Codex 会在 `~/.codex/sessions/` 里保存每个会话的记录，其中有你的照片，以及每张生成图未去 C2PA 的原版。还在修改时不要清理：对话就存在这份记录里，继续会话要靠它。

`--forget` 一次清理一个会话：默认是最近用过的那个，也可以跟会话名指定。它会：

- 通过 `codex delete` 删除 Codex 为这个会话保存的全部数据，包括会话记录和 Codex 数据库里的相关内容；
- 删除目录里的照片副本 `input-N`；
- 删除 `.cast-me-session`。之后这个会话就无法继续了。

生成的图会保留。其他会话不受影响。注意：不带会话名再运行一次 `--forget`，会清理下一个最近用过的会话。

`--forget --all` 对 `output/` 下的每个会话做同样的清理。动手前会先检查所有目录的会话记录，只要有一份不对就一个都不删。某个会话删除失败时，它会原样保留，其他会话照常清理，最后以非零状态退出。用 `--out` 放在 `output/` 以外的会话不在 `--all` 范围内，需要用 `--forget <完整路径>` 单独清理。

这些会话关闭了 Codex 的长期记忆，照片内容不会进入 `~/.codex/memories`。

## 工作原理

- **加载 skill**：会话开始时，脚本把 `skills/cast-me/SKILL.md` 作为开发者指令传给 Codex，并告诉它 `references/` 的位置。`references/` 的修改立即生效；`SKILL.md` 的修改只对新会话生效，因为 Codex 把指令存在会话里。
- **隔离**：每一轮都会带上以下 Codex 设置：关闭已安装 skill 列表，不读项目里的 `AGENTS.md`，关闭记忆，沙盒只读。全局的 `~/.codex/AGENTS.md` 仍会加载，Codex 没有提供关闭它的开关。
- **图片**：Codex 固定把生成的图存到 `~/.codex/generated_images/<会话 id>/`，这个位置无法配置。每一轮结束后，脚本把新的 PNG 移到会话目录，再用 `strip_png_c2pa.py` 处理。

## 限制

- 会话不能跨电脑。对话记录在本机的 `~/.codex` 里，把 `output/` 拷到别的电脑，图还在，但会话接不上。
- 继续会话时不会重新显示上一个问题。输入「继续」之类的话，Codex 会再问一遍。
- 只能在新会话开始时传入照片。

## strip_png_c2pa.py

从 PNG 中删除 C2PA 清单（`caBX` 数据块）、全部 XMP，以及同名的 `.c2pa` 附属文件。会先校验 PNG 结构，再原地改写文件。也可以单独使用：

```bash
python3 scripts/strip_png_c2pa.py image.png
python3 scripts/strip_png_c2pa.py some/folder   # 递归处理目录里的所有 PNG
```
