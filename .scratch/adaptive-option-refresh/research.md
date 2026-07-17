# Adaptive Option Refresh 调研

## 结论

可以做，而且不需要为 Finish、Shot、Styling、Performance 分别建立刷新流程。

当前 skill 已有完整的基础骨架：按 owner 划分的生产维度、`locked: explicit` / `locked: derived` / `suggested` / `unresolved` 状态、对话内 Shown Direction、差异签名、委托刷新和 Refresh Exhaustion。最小正确方案是加入一个通用的 **Scoped Option Refresh**：用户点名哪个维度就只刷新哪个维度；没有点名时刷新最近一次可刷新的 gate；只有明确要求 style / direction 时才走现有 Style Refresh。

这与 Codex 的官方交互模型一致：用户可以在后续消息里纠正方向或要求 another option，而不必从头开始；要保持结果稳定，提示契约应同时写清“哪些内容不能变”。Skill 默认也可以只由说明和按需加载的 reference 构成，因此本需求不需要脚本、数据库或新依赖。参见 [Prompting](https://learn.chatgpt.com/docs/prompting) 与 [Build skills](https://learn.chatgpt.com/docs/build-skills)。

“无限提供新选择”不能作为承诺。锁定条件足够多时，可见解空间必然耗尽；正确体验是维持差异门槛，并只请求放开一个最限制变化的字段。

这里的“做到完美”应定义为五个可验证结果：懒惰说法能落到正确维度；无关锁不变化；新批次有可见差异；当前对话内不重复已经展示的方案；空间耗尽时诚实停下而不是伪造新鲜感。它不等于无限 novelty，也不等于跨会话永久记忆。

## 当前选择面

| 选择面 | 当前形式 | 当前刷新能力 | 依据 |
| --- | --- | --- | --- |
| 通用 clarification gate | 2–4 个 A/B/C/(D) 具体选项、推荐和覆盖方式 | 无通用刷新语义 | `skills/cast-me/SKILL.md:24-34` |
| Output Type | 固定 A/B/C + `D) Custom`，属于用途分类 | 可显式改选，不需要 novelty reroll | `skills/cast-me/SKILL.md:57-88` |
| Creative Direction | 动态 A/B/C + permanent Custom；六部分 Direction Signature | 已支持重复刷新、去重、恢复、委托和耗尽 | `skills/cast-me/references/composition-director.md:23-89` |
| Decisive Moment | 多个可见时提供动态选择 | 无独立历史或刷新 | `skills/cast-me/references/composition-director.md:93-97` |
| Shot Direction | 两套近乎固定的 body-scale/crop A/B/C + Custom 模板 | 无 shot-scoped refresh 或去重 | `skills/cast-me/references/composition-director.md:99-133` |
| Perspective Intent | 三个稳定语义通道 + Custom；明确不是固定 preset | 通道不应扩张，具体表现应由 Shot 刷新 | `skills/cast-me/references/composition-director.md:135-146` |
| First-Pass Finish | 动态、图像特定 A/B/C + Custom；禁止固定 preset 和 palette-only 变化 | 无 finish-scoped history、freshness 或 exhaustion | `skills/cast-me/references/composition-director.md:161-177` |
| Styling | 专业头像固定为保留、简化、替换、Custom | 无 styling-scoped refresh | `skills/cast-me/references/styling-performance.md:35-61` |
| Performance | 按 decisive moment 生成可见行为选择 | 无 performance-scoped history 或 refresh | `skills/cast-me/references/styling-performance.md:77-87` |
| Role / Costume Version | 多版本时用标准 decision format | 属于事实和版本消歧，不需要 novelty | `skills/cast-me/references/styling-performance.md:113-128` |
| Canvas / Text / Layout | 一个 output-contract choice；精确文本逐字验证 | Layout 可刷新；exact text 不可自动改 | `skills/cast-me/references/composition-director.md:258-264` |
| Coverage / Identity Risk | 只从实际缺口生成证据、描述、推断或 staged 路径 | 不应创意刷新 | `skills/cast-me/references/identity-anchor.md:100-134` |
| Safety | 异常处理；只提供合规路径 | 不应使用 freshness 或 reroll | `skills/cast-me/SKILL.md:135-156` |

## 根缺口

1. `skills/cast-me/SKILL.md:45` 把任何 “another batch” 都强制路由到 Style Refresh。Finish gate 后说“这三个都不要，再来一批”会错误重开 creative direction。
2. Shown history 和六部分 Direction Signature 只属于 creative direction。直接拿它记录 Finish 或 Shot 会污染风格方向历史。
3. Finish 已要求 image-specific 且 palette-only 不足，但没有下一批、已展示项、等价判断或耗尽规则。
4. Shot 和专业头像 Styling 的示例很容易被当成永久菜单；重复请求时只会换措辞或返回同一骨架。
5. Decisive Moment、Performance 和 Layout 虽然可以动态生成，但没有 active-gate routing、历史和锁定后的局部重开语义。
6. 当前状态是字段级的，但 Style Refresh 是跨维度的；如果直接扩大 Style Refresh，会误开 scene、lighting、finish 或 composition，而用户可能只想换一个镜头、动作或 finish。

## 推荐：Scoped Option Refresh

Scoped Option Refresh 复用当前 gate，不增加新步骤：

- 刷新一个 owner 或该 owner 内用户明确点名的子字段。
- 维护一个 `last refreshable gate` 指针；选择已被采用或图片已经生成后仍保留该指针，使稍后的“刚才那几个都不要”仍能回到正确维度。
- 保留身份、输出要求和所有无关维度。
- 重开目标范围内的 `locked: derived`；目标范围内仍被用户明确要求保留的子字段继续是 `locked: explicit`。
- 记录该维度所有展示过的 A/B/C；记录被采用的 Custom 实例，不记录 `D) Custom` 占位符。
- 每个 refreshable creative gate 保留三个具体选择加 `D) Custom`。
- 用户说“换一个，你决定”时，内部选择并记录一个 Fresh Option，不再显示 gate。
- 用户明确恢复旧选项时照做；freshness 只限制自动推荐，不限制用户意图。

## 路由优先级

1. **未解决的安全、reference coverage、identity risk、exact-text gate 优先。** 这些 gate 只能按事实更新，不进入创意 freshness。
2. **用户显式点名 owner 或字段。** 如“换一批 finish”“给我新的镜头”“动作再来三个”；显式目标胜过当前 gate。
3. **用户未点名，但存在最近一次可刷新 gate。** “这三个不要”“再来一批”“还有吗”刷新该 `last refreshable gate`；它可以是仍待选择的 active gate，也可以是稍早已经采用的最近一个创意 gate。
4. **用户明确说 style / visual style / creative direction。** 走现有 Style Refresh 及其 `only change visual style` / `completely change direction` 分支。
5. **没有最近 gate，也没有点名。** “换个方向”可明确落到 Style Refresh；纯粹的“再来几个”没有可靠指代时，只问一次紧凑的 scope gate，不静默猜成 style。
6. **`you decide` / `pick one` 是修饰语。** 它不改变目标 owner，只把可见刷新变成 scoped delegated refresh。

## 每维 Freshness

每个维度维护独立、对话内的轻量签名。除已有 Creative Direction 的“三个部分”规则外，普通 Fresh Option 至少改变两个该维度的可见部分；只改名称、颜色、形容词、设备词或专业术语不算 fresh。

| Owner | Option Signature | Freshness |
| --- | --- | --- |
| Creative Direction | production context；medium/era；scene/decisive moment；composition grammar；lighting/color logic；finish | 保持现有规则：至少 3/6 不同 |
| Decisive Moment | 当前事件/动作；前后张力；故事证据；第一观感 | 至少 2 项不同；仍在锁定 creative direction 内 |
| Shot | body cutoff/subject scale；viewpoint/distance/projection；subject placement；spatial layers/background relationship | 至少 2 项不同；用户明确锁定的 crop 或 viewpoint 不参与重开 |
| Finish | overall feeling；light/contrast；person-environment color relationship；face/material treatment；texture/final character | 至少 2 项不同；palette-only 不算 fresh |
| Styling | silhouette/layers；materials；headwear/accessories；makeup/hair/grooming；props | 至少 2 项不同；保留用户指定物件 |
| Performance | action/body direction；expression/mouth；gaze；hands/prop interaction；energy | 至少 2 项不同；只改“更有力/更自然”不算 fresh |
| Layout / Output Contract | aspect/layout structure；subject/text-safe placement；safe areas/readability；required variants | 至少 2 项不同；exact text、平台硬要求和交付规格始终锁定 |

Perspective Intent 保持三个稳定语义通道；用户要求“更多透视创意”时生成新的 Shot 方案，而不是发明新的风险分类。Output Type、Role/Costume Version、Safety、Coverage、Identity Risk 和 exact-text verification 不维护 freshness 历史。

## 耗尽

当 Explicit Locks 使目标维度无法产生三个 Fresh Options：

1. 不降低该维度的 freshness 门槛。
2. 找出一个最限制变化的 Explicit Lock。
3. 用标准 decision format 询问是否只放开该字段，同时提供“保留全部锁定并停止刷新”和 `Custom` 路径。
4. 用户保留全部锁定时停止刷新，不提供伪新批次。

耗尽状态只属于当前 owner，不应重开其他维度，也不应自动升级为完整 Style Refresh。

## 边界

- 所有历史只在当前对话内；不增加数据库、用户配置或跨会话持久化。
- 很长的对话可能受上下文窗口与压缩影响，因此“当前对话内不重复”也只能在仍保留的会话状态内保证。若以后要求跨会话严格去重，那是需要显式持久化的另一项功能，不应混入本次改动。
- 普通 scoped refresh 不浏览网络。只有明确要求 current/latest/trending/date-bound visual directions 的 Style Refresh 才是 Trend Refresh。
- 不刷新安全边界、证据事实、身份风险分类或精确文本；可以根据新信息重新计算它们。
- 不为每个 owner 新建流程、类、配置或工具；这是 skill 的会话行为契约。
- 不承诺无限选择；保留 Custom、delegation 和 scoped exhaustion 即可覆盖懒用户的实际需求。
- 不自动生成第二张图或进入 revision；First-Pass Finish 仍属于首次生成，targeted revision 仍必须由用户明确请求。

## 最小实施点

1. `skills/cast-me/SKILL.md`
   - 替换 line 45 的全局 Style Refresh 路由。
   - 在现有 decision state 后加入 `last refreshable gate`、显式 owner 优先和一条按需加载规则。
   - 明确哪些 focused/classification gate 不参加 freshness。
2. 新增 `skills/cast-me/references/scoped-option-refresh.md`
   - 作为 routing、per-owner shown history、Custom/delegation、锁继承与 exhaustion 的单一来源。
   - 引用现有 Direction Refresh，不搬动或重写已经工作的 3/6 规则。
3. `skills/cast-me/references/composition-director.md`
   - 为 Shot、Decisive Moment、Finish、Layout 只写各自轻量 signature 和 owner 特例。
   - 将两个 Shot 菜单降级为示例形状，要求按当前场景和已锁字段生成。
4. `skills/cast-me/references/styling-performance.md`
   - 为 Styling 和 Performance 加 scoped refresh、独立 history 和 signature。
   - 将专业头像固定菜单降级为当前场景的示例形状。
5. `CONTEXT.md`
   - 只补最少 glossary：`Scoped Option Refresh`、`Shown Option`、`Fresh Option`；不要复制实现细节。
6. `evals/golden-conversations.md`
   - 加行为场景；不测试精确措辞或内部数据结构。

这是可逆的 skill-contract 扩展，不需要 ADR，也不需要生产代码或新依赖。

## 建议 Golden Tests

现有 Style Refresh 基线位于 `evals/golden-conversations.md:95-153`，Finish 基线位于 `evals/golden-conversations.md:155-195`。建议新增：

1. **Active Finish Refresh**：Finish gate 后“这三个都不要，再来一批”只刷新 Finish；scene、shot、styling、performance、canvas/text 全部保持。
2. **Explicit Owner Beats Active Gate**：Finish gate 当前可见，但用户说“给我新的镜头选择”；只刷新 Shot。
3. **Partial Shot Reopen**：“保持腰部以上，换三种镜头关系”；保留 explicit crop，只变化 viewpoint、placement 和 background relationship。
4. **Repeated Scoped Refresh**：Finish、Shot、Styling、Performance 分别连续三批；所有展示项计入各自历史，禁止 palette-only、改名和 adjective-only 伪变化。
5. **Scoped Custom**：采用一个 Custom Finish 或 Shot 后再刷新；不推荐等价方案，但每批仍保留 `D) Custom`。
6. **Scoped Delegation**：“换一个动作，你决定”；不显示 gate，内部选择并记录一个 Fresh Performance 后继续。
7. **Scoped Exhaustion**：用户锁死目标 owner 的所有组成部分后仍要三项；只询问放开一个限制字段，不放宽门槛，不升级为 Style Refresh。
8. **Focused Gate Boundary**：Safety 或 Coverage gate 后要求“更多选项”；仍只提供与实际风险相关的路径，不应用创意去重。
9. **Perspective Classification Boundary**：用户要求更多空间冲击方案；保持三条 perspective intent 语义，刷新主题化 Shot 表达，不发明第四种风险分类。
10. **Style Refresh Regression**：明确“only change visual style”仍按现有范围重开 medium/era、lighting/color、material treatment、finish，不受 scoped routing 破坏。

## 主要依据

- 决策状态与锁来源：`skills/cast-me/SKILL.md:38-49`
- 八维 owner 与耦合边界：`skills/cast-me/SKILL.md:94-119`
- Direction history、signature、freshness：`skills/cast-me/references/composition-director.md:29-57`
- Style Refresh、delegation、exhaustion：`skills/cast-me/references/composition-director.md:59-71`
- Dynamic Style Refresh 原始设计与测试边界：`.scratch/dynamic-style-refresh/PRD.md:40-88`
- First-Pass Finish 原始设计与测试边界：`.scratch/identity-safe-finish/PRD.md:44-86`
- Golden Conversations 是行为检查而非精确脚本：`evals/golden-conversations.md:1-21`
