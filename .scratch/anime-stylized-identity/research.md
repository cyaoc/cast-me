# 二次元与 Q版 形象的 identity 保持可行性调研

调研日期：2026-07-31；补充调研：2026-08-03（§20–§24）、2026-08-11（§25–§31，画风谱系）、2026-08-12（tiling/grime 状态复核，见 `tiling-grime-status.md`）

## 结论

方向可行，但**当前 CastMe 的 identity 契约不能直接套用到绘制媒介**。设计讨论中仍有一部分决定只是推演，本文逐条标注了强度。

- 两阶段流程（先定形象、再产出应用）不是新发明，是 OpenAI cookbook 为"角色漂移不可接受的流程"给出的正式做法，称为 character anchor。[GPT Image Generation Models Prompting Guide §6.4](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)
- 变形比例（头身比）属于 anchor 阶段的锁定项，官方示例 prompt 里直接写了 `Proportions suitable for picture books (slightly oversized head, expressive face)`。这支持"变形契约必须在定稿阶段确定、不在每张图重新决定"。[同上 §6.4](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)
- 批量生成（一次 prompt 最多 8 张、整批统一规划）同时解决了**表情包成套**与**多角度设定图自身内部一致性**两个问题，两者是同一机制的两个用途。但它依赖 Thinking mode，属于付费层能力，必须写成能力边界。
- Q版 下身份通道会发生**转移而非衰减**：体型、身高、性别、年龄的身体差异归零，识别改由发型、服装、眼型和小记号承担。这是 chibi 绘制领域的既有共识，不需要我们发明。[Art Rocket](https://www.clipstudio.net/how-to-draw/archives/155423) [Dessindigo](https://dessindigo.com/en/blog/drawing-tutorial/chibi-drawing)
- 头身比本身编码年龄（日式惯例：成年 7–8、初中以上 6–6.5、小学生 4–5、chibi 2–3）。这意味着 4–5 头身对成年人是**年龄漂移陷阱档**，不是一个中性的中间选项。[Anime Art Magazine](https://animeartmagazine.com/head-to-body-ratio-this-simple-anime-illustration-technique-will-give-you-perfect-proportions-every-time/)
- photo-to-anime 有一个独立于 likeness 的高频失败模式：**半转换**（uneven stylization），眼睛与头发完全动漫化、皮肤质感与光照仍是照片。设计讨论中完全没有覆盖它。[Kalon](https://www.kalon.ai/templates/photo-to-anime-ai)
- **否定式表述有反向激活风险**：扩散模型研究发现负面提示可能反而诱导该概念出现。这直接影响身份通道预算的写法——"本档已关闭 X"这类关闭声明不应进 prompt。[Understanding the Impact of Negative Prompts](https://arxiv.org/html/2406.02965v1)
- 学术侧的 identity-preserving stylization 一致把身份表示为**结构关系**（明确点名眼距、脸型、发际线）而非表面细节，与 CastMe 现有的 Protected Identity Cue 思路同向，但现有清单里有若干项在绘制媒介下不可表达。[UniPortrait](https://arxiv.org/pdf/2408.05939) [PortraitBooth](https://arxiv.org/html/2312.06354)
- 多人物（情侣、合照）的困难有机制性原因，叫 identity blending：同一张生成的脸会同时 attend 到多个身份特征。这不是提示词层面能解决的问题。[UniPortrait](https://arxiv.org/pdf/2408.05939)
- **多轮编辑会累积噪点，这是机制性的，不是提示词问题。**成因已被隔离到自编码器的编解码往返：把编辑指令置空、只做"原样复制"，噪声照样累积。约 5–10 步后出现可见静态噪声、绿色色偏与散点，指令遵循能力同步下降。因此**编辑链深度是唯一可靠的控制变量**。[Banana100](https://openaccess.thecvf.com/content/CVPR2026W/A4VM/papers/Tang_Banana100_Breaking_NR-IQA_Metrics_by_100_Iterative_Image_Replications_with_CVPRW_2026_paper.pdf) [Iterative Multi-Granular Image Editing](https://openaccess.thecvf.com/content/WACV2024/papers/Joseph_Iterative_Multi-Granular_Image_Editing_Using_Diffusion_Models_WACV_2024_paper.pdf)
- **模型自己察觉不到在变脏，通用画质指标也测不出来。**23 个 NR-IQA 指标里 21 个给退化图更高的分；模型的 reasoning summary 会幻觉"已完成降噪"。脏化必须按可数的编辑链深度管理，不能靠看图或让模型自评。这直接约束 Identity Review 的可承诺范围。[Banana100](https://openaccess.thecvf.com/content/CVPR2026W/A4VM/papers/Tang_Banana100_Breaking_NR-IQA_Metrics_by_100_Iterative_Image_Replications_with_CVPRW_2026_paper.pdf)
- **`gpt-image-2` 不支持透明背景。**Q版表情包通常需要透明底，这是必须写进能力边界的硬限制。[Customize image output](https://developers.openai.com/api/docs/guides/image-generation#customize-image-output)
- 现有 identity 契约与绘制媒介的冲突不止 §2 那一条，共四条，全部源于"只承认相机投影这一种形变理由"。修法是给限制加媒介维度，不是放松强度。见 §24。
- **动漫画风不是一个外观，Q版 也只是比例维度而非画风。** 渲染维度上至少有七个可区分的成品外观（赛璐珞平涂、半厚涂、厚涂、水彩、无线稿、单色网点、卡通渲染 3D），各有可见特征清单。见 §26。
- **"渲染外观"在产业里不是一个维度而是两个前后叠放的阶段**：仕上（平面色彩语言）与撮影（光学质感）由不同职能决定。因此平涂与柔光扩散是正交选项而非同一光谱上的两点，复古/现代的差异也主要落在撮影层与色板上，不落在画法上。见 §25、§27。
- **§12 判定"唯一无行业对应"的色彩逻辑轴，结论错误。** 它对应「色彩設計／色彩設定」这一有决定权的专职岗位，产出物是色指定表；学术侧把角色配色形式化为约 11 个色槽位。它与阴影层数是不同层次的决定。见 §30。
- **不能给各个画风做可达性排序。** 只有类目级证据（动漫类整体易于物质媒介类、水彩落在最难的桶）。网点、无线稿、厚涂在文生图上的表现完全无证据。见 §31。

因此建议：**先按单人物、按档位展开的通道矩阵进入 PRD；多人物与批量连续生成写成能力边界，不写成承诺。**

## 设计假设与证据对照

强度标签的含义：`官方` 指 OpenAI 官方文档或 cookbook；`学术` 指论文；`行业/实践` 指绘制行业教程与 photo-to-anime 实操报告；`未验证` 指有第三方说法但本次未核实到一手来源；`推演` 指本次讨论推出、目前无任何外部依据。

| 设计决定 | 证据 | 强度 |
| --- | --- | --- |
| 两阶段：先定稿、后应用 | cookbook character anchor 正式用例 | 官方 |
| 变形比例在定稿阶段锁定 | cookbook anchor 示例含比例指令 | 官方 |
| 画风参考图可行 | cookbook §5.1 Style Transfer | 官方 |
| 多图按角色标注、说明交互关系 | cookbook Prompting Fundamentals | 官方 |
| 每轮重复 preserve list 抑制漂移 | cookbook Constraints | 官方 |
| 跨多次生成的角色一致性不可保证 | Image generation limitations | 官方 |
| 批量参数 `n` 支持 1–8 张 | 官方模型页与 cookbook 示例 | 官方 |
| Thinking mode 下整批 8 图保持角色一致 | 多个第三方来源一致且描述具体，未核实到官方原文 | 行业/实践 |
| 批量可一次产出多角度参考包 | 同上，解决三视图自身一致性问题 | 行业/实践 |
| chibi 范围 2–4 头身，常用 2–3 | 多个绘制教程一致 | 行业/实践 |
| 主要分界在 2 vs 3 头身 | 2/3 头身的圆度、简化度、五官垂直位置、手指处理差异 | 行业/实践 |
| 头身比编码年龄 | 日式头身比与年龄对应惯例 | 行业/实践 |
| Q版 体型通道完全关闭 | chibi 体型不随原设计性别/身高/年龄变化 | 行业/实践 |
| 服装在 Q版 下承担识别功能 | chibi 识别依赖发型、服装、眼型、小记号 | 行业/实践 |
| 记号类特征（痣、疤、黑眼圈）是主力通道 | 同上 | 行业/实践 |
| 剪影是最稳的通道，需在缩略图尺寸成立 | 角色设计剪影测试 | 行业/实践 |
| 半转换是高频失败模式 | photo-to-anime 实操报告 | 行业/实践 |
| 风格化强度是双端失败的连续谱 | 同上 | 行业/实践 |
| 定稿阶段保持原头部角度与表情更利于对齐 | 同上 | 行业/实践 |
| 眼睛画法是强画风识别轴 | 眼睛渲染因艺术家与作品差异显著 | 行业/实践 |
| 背景处理是独立于角色画法的维度 | 日本动画产业里背景美术为独立职能，美术监督专责协调两者 | 行业/实践 |
| 定稿漂移随重做次数累积 | 单一第三方报告 + 用户一手体感确认，无量化拐点 | 行业/实践 |
| 身份表示为结构关系而非表面细节 | identity-preserving 主流方法 | 行业/实践 + 学术 |
| 年龄感有可分离的视觉编码 | anime 风格空间中的年龄维度 | 学术 |
| 多人物 identity blending | UniPortrait 问题陈述 | 学术 |
| 否定式表述有反向激活风险 | Reverse Activation（机制在有独立负面字段的扩散模型上验证） | 学术（迁移待验证） |
| 神态习惯携带身份信息 | dynamic identity signature，但受两个前提约束 | 学术 |
| 神态权重随用途与档位变化 | 由上述两个前提推出 | 学术 + 推演 |
| 系统自适应选项弱于固定选项 | 菜单研究：静态显著快于自适应，adaptable 最受偏好 | 学术（场景差异见 §19） |
| Medium Contract 作为条件触发的路径分支 | 无 | 推演 |
| 身份通道预算能提升 likeness | 正向效果无证据；反向风险已有依据 | 推演 + 反向证据 |
| 通道预算仅在有损时对用户可见 | 无（交互设计选择） | 推演 |
| 画风六轴的完整性 | 线条、上色、眼睛、背景有支持，质感经网点部分支持；色彩逻辑无 | 部分推演 |
| 画风名转译为可见特征 | 无外部依据，但与仓库既有"用可见锚点不用标签"原则一致 | 推演（§22 后补上一条独立理由） |
| `gpt-image-2` 不支持透明背景 | 官方 image generation guide | 官方 |
| `input_fidelity` 对 `gpt-image-2` 不可设置，且带参考图的 edit 更贵 | 同上 | 官方 |
| 参考图张数没有"最多 4 张"的上限 | 官方虚拟试衣示例一次传 5 张 | 官方 |
| 多轮编辑累积噪点，成因是编解码往返 | 空指令复制实验隔离出自编码器往返 | 学术 |
| 5–10 步出现可见散点与色偏 | Banana100 100 步复制实验 | 学术（模型为 Nano Banana Pro，迁移待验证） |
| 显式降噪指令无效 | 同上，20 步时带降噪与不带同样退化 | 学术 |
| 高频细节与小记号最先被简化 | Banana100 Simplification Bias | 学术 |
| 模型与通用画质指标都检测不到退化 | 21/23 指标反向，模型自评滞后且幻觉 | 学术 |
| 编辑几乎必然为对齐分辨率档而裁切 | Banana100 Aspect-Ratio Mismatch | 学术（迁移待验证） |
| GPT Image 2 有独立的 tiling / grime artifact | 论坛长贴汇总 + 具名 OpenAI 工程师公开回复 | 行业/实践 |
| 高频微结构上 artifact 最重、平坦人工表面最轻 | 同上 | 行业/实践 |
| `in the style of 艺术家名` 会因网页参考检索污染上下文而加重 artifact | 同上 | 行业/实践 |

## 官方依据

### 1. character anchor 是官方推荐的角色一致性流程

cookbook §6.4 `Children's Book Art with Character Consistency` 的定位是"多页插画流程中角色漂移不可接受"的场合，原文：`A reusable "character anchor" ensures visual continuity across scenes, poses, and pages while allowing environmental and narrative variation.`

流程是两步：

1. `images.generate` 产出 anchor，目标写明 `Lock the character's appearance, proportions, outfit, and tone`，背景要求干净以突出角色；
2. `images.edit` 带上 anchor 图，prompt 内含 `Character Consistency` 段落逐条列出不变量，并显式写 `Do not redesign the character`。

这直接支持两阶段设计，也支持"定稿图作为后续所有生成的实际图像输入"。[Prompting Guide §6.4](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

### 2. 变形比例属于 anchor 的锁定项

同一节的 anchor prompt 里，比例是和画风并列写出的：`Proportions suitable for picture books (slightly oversized head, expressive face)`。

两点含义：官方认为为插画目的调整头身比是正常需求，不是缺陷；比例属于 anchor 要锁定的内容，不是每张图重新决定的变量。后者对 CastMe 尤其重要，因为现有 `identity-anchor.md` 把"结构性大头、压缩躯干、小型四肢、玩偶感解剖"列为 Avoid，且只承认相机投影能解释它。

### 3. 画风参考与多图角色分工

cookbook §5.1 Style Transfer 的做法是描述"什么必须保持一致（style cues）、什么必须改变（new content）"，并加硬约束防漂移。Prompting Fundamentals 的 Multi-image inputs 要求按序号与描述引用每张输入（`Image 1: product photo… Image 2: style reference…`）并说明它们如何交互。

CastMe 现有的多图角色标注机制与此一致，可直接扩展出画风参考这一角色。

### 4. 批量生成与 Thinking mode

`n` 参数是官方批量参数，取值 1–8，cookbook 的 logo 示例用 `n=4` 一次得到四个方案。[GPT Image 2 Model](https://developers.openai.com/api/docs/models/gpt-image-2)

多个第三方来源一致描述：在 Thinking mode 下，一次 prompt 可产出最多 8 张连贯图像，角色、物体位置与视觉风格在整批中保持一致，原因是整批作为**一组统一规划**而非八次独立生成。Thinking mode 限 Plus / Pro / Business / Enterprise，免费层只有 Instant mode。有来源直接指出该能力最适合做 front / side / back / expression 参考包。[Flick](https://flick.art/blog/gpt-image-2-guide) [cuty.ai](https://www.cuty.ai/article/models/what-is-gpt-image-2) [CallSphere](https://callsphere.ai/blog/gpt-image-2-launch-overview-capabilities-2026)

对设计有两处影响：

- 表情包成套与多角度设定图是**同一机制的两个用途**。上一轮讨论中提出的"三视图自身的内部一致性谁保证"，答案是同批规划。
- `n` 产出并列变体还是连贯帧取决于 prompt 与模式，不是参数本身的固定语义。本文档早前版本断言"`n` 只产出并列变体、不可用于连续帧"，该断言不准确，已修正。

证据强度说明：`n` 的取值范围有官方依据；"整批一致"的行为描述来自多个独立第三方来源，措辞具体且互相吻合，但本次未核实到 OpenAI 官方原文。实操侧有报告称 8 张中约 5–6 张可用、2–3 张需单独重做，属单一来源。

### 5. 一致性不可保证

API 文档仍把 recurring characters 的视觉一致性列为已知限制，视觉理解也有已知误差。因此本需求同样只能是 best effort，Identity Review 不能升级为保证。[Image generation limitations](https://developers.openai.com/api/docs/guides/image-generation#limitations) [Vision limitations](https://developers.openai.com/api/docs/guides/images-vision#limitations)

## 行业与绘制实践

### 6. chibi 档位与各档的具体差异

chibi 通常 2–4 头身，最常用 2–3 头身；头部是全身的度量单位，第一个头长永远由头部占满，决定观感的是身体如何分配剩余高度。[CrimsyCreates](https://tips.clip-studio.com/en-us/articles/4953)

2 头身与 3 头身的差异是成体系的，可直接作为档位参数：[あまちゅう](https://tips.clip-studio.com/en-us/articles/4899)

- 比例越矮，形状越圆——2 头身的发梢、轮廓、眼睛、耳朵都比 3 头身更圆；
- 比例越矮，简化越多——2 头身省略头发分块，整体信息量刻意压低；
- 2 头身的五官垂直位置比 3 头身更靠下；
- 比例越高，身形越修长，3 头身需要比 2 头身定义更清晰的形状。

手部处理有明确分界：3 头身可以画手指细节，2 头身建议把手简化为拇指与四指两块。3 头身画出胸腰臀曲线会显得更成熟。[Art Rocket](https://www.clipstudio.net/how-to-draw/archives/155423)

比例分配的常用规则：2 头身为脸 1 : 身 1（躯干与腿各占身体的一半），3 头身为脸 1 : 躯干 1 : 腿 1。

### 7. 头身比编码年龄

日式插画的头身比与年龄有固定对应：成年 7–8 头身、初中以上学生 6–6.5、小学生 4–5、chibi 2–3。[Anime Art Magazine](https://animeartmagazine.com/head-to-body-ratio-this-simple-anime-illustration-technique-will-give-you-perfect-proportions-every-time/)

这条对档位设计有直接后果：4–5 头身不是"轻度 Q版"的中性选项，它在观感上会把成年人读成儿童。年龄漂移因此有两个来源——模型的默认偏好，以及比例本身携带的语义。

### 8. Q版 下的通道转移

chibi 会抹平原设计的身体差异：不论原角色的性别、脸大小、身高、体型、年龄如何，做成 2–3 头身后体型基本相同，一个六头身女孩和一个八头身男人的 chibi 体型是一样的。[Art Rocket](https://www.clipstudio.net/how-to-draw/archives/155423)

识别因此必须换通道承担。chibi 教学的原话是：chibi 都是大头、大眼、小身子，基本形状一样，要让人认出来就得 `Focus on the small details that characterize them`，具体点名发型、服装、眼型，以及疤痕、黑眼圈、纹身这类小记号。[Dessindigo](https://dessindigo.com/en/blog/drawing-tutorial/chibi-drawing)

同一来源还指出 chibi 会**强化**角色的标志性特征以便一眼认出，即通道转移伴随通道加权，不只是丢弃。

### 9. 剪影测试与缩略图可读性

角色设计的第一道检验是剪影测试：填成单一平色、去掉所有内部细节后仍应可辨认，并且必须在缩略图尺寸下成立。强剪影的判据包括用负空间分离四肢与躯干、避免轮廓杂乱、保留一两个标志性的剪影缺口。[Coartist](https://coartist.net/blog/character-design-readability-silhouette-shape-language-contrast) [Walt Disney Family Museum](https://www.waltdisney.org/sites/default/files/2020-05/T%26T_Silhouette-final2.pdf)

有一句直接支持"发型轮廓是最稳通道"：强剪影能在光照、取景、服装、上色、细节的任何变化下存活。[Paul Temple Studios](https://www.paultemplestudios.com/paultemple/silhouette-test-character-design)

迪士尼那份材料还建议用四分之三视角，因为它能暴露正面视角看不到的两侧差异。这与"正面最利于识别"存在 tradeoff；若定稿采用批量多视角参考包（§4），两者可以同时满足。

### 10. 半转换是最常见的失败模式

`uneven stylization`：模型把一部分特征完全转换（通常是眼睛与头发），另一部分留在照片状态（通常是皮肤质感与光照），产生诡异的混合体。[Kalon](https://www.kalon.ai/templates/photo-to-anime-ai)

给出的对策是正面写明皮肤也提交到赛璐珞语言，负面挡掉 `half-converted, mixed styles, partially realistic`。

这是一个独立于 likeness 的失败轴，设计讨论中完全没有覆盖。

### 11. 风格化强度是双端失败的连续谱

`Push stylization too little and you get a filtered photograph. Push it too far and the model replaces individual features with its default anime face.` 理想结果是保留可识别的结构，同时刻意重做线条、色彩、光照与背景。[Elser AI](https://www.elser.ai/blog/how-to-turn-a-photo-into-anime-with-elser-ai)

同一来源的其他可用实践：

- 不要要求保留每一个毛孔，动漫化本来就是简化，目标是保护结构关系；
- 去掉模糊的美化词，它们会诱导模型给出默认的理想化脸（与 CastMe 现有的形容词约束规则一致）；
- 风格化强度逐层加，不要一次拉满；
- 换姿势或加动作之前先建立可复用的角色设定图；
- 定稿阶段保持原始头部角度与表情，变量越少越容易对齐。

其示例 prompt 的结构与本次设计高度一致：先给具体结构特征（椭圆脸、直的深色眉、微微下垂的棕眼及其间距、长鼻梁、窄上唇、右分黑色波浪发、圆形银框眼镜），再给画风参数（中等线宽、克制的赛璐珞），最后显式禁止改变年龄、族裔、眼镜形状、发型。

注意其中保留了"长鼻梁"——这说明**等身 anime 仍可承载鼻梁与上唇厚薄**，存活率是档位的函数，不能按媒介一刀切。

### 12. 画风轴的行业对应

- 赛璐珞的定义是离散、不混合的阴影层；线稿通常用高对比、不透明的笔（G-pen）。[Art Rocket](https://www.clipstudio.net/how-to-draw/archives/162911)
- 日式有 1/2/3 阴影系统：第一层阴影最重要，动画通常只用第一层，插画才加第二、第三层，第三层用于环境光遮蔽。这比"赛璐珞"这个笼统说法可控得多，可作为上色轴下的具体参数。[1/2/3 Shadow system](https://www.youtube.com/watch?v=Mc19XdEe8qg)
- 学术侧做 manga 风格分类使用的特征是线段密度、线间夹角、网点（screentone）纹理与分格特征。[Line-Based Drawing Style Description for Manga Classification](https://dl.acm.org/doi/10.1145/2647868.2654962)

对比讨论中拟定的六轴（线条、上色、眼睛画法、色彩逻辑、质感后期、背景处理）：线条、上色、眼睛三轴有明确支持；背景轴见 §13；网点应补入质感轴；阴影层数应补为上色轴的参数；只有色彩逻辑一轴未找到对应的行业分类依据，暂列为推演。

**本节的两条结论已在 2026-08-11 的补充调研中被推翻或细化：色彩逻辑轴有明确的产业与学术对应（§30）；"上色"不是一个轴而是两个前后叠放的阶段（§25）。以 §25–§31 为准。**

### 13. 背景处理是独立职能

日本动画产业里背景美术与角色作画是分开的职能，背景常由不同的人甚至不同公司制作——存在专门做背景的公司为多个工作室服务。美术监督（bijutsu kantoku）统管背景美术，其职责明确包含**确保背景与赛璐珞角色不冲突**。[美術監督](https://ja.wikipedia.org/wiki/%E7%BE%8E%E8%A1%93%E7%9B%A3%E7%9D%A3) [Animation Obsessive](https://animationobsessive.substack.com/p/the-origin-of-a-master-painter) [Anime StackExchange](https://anime.stackexchange.com/questions/3941/are-background-and-foreground-delegated-separately-in-anime-production)

工作流分三层：[穴吹デザイン専門学校](https://web.anabukih.ac.jp/become/123781/)

1. **美術設定**：用线画画出世界观与场景的结构蓝图，确保建筑结构与尺度不与角色矛盾；
2. **美術ボード**：由美术监督绘制的概念画，确定背景的色味、照明、时间带、天气，作为全组共享的基准资料；
3. **背景画制作**：以美术ボード为参照量产实际背景。

两点对设计有用。其一，这证实背景处理是独立于角色画法的轴，而且行业专门设岗协调两者的和谐——正对应讨论中"背景轴与 Shot Direction 边界"的问题：Shot Direction 管背景是什么，背景轴管背景怎么画。其二，**美術ボード与本设计的"定稿"是同构物**，只是它锚定背景而定稿锚定角色。

一位美术监督的自述贴合这个边界：做背景画师时那种"不考虑与赛璐珞的和谐、只想画一张独立作品"的自我会消失，必须考虑与角色的和谐。

需要注意：本节只证实背景是独立轴，并未证实讨论中拟定的四个背景档位（厚涂 / 简略 / 照片感 / 纯色）。

## 学术侧

### 14. 身份表示为结构关系

identity-preserving 的主流做法是用人脸编码器提取结构特征后注入生成过程，综述性描述明确点名眼距、脸型、发际线。tuning-free 方法的两个已知短板是难以保留面部形状与纹理细节、以及倾向于复制参考脸而难以编辑，根因被归结为 `intrinsic face identity` 与 `face-relevant yet identity-irrelevant representations` 解耦不足。[UniPortrait](https://arxiv.org/pdf/2408.05939) [PortraitBooth](https://arxiv.org/html/2312.06354)

这个解耦问题正是本设计中 what/how 分离要处理的同一件事：签名特征提供 what（细长眼型、眼距偏宽），画风参考提供 how（线宽、高光数量、睫毛处理）。二次元的特殊困难在于画风主要体现在脸的画法上，两者在同一处像素上。

face stylization 方向的综述也记录了同类失衡：风格常常压过内容以致丢失人脸信息，或内容保住但与风格参考的相似度过低。[ConstFS](https://dl.acm.org/doi/10.1145/3769534.3769555)

### 15. 年龄感的可分离视觉编码

一项 anime 肖像风格空间研究发现其中一个风格维度专门控制年龄观感：往成熟方向增加时，脸颊变得不那么圆、下颌更长更尖、眼睛更小、上眼睑更平。[Anime Style Space Exploration](https://ar5iv.labs.arxiv.org/html/1805.07997)

这使年龄漂移可以用四个具体量约束（脸颊圆度、下颌长度与尖锐度、眼睛相对大小、上眼睑平坦度），而不是抽象地要求"保持年龄感"。

### 16. 多人物的机制性困难

多身份定制的主要挑战是 identity blending——同一张生成的脸同时 attend 到多个 ID 特征。这是方法层面的问题，不是提示词能规避的。[UniPortrait](https://arxiv.org/pdf/2408.05939)

实践侧的观察与此吻合：批量一致性在单主角加稳定环境下最好，两个以上外观各异的角色会显著提高漂移概率。

### 17. 否定式表述的反向激活风险

一项研究负面提示作用机制的工作发现了 **Reverse Activation**：在扩散早期引入负面提示，会反而导致该物体出现。论文的直接例子是把 `Glasses` 作为负面提示施加在前 3 步，最终输出反而生成了眼镜。[Understanding the Impact of Negative Prompts](https://arxiv.org/html/2406.02965v1) [ECCV 2024 PDF](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/12484.pdf)

机制有两条：

- **Inducing Effect**：负面提示会推高该概念方向上的估计噪声，即使正面提示里完全没有提到它；
- **Momentum Effect**：估计噪声倾向于保持既有方向，一旦被诱导就会持续。

论文还记录了**延迟效应**：负面提示的作用晚于正面提示，因为它必须等正面提示指定的目标先出现，才能 attend 到正确位置。

迁移边界必须写清楚：该研究的对象是带独立 negative prompt 字段、通过 classifier-free guidance 施加负面条件的扩散模型；GPT Image 2 是在正文 prompt 里写 `no watermark` 这类约束，机制不同，结论不能直接套用。

但它足以把讨论中的担心从直觉升级为有机制依据的风险，并给出一个可操作结论：**身份通道预算的三栏应有不同去向。**主力通道与次要通道是正面表述，可进 production prompt；"本档已关闭鼻梁"这类关闭声明是否定表述加元信息，只用于生成前的期望管理与生成后的 Review 对照，不进 prompt。确需在 prompt 中表达时应改为正面说法（"鼻子简化为一个点"），而非否定说法（"不画鼻梁"）。

这同时为 CastMe 现有那条"负面约束控制在约三到八条、且必须是可观察的失败模式"的规则提供了理论支持。

### 18. 神态习惯是动态身份签名，但受两个前提约束

神态习惯在心理学里称 idiosyncratic facial motion 或 dynamic identity signature，确实携带身份信息。有研究用面部关键点相对中性基线的位移训练判别模型，能以 45% 准确率跨六种表情辨认 24 名演员的身份（p<0.001）。[Idiosyncratic facial motions](https://doi.org/10.1167/jov.24.10.545) [Frontiers in Psychology](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.01211/full)

但被反复引用的 O'Toole 等人的结论给出了两个前提：这套次级识别系统要起作用，**观察者必须熟悉这张脸**（必须已经知道此人的习惯动作），且**观看条件必须较差**——否则更可靠的静态图像编码会主导识别，动态系统不会被启用。同时，越熟悉的脸，动态线索越重要，说明动态签名是随接触持续习得的。[Memory for Moving Faces](https://doi.org/10.7551/mitpress/8349.003.0005) [Exploring the Motion Advantage](https://doi.org/10.1080/17470218.2016.1138974)

把两个前提映射到本设计的用途上，结论是**神态的权重是场景的函数，不是恒定值**：

- **Q版表情包**：静态线索被极度简化（条件差）＋观众是认识本人的朋友（熟悉），两个前提同时成立，神态权重高；
- **社交头像**：观众多为不熟悉本人者，前提不成立，权重低；
- **等身 anime**：静态结构线索充足，静态编码主导，权重低。

还有一条技术限制：上述研究提取签名依赖**多个表情**的数据，从中找出跨表情稳定的个体模式。单张参考照片提取不出"跨表情稳定"的东西，因此讨论中担心的"把一次瞬间当成习惯"是成立的风险。

## 交互设计侧

### 19. 系统自适应选项弱于固定选项

菜单研究已有明确结论：在对照实验中**静态菜单显著快于系统自适应菜单**，因为自适应重排破坏空间一致性，妨碍用户建立可靠的心智模型；而 **adaptable（用户可控的定制）**最受偏好，且在用户具备布局经验后效率接近静态菜单。后续研究进一步表明连续选择时位置恒定的用户显著更快。[Findlater & McGrenere, CHI 2004](https://doi.org/10.1145/985692.985704) [论文全文](https://www.cs.ubc.ca/labs/imager/th/2004/Findlater2004/Findlater2004.pdf) [Constant serial positions](https://doi.org/10.1201/9781003417217-14)

讨论中"档位按用途自适应生成三档"在这个分类里正对应表现最差的 adaptive。

场景差异需要说明：菜单研究针对**反复使用同一组项目**的场景，空间记忆是关键变量；本设计面对的是一次性创作决策。而且本设计的自适应并非按使用频率重排，而是按已锁定的上下文生成相关选项，更接近上下文菜单。因此这是警示而非否证——真实风险落在重度用户身上：每次看到的档位都不同，无法建立稳定预期。

研究给出的最优形态是 adaptable，其在 CastMe 中的对应物是既有的 `D) Custom` 路径。

由此得到一个折中方案，可能优于原推演：**语义标签固定、具体数值随用途变化**。三档恒定为"保守 / 标准 / 强变形"，表情包用途下对应 3 / 2.5 / 2 头身，头像用途下对应 等身 / 微变形 / 轻 Q版。位置与语义稳定，内容适配上下文。

## 工具与工程侧

### 20. GPT Image 2 的能力边界更新

本次复核官方文档，四条与本设计直接相关：

- **不支持透明背景。**`background: "transparent"` 对 `gpt-image-2` 不受支持。Q版表情包通常要透明底，这是硬边界；官方在产品图一节给出的做法是输出不透明背景后再走下游抠图。[Customize image output](https://developers.openai.com/api/docs/guides/image-generation#customize-image-output)
- **`input_fidelity` 已不可设置。**官方原文：`For gpt-image-2, omit this parameter; the API doesn't allow changing it because the model processes every image input at high fidelity automatically`。好处是身份编辑不必再挑保真度档；代价是带参考图的 edit 请求 input token 明显更高，官方专门提示了成本影响。注意 cookbook §5.6–5.9 的示例代码仍在给 `gpt-image-2` 传 `input_fidelity="high"`，与官方模型表和 API 指南矛盾，属未更新残留，不要照抄。[Image input fidelity](https://developers.openai.com/api/docs/guides/image-generation#image-input-fidelity)
- **尺寸约束。**任意分辨率，但长边 ≤3840、双边为 16 的倍数、长短边比 ≤3:1、总像素 655,360–8,294,400。超过 2560×1440 官方标注为实验性、结果更不稳定。[Size and quality options](https://developers.openai.com/api/docs/guides/image-generation#size-and-quality-options)
- **参考图张数没有 4 张上限。**第三方资料常写"最多 4 张输入图"，但官方虚拟试衣示例一次传了 5 张（1 人 + 4 件单品）。这个数字不要写进 PRD。[Prompting Guide §5.2](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

### 21. 多轮编辑会累积噪点，这是机制性的

用户一手观察：多次修改同一张图后画面出现大量脏点、整体发脏。这是有名字的已知现象——iterative degradation / generational loss，成因已被学术工作隔离清楚。

**成因**：编辑要把图编码进潜空间再解码回像素，这个往返不是无损的。WACV 2024 的工作把编辑指令置空、只反复做 `I(e+1) = D(E(I(e)))`，噪声照样累积，从而证明**自编码器往返本身就是噪声源，与改了什么无关**。其解法是 latent iteration：把潜表示直接传给下一步，不重新编码解码后的像素。这是架构层修改，API 使用者拿不到——但它解释了为什么"回到源头图重来"有效而"在结果上继续修"无效。[Iterative Multi-Granular Image Editing](https://openaccess.thecvf.com/content/WACV2024/papers/Joseph_Iterative_Multi-Granular_Image_Editing_Using_Diffusion_Models_WACV_2024_paper.pdf)

**表现与拐点**：CVPR 2026 Workshop 的 Banana100 用"原样复制、不做任何改动"这个空操作跑了 100 步，结论具体：

- 约 **5–10 步**后出现可见的静态噪声、绿色色偏和**散点**（scatter points），正对应用户说的"脏点"；
- 伪影出现在**从未被要求修改的区域**；
- 指令遵循能力同步下降，后期连"在桌上加一个苹果"都做不到；
- **Simplification Bias**：角色表情网格的四种瞳色在第 2 步就被简化为两种；
- **Persistent Noise**：每轮 prompt 里显式写降噪指令**无效**，20 步时带降噪与不带降噪同样发绿、同样丢质感；模型的 reasoning summary 声称已降噪，实际没有；
- **Aspect-Ratio Mismatch**：复制时几乎必然裁切，以把输出对齐到某个分辨率档位；
- 模型**无法利用上下文里更早的干净图**自我纠正。

[Banana100 论文](https://openaccess.thecvf.com/content/CVPR2026W/A4VM/papers/Tang_Banana100_Breaking_NR-IQA_Metrics_by_100_Iterative_Image_Replications_with_CVPRW_2026_paper.pdf) [数据集](https://huggingface.co/datasets/kenantang/Banana100)

**检测不到**：23 个 NR-IQA 指标里只有 2 个能一致识别退化，其余 21 个给噪声图更高的分——某张图复制 20 次后 BRISQUE 从 34.1 掉到 -9.8（越低越好），与人眼判断完全相反。只有基于大 VLM 的 RALI 与 VisualQuality-R1 检出了全部退化。模型自评同样不可靠：平均要到第 20–37 步才第一次提到噪声，人眼 5–10 步就看见了。

**普适性与迁移边界**：Banana100 的主体是 Nano Banana Pro，另验证了 Nano Banana 2 Fast、FLUX.2 [dev] 与 Qwen Image Edit，三者都退化但噪声形态不同（皱纹 / 散点 / 质感简化加错误复制）。**未包含 `gpt-image-2`**。该数据集还**刻意排除了写实人脸**作为初始图，理由是人脸畸变过于不适——对本需求最关心的那类内容恰好没有数据。所以：机制普适性有依据，`gpt-image-2` 的具体拐点没有学术数据，不要写成"第 N 步开始变脏"。

### 22. GPT Image 2 另有一个独立的 tiling / grime artifact

这一条独立于 §21 的迭代退化，是 `gpt-image-2` 发布当天就被大量报告的问题，OpenAI 至今没有公开技术说明。社区称之为 tiling texture、grime、checkerboard、digital ripples。证据强度为 行业/实践：来源是 OpenAI 开发者论坛长贴的二手汇总，但可追溯到具名 OpenAI 工程师的公开回复。[apipass 汇总](https://apipass.dev/blogs/gpt-image-2-launch-tiling-texture-artifact)

- **两种形态**：一是基线噪声，干净会话里的第一张图也可能带；二是放大效应，同一会话里连续生成时逐张加重，第三到第五张可能不可用。OpenAI 在发布后数日修掉了放大效应，基线噪声仍在。
- OpenAI 工程师 Boyuan Chen 在发布后公开表示正在修（2026-04-24 起；2026-05-04 前后仍为 working on it 族回复），并有「修好后会亲自宣布」的社区复述。**2026-08-12 复核：未见该宣布落地。**更晚的一手信号是 OpenAI Peter Bakkum 于 2026-08-06 仍称正在处理 noise、野外持续可见。[Community 长帖](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535) [Bakkum 推文](https://x.com/pbbakkum/status/2085426695633580292) 同会话放大效应在 2026-04-24 前后被社区报告为「明显缓解」，但首帖（2026-05-12）仍保留残差放大条目；基线噪声在公开信息中**未**被宣布清除。强度：官方（工程师公开回复）+ 行业/实践（论坛）。**未做**本次生成实测。PRD 不应假设它已消失，也不应写成永久缺陷。详见 `tiling-grime-status.md`。
- **强度与画面内容强相关**：玻璃、岩石、结构化云、沙、织物纹理、毛发这类高频微结构最重；平坦人工表面、均匀背景、细节少的画面最轻。
- 论坛实测（用户 `_j`）用 API 的 edits 端点反复把输出喂回输入，几轮后出现与 ChatGPT 里相同的斑驳与块状叠加——**噪声跟着"有图片输入"这件事走，与是不是有状态会话无关**。这与 §21 的机制一致，也说明"改用 API"本身不解决问题，只有"不把生成结果当输入"才解决。
- **`in the style of 某艺术家 / 某流派` 会加重 artifact**，因为 thinking mode 会去检索网络参考图，检索回来的图片进入生成上下文形成污染。改为用自己的话描述画风（光照、色板、构图取向）更干净。**虚构或极冷门的画风名是最可靠的重度 artifact 触发条件之一**，模型不会优雅降级。
- 有一个流传说法称 `gpt-image-2` 是自回归架构、token 只解码一次，因此"绕过了 VAE 重编码损失、多轮编辑稳定性远超扩散模型"。这与用户一手观察、上述论坛 API 实测以及 artifact 的存在都矛盾，且 OpenAI 未公开过架构细节。**不要采信。**

### 23. 迭代退化对本设计的直接后果

**编辑链深度是唯一可靠的控制变量。**唯一被证据支持的对策是少做几步，并且每一步都从**干净的源头**出发，而不是从上一轮结果出发。提示词层面的补救都很弱：显式降噪指令被论文证明无效；`Remove the noise while keeping all the lines` 这类清理 prompt 只有单一来源说有时有用；`让画质更好 / 精修一下`这类模糊词反而会触发过锐化与加对比，把脏点变得更明显。

这给 CastMe 的三条既有规则补上了一个与身份无关的第二理由：

1. **"最多一次自动修正，之后停止并如实报告"**原本只是防无限重试，现在有了机制依据：第二次修正已经在把编辑链推向退化区。这条应保留，不应放宽。
2. **"身份整体漂移时排除失败图、从 Primary Identity Anchor 重生成"**原本的理由是不让坏脸进输入，现在还要加上切断噪声链。而且论文证明**模型无法利用上下文里更早的干净图**自我纠正，所以这条必须是真的更换实际图片输入；靠 prompt 写"参照更早那张"不成立。
3. **Identity Review 不能靠模型自评判断脏化。**模型比人眼晚 10–30 步才察觉，且会幻觉"已降噪"。脏化应作为**可数的结构性指标**管理（本次生成处在编辑链的第几层），而不是一个视觉判断项。

对 Q版 与成套产出的具体风险：

- **Simplification Bias 直接打击 Q版 的识别方案。**§8 的结论是 Q版 靠发型、眼型和小记号（痣、疤、黑眼圈）承担识别，而这些正是最先被简化掉的高频细节——论文里四种瞳色两步就变成两种。这使"多角度与整套表情必须一次生成"从效率问题升级为**身份问题**：逐张编辑推进会系统性地磨掉承担识别功能的那几个通道。§4 的批量与多面板结论因此得到加强。
- **裁切风险影响成套一致性。**编辑几乎必然为对齐分辨率档位而裁切，成套表情要求同尺寸时需显式校验。
- **画风轴的风险分级。**artifact 与迭代退化都在高频微结构上最重、在平坦人工表面最轻。赛璐珞平涂加干净背景的 Q版 恰好落在低风险区；厚涂背景、网点质感、飘散发丝、粒子特效落在高风险区。这为 §12 的质感轴与 §13 的背景轴提供了一个此前没有的风险维度。
- **画风参考的写法多了一个理由。**§22 的 style lookup 污染与仓库既有的"用可见锚点、不用画风标签"原则同向：写"细线、两层赛璐珞阴影、眼下无睫毛"比写"某某老师画风"既更可控，也更干净。

## 与现有 identity 契约的冲突

### 24. 四条把"相机投影"当成唯一合法形变解释的条款

`identity-anchor.md` 的限制强度本身没有问题，问题是这些限制被写成了媒介无关的常量：整份契约只承认一种形变理由——相机投影。§2 已点出其中一条，完整清单是四条。

| 条款 | 位置 | 冲突 |
| --- | --- | --- |
| `structurally oversized head, compressed torso, miniature limbs, or doll-like anatomy not explained by the selected projection` | Reference Transfer 的 Avoid 列表 | 唯一豁免是相机投影，而 Q版 是绘制约定。官方 cookbook §6.4 的 anchor prompt 直接写 `Proportions suitable for picture books (slightly oversized head, expressive face)`，本条会把官方推荐做法判成缺陷 |
| `age drift` | 同上，无任何前提 | 头身比编码年龄（§7），2–3 头身必然读作幼态。绘制媒介下本条自相矛盾 |
| `A review passes only when no source-supported Protected Identity Cue shows material, unaccepted drift`，及其后的 `Recognizability alone is insufficient` | Identity Review and Revision | Protected Identity Cues 是媒介无关的固定清单，含鼻根、鼻翼宽、人中长度、唇珠、皮肤质感等 Q版 下不存在的通道。强风格化会让多数条目发生 material change，Review 必然失败并触发那次自动修正，而修正方向是往照片拉回，正好制造 §10 的半转换。后半句对照片正确，对 Q版 相反——Q版 下可识别性恰恰是唯一有意义的判据 |
| `no waxy or plastic skin, no over-smoothed skin` | Identity Prompt Constraints，写在通用的 Face and identity 项内 | 同一段的 Style-specific finish 项懂得加 `for photorealistic requests` 前提，本项漏了。赛璐珞平涂本质上就是"过度平滑的皮肤" |

**不需要放松限制强度，需要给限制加一个媒介×档位维度。**Protected Identity Cues 由常量清单改为通道矩阵；上述三条 Avoid 加媒介前提；Review 只对该媒介契约下仍开放的通道判定漂移。这正是设计讨论中标为"推演"的 Medium Contract，它现在有了具体落点。仍须遵守 §17：关闭声明只用于 Review 对照与期望管理，不进 prompt。

框架层留了口子，不需要重写：`Priority` 已规定 locked intent 优先、冲突走 risk-choice gate 而非静默拒绝；Inference Boundary 已是成熟的显式授权机制；`composition-director.md` 的 Illustration recipe 已写明 `Preserve identity through the medium's actual shape and texture language rather than drifting into accidental photorealism or plastic 3D treatment`。

## 画风谱系（2026-08-11 补充）

本节回答"动漫画风不只有 Q版"这个问题。**先要分清：Q版 是比例维度，赛璐珞是渲染维度，两者正交。**§6–§8 处理的是比例，本节处理的是渲染。

### 25. 渲染外观是两个前后叠放的阶段，不是一个维度

日本动画产业里"画面看起来什么样"由两个不同职能先后决定：

1. **仕上（shiage，上色/精加工）**——决定平面色彩语言：底色、影色、影的边界硬度、线的颜色。[色彩設定（引 日本動画協会《TVアニメシリーズ制作における制作進行のマニュアル》2020）](https://ja.wikipedia.org/wiki/%E8%89%B2%E5%BD%A9%E8%A8%AD%E5%AE%9A)
2. **撮影（satsuei，合成）**——决定光学质感：把仕上素材、背景素材、3DCG 合成为最终画面并施加「撮影処理」。英文即 compositing。[撮影（アニメ制作）](https://ja.wikipedia.org/wiki/%E6%92%AE%E5%BD%B1_(%E3%82%A2%E3%83%8B%E3%83%A1%E5%88%B6%E4%BD%9C))

这个分工是硬的：数字化后原本属于仕上的笔刷与渐变作业有不少已移交撮影负责。[同上](https://ja.wikipedia.org/wiki/%E8%89%B2%E5%BD%A9%E8%A8%AD%E5%AE%9A)

**对设计的直接后果：「赛璐珞平涂」与「有 halation / 有柔光扩散」是两个正交选项，不是同一条光谱上的两点。** 一张画可以是硬边平涂 + 重度光学处理（现代深夜动画常态），也可以是硬边平涂 + 零光学处理（早期数字动画"ギラついて見える"的状态，见 §27）。原六轴把这两件事压进"上色"与"质感后期"两个位置不明的轴里，是混淆的来源。

还需注意：§26 的「塗り」分类是**插画界**体系，不是动画产业体系；动画产业侧对应的是仕上＋撮影两段。两套词汇混用是这个领域最常见的混淆源。

### 26. 塗り 的分类与各自的可见特征

分类本身有共识，但**边界数目有分歧**：玄光社给三分（アニメ塗り／水彩塗り／厚塗り）[genkosha](https://genkosha.pictures/illustration/18103116736)；CLIP STUDIO 官方运营的教学媒体给四分（＋CG塗り）[clipstudio.net](https://www.clipstudio.net/oekaki/archives/168849)；多个教学来源给四分但第二项叫ブラシ塗り [atam-academy](https://atam-academy.com/blog/37342/)。

有一条重要的元陈述：**这些名称没有明确的条件定义**，是"看起来是这种感觉的塗り"的通俗叫法。[atam-academy](https://atam-academy.com/blog/37342/) 因此任何把它们做成互斥选项的实现，都是在收紧行业本身没有收紧的边界，应当用可见特征而不是名称来定义档位。

| 塗り | 线 | 影 | 其他可见特征 | 强度 |
| --- | --- | --- | --- | --- |
| アニメ塗り／セル塗り | 线画是主角、被刻意保留突出 | ベタ塗り实心填充、不用模糊渐变、边界清晰 | 底色/1影/2影/高光的最小色数结构；高光小而锐利呈点状 | 官方 [CSP](https://www.clipstudio.net/oekaki/archives/168849) + 行业 [prismplane](https://prismplane.jp/anime_style_coloring/) [dat.ac.jp](https://www.dat.ac.jp/course/illust/illust-column/illust-school/anime-coloring-painting/) |
| ブラシ塗り／CG塗り／ギャルゲ塗り | 保留 | **以アニメ塗り为底，把影做成渐变或加模糊** | 喷枪画淡影后晕开融进底色；典型用于游戏角色 | 官方 [CSP](https://www.clipstudio.net/oekaki/archives/168849) + 行业 [Confidence Creator](https://confidence-creator.jp/column/24992/) |
| 厚塗り（英 impasto） | **常常没有主线**，或被色层盖掉融掉 | 边界暧昧、保留笔触纹理、吸色逐步过渡 | 不透明度低的颜料层层覆盖，像油画；不用油漆桶填色 | 官方 [CSP](https://www.clipstudio.net/oekaki/archives/168849) + 行业 [ani-emo](https://ani-emo.com/archives/1666) |
| 水彩塗り | 做色トレス使线变淡 | 边界变软、水彩境界强调 | 淡色调；有意制造不均匀；纸纹以 Divide 叠加再现纸张反光 | 官方 [CSP](https://www.clipstudio.net/oekaki/archives/168849) + 行业 [CSP TIPS](https://tips.clip-studio.com/en-us/articles/14864) |
| 線なし／lineless | **最小限度的彩色线**（五官、发丝分组），用比底色深几档的色而非纯黑 | 仍然有影 | 形体靠色块与明度差分离 | 行业 [CSP TIPS](https://tips.clip-studio.com/en-us/articles/4614) |
| モノクロ漫画＋网点 | — | 网点代替影 | 见下，四参数可控 | 官方 [CSP 手册](https://www.clip-studio.com/site/gd_en/csp/userguide/csp_userguide/590_material_plt/590_material_plt_function_tone_dlg.htm) |
| セルルック 3DCG／トゥーンレンダリング | 轮廓线勾形，黑色效果好但可上色 | **只用两到三个色阶**，不用平滑渐变 | 三者（トゥーンレンダリング＝セルシェーディング＝セルルック）同义 | 官方 [Autodesk](https://www.autodesk.com/jp/solutions/toon-shader) [Unity Toon Shader](https://docs.unity3d.com/ja/Packages/com.unity.toonshader@0.9/manual/GettingStarted.html) |

两条必须记的细节：

- **lineless ≠ flat。** 有教程明确说自己要 lineless 而**不是** flat，所以仍然加了阴影，否则会像剪纸拼贴。这是两个独立开关。[CSP TIPS](https://tips.clip-studio.com/en-us/articles/7577)
- **网点是本清单里参数最硬的一项**，CSP 官方手册给了四个独立参数：線数（frequency）、濃度（density）、形状（circle/square/lozenge/line/cross/ellipse/noise 等 24 种）、角度。[CSP 官方手册](https://www.clip-studio.com/site/gd_en/csp/userguide/csp_userguide/590_material_plt/590_material_plt_function_tone_dlg.htm)

需要修正的三项：

- **グリザイユ画法不是外观，是工序**——先画灰阶明暗再上色，目的是更快做出厚塗り，成品归入厚塗り。把它列成可选画风就是把工序错当结果。[genkosha](https://genkosha.pictures/illustration/18103116736)
- **「复古赛璐珞」不是塗り体系里的原生类别**，未找到任何来源把它列入分类。它在实践中是一套叠在アニメ塗り之上的后处理配方，见 §27。
- 「宝石塗り」「半厚塗り」各只有单一来源，且后者作者明说是自己起的名字。`未验证` 不应写进选项名。[ANOUE](https://anouemang.com/nurikata)

一条独立外部佐证：NeurIPS 2025 的 T2I 基准 OneIG-Bench 在 Anime 类目下使用的画风词表是 Celluloid、Chibi、comic、Cyberpunk、Ghibli、**Impasto**、Pixar、pixel art、3d rendering。这佐证了赛璐珞与厚涂确实被当作两个可区分的动漫画风类别，且 Impasto 是厚塗り的标准英文对应词。[OneIG-Bench, Table 9](https://proceedings.neurips.cc/paper_files/paper/2025/file/e9e9e5428189a3e49479547ef917e88d-Paper-Datasets_and_Benchmarks_Track.pdf) `学术`

### 27. 复古与现代的可见差异

**色板（最需要小心的一条）。** 赛璐珞时代可用颜料色数被预算硬性限制，但检索到的数字互相不一致：《机动战士高达》1979 TV 约 70 色、剧场版新作卡约 100 色、《Crusher Joe》约 120 色 [五島一浩, 文化厅媒体艺术](https://mediag.bunka.go.jp/article/da6/)（作者自述为杂志记忆＋DVD 小册子对谈补全）；另一来源称色票编号时代约 200 色 [六方ブログ](https://blog.loppo.co.jp/plotting-cie-xy-chromaticity-diagram/)。**只能写量级——两位数到低三位数的固定色板，数字时代无限制——不能写具体数。**

同一篇文化厅专栏给了一条重要的反向限定：**色板色数 ≠ 画面色数。** 赛璐珞是平涂所以角色层"色数≈颜料数"，但与之叠合的背景画是笔绘有渐变的，加上摄影照明、滤镜与胶片特性，一个画面里实际颜色趋于无限。**因此"复古＝色少"只对角色层成立，对整幅画面不成立。** [五島一浩](https://mediag.bunka.go.jp/article/da6/)

**线质。** 现代数字流程的线是二值化的（为上色效率去抗锯齿），因而产生锯齿，随后在撮影阶段用「スムージング」重新加回抗锯齿。[撮影（引 日本動画協会 2023 经产省委托调查报告）](https://ja.wikipedia.org/wiki/%E6%92%AE%E5%BD%B1_(%E3%82%A2%E3%83%8B%E3%83%A1%E5%88%B6%E4%BD%9C))

**"彩色线＝现代"是错的。** 色トレス（把主线改成黑色以外的颜色）在赛璐珞时代的仕上就在做，《宇宙戦艦ヤマト》有具体记录。正确的表述是：**赛璐珞时代它是个别处理，现代它变成常规且在撮影阶段批量施加。** [撮影，引色彩設計 辻田邦夫考据](https://ja.wikipedia.org/wiki/%E6%92%AE%E5%BD%B1_(%E3%82%A2%E3%83%8B%E3%83%A1%E5%88%B6%E4%BD%9C))

**光学处理是复古/现代差异最集中的地方，而且有一个可指认的单一操作。** 动画从胶片摄影转数字撮影时，画面"就那样会显得刺眼发亮（ギラついて見える）"，对策是全画面加一层扩散模糊柔化（把模糊过的画面以极低不透明度叠回原画，示例值 0.13）。[note.com 小林信行, Anime Toolbox](https://note.com/nyaa_toraneko/n/n177e8cfb5d2b)

其余可作为"现代"标记的具体效果，均出自同一位撮影监督的记述 [WEBアニメスタイル 泉津井陽一](https://animestyle.jp/2016/03/07/9837/)：环境光（宽幅圆形渐变或专用 halation 素材以合成模式加亮）是最常用的；**水平一直线的 anamorphic 型 flare 被明确称为"最近的流行"**；丸ボケ的形状由光圈决定，**圆形对应现代镜头、多边形略显古典**；透過光现代用 AE 加算模式，胶片时代是真实多重曝光因而产生真实晕染。

**一条重要的负面约束：扩散效果做过头会让整个画面发白，从而偏离原本的色彩設計。** [同上](https://animestyle.jp/2016/03/07/9837/) 这说明在产业内部，光学后处理与色彩设计是会互相破坏的两层，不是自由叠加。

**90 年代配方里最具体的一条技法：线画的颜色与较深的那层影色取同一个色。** 作者称这是 90 年代动画中非常常用的手法。同教程的其余要素：用固定复古色板而非自由取色、喷枪画脸颊红晕、最后叠含高斯模糊与柏林噪声的滤镜。[CSP TIPS KevinFarias](https://tips.clip-studio.com/ja-jp/articles/7044)

网上流传更长的复古清单（VHS 的 RGB 错位、关抗锯齿画粗线、瞳中十字反光）只见于低质量博客。`未验证`

### 28. 眼睛轴的可参数化分解

眼睛在多篇 CSP 教程里被一致地拆成同一组图层，这组图层就是天然的参数列表：**巩膜／上睫毛投下的阴影／虹膜底色／虹膜环／瞳孔／高光**。[CSP TIPS daromart](https://tips.clip-studio.com/en-us/articles/2674)

- **虹膜渐变**标准做法是上暗下亮（虹膜底色上方建乗算图层，由深到浅）。虹膜内部可画放射状纹理也可完全不画。[CSP 官方连载 Tsunoju](https://tips.clip-studio.com/en-us/articles/1212) [Pharmarr](https://tips.clip-studio.com/en-us/articles/10248)
- **高光规则最明确**：最大的高光放在光源方向那一侧、另一个较小的放对角，两眼高光必须同侧；大高光会压过虹膜边缘线但不能压过睫毛线；图层模式是 Add(Glow)，即它是**发光**而非白色填充。[HanairoHinode](https://tips.clip-studio.com/en-us/articles/11768) [frequencyniepan](https://tips.clip-studio.com/en-us/articles/11697)
- **眼睛高光在动画产业里属于撮影而非仕上**——撮影监督明确把"角色瞳孔的高光"与极强反射光一起列为透過光处理对象。这是一条重要的归属信息：**瞳孔高光强度是合成层参数，可独立于上色风格调整。**[泉津井陽一](https://animestyle.jp/2016/03/07/9837/)
- **睫毛**：给睫毛、眉毛、双眼皮线剪贴上色被描述为"表现光穿透毛发后的次表面散射"，且被明确标注为**可选步骤**。受光侧睫毛可画成白色。[daromart](https://tips.clip-studio.com/en-us/articles/2674) [Pharmarr](https://tips.clip-studio.com/en-us/articles/10248)
- **虹膜与眼白之间通常不用硬的深色线分界**；眼白不是纯白，底部取旁边肤色、眼睑下加淡灰与紫的阴影。[Pharmarr](https://tips.clip-studio.com/en-us/articles/10248) [Tsunoju](https://tips.clip-studio.com/en-us/articles/1212)

时代变化有一条可用的一手陈述（具名插画师受主流媒体采访）：**2000 年代是黑线画得很实、里面放一个大光泽；2020 年代常给睫毛用黑色以外的颜色，并有意识地画进景物的映入。** 该画师同时指出画风每年都在变，不止十年一变。[まいどなニュース](https://maidonanews.jp/article/14204250)

**一条负面发现必须记下**：本次检索到的最详细的一份"眼睛画法参数地图"（15 项分解）**其作者在文中自述该分类是用 ChatGPT 生成的**。结构诱人但无任何证据支撑，不可采信。若需要这样一张表，只能从上面的分项证据自行拼装。`未验证` [note.com 深夜ラテ](https://note.com/shinya_latte/n/n4eb544e71acd)

### 29. 线条轴

**三级线宽层级**：輪郭線（主線，最粗，明确与背景的边界并把角色收成整体）／境界線（副線，用于前后关系与脸部）／細線（质感与细节，用多了画面会挤）。[ORE7 STUDIO](https://www.ore7studio.com/illust_line)

加粗与减细的规则在多来源间一致 [canvas-cluster](https://canvas-cluster.com/line-art-line-weight/) [oekaki-zukan](https://oekaki-zukan.com/articles/22389)：重叠交叉处、靠前的形、与背景不易区分的外缘、眼周、影侧加粗；头发与衣服的内部线、靠后的形、衣褶细发束、细小纹样、光侧轮廓减细。

**线宽变化量本身是一个可连续调节的风格参数**，这是本节最可用的一条：

| 目标印象 | 强弱设定 |
| --- | --- |
| 有力、清晰 | 粗细差拉大 |
| 漫画感 | 外缘、重叠、影侧加强 |
| 一般彩色插画 | 只在重叠与看点处稍加强 |
| 淡雅柔和 | 以细线为基准、差值缩小 |
| 均质工整 | 线宽几乎统一 |

另有一条独立表述：均一的细线＝硬的印象，有强弱的粗线＝柔软的印象。[oekaki-zukan](https://oekaki-zukan.com/articles/22389)

**入り抜き**（起收笔渐细）的技术实现是把笔压映射到笔刷尺寸或不透明度；没有它所有线同一粗细，画面会"のっぺり"（扁平呆板）。[ペン画Log](https://hio-drawing.com/dessin/line-art-guide/)

**线色**：黑＝清晰有力、棕＝温柔自然、藏青＝时髦沉稳、灰或淡色＝轻盈通透。`行业/实践`（单一来源）[chiba-satoko](https://www.chiba-satoko.com/illustration-main-line/) 淡雅风格中线太黑会压过上色，用色トレス调整存在感。[canvas-cluster](https://canvas-cluster.com/line-art-line-weight/)

**线是否存在是三档而非两档**：有线 → 最小限度的彩色线（lineless）→ 无线/线被色层吃掉（厚塗り）。

3D 侧提供了一个有力的反证。Arc System Works 在 GDC 讲《Guilty Gear Xrd》时说明：轮廓用 inverse hull，通过顶点色 alpha 控制外扩量，从而做到**逐顶点的线宽控制、甚至在指定位置把线完全消除**。同一份资料还指出赛璐珞着色是二值的，因此**表面任何细微噪声都会变成极显眼的斑块**，脸部法线必须手工打磨。[ASW 官方 GDC PDF](https://www.ggxrd.com/Motomura_Junya_GuiltyGearXrd.pdf) [ASW Academy](https://convert.docswell.com/s/ASW_Academy/5LVY67-GG-Toonline-Eng) **推论：线宽在一张图内的变化、以及局部无线，是被当作必须专门解决的工程问题的，说明它们是这个 look 的核心可见特征而非细节。**

### 30. 色彩逻辑轴：§12 的"无对应"结论应当推翻

**结论：色彩逻辑作为独立于阴影层数的生产维度确实存在，而且在日本动画产业里有一个有决定权的专职岗位。**

「色彩設定／色彩設計」是着色时用哪些颜色的**最终决定权持有者**，英文写作 colour planning，下分色彩設計／色指定／仕上三个 section。职责核心是：**对作画所表现的一切事物，预先设定并规则化"对什么用什么颜色"**。[色彩設定](https://ja.wikipedia.org/wiki/%E8%89%B2%E5%BD%A9%E8%A8%AD%E5%AE%9A)

现职色彩設計本人把两层任务分得很清 [WEBアニメスタイル 辻田邦夫](http://www.style.fm/as/05_column/tsujita/tsujita01.shtml)：

1. **决定角色的基本色**
2. **决定该作品色味的方向性**——要和美术联动，在美術ボード上一边看一边定"夜景要暗到什么程度""傍晚的西晒是强还是弱"

产出物是**色指定表**，一份全组共享的、写明画面上出现的所有物体用什么颜色的指示书。[デジタルアーツ東京](https://www.dat.ac.jp/course/anime/anime-column/color_design/color_about/) 下游的「色指定」按场景的天候、时间、舞台、**角色心情**逐镜指定颜色。[同上](https://www.dat.ac.jp/course/anime/anime-column/color_design/color_work/)

最有说服力的一条佐证：**该岗位原本属于美術監督的职责范围，随分工细化才独立设岗。**[色彩設定](https://ja.wikipedia.org/wiki/%E8%89%B2%E5%BD%A9%E8%A8%AD%E5%AE%9A) 一个从别的岗位裂变出来的岗位，其存在本身就是"这是一个独立维度"的证据。

学术侧把它形式化过：一项研究从既有 26 部作品的角色中**每个角色抽取 11 个主要颜色**、按群归档，发现**一个角色的配色可以用 11 色再现**；问题定义明确写着"群内各角色的配色需要有一贯性，或者有平衡地互相区分"。[Journal for Geometry and Graphics 21(2):253–262, 2017；映像情報メディア学会技術報告 doi:10.11485/itetr.40.11.0_245](https://doi.org/10.11485/itetr.40.11.0_245) `学术`

**影色的推导有成文规则，且多来源一致：不能只降明度，必须移动色相。** 只降明度会得到浑浊发泥的影 [いちあっぷ](https://ichi-up.net/2016/068)；标准操作是 HSB 同时微调，明度下降、彩度维持或略升、色相往寒色偏 [dat.ac.jp](https://www.dat.ac.jp/course/illust/illust-column/illust-school/anime-coloring-painting/)；**肌肤是例外**，为保住血色影往红/橙偏 [prismplane](https://prismplane.jp/anime_style_coloring/)；避免纯黑作影色；白色部件用带一点色的 off-white 否则影层无法正常发色 [comic.smiles55](https://comic.smiles55.jp/guide/5257/)。注意这些是插画教程级来源，未核实到色彩設計岗位内部是否同用此规则。

**与阴影层数的边界很清楚**：阴影层数回答"每个色槽位内部切成几档、边界硬还是软"；色彩逻辑回答"有哪些槽位、每个取什么色、槽位之间如何保持一贯与区分、随场景整体如何位移"。同由仕上 section 执行，但是不同层次的决定。

### 31. 文生图可达性：只有类目级证据，不能做逐项排序

**本次调研没有找到任何按单个渲染外观拆分的可靠证据。** "厚涂能出、水彩会塌"这类逐项判断无法支撑。能站住的只有四条：

1. **类目级基准。** OneIG-Bench 把画风分 Traditional / Media / Anime 三类，在 22 个受测模型中 **Media 类目的分数几乎总是三类里最低的**（多数 0.29–0.37），Anime 类目在较新模型上明显更高（Seedream 3.0 达 0.524）。**watercolor 被归在最难的 Media 桶里，而 Celluloid 与 Impasto 在 Anime 桶。** 但论文没做逐画风拆分，且"风格分"是与参考图的嵌入相似度，是代理指标。[OneIG-Bench](https://proceedings.neurips.cc/paper_files/paper/2025/file/e9e9e5428189a3e49479547ef917e88d-Paper-Datasets_and_Benchmarks_Track.pdf) `学术`
2. **复古在数据侧是被结构性稀释的。** AniMatrix 构建动漫视频语料时报告：2010 年后数字制作的动画约占 **65%**，经典赛璐珞内容只占约 **8%**，必须专门重采样才能让稀有组合可学。同一篇还报告**风格名会携带内容偏置**——某导演风格的片段压倒性是风景定场镜头，必须设最低配额才能防止模型学成"该风格 ⇒ 风景"的捷径。[AniMatrix, arXiv:2605.03652](https://doi.org/10.48550/arxiv.2605.03652) `学术`
3. **风格词救不回模型不认识的概念。** 对 Midjourney 的研究发现「default images」现象：提示词不被认识时模型输出一组固定的窄主题图像，而**这些默认图像对风格修饰词的反应与普通生成一样**——换上 "in the style of cubism" 后同样的默认母题依然可靠出现。冷门或自造的画风名不会优雅降级，而是落进默认吸引子。[arXiv:2505.09166](https://arxiv.org/pdf/2505.09166) `学术`
4. **风格词脱离内容无效。** 把 DALL·E 的示例提示缩短到只剩 "An Impressionist oil painting"，"oil painting" 就变成内容主体；再缩到只剩 "Impressionist"，输出变成时而像时而完全不像的混乱结果。[The Reification of Style in AI Image Generation](https://doi.org/10.48431/hsah.0302) `学术`

**特别记一条：网点在文生图上的表现完全没有证据。** 它是规则性高频微结构，直觉上属高风险，但既然无证据就不应写进 PRD 的风险分级。lineless 与厚塗り是否更稳同样无证据。

## 仍未验证的假设

以下几条 PRD 不应写成既定事实：

1. **通道预算的正向效果**——机制建立在"把身份押注写进 prompt 并加权能提升 likeness"这一前提上。cookbook 支持"重复不变量抑制漂移"，但没有证据表明按通道分级比一般性的结构描述更好。反向风险已有依据（§17），正向收益仍未验证。
2. **色彩逻辑轴的具体形态**——轴本身已在 §30 得到产业与学术双重确认，原"无对应、暂列推演"的判断已推翻。仍未验证的是两点：§30 的 HSB 影色推导规则只在插画教程层面得到证实，未核实到动画制作现场文档；"每角色约 11 色"出自单一研究，不应当作通用槽位数写死。
3. **批量一致性的官方原文**——行为描述有多个互相吻合的第三方来源，但未核实到 OpenAI 官方原文；"8 张中 5–6 张可用"的命中率为单一来源。
4. **定稿漂移的量化拐点**——"4–5 次变体后开始偏"只有单一第三方来源。用户一手体感确认了"多次重做后容易漂移"的方向，但拐点位置无量化依据，不应写成具体次数阈值。
5. **反向激活结论向 GPT Image 2 的迁移**——机制在带独立负面字段的扩散模型上验证，GPT Image 2 的约束写在正文 prompt 内，是否同样触发未验证。保守处理（关闭声明不进 prompt）成本很低，因此建议直接采用保守做法而不等验证。
6. **Medium Contract 作为条件触发分支的形态**——仍是结构推演。§24 已给出它要解决的四个具体冲突点，但"条件触发分支"这一形态本身仍无外部依据。
7. **迭代退化在 `gpt-image-2` 上的具体拐点**——机制与"5–10 步"的量化都来自 Nano Banana Pro，另有三个模型佐证机制普适，但不含 `gpt-image-2`，且该数据集刻意排除了写实人脸。PRD 可以写"编辑链越深越脏、必须限深"，不能写具体步数阈值。
8. **tiling / grime artifact 的当前状态**——**（2026-08-12 复核）**截至复核日，**未发现** OpenAI 官方或 Boyuan Chen 的「已修复」宣布。社区长帖首帖（最后编辑 2026-05-12）仍将 Visible Noise Patterns / Noise Amplification 列为开放 bug。最新具名工程师公开信号是 Peter Bakkum 2026-08-06：仍 aware 且 working on it，并称野外持续可见。[Community 长帖](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535) [Bakkum 推文](https://x.com/pbbakkum/status/2085426695633580292) 强度：官方（工程师公开回复 + changelog 沉默）/ 行业/实践。PRD：**不要**假设已消失，也**不要**写成永久缺陷；写成需随 OpenAI 公开声明再刷新的时点性事实。详见 `tiling-grime-status.md`。
9. **清理型 prompt 的有效性**——`Remove the noise while keeping all the lines` 只有单一第三方来源说有时有用，而论文侧的证据是显式降噪指令无效。两者冲突，暂不作为对策写入。
10. **逐个渲染外观的可达性排序**（新）——只有类目级证据（Media 类目整体最难、动漫类整体较易），没有任何 Celluloid vs Impasto vs watercolor 的逐项分数。**网点、lineless、厚塗り 在文生图上是否稳定，完全没有证据**，不应写进风险分级。见 §31。
11. **赛璐珞时代色板的确切色数**（新）——检索到 70 / 100 / 120 / 200 四个数字，来源质量不一，最可追溯的一个作者自述为回忆重建。只能写量级。见 §27。
12. **「半厚塗り」「宝石塗り」是否为通用术语**（新）——各只有单一来源，且「半グリザイユ」的作者明说是自己起的名字。不应写进选项名。见 §26。
13. **眼睛画法的时代分期**（新）——只有一位具名插画师在媒体上的陈述可用（2000s 黑线大光泽 / 2020s 彩色睫毛与景物映入）；更细的三段分期只见于低质量博客。另外，检索到的唯一一份详细"眼睛参数表"作者自述为 ChatGPT 生成，不可采信。见 §28。

## 对已有讨论结论的修正

调研后需要改动的地方：

1. **通道阈值位置**：原推演为"4 头身丢脸型、3 头身丢眉眼"，应改为以 **2 vs 3 头身**为主分界，4 头身视为 chibi 上限。各档的具体差异用 §6 的行业参数替代拍定的数字。
2. **存活率分类的粒度**：原为按媒介的三层固定表，应改为**按档位展开的矩阵**。等身 anime 仍可承载鼻梁与上唇厚薄，Q版 不能。
3. **体型通道**：原判断为"部分保留"，应改为 Q版 下**完全关闭**。
4. **服装归属**：Q版 下服装承担识别功能，需进入通道预算。这与 CastMe 现有的 Styling / Identity 边界冲突，需要在该档位重新划线。
5. **年龄感**：不再作为独立的"中等存活"通道，改为与头身比强耦合的量，并用 §15 的四个具体视觉量表达。
6. **Identity Review 增加检查项**：除签名特征落实外，需检查风格化是否均匀落地（半转换）。
7. **新增显式参数**：风格化强度，因为它是双端失败的连续谱，不能隐含在画风选择里。
8. **画风轴调整**：质感轴补入网点，上色轴补入阴影层数（1/2/3 系统）；背景轴由推演改为已证实（§13）。
9. **定稿阶段的方向约束**：保持原始头部角度与表情、避免戏剧化打光与极端角度。这与 `identity-anchor.md` 现有的"表情、视线、脸部角度属于可为主题重设计的临时状态"存在张力，需要给定稿阶段单独说明——定稿阶段保守，应用阶段自由。
10. **多人物范围**：从普通用途降级为能力边界条目，写明 identity blending 的机制性限制，不承诺效果。
11. **通道预算的三栏分流**（新）：主力与次要通道进 prompt，关闭声明只用于期望管理与 Review 对照，不进 prompt；必要时改用正面表述。见 §17。
12. **档位呈现方式**（新）：由"完全自适应生成"改为**语义标签固定、数值随用途变化**，并保留 `D) Custom` 作为 adaptable 路径。见 §19。
13. **神态习惯**（新）：由"进不进清单"的二元问题改为**按用途与档位加权**——Q版表情包 下权重高，头像与等身下权重低；且必须标注为 inferred，不参与 Review 的失败判定。见 §18。
14. **定稿与成套的生成方式**（新）：优先使用批量生成，一次产出多角度参考包或整套表情，而非逐张生成后互相参考。逐张参考定稿降级为该能力不可用时的回退路径。见 §4。
15. **`n` 参数的语义**（新）：早前版本断言"`n` 只产出并列变体、不可用于连续帧"不准确，已在 §4 修正。
16. **编辑链深度成为一等约束**（新）：成套与多角度必须一次生成，不只是因为效率与批内一致（§4），更因为逐张编辑推进会累积噪点并优先磨掉小记号这类识别通道（§21、§23）。"从 Anchor 重生成"优于"在结果上继续修"，应成为默认路径而非回退路径。
17. **透明背景不可用**（新）：Q版表情包若需要透明底，必须写成能力边界并规划下游抠图步骤，不能假设模型能直接输出。见 §20。
18. **画风轴增加风险分级**（新）：质感轴的网点、背景轴的厚涂、以及飘散发丝与粒子特效属于 artifact 高风险区；赛璐珞平涂加干净背景属低风险区。见 §23。
19. **Identity Review 增加编辑链深度项，但不增加脏化的视觉判定项**（新）：模型察觉脏化严重滞后且会幻觉已降噪，通用画质指标也反向。脏化按可数的链深度管理，不写成一个让模型看图判断的检查项。见 §21、§23。
20. **画风轴由五轴改为六轴，且"上色"必须拆成两个阶段**（新）：渲染外观在产业里是仕上（平面色彩语言）与撮影（光学质感）两个由不同职能决定的前后阶段。平涂与柔光扩散是正交选项，不是同一光谱上的两点。原来把两者压进"上色"与"质感后期"是混淆的来源。见 §25。
21. **色彩逻辑轴恢复为正式轴**（新）：§12 判定的"唯一无对应的轴"结论错误。它对应「色彩設計／色彩設定」这一有决定权的专职岗位（英文 colour planning），产出物是色指定表；学术侧把角色配色形式化为约 11 个色槽位并处理群体一贯性与可区分性。它与阴影层数不重叠——层数管槽位内部切几档，色彩逻辑管有哪些槽位及其相互关系。见 §30。
22. **画风不等于变形档位，必须给出渲染外观的可选谱系**（新）：赛璐珞（アニメ塗り）、半厚涂（ブラシ塗り／CG塗り）、厚涂（厚塗り／impasto）、水彩、无线稿、单色网点漫画、卡通渲染 3D 是七个可区分的成品外观，各有可见特征清单。注意两条陷阱：グリザイユ是工序不是外观；lineless 与 flat 是两个独立开关。见 §26。
23. **复古/现代是撮影层与色板的差异，不是塗り层的差异**（新）：可指认的单一操作是数字化后为消除"ギラつき"而全画面加的扩散模糊。其余现代标记为环境光 halation、anamorphic 型水平 flare、圆形丸ボケ。90 年代最具体的技法是线色取深影色同色。**"复古＝色少"只对角色层成立**，整幅画面不成立。见 §27。
24. **不提供渲染外观的可达性承诺或分级**（新）：现有证据只支持两条通用告诫——动漫类画风整体比物质媒介类（水彩所在的桶）更易复现；风格名会携带内容偏置，且冷门风格名不会优雅降级而是落进模型的默认吸引子。逐项难易排序无证据基础，§23 中把网点列为 artifact 高风险区的说法在文生图侧没有依据支撑，只能保留其作为高频微结构的一般性提示。见 §31。

## 最终判断

- **单人物、等身与 Q版 的二次元形象生成：可行。** 官方有 character anchor 流程，行业有成体系的档位与通道知识，实践有可用的 prompt 结构。
- **成套（表情包）与多角度定稿：机制可行，依赖面能力。** 批量生成是首选路径，一次统一规划天然优于八次独立生成；但它依赖 Thinking mode 这类付费层能力，须按 `identity-preservation-reliability/research.md` 的既有写法写成 surface capability boundary，不可用时回退到逐张参考定稿，并且不得声称使用了批量一致性。
- **多人物（礼物插画）：不建议进本期。** 困难是方法层面的（identity blending），且 CastMe 现为单 Primary Identity Anchor 架构。
- **"一眼像"的承诺边界不变。** 与现有 identity 契约一致，只能是 best effort，不提供相似度分数或身份保证；Q版 档位下还需在生成前如实说明哪些通道已被关闭。
- **多轮编辑不是安全的迭代方式。**画面变脏是编解码往返累积造成的机制性问题，提示词层面无解。设计上必须把"从干净源头重生成"作为默认路径、给编辑链设深度上限，并且不依赖模型自评或通用画质指标来发现退化。
- **现有 identity 契约需要加一个媒介维度，而不是放松。**四条冲突条款（§24）全部源于只承认相机投影这一种形变理由；框架层已有 risk-choice gate 与 Inference Boundary 可以承载媒介契约，不需要重写模块。
- **PRD 可以开始写**，但需要把上节十九条修正吸收进去，并把"仍未验证的假设"整节保留为 Further Notes 的依据，不要把推演写成结论。
