# Image Prompt Quality 调研

## 结论

当前 skill **已经覆盖了大部分正确做法**：写实输出要求真实摄影语言、真实皮肤与普通瑕疵；CG / game key art 已要求材质、电影化环境、动态姿态与可读轮廓；负面约束也已经按输出类型动态选择。真正不该加入的是全局固定的 `8K, HDR, masterpiece` 词串。

OpenAI 的当前建议是：用具体的主体、构图、光线、材质和约束控制画面；写实场景直接说 `photorealistic`，并描述毛孔、皱纹、织物磨损和自然光；需要更高保真度时使用实际的 `quality` / `size` 控制，而不是把 `8K` 写进提示词。[GPT Image 2 prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide) [Image API guide](https://developers.openai.com/api/docs/guides/image-generation)

最小正确方案不是建立一份所有图片共用的“神词表”，而是在现有 `Realistic Portrait` 与 `CG or Game Key Art` recipe 内补强两个**按媒介选择的质量核心**，并继续把短小、相关的负面约束放在同一个 OpenAI prompt 中。

## 当前 repo 审计

| 关注点 | 当前状态 | 判断 |
| --- | --- | --- |
| 固定 `8K` | `composition-director.md:181` 明确禁止依赖 `8K`、`HDR`、`masterpiece` | 正确，不应反转 |
| 写实皮肤 | `composition-director.md:177-179,220-224` 已要求 pores、fine lines、肤色、年龄感、独特痣/雀斑/疤痕与普通瑕疵 | 基础充分；可补显式 `photorealistic` 和“真实拍摄瞬间” |
| 光学语言 | `composition-director.md:152-163,175` 已把镜头、景深、光源和焦点绑定到可见结果 | 正确；不需要固定设备参数 |
| CG 冲击力 | `composition-director.md:234-244` 已有轮廓、电影光、环境、材质和动态姿态 | 方向正确；“premium / cinematic”仍偏抽象，可补焦点层级、尺度、空间层次、材质响应和受控特效 |
| 负面提示 | `identity-anchor.md:156-164` 与 `composition-director.md:204-214` 已按人脸、身体、文字、构图和媒介选择短约束 | 正确；OpenAI 不应套用 Stable Diffusion 的长负面词袋 |
| 输出分辨率 | `composition-director.md:264-270` 已把像素尺寸归为 delivery requirement，并禁止声称提示词完成转换 | 正确；需要明确真 8K 不可由词语保证 |

## 官方依据

### 1. `8K` 不是实际分辨率控制

- Codex 内置图片生成当前使用 `gpt-image-2`；官方要求用自然语言描述用途、主体、场景、构图、风格、尺寸、光线、材质和不应出现的内容，并优先使用具体视觉语言，而不是宽泛的“更漂亮”。[Codex image generation](https://learn.chatgpt.com/docs/image-generation)
- GPT Image 2 的真实输出由 `size` 和 `quality` 控制。当前 API 最大支持 `3840x2160`；超过 `2560x1440` 属于 experimental。`8K`（通常指 `7680x4320`）不在支持范围内。[Create image API reference](https://developers.openai.com/api/reference/resources/images/methods/generate)
- OpenAI 较早的 GPT Image 1.5 官方指南也直接说明，摄影、构图、光线等具体词通常比泛化的 `8K/ultra-detailed` 更可靠。[GPT Image 1.5 prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-1.5-prompting_guide)

因此：`8K` 最多是模糊的审美暗示，不能改变像素尺寸，也不应成为固定质量词。若用户明确要求真 8K，应把它记录为下游交付要求；只有用户同意额外放大流程时再做 upscale，不应在首轮生成里假装已经交付。

### 2. 写实质感应来自可见的物理线索

OpenAI 的 GPT Image 2 指南建议直接写 `photorealistic`，并把视觉媒介、材质、形状和纹理说具体；相机参数主要用于高层次的观感与构图，不应被当成精确物理模拟。[GPT Image 2 prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

同一指南对自然写实的建议更具体：像真实照片正在当下被拍摄一样描述画面，写出镜头观感、光线、构图、毛孔、皱纹、织物磨损和日常瑕疵，避免过度棚拍感或重修饰；细节重要时用更高质量设置。[Natural photorealism example](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide#43-photorealistic-images-that-feel-natural)

这支持在现有 Natural Retouch 之外加入一个简短的写实质量核心，而不是堆 `ultra-realistic, 8K, HDR, masterpiece`：

```text
Photorealistic [capture context], as a real moment captured on camera.
[Framing and perspective consequence]; motivated [light source and direction]; believable exposure and natural color.
Preserve real skin texture: pores, fine lines, subtle tone variation, and distinctive marks; realistic fabric weave, wear, reflections, and surface imperfections. No heavy retouching or plastic skin.
```

其中方括号内容必须来自已锁定的 shot / lighting / styling，不能成为另一套固定 preset。

### 3. CG / game key art 的“冲击力”也不是一个神词

OpenAI 的通用提示建议要求具体描述材质、形状、纹理和媒介；构图要写明 framing、viewpoint、angle 与 lighting。对宽幅、电影化、低光、雨或霓虹场景，还应补充尺度、氛围和颜色，防止模型用表面风格替代真实空间与材质。[GPT Image 2 prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

据此，repo 可把现有 key-art recipe 收紧为以下质量核心：

```text
Cinematic game key art with one dominant, identity-preserving hero silhouette.
[Locked viewpoint] creates clear foreground, hero, and deep-world layers; large-scale environmental stakes remain readable behind the subject.
Physically coherent [costume and world materials] with distinct roughness, wear, edge response, and light behavior.
Controlled high-contrast key and separation light, deliberate color contrast, atmospheric depth, and restrained particles or energy effects that support the action rather than obscure the face or silhouette.
```

它把“视觉冲击”拆成可验证结果：第一眼英雄轮廓、第二眼世界尺度与事件、第三眼材质细节；无需新建 CG 参数表。

### 4. OpenAI 的负面约束写在同一个 prompt 中

OpenAI Images API 的生成请求列出了 `prompt`、`quality`、`size`、`background`、格式等字段，但没有单独的 `negative_prompt` 字段；这是从当前完整请求参数表得出的接口结论。[Create image API reference](https://developers.openai.com/api/reference/resources/images/methods/generate)

Codex 官方文档要求直接声明图片不得包含的内容；OpenAI 的官方示例也在普通 prompt 中使用 `No trademarks`、`No watermarks`、`Avoid tiny text`、`Do not add new elements` 等约束。[Codex image generation](https://learn.chatgpt.com/docs/image-generation) [GPT Image 2 examples](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

作为对比，Stability AI 的 API 明确提供独立的 `negative_prompt` 参数；这说明该字段是 provider-specific 能力，不能直接迁移到 OpenAI/Codex。[Stability AI API reference](https://platform.stability.ai/docs/api-reference)

因此继续沿用当前 repo 的规则：

- 先写正向、具体的视觉目标。
- 在同一 prompt 末尾保留一个短 `Constraints` / `Avoid` 段。
- 只选本次高概率失败项，通常 3–8 条；不要无差别粘贴“low quality, bad anatomy, worst quality...”长词袋。
- 用完整、可观察的约束，例如 `preserve the same face structure`、`no plastic skin`、`no random text or watermark`、`effects do not cover the face or hero silhouette`。

## 推荐实施方案

只改现有提示契约，不增加步骤、依赖或新用户问题：

1. 在 `composition-director.md` 的 `Realistic Portrait` / `Professional Headshot` recipe 中，要求最终 prompt 显式包含 `photorealistic` 或等价真实拍摄语义，并把 Natural Retouch 翻译成真实皮肤、衣料和环境材质的可见线索。
2. 在 `CG or Game Key Art` recipe 中，把抽象的 `premium` / `cinematic` 补成英雄轮廓、尺度与三层空间、材质光照响应、色彩分离和受控特效；继续保护脸部身份。
3. 保持现有 adaptive negatives，明确它们放在同一个 OpenAI prompt 中；不要新增 Stable Diffusion 风格的全局负面词表。
4. 保留 `8K` 禁令。若用户要求具体像素，记录真实 delivery requirement；在 Codex 内置生成无法保证时如实说明，只有用户要求时才进入独立放大流程。
5. 在 `evals/golden-conversations.md` 增加三条行为检查：写实默认必须出现真实拍摄与皮肤/材质线索；CG 默认必须出现轮廓/尺度/材质/光色层级；两者都不得靠 `8K/HDR/masterpiece` 或通用长负面词袋充当质量控制。

## 不建议

- 不添加所有输出共用的 `8K, HDR, ultra-detailed, masterpiece, best quality` 固定尾巴。
- 不把摄影皮肤词强塞进 CG，也不把 CG 的粒子、辉光、电影调色强塞进写实头像。
- 不新增“负面提示词”提问；只有用户有明确避项或主题破坏风险时才问。
- 不承诺 Codex 内置生成直接交付真 8K；实际像素与后续放大是交付能力问题，不是文案问题。

## 2026-07-16 补充：4K、通用视觉冲击与分类型模板

### 结论修正

1. **不建议把“最高 4K + `quality=high`”强制到每一次生成。** GPT Image 2 的 `size` 和 `quality` 才是实际输出控制；当前 `3840x2160` 是最大支持尺寸，但超过 `2560x1440` 的分辨率仍标为 experimental。官方同时把质量设置定义为延迟/保真度权衡：低延迟或高吞吐场景应先评估 `low`，近景人像、身份敏感编辑、密集文字和高分辨率成品再比较 `medium` / `high`。[Create image API reference](https://developers.openai.com/api/reference/resources/images/methods/generate) [GPT Image 2 prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)
2. **不建议把“视觉冲击”解释成所有图片都要强反差、戏剧光、夸张姿态或电影调色。** OpenAI 对自然写实的官方建议恰好要求真实抓拍语义、普通瑕疵，并避免棚拍修饰、电影光和戏剧化调色；这些“冲击力手段”会直接破坏纪实、人像和可信职业头像。[Natural photorealism](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide#43-photorealistic-images-that-feel-natural)
3. **可安全设为全局默认的是“意图清楚、第一眼可读、焦点不竞争”。** OpenAI 要求提示词说明用途或受众、主体、发生的事、构图、视觉风格与必要约束，并建议明确 framing、viewpoint、placement、lighting 和 material；由此可以推导出全类型的焦点清晰契约，但不能推导出全类型的戏剧化契约。[Codex image generation](https://learn.chatgpt.com/docs/image-generation) [OpenAI Academy image prompting](https://openai.com/academy/image-generation/) [GPT Image 2 prompting fundamentals](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

### 4K / 质量默认边界

以下为**推导建议，不是 OpenAI 官方固定策略**：

| 场景 | 默认建议 | 理由与边界 |
| --- | --- | --- |
| 构图探索、方向预览、批量变体 | 非 4K；`low` 或 `medium` | 官方把 `low` 定位为延迟敏感和高吞吐起点；探索阶段强制最高尺寸会放大等待与用量，却不会替代构图判断。[GPT Image 2 prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide) |
| 最终身份人像、近景头像、身份敏感编辑 | `high`；尺寸按实际交付用途 | 官方明确建议此类任务比较 `medium` / `high`；写实细节还应依赖真实皮肤、衣料和光线描述，而不是 `4K` 词语。[GPT Image 2 prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide) |
| 社交头像、小尺寸缩略图 | `medium` 通常足够；只有同时需要大图复用时才升高 | 小尺寸成功标准是脸和轮廓立即可读。更大像素不能修复焦点弱、背景拥挤或脸占比不足；这是由官方“用途/受众 + placement + composition”规则推导出的边界。[Codex image generation](https://learn.chatgpt.com/docs/image-generation) [GPT Image 2 prompting fundamentals](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide) |
| 海报、杂志封面、广告成品、密集文字 | `high`；按版式请求实际尺寸 | 官方建议密集文字、详细信息图和高分辨率成品比较或使用 `high`，并要求精确文字与层级；最高尺寸仍须接受 experimental 边界。[GPT Image 2 prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide) [Create image API reference](https://developers.openai.com/api/reference/resources/images/methods/generate) |
| 明确要求 4K 的最终成品 | 仅在调用面实际暴露 `size` 时请求最大兼容尺寸，并验证文件像素 | API 可用 `size` 请求真实像素；把 `4K` 写进 prompt 不能证明文件尺寸。Codex 官方把程序化尺寸/质量控制指向 Image API，因此没有参数控制的调用面只能记录交付要求，不能声称已保证 4K。[Image generation API guide](https://developers.openai.com/api/docs/guides/image-generation) [Codex image generation](https://learn.chatgpt.com/docs/image-generation) |

建议的默认契约是：**最终、身份敏感的首轮成品默认 `quality=high`；分辨率默认使用与目标画幅匹配的最高非 experimental 尺寸。只有明确 4K 交付需求时才启用 experimental 最大尺寸，并在生成后检查实际宽高。** 当前官方范围要求宽高可被 16 整除、画幅比在 `1:3` 到 `3:1` 之间，且还要满足模型的像素与边长限制。[Create image API reference](https://developers.openai.com/api/reference/resources/images/methods/generate)

### 通用“第一眼效果”契约

以下为**推导建议**，用于替代全局“dramatic / cinematic / high impact”固定词：

```text
Audience effect: <the one feeling or judgment the image should create first>.
First read: <one primary face, silhouette, action, product, or message> reads immediately at the intended display size.
Focal hierarchy: supporting world, props, text, effects, and texture reinforce that first read and do not compete with it.
```

这三行来自官方要求的 purpose/audience、main subject/action、composition/placement 与 constraints 的组合；它是一份 repo 级推导契约，不是 OpenAI 原文模板。[OpenAI Academy image prompting](https://openai.com/academy/image-generation/) [Codex image generation](https://learn.chatgpt.com/docs/image-generation) [GPT Image 2 prompting fundamentals](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

“冲击力”按类型解释：

- 自然人像、职业头像、纪实抓拍：可信、亲近、眼神或表情有存在感；默认不等于戏剧化。
- 电影海报、CG / game key art：强轮廓、故事事件、尺度和光色张力；可默认更戏剧化。
- 编辑、商业、社交头像、插画：由使用场景决定，可能大胆，也可能克制；只固定第一眼读法，不固定情绪强度。

这一区分是**推导建议**。官方自然写实示例要求 honest、unposed、natural color、no glamorization / heavy retouching；广告示例则要求 audience、concept、composition、strong color direction 和清晰文案，证明不同用途不能共享同一种“冲击”手段。[Natural photorealism](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide#43-photorealistic-images-that-feel-natural) [Ads generation](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide#46-ads-generation)

### 分类型风格模板

下面均为**根据官方 prompting fundamentals、用例和当前 repo 身份保护契约推导的模板，不是 OpenAI 官方逐字模板**。它们只补每个类型真正不同的质量核心；已锁定的身份、动作、画幅、文字和场景仍由现有 production prompt 提供。

#### Realistic Portrait

```text
Audience effect: immediate human presence and believable emotional connection.
Photorealistic <capture context>; <close or medium-close framing> with the eyes/expression as the first read and a quiet supporting background.
Motivated <natural or practical light>, believable exposure and natural color; real pores, fine lines, tone variation, hair, fabric wear, and ordinary imperfections.
Constraints: no heavy beauty retouching, plastic or waxy skin, glamorized staging, HDR halos, or CG sheen.
```

依据：官方建议显式使用 `photorealistic`，像真实时刻被拍下一样写 lens / lighting / framing，并要求 pores、wrinkles、fabric wear 与 imperfections；自然写实应避免过度棚拍和修饰。[Natural photorealism](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide#43-photorealistic-images-that-feel-natural)

#### Professional Headshot

```text
Audience effect: competent, trustworthy, and approachable without looking generic.
Face-dominant clean composition; direct, natural expression; clear separation from a simple background and useful negative space for the intended profile/layout.
Controlled soft editorial or business light, natural skin color, realistic hair and garment texture, Natural Retouch only.
Constraints: no stock-photo grin or pose, no over-smoothing, face reshaping, costume replacement, fantasy scene, or unrequested dramatic low-key lighting.
```

依据：这是从官方的 intended audience、placement、concrete lighting/materials、身份敏感任务使用更高质量，以及自然写实的真实质感规则推导的职业头像模板；OpenAI 没有发布一份逐字“professional headshot”固定模板。[Codex image generation](https://learn.chatgpt.com/docs/image-generation) [GPT Image 2 prompting fundamentals](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide) [Natural photorealism](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide#43-photorealistic-images-that-feel-natural)

#### Cinematic Poster

```text
Audience effect: one decisive story promise understood before any detail.
First read: one identity-preserving hero silhouette or face; second read: the conflict/world; third read: story-bearing texture. Reserve explicit title-safe space.
Motivated dramatic key and separation light, controlled bold color contrast, atmospheric depth, and restrained effects that support the silhouette.
Constraints: no competing focal points, face-obscuring effects, muddy values, random text, fake logos, or equal-weight detail everywhere.
```

依据：官方要求电影化、宽幅、低光等画面补足 scale、atmosphere 与 color，版式需要明确 placement；OpenAI Images 2.0 的官方展示也用 bold typography、cinematic portrait、street photography 和 cohesive art direction 描述海报成果。[GPT Image 2 prompting fundamentals](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide) [Introducing ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/)

#### CG / Game Key Art

```text
Audience effect: heroic, kinetic, or epic presence; this lane defaults to dramatic impact unless the brief says otherwise.
One dominant identity-preserving hero silhouette with a readable action line; clear foreground, hero, and deep-world layers; environmental scale supports the stakes.
Controlled high-contrast key/separation light and one deliberate color accent; distinct skin, cloth, leather, metal, stone, and effect responses with coherent wear and roughness.
Constraints: no cheap plastic surfaces, flat lighting, muddy values, weak silhouette, uniform detail, clutter, or effects covering the face/action.
```

依据：官方通用规则要求具体写 medium、materials、shapes、textures、viewpoint、angle、lighting、scale、atmosphere 和 color；“默认 heroic / kinetic / epic”及三层空间是 repo 用途导向的推导，而不是官方固定措辞。[GPT Image 2 prompting fundamentals](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

#### Editorial / Magazine

```text
Audience effect: a specific point of view about the person, fashion, or story—not generic luxury.
One intentional pose, gesture, or gaze drives the first read; use asymmetry or negative space only when it serves cover/editorial hierarchy.
Refined but brief-specific palette and fashion/editorial light; tactile textiles, believable skin, and medium-appropriate grain or print texture.
Constraints: no fake masthead or cover lines, stock posing, generic beige-and-gold luxury, excessive retouching, or decorative clutter.
```

依据：官方要求用途、受众、composition/placement 和具体 light/material；Images 2.0 的官方示例把 luxury fashion spread 描述为 sculptural gowns、dramatic poses、minimalist high-fashion photography，也展示了克制的 editorial poster，说明“编辑感”既可大胆也可极简。[OpenAI Academy image prompting](https://openai.com/academy/image-generation/) [Introducing ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/)

#### Social Avatar

```text
Audience effect: instant recognition and the intended personality at thumbnail size.
Face-dominant crop, clean silhouette, simple background, and one clear color/shape separation; keep critical identity features readable when reduced.
Clean motivated light and restrained texture; polish the face without erasing real identity evidence.
Constraints: no tiny text, dense scenery, small props, weak face/background separation, or complex full-body staging.
```

依据：这是从官方“用途/受众”、明确 placement、清晰主体、负空间和跨尺寸可读性原则推导的头像模板；官方 logo 示例也明确把 strong silhouette、balanced negative space 和 small/large-size readability 作为可见控制，但这些原则在此只用于头像构图，不把人像当 logo。[Codex image generation](https://learn.chatgpt.com/docs/image-generation) [GPT Image 2 prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide#45-logo-generation)

#### Commercial Campaign Visual

```text
Audience effect: the target audience understands the brand mood, hero subject/product, and one message immediately.
Write it as a creative brief: audience, positioning, culture/context, concept, hero hierarchy, scene, and message-safe negative space.
Use brand-appropriate color direction and product-congruent light; render skin, wardrobe, packaging, and product materials believably.
Constraints: exact supplied copy only; no invented logos, slogans, claims, extra text, watermark, unrelated brand cues, or competing clutter.
```

依据：官方广告指南明确要求 creative brief 包含 brand、audience、culture、concept、composition 和 exact copy，并建议写 positioning、vibe、scene、tagline、strong color direction、natural poses 与 clean composition。[Ads generation](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide#46-ads-generation)

#### Generic Illustration / Non-photographic

```text
Audience effect: the concept, story beat, or emotion reads through shape, gesture, and color before surface detail.
One dominant figure/action plus only a few story-bearing objects; define the intended medium explicitly: <watercolor / ink / flat vector / painted concept art / collage / other>.
Use medium-coherent linework, brush edges, paper or print texture, palette, and lighting rather than photographic skin/camera polish.
Constraints: no accidental photorealism, plastic 3D surfaces, incompatible mixed styles, decorative clutter, random text, or character redesign.
```

设置这一通道有依据：官方要求明确 visual medium 并使用针对媒介的 quality levers，例如 watercolor、textured brushstrokes；官方儿童绘本示例也分别锁定 watercolor、soft outlines、warm earthy colors、角色比例和 no text / no watermark / no redesign。[GPT Image 2 prompting fundamentals](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide) [Children's book art example](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide#64-childrens-book-art-with-character-consistency-multi-image-workflow)

### 推荐的需求边界

以下为**最终推导建议**：

- 所有输出都必须有明确的 intended audience effect、第一视觉读法和不竞争的焦点层级。
- 只有 Cinematic Poster 与 CG / Game Key Art 默认采用戏剧性视觉冲击；Commercial、Editorial 和 Illustration 根据 brief 决定强度；Realistic Portrait、Professional Headshot、Documentary/Candid 与 Social Avatar 默认以可信、亲近、清晰或小尺寸识别力构成“冲击”。
- 最终身份敏感成品默认 `quality=high`；探索、批量变体和简单小尺寸资产不强制 high。
- 默认不强制 experimental 4K。最大非 experimental 尺寸作为稳定默认；明确最终 4K 交付时才请求最大兼容尺寸并验证像素。
- `4K`、`high quality`、`cinematic`、`impactful` 不能作为 prompt 里的替代性质量词；真实参数控制交付，具体构图、光、色、材质和短约束控制可见结果。
