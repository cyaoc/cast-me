# GPT Image 2 tiling / grime artifact 当前状态复核

复核日期：2026-08-12  
对应：`anime-stylized-identity/research.md`「仍未验证」第 8 条 / §22  
范围：公开信息核验（2026-05-07 → 2026-08-12）；**无**一手生成实测。

强度标签（与 research.md 一致）：`官方` / `行业/实践` / `未验证` / `推演`。二手博客（apipass、startupfortune 等）只作线索，不作权威。

---

## 结论

- **未找到** OpenAI 官方 changelog / docs / 具名工程师的「tiling / grime / visible noise 已修复」宣布。证据强度：检索范围内的否定结论（官方沉默 + 工程师仍称在修）。
- **最新一手工程师信号**是 OpenAI 的 Peter Bakkum（[@pbbakkum](https://x.com/pbbakkum)）于 **2026-08-06** 回复：`We're aware of it and working on it, this problem is actually driving me insane because I see it in the wild constantly`。[推文](https://x.com/pbbakkum/status/2085426695633580292)（经社区帖转载与日期标注：[Community #355](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/355)）
- Boyuan Chen（[@BoyuanChen0](https://x.com/BoyuanChen0)）在公开检索中**未见**其承诺的「修好后亲自发推宣布」。其最后可追溯的同类表态仍停在 2026-05-04 前后的「正在修 / working on it」族回复（见时间线），而非「已修好」。
- 社区长帖首帖（维护者 Daller）**最后编辑 2026-05-12**，Bugs 区仍保留 **Visible Noise Patterns** 与 **Noise Amplification**；**Fixed Bugs: (non)**。按该帖自己的规则，修好的条目会从首帖删除——因此截至该编辑日，维护者未把噪声标为已修。[首帖](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535)
- OpenAI API changelog 有 GPT Image 2 发布与 DALL·E 下线等条目，**无** tiling / grime / noise pattern 修复条目；模型页可见快照仍为 `gpt-image-2` / `gpt-image-2-2026-04-21`，未见更新快照名暗示专项修复。[Changelog](https://developers.openai.com/api/docs/changelog) [Model](https://developers.openai.com/api/docs/models/gpt-image-2)
- **对 PRD**：应写成时点性开放问题——「截至 2026-08 仍无官方修复宣布，工程师公开仍称在修；社区仍见典型 pattern」。**不要**假设已消失，也**不要**写成永久缺陷或已证实的隐水印策略。

---

## 证据时间线

| 日期 | 事件 | 来源 | 强度 |
| --- | --- | --- | --- |
| 2026-04-22 | 社区长帖开帖；会话内噪声放大被大量报告 | [Community #1 / #3](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535) | 行业/实践 |
| 2026-04-24 | Daller：同会话连续生成的 **amplification 明显缓解**；**基线噪声仍在** | [#21](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/21)、[#27](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/27) | 行业/实践 |
| 2026-04-24 | Boyuan Chen：`I am actively fixing various issues from the community feedback` | [X status](https://x.com/boyuanchen0/status/2047738501647728937)（论坛转载 [#25](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/25)） | 官方（具名工程师公开回复） |
| 2026-04-25 | Daller：`It is definitely NOT fixed. Only the image carryover has been corrected.` | [#33](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/33) | 行业/实践 |
| 2026-05-04 | 用户汇总 Boyuan 对 noise bug 的系列回复（`actively working on it` / `Working on it` / `working on a fix now` 等） | [#139](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/139) | 行业/实践（转述工程师表态；非官方 docs） |
| 2026-05-05 | 用户称 BoyuanChen0「working on it and will announce when fixed」 | [#159](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535)（同线程 2026-05-05） | 行业/实践（二手复述承诺；未在本次复核中打开原推全文） |
| 2026-05-07 | apipass 二手文停更点：仍称未宣布修复；线索指向 Boyuan 5/4 `working on it` | [apipass](https://apipass.dev/blogs/gpt-image-2-launch-tiling-texture-artifact)（**线索，非权威**） | 未验证（相对一手） |
| 2026-05-12 | 长帖首帖最后编辑；Bugs 仍列 Visible Noise + Noise Amplification；Fixed Bugs `(non)` | [首帖](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535)（`updated_at` 经 Discourse JSON：`2026-05-12T00:36:44.902Z`） | 行业/实践 |
| 2026-05-31 | 用户称找到「unresolved pattern」的 workaround——措辞默认问题仍未解决 | [#303](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/303) | 行业/实践 |
| 2026-06-17 | Daller 提供「强制触发 pattern」的复杂自然/幻想 prompt；同会话多图、ChatGPT 路径 | [#308](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/308) | 行业/实践 |
| 2026-06-17 | 部分用户争论「是否只是 prompt 过载」；另有人仍看见强 pattern（同线程续帖） | [#310](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/310)–[#312](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/312) | 行业/实践（观察分歧，不作根因结论） |
| 2026-07 | 长帖活跃议题更多转向手部/解剖；**不构成**「噪声已消失」的证据 | [#336](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/336) 起 | — |
| 2026-08-06 | Peter Bakkum：仍 aware，仍 working on noise；称野外持续可见 | [https://x.com/pbbakkum/status/2085426695633580292](https://x.com/pbbakkum/status/2085426695633580292) | 官方（具名工程师公开回复） |
| 2026-08-07 | VeitB 转载上述推文；Daller 附和：野外仍见 typical pattern | [#355](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/355)、[#356](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/356) | 行业/实践 + 官方（经转载） |
| 2026-08-12 | 本次复核：changelog / model docs **未**记载该 artifact 修复；未见 Boyuan 修复宣布 | [Changelog](https://developers.openai.com/api/docs/changelog)、[gpt-image-2](https://developers.openai.com/api/docs/models/gpt-image-2) | 官方（沉默本身是证据边界） |

---

## A/B/C 分项判定

### A. 同会话放大 / carryover 效应

**判定：部分缓解有社区共识；「已完全修好」无官方宣布；首帖仍将其列为开放 bug（残差 / 依赖上一图数据时）。**

- **支持「放大曾被明显缓解」**：2026-04-24 Daller 称 amplification gone、每张新生成不再强依赖上一张（[#21](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/21)）。同日其又确认噪声本身仍在（[#27](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/27)）。
- **支持「并非干净结案」**：首帖（2026-05-12 编辑）仍写：amplifier「fixed a bit」，但 **Noise Amplification** 仍在 Bugs，并写「still amplifies over time」「keeps data from the preview picture」；workaround 仍是重启会话。[首帖 Bugs](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535)
- **与「图片输入 / edits 链」区分**：早期线程与 `_j` 等实测指出，把输出再喂回 edits 仍会叠斑驳（research.md §22 已记）。本次未重做实测；**不能**把「纯文本同会话放大缓解」外推为「编辑链放大已消失」。
- **官方**：未见 changelog 条目声明 carryover 已修。

### B. 基线 tiling / grime / noise

**判定：未宣布修复。最新一手信号仍是「在修」（2026-08-06 Peter Bakkum），而非「已修好」。**

- Boyuan Chen：可核到的公开表态为 2026-04-24 起的「actively fixing」、2026-05-04 前后线程汇总的「working on it」族回复；**未见**其承诺的 fix-announcement 推文落锤。
- Peter Bakkum 2026-08-06：明确仍在处理 noise，且称野外持续可见。[推文](https://x.com/pbbakkum/status/2085426695633580292)
- 官方 docs / changelog：无将该现象列为已知 limitation，也无「已修复」条目。[Changelog](https://developers.openai.com/api/docs/changelog)
- 社区首帖仍将 Visible Noise Patterns 列为开放问题，并写 **NO FIX POSSIBLE**（指 prompt 修不好，非指 OpenAI 永不修）。[首帖](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535)

### C. 2026-05 之后社区报告

**判定：仍有同类报告；未见可信的一手「已经好了」确认。**

- 2026-05-31：仍称 unresolved pattern（[#303](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/303)）。
- 2026-06-17：维护者仍发触发 prompt，默认 bug 可复现（[#308](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/308)）。
- 2026-08-07：工程师承认 + 维护者称野外仍见 typical pattern（[#355](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/355)、[#356](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/356)）。
- 未发现 OpenAI 官方账号或 Boyuan Chen 的「noise/tiling fixed」宣布被社区当作结案依据。

---

## 对 research.md 第 8 条与 §22 的建议改写

### 第 8 条（可粘贴）

> 8. **tiling / grime artifact 的当前状态**——**（2026-08-12 复核）**截至复核日，**未发现** OpenAI 官方或 Boyuan Chen 的「已修复」宣布。社区长帖首帖（最后编辑 2026-05-12）仍将 Visible Noise Patterns / Noise Amplification 列为开放 bug。最新具名工程师公开信号是 Peter Bakkum 2026-08-06：仍 aware 且 working on it，并称野外持续可见。[Community 长帖](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535) [Bakkum 推文](https://x.com/pbbakkum/status/2085426695633580292)  
> 强度：官方（工程师公开回复 + changelog 沉默）/ 行业/实践（论坛首帖与后续报告）。  
> PRD：**不要**假设已消失，也**不要**写成永久缺陷；写成需要随 OpenAI 公开声明再刷新的时点性事实。详见 `.scratch/anime-stylized-identity/tiling-grime-status.md`。

### §22 相关段落（可粘贴替换原「截至 2026-05-07…未核实此后」句）

> OpenAI 工程师 Boyuan Chen 在发布后公开表示正在修（2026-04-24 起；2026-05-04 前后仍为 working on it 族回复），并有「修好后会亲自宣布」的社区复述。**2026-08-12 复核：未见该宣布落地。** 更晚的一手信号是 OpenAI Peter Bakkum 于 2026-08-06 仍称正在处理 noise、野外持续可见。同会话放大效应在 2026-04-24 前后被社区报告为「明显缓解」，但首帖（2026-05-12）仍保留残差放大条目；基线噪声在公开信息中**未**被宣布清除。  
> 强度：官方（工程师公开回复）+ 行业/实践（论坛）。**未做**本次生成实测。

---

## 仍未核实

- Boyuan Chen「修好后亲自发推」的**原推全文 URL**（本次见到的是社区转述与 4/24 状态推；5/4「working on it / will announce」的逐字原推未在本次全部打开）。
- Peter Bakkum 推文上下文：回复对象 `@Angaisb_` 的原帖内容是否 100% 指向同一类 tiling/grime（社区理解为 noise/typical pattern；**未**在 X 上打开父推全文核对）。
- 静默后端改动是否在部分账号/区域减轻基线噪声（无 API/ChatGPT 实测；changelog 无条目不能证明「无改动」，只能证明「无公开宣布」）。
- 首帖 2026-05-12 之后是否有未反映到首帖 Bugs 区的维护者立场变化（末帖 2026-08-07 Daller 仍称野外可见 typical pattern，与「已修」相反）。
- 放大效应在 **API 无状态 generations** vs **ChatGPT 同会话** vs **edits 喂回** 三条路径上的当前差异（早期有讨论；本次未重测）。

---

## 检索说明（方法边界）

- 一手优先：OpenAI Community 长帖（Discourse JSON 核日期）、具名工程师 X 状态链接、OpenAI API changelog / model 页。
- 二手（apipass 等）仅用于回溯到 2026-05-07 断点；其文本身停在 May 7，**不能**证明 5 月之后状态。
- 未使用生成 API，未假装实测。
