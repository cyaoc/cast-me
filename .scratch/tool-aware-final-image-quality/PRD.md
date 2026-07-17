Status: ready-for-agent

# Tool-Aware Identity Input and Final-Image Verification

## Problem Statement

CastMe promises to turn a user-provided person image into a polished final asset while preserving visible identity, but three parts of the current contract remain weaker than the active OpenAI image workflow.

First, the skill describes the input image as the identity reference without explicitly requiring the generation or editing call to carry the actual image. That leaves room for an implementation to substitute a textual description when the reference is inaccessible, which cannot satisfy an identity-preserving request.

Second, the final-asset quality contract identifies explicit 4K output as experimental but does not apply the current model's documented total-pixel threshold. Other dimensions above the same threshold can therefore be treated as stable even though they are experimental.

Third, final review names the right failure categories but does not define the inspection scale. First Read must be judged at the intended display size, while small identity, hand, prop, and exact-text failures require focused inspection at the original available resolution.

The skill needs to close these gaps without adding an API integration, a quality questionnaire, a new workflow stage, automatic retries, or controls that the active generation surface does not expose.

## Solution

Require every identity-preserving generation or edit to pass each required person reference as an actual image input to the active generation surface. A text description may clarify reference roles or visible evidence, but it must never replace the image that anchors identity. If a required identity reference is no longer available to the tool, stop before generation and ask the user to reattach it.

Generalize the experimental-size rule from 4K alone to any output above 3,686,400 total pixels, the area of 2560 by 1440. Keep the existing conditional control boundary: use this rule only when the active surface exposes a real size control, continue without another gate when it does not, and claim an exact size only after verifying the resulting dimensions. An explicit experimental-size request receives a short truthful warning and proceeds when controllable; it does not create a new confirmation question.

Review visible results at two relevant scales. Judge First Read, hierarchy, composition, and intended-use readability at the target display size. Then inspect only the high-risk regions actually present in the image at the original available resolution: the face and identity geometry, visible hands and prop interactions, and required exact text. Preserve angle-correct and natural facial asymmetry rather than treating symmetry as a quality goal. If the result or required inspection resolution is unavailable, do not claim visual verification.

## User Stories

1. As a user requesting an identity-preserving image, I want my person reference passed to the image model as an actual image, so that likeness is anchored in visible evidence rather than a prose approximation.
2. As a user requesting an edit of my image, I want the image being edited to remain an actual tool input, so that the edit does not silently become a text-to-image regeneration.
3. As a user who supplied several required identity angles, I want every reference needed for the chosen target angle passed as an image input, so that the model receives the evidence the skill relied on.
4. As a user who supplied identity, wardrobe, pose, or style references, I want each included image's role stated clearly, so that supporting references do not overwrite the Primary Identity Anchor.
5. As a user whose reference image is no longer accessible to the generation tool, I want the skill to ask me to reattach it before generating, so that it does not pretend a text description can preserve my identity.
6. As a user whose old reference remains visible only as conversation history that the active tool cannot include, I want generation to pause at that specific missing input, so that unrelated creative choices are not reopened.
7. As a user who describes additional identity details in text, I want those details treated as supporting description rather than a replacement reference, so that the actual image remains authoritative.
8. As a user who accepts inference for missing body scale, angle, or performance evidence, I still want the face identity image passed to the model, so that accepted inference does not become permission for text-only identity generation.
9. As a user requesting a normal final asset, I want the highest stable non-experimental size compatible with my aspect ratio when real size control exists, so that nominal resolution does not reduce reliability.
10. As a user requesting an output at or below 3,686,400 total pixels, I want it kept outside the experimental-size rule, so that the skill does not overstate risk.
11. As a user requesting an output above 3,686,400 total pixels, I want it labeled experimental, so that I understand the documented reliability boundary before delivery.
12. As a user requesting a 2048 by 2048 image, I want its total pixel area recognized as experimental, so that a square dimension is not misclassified merely because neither edge is called 4K.
13. As a user requesting a 2048 by 1152 image, I want it treated as a stable-size candidate when supported, so that the skill applies the total-pixel threshold rather than a vague 2K label.
14. As a user explicitly requesting 4K, I want it handled as one instance of the general experimental-size rule, so that 4K does not need a separate and inconsistent quality concept.
15. As a user explicitly requesting an experimental size, I want a concise warning followed by generation when the surface can control it, so that I am informed without being forced through another confirmation gate.
16. As a user working on a surface without a real size control, I want generation to continue, so that an unavailable technical control does not block the creative workflow.
17. As a user working on a surface without a real size control, I want exact size and experimental-size application left unverified, so that delivery claims remain truthful.
18. As a user receiving a generated asset, I want exact pixel dimensions claimed only after the output was inspected, so that prompt wording is not mistaken for file verification.
19. As a viewer of a final asset, I want its First Read checked at the intended display size, so that the main person, face, silhouette, action, emotion, product, or message registers in actual use.
20. As a user receiving a portrait or avatar, I want the face inspected at the original available resolution, so that small identity drift and facial-plane errors are not missed in a thumbnail.
21. As a user receiving an action image with visible hands, I want hands and relevant prop contact inspected closely, so that malformed fingers or broken interaction geometry are not hidden by the overall composition.
22. As a user requesting exact text, I want each required string inspected character by character at a readable scale, so that a visually plausible title is not mistaken for correct delivery.
23. As a user receiving an image without visible hands, props, or exact text, I want those checks skipped, so that review remains focused on real risks rather than becoming a fixed checklist.
24. As a user depicted at a three-quarter or profile angle, I want natural and angle-correct facial asymmetry preserved, so that review does not push the face toward artificial symmetry or a frontal redesign.
25. As a user whose generated output is not visible to the assistant, I want visual QA reported as unavailable, so that the skill does not claim to have inspected an unseen asset.
26. As a user whose output is visible only below the resolution needed for a focused check, I want that region marked unverified, so that low-resolution inspection is not overstated.
27. As a user whose result has one visible defect, I want the existing Surgical Revision behavior preserved, so that review does not trigger a new concept or broad regeneration.
28. As a user receiving a satisfactory first result, I do not want an automatic second pass, so that final-image verification does not create extra generation cost or identity drift.
29. As a beginner, I want these input, size, and review rules handled internally, so that stronger quality does not add a technical questionnaire.
30. As a user on any supported OpenAI image surface, I want the skill to use only controls the surface actually exposes, so that API capabilities are not falsely presented as available tool controls.

## Implementation Decisions

- Extend the existing coordinating workflow and owner modules; do not introduce another generation or review stage.
- Make actual image attachment a hard precondition for identity-preserving generation and editing. Text may describe or disambiguate a reference but cannot replace the Primary Identity Anchor.
- Pass every person reference required by the resolved Reference Coverage to the active image tool. Continue to label multiple input roles and preserve the Primary Identity Anchor over style, pose, wardrobe, or supporting-angle references.
- If a required identity image cannot be included through the active surface, ask only for that image to be reattached. Preserve all existing Explicit Locks, Derived Locks, accepted risks, and resolved creative choices.
- Do not reinterpret accepted inference for missing body, angle, or performance evidence as permission to omit the actual face identity reference.
- Define experimental size by total output area: more than 3,686,400 pixels is experimental. The comparison is strictly greater than; the threshold itself is not experimental under this rule.
- Treat 4K as an example of experimental output rather than as the sole special case.
- Apply exact size behavior only when the active surface exposes a real size control. When it does not, continue without another gate and do not claim that an exact size or experimental setting was applied.
- When the user explicitly requests a controllable experimental size, state the experimental status concisely and proceed. Do not add a confirmation question or quality questionnaire.
- Claim an exact pixel size only after the generated asset's dimensions have been verified.
- Keep the existing Final-Asset Quality default: normal person-centered work targets the highest stable non-experimental size compatible with the selected aspect ratio when that control exists.
- Add a two-scale review rule inside the existing review step. Use intended display size for First Read and overall hierarchy; use original available resolution for relevant high-risk regions.
- Focus close review on face identity and geometry, visible hands and prop interactions, and required exact text. Skip absent or irrelevant regions.
- Evaluate facial coherence against the selected angle, projection, head turn, and gaze. Do not use bilateral symmetry as a general success criterion.
- Preserve truthful-review boundaries. If the output or sufficient inspection resolution is unavailable, report the corresponding review as unavailable or unverified.
- Preserve existing targeted-revision behavior. Review does not schedule an automatic edit, second generation, upscaling step, or post-processing stage.
- Keep current domain vocabulary. These changes refine Primary Identity Anchor, Reference Coverage, Final-Asset Quality, First Read, and Surgical Revision; they do not introduce a new domain term or require an ADR.

## Testing Decisions

- Use the existing golden-conversation behavior suite as the single high-level testing seam. Tests should assert observable routing, generation readiness, user-visible warnings, review claims, and preservation behavior rather than exact internal wording or section-loading mechanics.
- Add a scenario where an accessible person reference is carried into identity-preserving generation as an actual image input rather than summarized into text.
- Add a scenario where the required identity reference is unavailable to the active tool. The expected behavior is one focused reattachment request, no generation, no text-only fallback, and no reopening of resolved choices.
- Add a multi-reference scenario that distinguishes the Primary Identity Anchor from supporting angle, wardrobe, pose, or style inputs and carries every required person reference into the generation call.
- Add a scenario proving that accepted inference for missing body, angle, or performance coverage does not remove the actual identity-image requirement.
- Add boundary scenarios for exactly 3,686,400 total pixels and for a value above it. Only the value above the threshold is experimental.
- Add representative dimension scenarios: 2048 by 1152 remains below the threshold, while 2048 by 2048 and 3840 by 2160 are experimental.
- Add a no-size-control scenario that continues generation without another gate and does not claim an exact size or experimental setting was applied.
- Add an explicit experimental-size scenario that gives a concise warning and proceeds when controllable without asking for confirmation.
- Add an exact-size delivery scenario that permits the claim only after output dimensions are verified.
- Add a two-scale review scenario that checks First Read at intended display size and then inspects only the face, hands or prop interaction, and exact text that are present and relevant.
- Add a profile or strong-angle scenario ensuring that review accepts angle-correct asymmetry and does not demand a frontal or artificially symmetric face.
- Add an unavailable-output and insufficient-resolution scenario ensuring the skill does not claim visual QA it could not perform.
- Preserve the existing Surgical Revision scenario to prove that a detected local defect does not reopen creative direction or trigger an automatic second pass.
- Run the existing structural skill validator after the behavior suite. Treat it as a packaging and reference-integrity check, not a second behavior-testing seam.
- Run the repository's ordinary whitespace and diff checks to catch malformed Markdown without expanding the feature's test surface.

## Out of Scope

- Adding, requesting, or documenting an `input_fidelity` control for GPT Image 2.
- Adding explicit mask generation or mask upload behavior.
- Claiming that a mask guarantees pixel-identical preservation outside the selected region.
- Building an Image API integration, image-tool wrapper, or another runtime component.
- Exposing or adding model, quality, size, mask, candidate-count, or fidelity controls that the active image surface does not provide.
- Changing the current GPT Image 2 model selection.
- Adding a CJK-specific warning or claiming that non-Latin text is categorically less accurate than English.
- Generating multiple candidates by default or adding a default candidate-selection workflow.
- Automatic retries, automatic revisions, second-pass finishing, upscaling, or external design-tool automation.
- Replacing the existing exact-text verification and clean no-text-base fallback.
- Adding a new review service, computer-vision scorer, face matcher, or pixel-difference system.
- Changing identity-risk gates, safety handling, creative clarification, Scoped Option Refresh, First-Pass Finish, or output recipes beyond the three agreed corrections.
- Adding new domain glossary terms or an ADR for these reversible contract refinements.

## Further Notes

- The current OpenAI image guide states that GPT Image 2 processes image inputs at high fidelity automatically, so an `input_fidelity` rule would not improve this workflow.
- The guide describes GPT Image masks as prompt-based guidance rather than an exact structural guarantee, and the active built-in image tool does not expose a mask argument.
- The documented experimental boundary is based on total pixels, not on whether either edge is informally called 2K or 4K.
- The active built-in tool supports actual reference-image inputs but does not expose model, quality, size, mask, candidate-count, or input-fidelity parameters. The specification therefore strengthens only behavior the skill can truthfully enforce.
