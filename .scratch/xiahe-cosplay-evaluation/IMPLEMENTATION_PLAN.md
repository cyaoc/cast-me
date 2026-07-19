# 夏禾 cosplay 身份保真与流程收敛修改方案

Status: ready-for-human

## 目标

让 CastMe 在人物 cosplay 流程中做到四件事：

1. 角色资料只决定妆发、服装、道具与表演，不把人物改成通用的理想化 cosplay 脸。
2. `polished`、`fresh skin`、`defined eyes` 等造型词不改变眼形、鼻唇、下颌、年龄感或真实可见的皮肤纹理。
3. 成片即使构图、服装、手部和清理都合格，只要身份发生未接受的实质漂移，就先判定未完成并走正确恢复路径。
4. 用户可以在任一普通创意选择门显式选择“当前选项＋其余采用推荐默认值”，避免明明愿意委托却仍经历多轮表单式提问。

## 当前基线

当前 `main` 已经包含大部分正确规则，不能再重复堆提示词或新增工作流：

- `identity-anchor.md` 已定义具体身份结构、Reference Appearance、过滤遮挡边界、身份优先复核和 identity-wide 恢复。
- `composition-director.md` 已禁止 Natural Retouch 扩眼、收窄鼻或下颌、填唇、消除毛孔和年轻化。
- `styling-performance.md` 已要求命名角色优先使用官方资料、先锁定主要版本，并禁止角色参考提供人物脸部身份。
- Golden Conversations 113、114、115、118 已分别覆盖具体身份描述、夏禾角色边界、妆容形容词边界和“画面很干净但身份仍失败”。
- 普通选择已经支持 `use recommended defaults` / `generate now`，但并非每个普通 Choice Gate 都明确把这个快捷回复展示给用户。

因此实际修改面只保留两处：

| 文件 | 修改 |
| --- | --- |
| `skills/cast-me/SKILL.md` | 让每个普通创意 Choice Gate 的回复提示显式展示局部选择和全局默认快捷方式 |
| `evals/golden-conversations.md` | 增加一个 UX 回归场景和两个跨规则集成场景 |

明确不修改：

- `identity-anchor.md`
- `composition-director.md`
- `styling-performance.md`
- `CONTEXT.md`
- 任何新模块、模型评分器、人脸 embedding、相似度阈值、滤镜检测器或角色专用规则

只有新增回归场景证明上述现有规则存在矛盾时，才允许在对应 owner 文件修正那一处矛盾；不能借机重写现有身份系统。

## 成功标准

- 用户在普通创意 Gate 中始终能看见两种回复方式：只锁定当前选择，以及锁定当前选择并委托剩余普通选择。
- 裸 `A` 仍只解决当前维度；`A + use recommended defaults`、`generate now` 或全局 `you decide` 才结束后续普通选择。
- 身份、Reference Coverage、安全和精确文字冲突等 focused gate 不得被默认值快捷方式跳过。
- 角色存在多个主要版本时，在生成前只问一次版本选择；选择内容来自可靠的一手视觉资料，角色资料永远不提供人物脸部身份。
- 生产提示先写来源图中实际可见的身份关系，再写夏禾妆发、服装、表演与成片质感；不能从 `cosplay`、`polished`、`fresh skin` 等词推导大眼、尖脸、细鼻、丰唇或瓷肌。
- 参考图经过未知妆容或滤镜时，只保留实际可见的 Reference Appearance；只有目标关键身份线索被遮住时才触发一次 Reference Coverage gate，不得声称恢复了不可见的裸脸或自然毛孔。
- 可见成片出现脸宽、眼部关系、鼻部、唇部、下颌、年龄感或皮肤纹理的多处独立漂移时，Identity Review 必须先失败；其他规格合格不能抵消失败。
- identity-wide 失败只从 Primary Identity Anchor 和锁定 brief 重新生成，并排除失败成片；最多一次恢复并再次复核。
- Skill 验证通过、Golden Conversations 顺序连续、`git diff --check` 无错误。

## Task 0：固定复现边界，不从结果倒推原因

**不修改文件。**

- [x] 收集能够获得的原始 Primary Identity Anchor、最终成片、第一次失败成片、实际生产 prompt、实际图片输入及其角色、完整选择记录、目标夏禾版本和当次实际使用的 CastMe 内容。
- [x] 将问题分别标记为以下一种或多种，不允许统称为“美颜导致”：
  - 输入证据不足或参考图滤镜遮住关键线索
  - 生产 prompt 引入结构性美颜要求
  - 模型在角色造型与身份之间发生输出漂移
  - Identity Review 错误放行
  - 实际运行内容与当前仓库版本不一致
- [x] 若原图或运行记录不可得，只实现下述已确认的 UX 暴露和行为回归，不增加猜测性的 prompt 规则。

完成条件：每个后续修改都能指向一个可复现行为，而不是指向“夏禾”“粉发”或某种滤镜名称。

## Task 1：先补行为回归

**文件：**

- Modify: `evals/golden-conversations.md`

### 场景 A：普通 Gate 必须显示全局默认快捷方式

- [x] 新增一个顺序对话场景：用户请求人物 cosplay，若干普通创意维度仍未解决。
- [x] 第一个普通 Gate 的回复说明必须同时展示：
  - `A`：只选择当前推荐项，继续询问真正未决的下一维度。
  - `A + use recommended defaults`：选择当前项，并对其余普通创意维度采用推荐默认值。
- [x] 用户采用第二种回复后，不再出现普通 Direction、Shot、Styling、Performance、Canvas 或 Finish 提问。
- [x] 保留 focused Reference Coverage、身份风险、安全和精确文字冲突的阻断能力。

这个场景在当前契约下应先暴露缺口：默认快捷语义已经存在，但每个普通 Gate 的回复提示尚未被统一要求展示。

### 场景 B：命名角色版本先锁定，资料不接管人物脸

- [x] 输入只说“把我做成夏禾 cosplay”，且在线调研发现至少两个主要视觉版本。
- [x] 期望先展示一个版本 Choice Gate：A/B 提供有一手资料支持的实质版本；只有确有第三个版本时才用于 C，否则 C 保持当前状态并停止；`D) Custom` 永久可用。
- [x] 未锁定版本前不写角色专用生产 prompt；锁定后不重复询问。
- [x] 期望明确：角色资料只提供发型、妆容颜色与画法、服装、配件、道具和表演，不提供脸型、眼形、鼻唇、下颌、肤色、年龄感或身体身份。
- [x] 不把白色无袖、黑色机车装或任一版本硬编码成“夏禾唯一正典”。

该场景是现有规则的回归覆盖，正常情况下不要求修改 `styling-performance.md`。

### 场景 C：夏禾成片规格合格但身份失败

- [x] 输入包含清晰 Primary Identity Anchor，并锁定 9:16、半身、平视、无文字、指定夏禾版本、长粉发、目标服装、黑手套、从容危险的表演和自然皮肤质感；用户随后采用推荐默认值。
- [x] 期望不再出现普通选择门。
- [x] 生产 prompt 必须先描述来源图实际支持的脸型过渡、眼部关系、鼻部、唇部、下颌、皮肤与年龄感，再写角色造型。
- [x] 生产 prompt 不得自行加入 `large eyes`、`full lips`、窄下颌、细鼻、幼态或瓷肌要求。
- [x] 可见结果满足比例、构图、服装、无文字和手部要求，但脸宽、眼部关系、鼻部、唇部、下颌和皮肤纹理出现多处独立漂移。
- [x] 期望先判 Identity Review 失败，不得以规格执行正确为由完成交付。
- [x] 若当前生成表面可独立选择输入，则从 Primary Identity Anchor 与锁定 brief 新生成一次，排除失败成片；否则只请求重新附加 Anchor。第二次仍失败时报告具体漂移并停止。

该场景把已有 113、114、115、118 串成一次真实顺序回归，不新增夏禾专用产品规则。

## Task 2：统一暴露默认值快捷回复

**文件：**

- Modify: `skills/cast-me/SKILL.md`

- [x] 在共享 Choice Gate 格式规则中增加一句：每个普通创意 Gate 的结尾必须本地化展示两种回复示例——只选当前项，以及“当前项＋其余采用推荐默认值”。
- [x] 保持裸字母语义不变：裸 `A` 不能静默锁定尚未展示的维度。
- [x] 保持全局委托语义不变：`use recommended defaults`、`generate now` 或无作用域的 `you decide` 停止普通选择。
- [x] 明确该快捷方式只处理普通创意维度，不能接受未说明的 Inference Boundary，也不能跳过 focused identity、coverage、safety 或 exact-text gate。
- [x] 复用现有 `composition-director.md` 中 `B + use recommended defaults` 的句式，不创建新的 Gate 类型、状态或 helper 文件。

预期修改是一条共享格式规则及必要的邻近措辞调整；若超过一个短段落，应重新检查是否重复了第 62–64 行已有语义。

## Task 3：证明现有身份规则已经覆盖，不继续加负面词

**不预设修改文件。**

- [x] 对照场景 B/C，逐条定位现有 owner：
  - 具体来源身份描述和 prompt 优先级：`identity-anchor.md`
  - Reference Appearance / Appearance Coverage：`identity-anchor.md`
  - Natural Retouch：`composition-director.md`
  - 角色版本和参考角色边界：`styling-performance.md`
  - Identity Review 与恢复：`identity-anchor.md`
- [x] 确认场景 B/C 的每个期望都有现有明确规则支持。
- [x] 不增加统一负面词列表，不增加 `large eyes` / `full lips` 黑名单，不检测具体滤镜品牌，也不增加“正面＋3/4 必须同时提供”的固定门槛。
- [x] 只有某项期望在现有 owner 中没有表达时，才在该 owner 增加最短的一句通用规则，并补充对应 Expected；不得在协调器复制 owner 规则。

完成条件：除 Task 2 的 UX 规则外，默认不产生 Skill 行为修改。模型的非确定性不能通过重复同义 prompt 变成保证。

## Task 4：验证

### 4.1 Skill package

使用隔离的临时 `uv` 环境，不改项目或全局 Python：

```bash
castme_validate_dir="$(mktemp -d /private/tmp/castme-validate.XXXXXX)"
uv venv "$castme_validate_dir/.venv"
uv pip install --python "$castme_validate_dir/.venv/bin/python" pyyaml
"$castme_validate_dir/.venv/bin/python" \
  /Users/cyao/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/cast-me
```

期望输出：`Skill is valid!`

### 4.2 Golden Conversations

- [x] 确认编号连续，没有覆盖或重命名既有场景。
- [x] 逐个审查新场景：每条 Expected 都能定位到共享协调规则或唯一 owner。
- [x] 复查既有 77–79、113–115、118，确保没有因新场景产生相互矛盾。
- [x] 运行：

```bash
rg -n '^## [0-9]+\.' evals/golden-conversations.md
git diff --check
git status --short
```

### 4.3 差异范围

最终实现差异默认只能包含：

```text
skills/cast-me/SKILL.md
evals/golden-conversations.md
.scratch/xiahe-cosplay-evaluation/research.md
.scratch/xiahe-cosplay-evaluation/IMPLEMENTATION_PLAN.md
```

若出现其他生产文件，必须说明哪一个新场景证明原 owner 确有缺口；否则撤销该额外修改。

## 非阻断的实图因果实验

这个实验用于回答“美颜、prompt、模型各占多少”，不是合并实现的门槛，也不把私人照片提交到仓库。

| | 中性身份锁 prompt | 含结构性美颜词的诊断 prompt |
| --- | --- | --- |
| 清晰少滤镜参考 | A | B |
| 同一人物的当前美颜参考 | C | D |

- 每格保持角色版本、构图、服装、表演、画幅和其他条件一致，并重复生成至少三次。
- A/C 的稳定差异用于估计参考图影响；A/B 的稳定差异用于估计 prompt 影响；A 中仍出现的波动归入模型输出不确定性。
- 复核只比较来源图支持的相对关系和可见纹理，不使用生物识别分数。
- 无论根因来自哪一格，只要明显身份漂移仍被放行，都单独记录为 Identity Review 缺陷。

## 非目标

- 不保证 GPT Image 2 的精确身份一致性。
- 不凭一张生成图判断参考图用了哪种美颜。
- 不重建参考图中不可见的裸脸、毛孔或真实无滤镜结构。
- 不为夏禾或任何角色写身份例外、固定脸型、固定服装或固定气质模板。
- 不把七轮对话本身当作 bug；只修复用户没有被明确告知全局默认快捷方式，或接受该快捷方式后仍继续普通提问的情况。
- 不增加依赖、运行时服务、持久状态、评分系统或新的工作流阶段。

## 交付结果

实现完成后应得到一个很小的产品差异：一处共享 UX 规则，加三条高信号行为回归。身份、美颜、角色研究与恢复逻辑继续由现有 owner 负责；实图模型漂移通过运行评估暴露，而不是用更多同义负面提示词掩盖。
