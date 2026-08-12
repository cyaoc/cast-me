# CastMe 架构、职责与端到端流程地图

> 文档类型：当前架构（As-Is）与优化导航（To-Be Compass）
> 基线：`feat/anime-adaptation` 分支，2026-08-12
> 阅读顺序：系统与模块 → 总流程 → 端到端场景 → 路由参考 → Golden 覆盖 → 优化方向

## 0. 系统本质

CastMe 不是传统应用，没有仓库内的常驻服务、数据库或图像生成代码。它是一个声明式 Agent Skill：宿主读取 Markdown 合约，在当前对话中维护决策状态，再通过宿主提供的图像生成或编辑能力调用 GPT Image 2。

因此：

- Module 是一组有明确职责与 Interface 的行为合约。
- 稳定的 Markdown 标题是 Interface 所在的 Seam。
- ChatGPT、Codex 或其他 API 宿主提供真正执行图像能力的 Adapter。
- 只有 `skills/cast-me/` 会作为运行时包安装；仓库其他文件用于说明、治理和验证。

```mermaid
flowchart LR
    U["用户<br/>人物参考图 + 目标"] --> H["宿主<br/>ChatGPT / Codex / API 宿主"]

    subgraph PKG["运行时包：skills/cast-me"]
        META["agents/openai.yaml<br/>发现与默认入口"]
        K["SKILL.md<br/>协调、路由、状态、生命周期"]
        I["Identity Anchor<br/>身份、证据与固定根"]
        C["Composition Director<br/>方向、镜头、Character Sheet 与提示词"]
        S["Styling & Performance<br/>造型与表演"]
        R["Scoped Option Refresh<br/>局部刷新与新鲜度"]
        META --> K
        K --> I
        K --> C
        K --> S
        K --> R
    end

    H --> META
    K --> G["宿主图像 Adapter<br/>GPT Image 2"]
    G --> O["可见结果"]
    O --> K
    K --> F["最终结果或明确的未完成说明"]
    W["外部视觉资料<br/>仅趋势或特定角色、制服、历史服装分支"] -.条件触发.-> K
```

### 仓库层次与信息源职责

| 层次 | 文件 | 职责 | 是否运行时自动读取 |
| --- | --- | --- | --- |
| 安装入口 | `skills/cast-me/agents/openai.yaml` | 展示名、默认提示、隐式调用元数据 | 是 |
| 协调 Module | `skills/cast-me/SKILL.md` | 路由、Choice Gate、决策状态、四阶段生命周期、完成条件 | 是 |
| 所有者 Module | `skills/cast-me/references/*.md` | 身份、构图、造型表演、局部刷新领域知识 | 按需 |
| 用户说明 | `README.md` | 安装、调用和用户示例 | 否 |
| 规范术语 | `CONTEXT.md` | 唯一领域词汇表 | 否 |
| 架构决定 | `docs/adr/*.md` | 已接受的模块边界和取舍 | 否 |
| 规格与研究 | `.scratch/*` | PRD、研究、实施计划 | 否 |
| 行为验证 | `evals/golden-conversations.md` | 可观察行为回归合约 | 否 |
| 贡献约束 | `AGENTS.md`、`docs/agents/*.md` | 修改、Issue、术语与 Triage 规则 | 否 |

运行时、规范术语、ADR、Golden 或 README 相互矛盾时，应把它视为文档或实现漂移并显式修复，不能用简单的文件优先级掩盖冲突。

安装路径只有入口不同：ChatGPT 本地上传 `skills/cast-me` 后通过自动匹配或 `@CastMe` 调用；Codex 安装同一目录后在新会话中用 `$cast-me`。两者进入同一套运行时合约。

## 1. Module、Interface 与职责

```mermaid
flowchart TB
    K["协调 Module：SKILL.md"]

    subgraph ID["Identity Anchor"]
        I1["Primary Identity Anchor<br/>Character Sheet 角色边界"]
        I2["Reference Transfer / Coverage"]
        I3["Deformation Tier → Medium Contract<br/>Protected Identity Cue / Visible Body Evidence"]
        I4["Identity Review / Fixed-root Recovery"]
    end

    subgraph COMP["Composition Director"]
        C1["Creative Direction / First Read"]
        C2["Shot / Perspective / Camera"]
        C3["Final-Asset Quality / First-Pass Finish"]
        C4["Layout / Text / Prompt Structure"]
    end

    subgraph STYLE["Styling & Performance"]
        S1["Styling Direction / Character Read"]
        S2["妆发、服装、配饰、道具"]
        S3["动作、表情、视线、手部、姿态几何"]
        S4["角色、制服、历史服装研究"]
    end

    subgraph REFRESH["Scoped Option Refresh"]
        R1["目标路由"]
        R2["分区历史与 Fresh Option"]
        R3["Delegated Refresh / Exhaustion"]
    end

    K --> I1
    K --> C1
    K --> S1
    K --> R1
    C2 -.身份证据约束.-> I2
    S1 -.身份与身体证据约束.-> I3
    C1 -.造型与表演内容.-> S1
    R1 -.调用目标区域可见签名.-> C1
    R1 -.调用目标区域可见签名.-> S1
```

### Module Interface 一览

| Module | Interface 输入 | 拥有 | 明确不拥有 | 输出 |
| --- | --- | --- | --- | --- |
| `SKILL.md` | 用户请求、参考图、对话状态、宿主能力 | 路由、Gate 格式、状态、生命周期、安全异常、完成条件 | 各视觉领域的具体生产知识 | 下一道问题、生产提示词、调用或停止说明 |
| `identity-anchor.md` | 人物图、已锁媒介、显式 Deformation Tier/Custom、目标角度/身体/动作、可见结果 | 身份锚、证据、Deformation Tier、Medium Contract、Character Sheet 角色、Coverage、Inference Boundary、Identity Review 与固定根恢复 | 具体镜头、造型、表演选项 | 变形 Gate、身份约束、媒介通道记录、身体证据梯度、风险 Gate、实际输入与恢复路径 |
| `composition-director.md` | 用途、方向、画布、镜头、成片要求 | First Read、方向、镜头、透视、成片质量、Character Sheet 设计锁、Finish、布局、文字、提示词结构 | 妆发服装与表演内容 | 构图与成片贡献、输出合约、提示词骨架 |
| `styling-performance.md` | 角色/故事、妆发服装、道具、动作 | Styling Direction、Character Read、Story Makeup、Look Continuity、表演、姿态、视觉研究 | 裁切、相机位置、背景空间、身份证据本身 | 造型表演贡献、研究锚点、姿态链 |
| `scoped-option-refresh.md` | 更多、换一批、换某项、你决定 | 刷新目标、最近 Gate、分区历史、新鲜度、委派、耗尽 | 目标区域的具体候选内容 | 新批次、内部选项或重开一个限制锁的 Gate |
| 宿主图像 Adapter | 提示词、实际图像、可用控制 | 执行生成或编辑 | CastMe 领域决策与完成判断 | 图像及可验证的能力、尺寸信息 |

### 刻意不拆出的职责

| 关注点 | 当前归属 | 约束 |
| --- | --- | --- |
| 妆容 | `Styling Direction` | 不增加 Makeup Gate 或独立化妆 Module |
| 润饰和成片 | `First-Pass Finish` | 第一次生成时完成，不建立强制后处理流程 |
| 安全 | `SKILL.md` 异常分支 | 不是普通创意维度 |
| Physical Scene Coherence | Composition 内部检查 | 不是新的用户 Gate |
| Medium Contract | Identity Anchor + 既有非摄影 Output Recipe | 不增加问题、Gate、Module、流程阶段或运行时组件 |
| Deformation Tier | Identity Anchor + 既有 Choice Gate | A/B/C 语义顺序固定、具体比例按用途适配；身体证据梯度属于该 Tier，不增加独立身体 Gate、Module 或持久比例档案 |
| Character Sheet | Identity Anchor 的实际输入/固定根规则 + Composition 的设计与应用提示词 | 是普通锁定产物，不增加 Module、Agent、Gate 或持久角色库；无连续性要求的单张绘图不使用 |
| Identity Review | Identity Anchor | 身份通过与恢复分类由同一所有者判断 |
| Look Continuity | Styling，仅系列任务 | 单张图不创建连续性状态 |
| 质量与尺寸 | Composition + 宿主事实 | 不添加质量问卷，不声称不可验证的控制 |

这些边界对应现有 ADR：身份优先于未确认的故事变换；妆容留在 Styling；风险由 Protected Identity Cue 是否被替换或遮挡触发；Character Read 是创意意图；Story Makeup 必须穿过 Finish；优先加深现有 Styling 和 Identity Module；身份约束通过已锁媒介与显式 Deformation Tier 的 Medium Contract 解析；复用绘制角色先生成一个锁定 Character Sheet，再让应用从 Sheet 与 Anchor 独立分支。

## 2. 共享决策状态与用户 Interface

所有 Module 共用当前对话中的决策状态。它不是数据库，也不承诺跨会话历史。

```mermaid
flowchart LR
    INPUT["输入<br/>人物图、目标、约束、用户回答"] --> STATE["Conversation Decision State"]

    STATE --- E["locked: explicit<br/>用户直接指定、选择或覆盖"]
    STATE --- D["locked: derived<br/>选项前提或已接受默认"]
    STATE --- S["suggested<br/>预览过但尚未采用"]
    STATE --- U["unresolved<br/>仍缺且影响生产"]
    STATE --- RISK["已接受风险<br/>只覆盖已命名范围"]
    STATE --- COVER["Reference Coverage<br/>verified / described / inferred / missing"]
    STATE --- TIER["Deformation Tier<br/>conservative / standard / strong / Custom<br/>选择或显式委派 + 用途适配比例"]
    STATE --- MEDIUM["Medium Contract<br/>每个 cue = open / transferred / closed"]
    STATE --- ROOT["Fixed root<br/>Anchor + 必需参考 + 锁定产物"]
    STATE --- HIST["分区 Shown Option<br/>最近 refreshable Gate"]

    STATE --> ROUTE["选择下一位所有者"]
    STATE --> PROMPT["生成完整提示词"]
    STATE --> REVIEW["审查和恢复继承全部有效决定"]
    TIER --> MEDIUM
```

### 状态变化规则

| 当前状态 | 事件 | 新状态 |
| --- | --- | --- |
| `unresolved` | 用户直接指定或选择当前维度 | `locked: explicit` |
| `suggested` | 已选选项把它作为明确前提，或用户接受推荐默认 | `locked: derived` |
| `suggested` / `derived` | 用户重复、细化或覆盖 | `locked: explicit` |
| `derived` | Scoped Refresh 命中其所属区域 | `unresolved` |
| `explicit` | 用户明确重开该字段 | `unresolved` |
| 已锁摄影媒介 | Creative Direction 锁定 | 按既有 photographic default 解析一次请求级 Medium Contract，不需要 Deformation Tier |
| 已锁绘制媒介、Deformation Tier 未解决 | 进入下一项普通选择 | 显示 A `conservative` / B `standard` / C `strong` / D Custom 的本地化 Gate；每项给出按用途适配的具体比例与可见后果 |
| 已锁媒介 + 已选择/显式委派 Tier 或具体 Custom 变形 | 当前选择完成 | 解析并记录一次请求级 Medium Contract 与身体证据梯度 |
| 已有 Medium Contract | Style / Scoped Refresh 明确重开媒介或 Deformation Tier | 重新解析；只有 closed 集合改变才再次披露 |
| 可复用绘制角色或同一绘制角色至少两张图 | 生成前 | 先从 Anchor 生成并锁定一个 Character Sheet；每个应用的固定根加入该 Sheet |

`locked: explicit` 始终优先于冲突的非显式值。Medium Contract 只读取已锁媒介与用户显式选择的 Deformation Tier 或具体 Custom 变形；`anime`、`chibi`、风格名、Anchor、结果、灯光、构图、遮挡、分辨率和其他场景条件都不参与推断。等比例保留可表达结构 cue 与身体证据，中间比例简化身体证据，次短比例可明确携带胸/腰/臀曲线并披露更成熟观感，最短比例在生成前披露无法携带源图身形。接受某个风险只覆盖已命名的 cue、遮挡、角度、变换、缺失证据或 Medium Contract 关闭的通道，不是全局免责。

### Choice Gate 合约

每个用户可见 Gate 都使用同一个 Interface：

1. 本地化推荐句和一个简短理由。
2. A/B/C 三个当前范围内有效的具体方案；只有两个实质方案时，C 表示保持现状并停止。
3. 永久存在的 `D) Custom`，只允许在当前 Gate 范围内自定义。
4. 回复示例同时展示裸推荐项，以及推荐项加本地化 `use recommended defaults`。

D 占位符本身不创建锁或历史；具体 Custom 答案才由当前 Gate 校验。裸字母只解决当前选项拥有的字段。全局 `you decide` 结束普通澄清，但不会绕过 Reference Coverage、身份风险、安全或精确文字 Gate。

Deformation Tier 复用该 Interface，但它不是每次重写的风格菜单：A/B/C 始终按 `conservative`、`standard`、`strong` 的语义顺序出现，显示标签本地化；每项的具体头身比例和圆润度、简化、五官位置、手部与身体曲线后果按用途适配。身体证据取舍写入同一道 Gate，不另问身体形状。

八个生产维度只是内部检查顺序，不是八轮问卷：输出类型/画布 → 创意方向 → 镜头/透视 → 造型/妆发/道具 → 画幅/文字 → 表演 → Finish → 避免项。已锁定、无关或已接受默认的维度直接跳过。

## 3. 唯一总流程

后面的九个场景流程都复用这条主干。任何场景都必须能从 P1 走到 P11，或在一个明确阻塞处诚实停止。

```mermaid
flowchart TD
    P1["P1 输入与参考角色<br/>确认 Primary Identity Anchor 和其他参考用途"] --> P2["P2 输出与 Brief<br/>确定用途、画布和已知锁"]
    P2 --> P3["P3 自适应决策循环<br/>绘制角色先显式解决 Deformation Tier<br/>其余一次只解决一个维度或真正紧耦合组"]
    P3 --> ORDINARY{"普通选择是否已锁定、无关、默认或委派？"}
    ORDINARY -- 否 --> GATE["显示一个 A/B/C/D Choice Gate"]
    GATE --> P3
    ORDINARY -- 是 --> P4{"P4 是否仍有聚焦阻塞？<br/>Coverage / 身份风险 / 安全 / 精确文字"}
    P4 -- 是 --> FOCUSED["只处理当前阻塞并保留全部状态"]
    FOCUSED --> P3
    P4 -- 否 --> P5["P5 按稳定标题加载活跃所有者章节"]
    P5 --> P6["P6 合成生产提示词<br/>身份在前；检查 Physical Scene Coherence 和组合风险"]
    P6 --> P7["P7 实际输入与宿主能力<br/>附上完整固定根；只使用真实控制"]
    P7 --> P8["P8 生成或编辑"]
    P8 --> P9{"P9 Identity Review 是否通过？"}
    P9 -- 是 --> P10{"P10 活跃所有者审查是否通过？"}
    P10 -- 是 --> P11["P11 最终结果"]
    P10 -- 否 --> RECOVERY["恢复分类<br/>窄修改或重新生成"]
    P9 -- 否 --> RECOVERY
    RECOVERY --> CAPABLE{"结果可见且宿主可执行正确输入选择？"}
    CAPABLE -- 否 --> STOP["保留决策状态，说明边界或只请求重附 Anchor"]
    CAPABLE -- 是 --> ONCE["最多一次自动修正"]
    ONCE --> P9
```

Deformation Tier 和 Medium Contract 不增加 P 编号：绘制角色在 P3 通过既有 Choice Gate 显式选择按用途适配的比例，Identity Anchor 随后用已锁媒介与该 Tier/Custom 解析并记录一次请求级 Medium Contract 和身体证据梯度。在 P6 前，closed channel 与最短比例造成的源图身形损失只做非提问式说明；P6 用正面比例语言，不复制这些说明；P9 读取同一记录，Character Sheet、应用和重生成都不重新解析。Character Sheet 也不增加 P 编号或新 Module：它只在连续性条件命中时把 P6–P8 分成先生成 Sheet、再从 Anchor + Sheet 独立生成应用的两段。

### 完成条件

- 所有必需聚焦 Gate 已解决。
- 每张必需人物参考和当前操作需要的锁定产物都作为实际图像输入传入。
- 用户锁定意图没有被静默改变。
- 绘制角色已有选择或显式委派的 Deformation Tier/具体 Custom 变形，且整项请求只使用同一份 Medium Contract 与身体证据梯度。
- 必要的 closed-channel 说明已在生成前显示，且没有进入生产提示词。
- 可见且可检查的结果通过 Identity Review。
- 本次参与生成或修改的所有者贡献都体现在提示词或修改中。
- 对质量、尺寸、文字、工具控制和视觉检查的声称都可验证。

## 4. 九个端到端场景流程

| 编号 | 流程族 | 主要区别 |
| --- | --- | --- |
| F1 | 简单头像与人像 | 最短普通路径，不制造故事问题 |
| F2 | 全局默认与委派 | 普通未解决项转为 Derived Locks，聚焦 Gate 仍保留 |
| F3 | Cosplay 与角色妆容迁移 | 真人是唯一身份锚，角色资料只提供造型 |
| F4 | 全身动作与证据缺失 | Coverage 和 Inference Boundary 保留已锁镜头与动作 |
| F5 | Style / Scoped Refresh | 只重开目标区域，维护分区历史和新鲜度 |
| F6 | 精确文字与场景冲突 | 完整允许文字集，一次 Physical Scene Coherence 确认 |
| F7 | 系列连续性 | 基础 Look Continuity + 每张图的故事状态变化 |
| F8 | 局部修复与身份漂移 | 先审查，再按结果可靠性和总修改范围选操作 |
| F9 | 安全与宿主能力限制 | 不静默改需求，不声称不可执行或不可检查的动作 |

### F1. 简单头像与人像

```mermaid
flowchart TD
    U["输入<br/>人物图 + LinkedIn、头像或自然人像目标"] --> I["P1 Identity<br/>人物图成为实际 Primary Identity Anchor"]
    I --> B["P2 Brief<br/>锁定用途；源图姿态、自拍透视和背景不是默认锁"]
    B --> Q["P3 轻量路径<br/>裁切/背景 → 必要时造型 → 表情视线 → First-Pass Finish"]
    Q --> MISSING{"仍有影响结果的普通选择？"}
    MISSING -- 是 --> G["一个 A/B/C/D Gate<br/>不问设备参数，不制造故事或道具问题"]
    G --> Q
    MISSING -- 否 --> F{"P4 是否有真实 Coverage、身份风险或文字冲突？"}
    F -- 是 --> FG["只显示当前聚焦 Gate"]
    FG --> F
    F -- 否 --> P["P5/P6 Identity + Composition<br/>具体身份结构、First Read、Shot、Natural Retouch、输出合约"]
    P --> T["P7/P8<br/>传入 Anchor；有真实控制才请求 high/稳定尺寸；生成"]
    T --> R["P9/P10<br/>先审身份，再看头像可读性、背景、造型和 Finish"]
    R --> O["P11<br/>通过则完成；失败进入 F8"]
```

### F2. 全局默认与委派

```mermaid
flowchart TD
    U["输入<br/>人物图 + 已明确要求 + 全局 you decide / use recommended defaults"] --> E["P1/P2<br/>用户已写明的用途、服装、文字等记录为 Explicit Locks"]
    E --> D["P3<br/>普通 suggested / unresolved 采用推荐结果并记录 Derived Locks"]
    D --> BLOCK{"P4 是否有 Coverage、身份风险、安全或精确文字阻塞？"}
    BLOCK -- 是 --> G["只显示该聚焦 A/B/C/D Gate<br/>回答后不重开普通问题"]
    G --> BLOCK
    BLOCK -- 否 --> LOAD["P5<br/>只加载实际需要的 Identity、Composition、Styling 章节"]
    LOAD --> P["P6<br/>合成完整提示词；显式锁优先，默认只补空缺"]
    P --> T["P7/P8<br/>附上实际人物图并生成"]
    T --> R["P9/P10<br/>Identity Review → 活跃所有者审查"]
    R --> O["P11<br/>通过则完成；失败进入 F8"]
```

局部刷新中的 `you decide` 只委派已解析出的刷新目标，不等于本流程的全局默认。

### F3. Cosplay 与角色妆容迁移

```mermaid
flowchart TD
    U["输入<br/>真人照片 + 指定角色/版本或角色参考"] --> I["P1 Identity<br/>Image 1 = Primary Identity Anchor<br/>角色资料绝不提供脸或身体身份"]
    I --> V{"P2 角色是否有多个主要版本？"}
    V -- 是 --> VG["Role/Costume Version Gate<br/>基于官方或可靠视觉资料选择"]
    V -- 否 --> RESEARCH["Styling Research / 用户已给资料<br/>需要研究时优先官方或可靠视觉来源；提取妆容画法、发型、服装、道具和表演"]
    VG --> RESEARCH
    RESEARCH --> STATE["P3 Styling Direction<br/>只解决未锁字段；真人可见脸部关系保持为 Protected Identity Cues"]
    STATE --> RISK{"P4 妆容会替换、重画或遮挡 Protected Identity Cue？"}
    RISK -- 是 --> RG["Identity Risk Gate<br/>风险按具体 cue 和处理范围限定"]
    RISK -- 否 --> PROMPT
    RG --> PROMPT["P5/P6 提示词<br/>先写真人源图可见身份结构，再写角色妆容、发型和服装"]
    PROMPT --> INPUTS["P7 参考角色分工<br/>真人 Anchor 必须实际输入；角色图若输入则标注 styling-only"]
    INPUTS --> GEN["P8 生成"]
    GEN --> IR{"P9 先与真人 Anchor 做 Identity Review"}
    IR -- 失败 --> FAIL["即使妆容和服装准确也不完成<br/>进入 F8，身份整体漂移时排除失败图重生成"]
    IR -- 通过 --> SR["P10 再审角色版本、妆容画法、服装、道具和表演"]
    SR --> O["P11<br/>全部通过才完成"]
```

关键不变量：妆容改变颜料、线条、质感、覆盖方式和修饰，不授权放大眼睛、缩鼻、改唇形、改下颌、换肤色或改变年龄感。源图已有妆容但来源未知时，它是 Reference Appearance；只有目标需要的身份 cue 被遮挡才形成 Appearance Coverage 缺口。

### F4. 全身动作与证据缺失

```mermaid
flowchart TD
    U["输入<br/>近景/半身 Anchor + 全身动作 + 强视点或道具"] --> LOCKS["P1/P2<br/>锁定用户要求的 Shot、相机、投影、动作、视线和造型"]
    LOCKS --> C["P3 Identity Coverage<br/>分别记录脸、外观、身体、角度、动作证据"]
    C --> GAP{"P4 目标关键证据缺失？"}
    GAP -- 是 --> G["Coverage Gate<br/>A 补真实参考 / B 描述 / C 精确 Inference Boundary / D Custom"]
    GAP -- 否 --> P
    G --> P["P5/P6<br/>提示词区分 verified、described、inferred；不降低已锁镜头和动作"]
    P --> I["P7<br/>Anchor 和所有必需人物参考作为实际图像输入"]
    I --> GEN["P8 生成"]
    GEN --> R["P9/P10<br/>身份、目标角度、世界空间人体、投影比例、姿态链和手/道具审查"]
    R --> PASS{"全部通过？"}
    PASS -- 是 --> O["P11 完成"]
    PASS -- 否 --> FAIL{"是否为多处相连比例错误、身份整体漂移或需扩展裁切？"}
    FAIL -- 否 --> LOCAL["一个可靠局部缺陷<br/>进入 F8 Surgical Edit"]
    FAIL -- 是 --> REGEN["Structural Scale Failure / 非局部失败<br/>从 Anchor + 锁定 Brief 重生成，失败图不得作为比例或构图证据"]
```

Inference Boundary 只允许推断逐项列出的未知区域或事实；它不会把已验证身体证据改成可变项，也不能替代 Primary Identity Anchor。

### F5. Style / Scoped Refresh

```mermaid
flowchart TD
    U["输入<br/>更多、换一批、换某项或 pick one"] --> TARGET["P1/P2 解析目标<br/>命名区域 → 未解决可见 Gate → 最近 refreshable Gate → 范围 Gate"]
    TARGET --> CLASS{"目标是可刷新创意区域？"}
    CLASS -- 否 --> FOCUSED["按原证据、分类、身份风险或文字问题处理<br/>不应用创意新鲜度"]
    CLASS -- 是 --> STATE["P3<br/>保留身份、输出、精确文字、无关值与所有 Explicit Locks<br/>只重开目标区域 Derived Locks"]
    STATE --> DELEGATE{"用户是否委派？"}
    DELEGATE -- 是 --> PICK["内部选择并记录一个兼容 Fresh Option"]
    DELEGATE -- 否 --> BATCH["顺序生成 A/B/C<br/>逐个对当前批次和分区历史检查新鲜度"]
    BATCH --> FULL{"能组成完整三项？"}
    FULL -- 否 --> EX["Refresh Exhaustion Gate<br/>只询问是否重开最限制变化的一个 Explicit Lock"]
    FULL -- 是 --> SHOW["显示 A/B/C + 永久 D) Custom<br/>展示时立即记录 A/B/C"]
    SHOW --> SELECT["用户选择或提供具体 Custom"]
    PICK --> READY
    FOCUSED --> READY
    SELECT --> READY["P4<br/>检查并解决所有仍待处理的 Coverage、身份风险、安全或精确文字 Gate"]
    EX --> READY
    READY --> P["P5/P6/P7<br/>所有选择解决后才合成提示词和实际输入"]
    P --> GEN["P8 生成"]
    GEN --> R["P9/P10/P11<br/>Identity Review → 目标所有者审查 → 完成或 F8"]
```

Creative Direction 使用六段 Direction Signature，至少三段不同；其他区域使用所有者可见签名，至少两部分不同。重命名、只换色板、形容词或设备词不算 Fresh Option。询问新选项本身不会生成或修改图片。

只有刷新明确重开媒介或 Deformation Tier/Custom 变形时，Identity Anchor 才重新解析 Medium Contract 与身体证据梯度；Finish、Shot、Styling、Performance、Layout 等其他刷新继续复用原记录。closed 集合未改变时不重复说明。

### F6. 精确文字与场景冲突

```mermaid
flowchart TD
    U["输入<br/>人物图 + 海报/封面 + 精确文字或裁切要求"] --> LOCKS["P1/P2<br/>锁定允许文字集、画幅、服装和构图要求"]
    LOCKS --> D["P3<br/>方向、Shot、Styling、Performance、Finish 分别解决"]
    D --> CONFLICT{"P4 是否有品牌关键文字歧义或两个不兼容 Explicit Locks？"}
    CONFLICT -- 是 --> G["一次聚焦 Gate<br/>只给直接可行的冲突解决路径，保留所有无关锁"]
    CONFLICT -- 否 --> P
    G --> COVER{"解决冲突是否扩展了裁切？"}
    COVER -- 是 --> CG["Reference Coverage Gate<br/>处理新暴露身体、角度或动作证据"]
    COVER -- 否 --> P
    CG --> P["P5/P6<br/>列出完整 allowed-text set；逐项指定角色、层级、字形特征、颜色、相对尺寸和精确区域"]
    P --> I["P7<br/>实际 Anchor 输入；提示词禁止允许集以外文字"]
    I --> GEN["P8 生成"]
    GEN --> IR{"P9 Identity Review 通过？"}
    IR -- 否 --> F8["进入 F8"]
    IR -- 是 --> TEXT["P10<br/>目标尺寸看 First Read；原始可用分辨率逐字检查精确文字"]
    TEXT --> O["P11<br/>通过则完成；一次文字窄修改仍失败时提供无文字底图路径，不虚报成功"]
```

普通缺失字体和排版由方向、布局、First Read、色彩和显示尺寸内部推导，不建立常规 Typography Gate。

### F7. 系列连续性

```mermaid
flowchart TD
    U["输入<br/>同一人物的多张关联图或连续故事"] --> BASE["P1/P2<br/>同一 Primary Identity Anchor + 系列用途与共同输出锁"]
    BASE --> LOOK["P3 Styling<br/>建立一次 Look Continuity：基础妆容、发型、服装、配饰"]
    LOOK --> EVOLVE["记录每张图明确的故事状态变化<br/>湿度、磨损、受伤、污渍、妆容崩解、服装损伤"]
    EVOLVE --> OTHER["分别锁定其他系列不变量<br/>道具状态、光向、地点地理、色彩处理"]
    OTHER --> EACH["P3/P4<br/>对每张图单独解决决定性时刻、Shot、Performance 和必要 Coverage"]
    EACH --> DRAWN{"可复用绘制角色<br/>或同一绘制角色至少两张图？"}
    DRAWN -- 否 --> P["P5/P6<br/>每张图生成完整提示词；共同锁 + 当前图变化"]
    P --> I["P7/P8<br/>每次传入完整固定根并独立生成"]
    DRAWN -- 是 --> TIER["P3 Deformation Tier<br/>显式选择用途适配比例<br/>解析一次 Medium Contract 与身体证据梯度"]
    TIER --> DP["P5/P6<br/>用共同 Tier/Contract 为 Sheet 与每张应用生成完整提示词"]
    DP --> SHEET["P7/P8 在任何应用前<br/>从 Anchor 生成一次干净背景 Character Sheet<br/>锁定并加入应用固定根"]
    SHEET --> A1["应用 1<br/>Anchor + Sheet + 应用 1 完整 Brief"]
    SHEET --> A2["应用 2<br/>Anchor + Sheet + 应用 2 完整 Brief"]
    SHEET -. 同一固定根 .-> AN["应用 N（若有）<br/>Anchor + Sheet + 当前应用完整 Brief"]
    I --> R["P9/P10<br/>每张先做 Identity Review，再审当前图与跨图连续性"]
    A1 --> R
    A2 --> R
    AN --> R
    R --> O["P11<br/>整组通过才完成"]
```

Character Sheet 在干净背景上锁定已选择的 Deformation Tier/Custom 比例、脸部构造、头发、眼睛画法、服装、色板、线条和阴影处理。每个应用都明确标注 Anchor 与 Sheet：Anchor 决定是谁，Sheet 决定如何画且绝不提供身份证据；提示词禁止重新设计角色。应用 1、应用 2 和任何后续应用从同一固定根独立分支，彼此不作输入，并分别保留场景、表情、视线、姿态、相机和输出锁；全部读取同一 Medium Contract，不从 Sheet、应用或结果再次推断比例。无连续性要求的单张绘图不创建 Sheet；单张图片也不创建 Look Continuity。

### F8. 局部修复、身份漂移与重生成

```mermaid
flowchart TD
    U["输入<br/>可见结果 + 完整固定根 + 修改请求或质量失败"] --> AVAILABLE{"P1/P9<br/>结果、Anchor 和相关区域是否同时可见可查？"}
    AVAILABLE -- 否 --> B["P11<br/>说明审查边界，不声称通过、修复或完成"]
    AVAILABLE -- 是 --> IR{"Identity Review 是否通过？"}
    IR -- 是 --> OWNER["P10<br/>只审查参与过的其他所有者"]
    OWNER --> PASS{"全部通过？"}
    PASS -- 是 --> O["P11 最终结果"]
    PASS -- 否 --> SCOPE
    IR -- 否 --> SCOPE{"结果是否可靠、缺陷是否为一个连贯局部单元？"}
    SCOPE -- 否 --> WIDE["身份整体漂移、Structural Scale Failure、Uneven Stylization<br/>或同时要求姿态、相机、裁切等非局部变化"]
    SCOPE -- 是 --> DIRECT{"用户是否明确坚持编辑这个结果<br/>且它不是下游复用的锁定产物？"}
    DIRECT -- 是 --> EDIT["Direct Edit<br/>输入 = 结果 + Anchor；不重复加入锁定产物"]
    DIRECT -- 否 --> FRESH{"当前 exchange 生成、可见、无 generated input<br/>且不是复用产物？"}
    FRESH -- 是 --> EDIT
    FRESH -- 否 --> WIDE
    WIDE --> CAP{"宿主能否包含完整固定根、排除失败图并启动新生成？"}
    CAP -- 否 --> REATTACH["保留所有锁，只请求重附 Anchor"]
    CAP -- 是 --> REGEN["从完整固定根 + 锁定 Brief 新生成<br/>失败图不得作为任何图像输入或证据"]
    EDIT --> ONCE
    REGEN --> ONCE
    ONCE["最多一次自动修正"]
    ONCE --> AGAIN["再做一次 Identity Review"]
    AGAIN --> END{"通过？"}
    END -- 是 --> OWNER
    END -- 否 --> STOP["报告具体未解决缺陷并停止<br/>不再重试，不宣称完成"]
```

Identity Review 先读取生成前记录的 Medium Contract，再判断是否完成并决定恢复范围。它只审 open 与 transferred 通道：任一 structural cue 仍 open 时，recognizability 不能替代逐 cue 审查；没有 structural cue open 时，transferred cues 的识别性决定完成，并额外要求缩略图尺寸的 filled silhouette 可辨。closed cue 的缺席本身不是失败或修正理由。妆容、服装或场景做得漂亮不代表身份通过；“用户说不像”也不会自动证明它只是局部缺陷。

固定根由 Primary Identity Anchor、必需可靠人物参考和每张图都复用的锁定产物组成，修正时不随失败结果增长。Character Sheet 是应用固定根中的锁定产物；失败应用必须从 Anchor + Sheet + 完整应用 Brief 重生成，失败 Sheet 必须从它自己的固定根 + Sheet Brief 重生成，两者都排除失败图。用户明确坚持局部编辑某个应用时，先建议重生成，但仍允许只以该应用 + Anchor 直接编辑，不再次加入 Sheet；复用的 Sheet 本身始终不可编辑。

Uneven Stylization 即使人物仍可识别且身份通道无漂移也让 Identity Review 失败，并且从不走 Surgical Edit。宿主能力允许时，用同一次有上限的新生成从 Primary Identity Anchor 和完整锁定 Brief 同时处理它与可能并存的身份漂移；只附必需且可靠的支持参考，失败图不进入任何图像输入或身份、脸、姿态、身体、构图等证据角色。Composition 的非摄影配方为皮肤、头发、眼睛、服装、灯光和背景逐项正面重述所选媒介，不描述失败图哪些表面仍是摄影处理，也不用负面指令表达其消失。

F8 是主流程的窄修改例外：已有可见结果时直接从 P9 审查开始，不重新走普通创意澄清；只有需要全新生成时才复用锁定 Brief 和正确实际输入回到生成步骤。

### F9. 安全与宿主能力限制

```mermaid
flowchart TD
    U["输入<br/>含安全风险、工具拒绝或能力要求"] --> SAFETY{"P2/P4 安全分类"}
    SAFETY -- 无安全风险 --> NORMAL["P1/P3<br/>保留 Anchor、原服装类别、创意意图和所有锁<br/>轻风险时最多添加一个必要的非情色、合龄或不透明限定"]
    SAFETY -- 轻风险且意图明确 --> NORMAL
    SAFETY -- 高风险 --> G["安全 Gate / 拒绝 / 合规重定向<br/>不静默换服装、裁切、姿态或概念"]
    G --> CHOICE{"用户选择合规路径？"}
    CHOICE -- 否 --> STOP["P11 停止"]
    CHOICE -- 是 --> NORMAL
    NORMAL --> P["P5/P6<br/>在保留已确认意图的前提下合成提示词"]
    P --> CAP{"P7 宿主是否真实支持所需图像输入、编辑、新生成、质量、尺寸或检查？"}
    CAP -- 否 --> LIMIT["继续可执行部分或请求重附 Anchor<br/>不声称 high、精确尺寸、输入排除、视觉 QA 或自动修正"]
    CAP -- 是 --> GEN["P8 生成"]
    LIMIT --> POSSIBLE{"仍可安全且诚实地生成？"}
    POSSIBLE -- 否 --> STOP
    POSSIBLE -- 是 --> GEN
    GEN --> BLOCKED{"工具是否拒绝？"}
    BLOCKED -- 是 --> REPORT["如实说明工具拒绝<br/>提供尽量保留原设置、角色、服装类别和视觉风格的修改路径"]
    BLOCKED -- 否 --> R["P9/P10<br/>Identity Review → 活跃所有者审查"]
    REPORT --> CHOICE
    R --> O["P11<br/>通过则完成；失败进入 F8"]
```

安全处理保持工具无关；能力处理保持事实优先。提示词中的 4K、high quality 或“保留 Anchor”不能替代真实控制。

## 5. 按需读取与所有者路由参考

协调 Module 通过稳定标题只读取当前活跃章节；宿主不支持分段读取时，整文件读取是正确性后备。分段读取不是正确性依赖，也不维护额外 read-state tracker。

| 活跃条件 | 必读章节 | 条件追加 |
| --- | --- | --- |
| 普通人物图生成 | Identity：`Priority`、`Reference Transfer`、`Reference Coverage` | 无 |
| 绘制角色、非摄影媒介或明确请求变形 | Identity：`Reference Transfer`、`Deformation Tier`、`Identity Prompt Constraints`；Composition：`Illustration or Other Non-Photographic Output` | 绘制角色先显式选择 Tier/Custom，再使用 Identity 已解析的请求级 Medium Contract 与身体证据梯度；Composition 不重新解析，也不把 closed-channel 或身形损失说明写入提示词；Uneven Stylization 重生成时为每个可见表面写正面媒介语言 |
| 可复用绘制角色或同一绘制角色至少两张图 | Identity：`Character Sheet`；Composition：`Character Sheet Applications` | Sheet 先于任何应用；应用实际输入都标注 Anchor 与 Sheet，并彼此独立 |
| 写最终提示词前 | Identity：`Identity Prompt Constraints`；Composition：`Final-Asset Quality`、`First-Pass Finish`、`Prompt Structure` | 所有当前活跃所有者章节 |
| 创意方向、First Read、决定性时刻 | Composition：`Creative Direction`、`Directorial Intent and Decisive Moment` | 需要选项时加 `Direction Atlas and Freshness`；刷新时加 `Style Refresh` |
| 镜头、透视、相机、投影 | Composition：`Shot Direction` | 按需加 `Perspective Intent`、`Camera and Capture Plan`；侧脸/动作/强透视加身份与姿态章节 |
| 物理世界、品味、媒介配方 | Composition 对应的 `Art Direction and Physical World`、`Taste Rules`、`Prompt Craft Rules` 或 `Output Recipes` 子节 | 只读相关媒介 |
| 服装、头饰、首饰、配件、妆发、道具 | Styling 对应的 `Ownership`、`Risk and Facial Treatment`、`Category Routing`、`Styling Direction` 或 `Props` | 按实际字段选择 |
| 故事造型、Delegated Styling、Story Makeup、Look Continuity | Styling：`Ownership`、`Risk and Facial Treatment`、`Styling Direction`、`Prompt Contributions` | 源造型遮挡关键身份 cue 时加 Identity `Reference Coverage` |
| 姿态、动作、表情、视线、手部、表演 | Styling：`Performance Direction` | 非简单动作加 `Pose Geometry`；脸角度影响身份时加 Identity `Face Visibility and Performance Integrity` |
| 指定角色、制服、历史服装 | Styling：`Role, Costume, and Visual Research` | 多版本时先走版本 Gate |
| 精确文字、布局、交付、变体、系列 | Composition：`Layout and Output Contract` | 文字或分区复杂时加 `Prompt Craft Rules` |
| 展示或替换可刷新 Gate | Refresh：`Scope`、`Visible Gate and History` | 按分支加 `Route the Target`、`Locks and Continuity`、`Refresh Exhaustion`，并加载目标所有者 |
| 审查可见结果 | 先 Identity：`Identity Review and Revision` | 再只读实际参与生成或修改的所有者审查段落 |
| 对可见结果做窄修改 | Identity：`Identity Review and Revision` + 修改项所有者 | 涉及脸时加 `Priority`、`Identity Prompt Constraints`；只在真正触及时补其他核心章节 |

### 提示词合成顺序

1. 用途、画布、布局。
2. Primary Identity Anchor、源图可见身份结构、Reference Transfer、Coverage，以及显式 Deformation Tier/Custom 所解析的 open / transferred 通道和可表达身体证据；比例、圆润度、简化、五官位置、手部与身体曲线都用正面绘制语言；应用随后标注 Character Sheet 的绘制设计角色，绝不把它当身份证据；closed-channel 与身形损失说明不进入提示词。
3. 已锁意图、First Read、创意方向和决定性时刻。
4. Shot、相机/透视、世界空间人体与投影比例。
5. Styling、Performance、Props、Pose Geometry。
6. 有动机的灯光/色彩、First-Pass Finish、材质和纹理。
7. 精确文字允许集、平台和交付约束。
8. 约 3–8 个本次最可能发生且可观察的失败约束。

禁止用固定高质量后缀、万能负面词表、空字段或紧凑配置块代替完整生产提示词。

### 外部研究、质量与能力

| 条件 | 行为 |
| --- | --- |
| 普通换一批 | 使用当前对话历史与 Direction Atlas，不浏览 |
| 明确 current / latest / trending | Trend Refresh，必须实时研究；无法验证就明说 |
| 指定角色、制服、历史服装 | 优先官方或可靠视觉资料，只提取生产锚点 |
| 正常人物成片 | 按 final asset 处理，不加质量问卷 |
| 有真实质量控制 | 请求 `high` |
| 有真实尺寸控制 | 请求不超过 `3,686,400` 总像素且符合画幅的最高稳定尺寸 |
| 用户要求更高尺寸 | 视为实验尺寸；控制可用时简短警告后继续 |
| 控制不存在 | 继续可执行部分，但不声称已设置 high、2K、4K 等 |
| 需要精确尺寸 | 实际检查输出像素后才能声称 |
| 结果不可见或分辨率不足 | 对相应审查标记 unavailable / unverified |

## 6. Golden 1–141 覆盖矩阵

每个编号在下表恰好出现一次，表示它的主要端到端流程族；Shared Checks 仍横跨全部流程。场景可以触及多个 Module，但不需要复制多张完整图。

| Golden 编号 | 主流程 | 覆盖主题 |
| --- | --- | --- |
| 1 | F1 | 模糊专业头像 |
| 2 | F2 | 显式全局委派 |
| 3-4 | F1 | 引导式人像、已有部分锁 |
| 5 | F4 | 高风险近景到全身动作 |
| 6 | F6 | 精确文字海报 |
| 7 | F7 | 系列连续性 |
| 8 | F8 | 手部窄修改 |
| 9-11 | F4 | 目标角度身份、透视选择、动作姿态链 |
| 12 | F8 | 保留强投影的协调修复 |
| 13-22 | F5 | Style Refresh、历史、Custom、锁来源、趋势、委派与耗尽 |
| 23-29 | F1 | First-Pass Finish 默认、选择、媒介适配与窄修改 |
| 30-46 | F5 | Finish/Scoped Refresh、目标优先级、分区历史、委派、耗尽与分类边界 |
| 47-49 | F1 | 全身/跨媒介成片质量与预览例外 |
| 50 | F9 | 宿主无质量或尺寸控制 |
| 51-58 | F1 | 实验尺寸、First Read、输出配方和短约束 |
| 59 | F5 | 历史不可用时不承诺精确去重 |
| 60 | F4 | 可访问身份图仍必须作为实际输入 |
| 61 | F9 | 必需身份图对工具不可用 |
| 62-63 | F4 | 多参考角色分工、Inference 不替代身份图 |
| 64-66 | F1 | 实验尺寸面积、警告与实际尺寸检查 |
| 67-68 | F8 | 双尺度审查、强角度自然不对称 |
| 69-70 | F9 | 证据不可用限制声称、质量和尺寸控制独立 |
| 71-76 | F6 | 多条精确文字、品牌排版、显式锁冲突与恢复 |
| 77-92 | F3 | Reference Appearance、造型委派、妆容风险、Story Makeup 与物理一致性 |
| 93-94 | F7 | 系列 Look Continuity 与单图不创建连续性 |
| 95 | F1 | 身份可读但不必成为 First Read |
| 96-97 | F8 | 可见 cue 漂移与造型导致的窄恢复 |
| 98 | F4 | 近景扩展全身的比例恢复 |
| 99 | F3 | 厚重服装仍保留可见上身证据 |
| 100-103 | F4 | 累积风险、充分证据、组合 Coverage 与组合 cue 变换 |
| 104-105 | F9 | Anchor 不可用、宿主受限时不伪装重生成 |
| 106 | F3 | 跨类型参考角色保持通用 |
| 107-112 | F8 | 局部/整体身份失败、自动恢复上限、风险范围与尽力而为 |
| 113-115 | F3 | 源图身份细节优先、角色不供脸、妆容形容词不改结构 |
| 116-117 | F6 | 裁切与服装锁冲突、扩裁触发新 Coverage |
| 118 | F8 | 干净呈现不能替代 Identity Review |
| 119 | F2 | 普通 Gate 的全局默认捷径 |
| 120 | F3 | 可靠来源解决角色版本 |
| 121 | F8 | Cosplay 执行干净也不能掩盖身份整体漂移 |
| 122 | F5 | Medium Contract 请求级记录、closed-channel 披露与刷新边界 |
| 123-124 | F1 | 请求变形与年龄解释测试、媒介表面处理 |
| 125-126 | F8 | structural-open 边界、transferred 识别与缩略图 silhouette 下限 |
| 127 | F8 | Uneven Stylization 独立失败并从 Anchor 重生成，不做 Surgical Edit |
| 128-131 | F8 | 固定根重生成、generated input 新鲜度、复用产物与未知 provenance |
| 132 | F7 | 多轮修改和系列图片不增长 generated-input chain |
| 133-136 | F8 | 清理请求与自动修正沿完整固定根重生成 |
| 137 | F7 | 一个 Character Sheet 锚定两个独立且不同的应用 |
| 138 | F8 | 应用、Character Sheet 与用户坚持局部编辑的固定根恢复边界 |
| 139 | F1 | Deformation Tier 在不同用途保持稳定语义顺序并适配具体比例 |
| 140 | F7 | Tier 解析一次身份通道与完整身体证据梯度，并由 Sheet 与应用复用 |
| 141 | F9 | 年轻观感、成熟曲线说明与 child-reading / adult-emphasis 冲突解析 |

当前编号场景没有单独覆盖安全 Gate 或生成工具安全拒绝；F9 的安全分支来自运行时合约和 Shared Checks。只有后续安全行为发生变更时，才增加最小专门 Golden 场景。

## 7. 维护、验证与优化方向

### 变更影响矩阵

| 变更类型 | 首要所有者 | 还要检查 |
| --- | --- | --- |
| 触发、Gate、状态、生命周期 | `SKILL.md` | 所有参考路由、对应 Golden |
| 身份证据、Coverage、审查、恢复 | `identity-anchor.md` | SKILL 路由、Styling/Composition 依赖、Context、Golden |
| 方向、镜头、Finish、布局、提示词 | `composition-director.md` | Identity/Styling Interface、Golden |
| 妆发服装、道具、表演、角色研究 | `styling-performance.md` | Identity 风险、Composition Shot、Golden |
| 刷新、历史、新鲜度 | `scoped-option-refresh.md` | 目标所有者可见签名、Golden |
| 规范术语或架构决定 | `CONTEXT.md` / `docs/adr/` | 全部运行时使用处、本文档、Golden |
| 安装、调用、示例 | `README.md` / `openai.yaml` | 当前宿主真实能力 |

### 当前规模基线

| 资产 | 当前规模 |
| --- | ---: |
| `SKILL.md` | 4,124 词 |
| `composition-director.md` | 6,365 词 |
| `identity-anchor.md` | 6,224 词 |
| `styling-performance.md` | 2,795 词 |
| `scoped-option-refresh.md` | 788 词 |
| 运行时 Markdown 合计 | 20,296 词 |
| `CONTEXT.md` | 39 个规范术语，1,919 词 |
| `docs/adr/` | 8 条 ADR |
| `golden-conversations.md` | 141 个场景，15,628 词 |

### 优化优先级

1. **先守住唯一所有者**：术语在 Context，行为在所有者，协调 Module 只路由，Golden 只描述可观察结果。
2. **保持稳定标题 Seam**：章节改名时同步路由和 Golden；整文件读取继续作为后备。
3. **先测再压缩**：只有实际上下文成本或遗漏证据出现时，才压缩重复合约；不能删除安全、身份、文字和交付边界。
4. **先静态检查再建评测框架**：人工审查开始漏项时，先检查场景编号、Input/Expected、标题引用和确定性 Gate 结构。
5. **优先加深现有 Module**：只有两个子域持续独立变化且发生真实所有权冲突时，才新增 Seam。
6. **宿主差异按事实处理**：出现第二个具体宿主行为且规则真正分叉时，再定义显式 Adapter 合约。

没有真实失败证据时，不增加独立 Makeup Module、强制后处理、持久化选项历史、read-state tracker、普通刷新联网、质量问卷、固定风格目录、身份分数、无限重试或只有一个实现的抽象 Adapter。

### 架构变更完成定义

- 能指出唯一首要所有者，并说明其他 Module 只是依赖还是共同拥有。
- 没有新增与 `CONTEXT.md` 竞争的同义词，也没有静默违反 ADR。
- `SKILL.md` 路由仍指向真实稳定标题。
- Explicit、Derived、Suggested、Unresolved 状态语义没有被绕过。
- 普通 Gate、聚焦 Gate、Scoped Refresh 和恢复路径没有相互吞并。
- 新行为能落到总流程 P1–P11 和一个流程族中。
- Golden 覆盖表仍无遗漏、无重复，新增或改变行为有对应可观察场景。
- 结构校验、Golden 审计与 `git diff --check` 通过。
- 本文档相应图、职责、规模或优化触发条件已同步更新。
