# CastMe 妆造设计与身份稳定性研究

调研日期：2026-07-17

## 结论

**需要妆造设计能力，但没有必要新增“化妆师”和“造型师”两个常驻角色，也不应增加一个必经阶段。**

CastMe 现有 `Styling and Performance Director` 已经拥有 wardrobe、hair、makeup、grooming 和角色造型，现有 identity 边界也已覆盖结构性改脸、肤色、年龄感与自动美化风险（`skills/cast-me/references/styling-performance.md:3-21,35-47`；`skills/cast-me/references/identity-anchor.md:25,39-54,96,158-166`）。真正缺的不是新角色，而是把这个现有模块深化为一个**按需启用的妆造设计视角**：故事需要时统筹妆、发、服装；不需要时沿用本人造型或只做整理。

这个组织方式也符合真实制作：妆发设计师根据导演和剧本设计人物并负责连续性，服装设计师通过服装参与人物与故事塑造；大制作会拆分岗位，小制作通常合并妆发岗位。[ScreenSkills：Hair and make-up designer](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/craft/hair-and-make-up-designer-film-and-tv-drama/) [ScreenSkills：Costume designer](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/craft/costume-designer-film-and-tv-drama/) [Costume Designers Guild：What is Costume Design?](https://costumedesignersguild.com/what-is-costume-design/)

## 证据

### 1. 妆容可以帮助表达，也确实会影响身份识别

- Ueda 与 Koyama 的实验中，轻妆更容易被识别，重妆更难；首次看到的是带妆脸时，后续识别也更困难。[Influence of Make-up on Facial Recognition](https://journals.sagepub.com/doi/10.1068/p6634)
- Tagai 等人的实验中，无妆和轻妆脸的识别表现高于重妆脸，重妆还带来更多错误认脸；但该研究只招募日本女性，三种妆容使用了不同人物且包含数字修饰，不能据此制定跨人群的“妆多浓”数值阈值。[Faces with Light Makeup Are Better Recognized than Faces with Heavy Makeup](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.00226/full)
- 后续使用同一批模特无妆、轻妆、重妆照片的研究仍发现，重妆配对的身份判断低于轻妆与无妆；轻妆与无妆谁更有利并不稳定，但“重妆更可能遮蔽个体特征”是较一致的方向。[The light-makeup advantage in facial processing](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0172489)
- 眉毛本身是强身份线索：熟悉脸去掉眉毛造成的识别损失甚至大于去掉眼睛。因此，重画眉峰、眉眼距离和整体眉形不能被当成无风险润色。[The Role of Eyebrows in Face Recognition](https://journals.sagepub.com/doi/10.1068/p5027)

**证据允许的结论：**身份安全不等于“完全不化妆”；安全默认应是突出而不是替换本人的个体特征。证据不支持一个通用的轻妆/重妆强度数字。

### 2. 发型既是造型工具，也是身份线索

- 在保持眼、鼻、口不变、只改变发型的实验中，旧脸识别准确度由约 0.80 降至 0.50，且观看方式更接近一张新脸。[Holistic Representations of Internal and External Face Features](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2012.00087/full)
- 熟悉与陌生面孔的识别机制不同。自然照片分类实验显示，熟悉脸更能依靠内部特征（眼、鼻、口）跨图片识别；陌生脸更容易依赖头发、耳朵和轮廓等外部特征。[The importance of internal and external features in recognizing faces](https://journals.sagepub.com/doi/10.1177/03010066221122299)
- 学习多角度的新脸时，降低对发型这一突出外部特征的依赖，反而有助于把内部身份线索迁移到新角度。这说明头发很显眼，但不是稳定身份的全部。[The importance of internal facial features in learning new faces](https://eprints.bournemouth.ac.uk/23013/)

**证据允许的结论：**不能简单规定“发型永远不许变”，也不能假设“只改头发就不伤身份”。面向不熟悉本人的观众、且只有单张参考时，应更保守地处理发际线、发型轮廓、分缝和遮脸关系。

### 3. 单张照片不足以代表一个人的完整身份变化范围

同一人的自然照片变化可能很大；Jenkins 等人发现，陌生观察者会把同一个人分成多个身份，而熟悉观察者能正确归一。[Variability in photos of the same face](https://eprints.gla.ac.uk/67032/) 暴露于同一人的多张高变化照片，也比单张或低变化照片更能提升后续身份核验。[Variation in Photos of the Same Face Drives Improvements in Identity Verification](https://pubmed.ncbi.nlm.nih.gov/26562899/)

**产品推论：**高变化妆造不能只靠一句“same person”抵消风险。若用户要大改发型、重妆、年代妆或特效妆，多角度、不同表情的本人参考更有价值；但不应为普通妆发整理强制用户补图。

### 4. 服装是更低面部风险的叙事杠杆

行业职责明确把服装用于传达人物身份和故事。[Costume Designers Guild](https://costumedesignersguild.com/what-is-costume-design/) 实验也显示，仅替换同一张脸所配的上身服装，就能快速、稳定地改变观众对人物能力与社会地位的印象，说明服装能承担强叙事而无需重画面部。[Economic status cues from clothes affect perceived competence from faces](https://www.nature.com/articles/s41562-019-0782-4)

**产品推论：**职业、时代、阶层、阵营和故事状态应优先由服装轮廓、材质、层次、配饰承担；不要让面部妆容独自承担全部角色变化。服装仍可能是观众熟悉的个人标志，所以替换标志性服装或头饰仍应显式确认。

## 最小产品模型

不增加 agent、不增加强制步骤，只深化现有 Styling 维度：

1. **按需激活。** 只有妆造会实质改变故事、角色或本人外观时，才进入现有 Styling 选择；否则沿用本人造型或内部使用轻度整理默认值。
2. **明确所有权。** 实际“画在/穿在人物身上”的妆容、发型、服装与配饰归 Styling；数字磨皮、皮肤质感、全局色彩与成片表面归 First-Pass Finish。不要把角色妆容当成普通后期润色。
3. **一次解决一个整体 Look。** 复用现有 A/B/C + `D) Custom` 形式，每个可见选项只需说明：故事读感、妆发、服装/配饰，以及身份风险。不要分别问“妆怎么选、头发怎么选、服装怎么选”。
4. **内部只保留三档，不做参数表：**
   - `Preserve / Groom`：保留原妆发与标志性服装，只整理飞发、油光、临时瑕疵和服装状态；普通头像、职业照默认走这里。
   - `Character Styling`：妆、发、服装服务故事，但不替换受保护的身份线索；叙事肖像、海报、时尚编辑默认优先推荐这里。
   - `Transformation`：重妆、大幅换发型/假发、年代老化、舞台/特效妆或义体。只有实际触碰受保护锚点时才进入现有 identity risk-choice gate，不另建“美容风险流程”。
5. **系列才记录连续性。** 多图、多场景或角色弧需要一份简短 Look Continuity：发型轮廓/分缝/长度/颜色、妆容形状与强度、服装层次与配饰、故事时点、允许变化。单张图不创建新状态系统。

## 身份漂移控制：如何把握“还是这个人，但妆造成这样”

以下是基于研究与 CastMe 现有契约的**产品设计推论**，不是文献给出的数值标准：

1. **Identity First Read，Story Styling Second Read。** 在目标展示尺寸下，观众第一眼先认出这个人，第二眼才读到角色与妆造。若首先只看到“某种妆”或“某个发型”，说明妆造压过身份。
2. **明确不可替换项。** 保持脸型与骨相、五官比例、眉眼关系、鼻口下巴结构、肤色、年龄感、发际线和真实标志性痣/雀斑/疤痕；妆容只能围绕它们设计。
3. **按“替换了多少身份线索”判断风险，不按妆名判断。** 所谓自然妆若同时重画眉形、眼型、唇形、面部轮廓和肤质，仍是高风险；戏剧妆若保留结构、标志和可读轮廓，也可能仍可识别。
4. **避免叠加多个强变化。** 没有故事必要时，不要同时大改眉眼/轮廓、肤质、发型轮廓与颜色，再加入遮脸头发或头饰。需要叠加时，明确告诉用户 likeness 会下降，并让用户接受风险或补充本人参考。
5. **让服装先承担故事。** 可以大胆改服装、材质与配饰，再用妆发补充；只有故事确实要求面部变化时才提高妆容强度。
6. **实际图片输入始终优先。** Primary Identity Anchor 必须继续作为图片输入；高变化时可增加 supporting identity angles。文字里的“same person”不能代替本人图。
7. **生成后先审身份，再审妆造。** 先检查“像不像同一个人”，再检查妆发和服装是否讲对故事；失败时只回退造成漂移的妆造项，不重开场景、构图与其他锁定选择。
8. **“气质”只写可见结果。** 根据用户声明的角色/故事和参考图中可见的神态、线条、造型线索设计，不把外表推断成真实人格、身份或敏感属性。

## 何时跳过妆造设计

- 头像、证件感职业照、普通生活肖像，且原妆发/服装不妨碍用途。
- 用户明确要求保持当前妆发、衣服或“就像本人平时”。
- 脸部近景中服装几乎不可见，故事也不依赖角色转换。
- 用户已经给出足够明确的妆、发、服装要求，无需再给选择。
- 用户接受推荐默认值，且妆造不是 production-critical；内部执行 `Preserve / Groom` 即可。

应激活的典型情形：时尚编辑、电影海报、角色扮演、历史/职业服装、舞台或特效妆、显著换发型、系列连续性，以及原造型与目标角色明显冲突。

## 未回答与弱证据

- 妆容研究多集中于女性、日本或欧美样本，且“轻/重妆”的定义受文化、年代、肤色和场景影响；没有跨文化通用的安全强度。
- 实验研究测的是人类对真实或数字修饰照片的识别，不是 GPT Image 2 的身份保持率；不能把实验效应直接当成模型阈值或保证。
- 熟悉观众通常比陌生观众更能跨外观变化认人。CastMe 无法知道最终受众的熟悉度，面向公开传播时应按“弱熟悉/陌生观众”保守设计。
- 没有证据证明新增一个名为“化妆师”的 agent 会比深化现有 Styling 模块更好；这是产品组织问题，应通过 golden conversations 和实际生成对照验证。
- 没有可靠研究把一个人的“气质”唯一映射为某套妆发。该映射应被视为可讨论的创意判断，而不是对本人内在性格的事实判断。
- 没有科学支持固定的“一次只能改一个大项”规则；“避免同时替换多个身份线索”是可解释、可撤销的产品启发式。

## 最小验证建议

只需四个行为用例：普通头像跳过妆造；叙事海报启用整体 Look；重妆 + 大改发型触发已有身份风险选择；系列图保留 Look Continuity。视觉结果按同一顺序人工检查：**同一人第一读 -> 故事适配 -> 妆发服连续性**。不需要另造自动人脸分数或新评测系统。
