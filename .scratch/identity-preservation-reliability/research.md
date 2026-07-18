# Identity Preservation Reliability 可行性调研

调研日期：2026-07-18

## 结论

方案的方向正确，但按当前 PRD 原文，结论是 **部分可行、一个核心恢复路径在默认内置图片生成面上不可普遍保证**。

- GPT Image 2 支持图片输入、参考图生成、编辑、多图输入和高保真图片输入；OpenAI 也明确把它推荐给 identity-sensitive edits。因而“始终使用真实 Primary Identity Anchor、明确多图角色、重复不变量、局部修改”有正式能力依据。[GPT Image 2 model](https://developers.openai.com/api/docs/models/gpt-image-2) [Image generation guide](https://developers.openai.com/api/docs/guides/image-generation) [GPT Image 2 prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)
- OpenAI 同时明确说明，跨多次生成的角色一致性仍可能失败；视觉模型也可能描述错误，并不提供生物识别或确定性的身份判定。因此 Identity Review 只能是定性、最佳努力的视觉复核，不能升级成保证。[Image generation limitations](https://developers.openai.com/api/docs/guides/image-generation#limitations) [Vision limitations](https://developers.openai.com/api/docs/guides/images-vision#limitations)
- 用 Responses / Images API 实现时，调用方可以明确列出参考图片，并可用 `action: "generate"` 强制新生成，所以“排除失败图、只从 Primary Identity Anchor 与锁定 brief 重生成”在 API 编排中可落实。[Multi-turn image generation](https://developers.openai.com/api/docs/guides/image-generation#multi-turn-image-generation) [Create a new image using image references](https://developers.openai.com/api/docs/guides/image-generation#create-a-new-image-using-image-references)
- 纯 ChatGPT / Codex Skill 是可复用的工作流说明。官方文档说明它能规定步骤、资源和预期结果，但没有把 Skill 描述成底层工具调用的确定性控制器。[Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins)
- 当前默认内置图片工具可使用本地路径，或把最近若干会话图片一起带入；两种方式不能混用，也没有任意排除其中一张会话图片的选择器。当 Primary Identity Anchor 只有会话图片、而失败结果比它更新时，无法普遍做到“自动带入旧 Anchor，同时完全排除新失败图”。这与 PRD 的强制排除条款直接冲突。

因此，**不应直接按当前 `ready-for-agent` 状态实现**。先做一个最小产品选择即可，不需要新模块：

1. 保持纯 Skill 和默认内置图片工具：当 Anchor 不能被独立选中时，复用现有 reattachment 行为，请用户只重新附上 Primary Identity Anchor；保留所有锁，但该分支不再声称是全自动恢复。
2. 若“一次无人工介入的自动重生成”不可退让，则必须把可明确控制输入列表与 `action` 的 API 编排纳入范围；这与 PRD 当前“无 API integration / wrapper”边界冲突。

最小且符合当前 repo 方向的是方案 1。

## 能力与 PRD 条款对照

| PRD 能力 | GPT Image 2 / API | 纯 ChatGPT / Codex Skill | 判断 |
| --- | --- | --- | --- |
| 后续推荐继承锁与已知身份风险 | 不依赖模型参数 | Skill 可规定决策流程 | 可行 |
| 生成前做定性的组合风险检查 | 不依赖模型参数 | Skill 可按 Reference Coverage 与 Protected Identity Cues 检查 | 可行，但属于模型判断，不是硬保证 |
| 每次生成都传入真实 Primary Identity Anchor | API 可显式提供图片 | 只有当前工具能实际取得并选择该图片时成立 | 条件可行；不可用时必须 reattach |
| 多图按身份、角度、服装、风格分工 | API 支持一张或多张参考图 | 官方建议按顺序标识并说明关系 | 可行 [ChatGPT image generation](https://learn.chatgpt.com/docs/image-generation#use-multiple-reference-images) |
| 局部缺陷用“结果图 + Anchor”做手术式编辑 | API 支持多图编辑 | 当前两张图都可作为实际输入时成立 | 条件可行 |
| 身份整体漂移时排除失败图并重新生成 | API 可显式选择输入并强制 `generate` | Anchor 仅在较早会话上下文时，当前内置工具不能普遍独立选择它 | **按当前默认面不可普遍实现** |
| 自动检查结果并只重试一次 | API 编排可控制 | Skill 可要求代理执行，但依赖结果可见、视觉复核可靠、输入可选和工具仍可调用 | 条件可行，不是平台保证 |
| Identity Review 区分局部缺陷与整体漂移 | 视觉模型可看图 | 可作为结构化定性复核 | 可行但不确定；必须允许 unavailable / ambiguous |
| 不使用分数、名单、角色或姿势硬编码 | 不需要额外能力 | 复用现有领域语义即可 | 可行且正确 |
| 最多一次恢复，仍失败就停止 | 不需要新模型能力 | Skill 可规定停止与诚实报告 | 可行 |

## 官方依据

### 1. 模型支持身份敏感的参考图和编辑工作流，但不保证一致性

GPT Image 2 接收文本和图片，输出图片，并支持 generation、editing 与高保真图片输入。当前 API 文档还说明，GPT Image 2 会自动以高保真方式处理所有图片输入，不需要也不能设置 `input_fidelity`。[GPT Image 2 model](https://developers.openai.com/api/docs/models/gpt-image-2) [Image input fidelity](https://developers.openai.com/api/docs/guides/image-generation#image-input-fidelity)

OpenAI 的 GPT Image 2 prompting guide 把 identity-sensitive edits 列为推荐用途，并建议：

- 明确写出哪些内容改变、哪些必须保持；
- 每一轮重复 preserve list；
- 多张图片按序号和角色说明；
- 用小而单一的后续修改减少漂移。

这些做法直接支持 PRD 的 Primary Identity Anchor、多图角色、锁继承和手术式修改。[GPT Image 2 prompting fundamentals](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide#2-prompting-fundamentals)

但 API 文档仍把 recurring characters 的视觉一致性列为已知限制。因此“改进身份可靠性”可行，“保证像本人”不可行；PRD 的 best-effort 与 no identity guarantee 边界是正确的。[Image generation limitations](https://developers.openai.com/api/docs/guides/image-generation#limitations)

### 2. API 可以真正控制“编辑”与“重新生成”

Responses API 支持把图片输入和输出留在多轮上下文中，并提供 `action`：`auto`、`generate`、`edit`。调用方还可以通过 URL、Base64 或 file ID 明确提供一张或多张参考图。[Multi-turn image generation](https://developers.openai.com/api/docs/guides/image-generation#multi-turn-image-generation) [Reference image inputs](https://developers.openai.com/api/docs/guides/image-generation#create-a-new-image-using-image-references)

所以在 API 编排中，以下调用语义是可实现并可测试的：

```text
action = generate
image inputs = [Primary Identity Anchor, required supporting references]
excluded inputs = [failed generated result]
prompt = locked production brief + repeated identity invariants
```

这不是模型保证，但输入形状和生成/编辑模式可以由调用方确定。

### 3. ChatGPT 支持参考图片和多图角色，但公开 Skill 契约没有同等底层控制承诺

ChatGPT 官方文档要求在编辑或视觉引导时附上参考图片；多图时要标识每张图片并说明关系。它也建议每次只改一个元素，并明确什么改变、什么保持。[ChatGPT image generation](https://learn.chatgpt.com/docs/image-generation) [Image inputs](https://learn.chatgpt.com/docs/image-inputs)

但 Skills 文档只承诺可复用的任务说明、资源和流程一致性，并要求通过实际测试持续修正漂移。它没有承诺 Skill 能强制选择底层图片集合、排除某张上下文图片、指定 `action`，或总能在交付前自主完成视觉复核和第二次生成。[Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins)

当前本地 imagegen 说明也把默认编辑对象限定为会话中已经可见的图片，并明确内置工具不承诺任意文件路径控制。它支持“看得见并可用”的工作流，却不能替 PRD 证明任意输入选择。[Local imagegen skill](/Users/cyao/.codex/skills/.system/imagegen/SKILL.md)

### 4. Identity Review 只能是最佳努力的视觉判断

官方视觉文档说明，模型可能在空间定位、图片旋转、细节缩放和描述准确性上出错。因此 PRD 使用 Protected Identity Cues、角度一致的面部平面和修复范围做定性判断是合理的，但测试不能把模型自己的判断当作身份真值。[Vision limitations](https://developers.openai.com/api/docs/guides/images-vision#limitations)

应保留以下边界：

- 看不到结果或分辨率不足时，review 为 unavailable / unverified；
- 局部与整体漂移不使用固定错误数、相似度或生物识别阈值；
- ambiguous 时不自动重试；
- 复核通过表示工作流未发现明确失败，不表示身份验证成功。

## PRD 中需要收紧的三处

不需要重写方案，只需给三条绝对语句加同一个执行面前提。

### 1. “每次传入真实 Anchor”

当前写法可以保留为目标合同，但 acceptance test 应要求可观察证据：只有工具调用确实能取得并选择 Anchor 时才继续；否则走现有 focused reattachment，不能只靠提示词声称已经传入。

### 2. “排除失败图并自动重生成”

改为：只有 active generation surface 能独立选择 Primary Identity Anchor、明确排除失败结果，并发起新 generation 时，才执行自动恢复。否则保留 brief 与全部锁，要求重新附上 Anchor，然后再生成。不要把失败图降格成“仅构图参考”作为默认补丁，因为这仍会把失败人脸留在模型输入中，违背本需求的根因判断。

### 3. “自动 Identity Review 后只重试一次”

保留一次上限，但增加 `capability available and verifiable` 前提。Golden conversations 可以稳定测试路由、prompt 义务、停止语义和诚实报告；它们不能证明某次生成真的保持了本人身份。实际图像质量需要单独的人类/视觉 eval 样本，而不是把语义对话测试当成像素级保证。

## 最小修改建议

只在 PRD 的 Implementation Decisions 和 Testing Decisions 各补一条，不建新模块、不引入参数表：

```text
Surface capability boundary: claim actual-image inclusion, failed-result exclusion,
or automatic regeneration only when the active generation surface exposes and
executes that control. If the Primary Identity Anchor cannot be independently
selected, preserve all locks and route only to the existing focused reattachment
behavior; do not substitute text or claim an automatic correction.
```

测试相应分成两条：

1. 可独立选择 Anchor 的调用面：断言实际输入包含 Anchor、排除失败图，并且只发起一次新 generation。
2. 不可独立选择 Anchor 的调用面：断言保留全部锁、只要求重附 Anchor、不把失败图带入、不声称已自动恢复。

## 最终判断

- **模型与提示策略：可行。**
- **API 编排版本：完整可行，但身份效果仍是 best effort。**
- **当前纯 Skill + 默认内置图片工具版本：预防、局部修复、定性复核和有界停止可行；“Anchor-only 且排除失败图的全自动重生成”不可普遍实现。**
- **PRD：需要一个很小的 surface-capability boundary 后再进入实现。**

这不是要 hard-code 特定人物、角色或失败模式；相反，它把唯一的分支放在当前工具是否真的具备所需输入控制上。
