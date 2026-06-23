# Identity Anchor

Use this reference whenever a person reference image is involved. Its job is to protect visible identity likeness and natural, non-deformed human structure.

## Priority

Apply output priorities in this order:

1. visible identity likeness
2. natural non-deformed anatomy
3. composition, scene, pose, lighting, styling transformation, and performance ambition

When these conflict, recommend simplifying the scene, crop, action, hand work, props, camera ambition, beautification, or styling before sacrificing likeness or natural body structure. This is the default recommendation, not a silent override of the user's choice.

Use `styling-performance.md` for the styling/performance decision itself. This module's veto means veto silent high-risk execution, not veto user choice: when styling, performance, beautification, camera, or composition choices risk face drift or body deformation, require the coordinating director to present a risk-choice gate unless the user already accepted that risk.

Treat identity preservation as best effort, not guaranteed. Do not identify the person, infer sensitive traits, transform the person into a celebrity, or claim consent/ownership/age/relationship details the user did not provide.

Use `user-provided self-reference image` only when the user explicitly says the image is them, a selfie, or their own image. Otherwise use `user-provided person reference image`.

Use the input image as the identity reference.

## Reference Transfer

Do not treat every visible detail in the reference image as fixed.

Preserve after the user requests it, accepts recommended defaults, or when the detail is not a production-critical creative choice:

- visible identity
- selected or distinctive wardrobe, headwear, jewelry, and accessories
- user-specified props, text, product, or brand elements

Preserve these visible identity anchors:

- face outline and bone structure
- facial proportions, forehead proportion, and overall recognizability
- brow and eye relationship
- eyebrow shape
- eye shape, size, eyelid structure, and eye distance
- nose bridge, nose root, nose tip, and nostril/alar width
- lip thickness, cupid's bow, mouth corners, and philtrum length
- chin shape and jawline
- skin tone and age impression
- hairstyle and hairline
- recognizability across different theme-appropriate expressions
- original wardrobe, headwear, jewelry, and accessories unless the user asks to replace them, including style, color, material, pattern, cut, layers, wearing method, headwear outline, dangling elements, and major structure
- visible body silhouette and stance when a full-body or three-quarter source provides them
- distinctive visible styling details

Redesign temporary reference-photo state after the relevant choice is resolved and when useful for the requested theme:

- expression
- gaze direction
- face angle
- pose/action
- crop scale and head size in frame
- background
- lighting
- camera angle
- selfie, livestream, screenshot, or casual capture perspective
- screenshot UI, stickers, comments, stream overlays, clutter, and original low-quality capture artifacts

Avoid:

- face drift
- age drift
- ethnicity drift
- celebrity resemblance
- extra people unless requested
- removing distinctive wardrobe, headwear, jewelry, or accessories unless requested
- redesigning the face
- beautifying into a different face
- changing face width, eye shape, nose structure, lips, chin, jawline, skin tone, or age impression
- random text
- watermarks
- distorted face or hands
- copying the source close-up crop scale into a full-body image
- oversized head, tiny body, doll-like proportions, chibi proportions, compressed torso, or miniature limbs unless explicitly requested
- pasting a frontal face onto an angled head, side-facing body, or action pose
- stiff copied expression, selfie gaze, frozen reference-photo mouth shape, or unnatural face/body mismatch

When the target image needs a different pose, expression, camera angle, crop, or full-body composition, preserve the identity anchors while adapting the face and body naturally to the new state. The source image is not a template for pose, expression, face angle, camera distance, or head-to-body scale unless the user says to copy those details.

For close-up or half-body references used in full-body outputs, state that the input is only a face/visible-styling reference. Do not preserve the source image's close-up head scale. Use natural human proportions, camera distance appropriate for a complete standing or seated figure, balanced head-to-body scale, realistic shoulder width, torso length, legs, and feet.

For full-body and three-quarter outputs, require natural adult human proportions: realistic head-to-body scale, shoulder width, torso length, leg length, and limb size. Identity similarity must come from facial structure and visible styling anchors, not from enlarging the head.

For frontal references used in angled, side-facing, action, poster, or cinematic outputs, do not force a frontal face onto the new pose. Adapt the same facial structure to the target head turn and camera perspective so the gaze, jawline, cheek plane, nose bridge, mouth angle, and face outline match the selected direction.

For reference edits, be surgical: state the target transformation first, then name what must remain unchanged. Repeat identity invariants on every edit or revision: same person, same face structure, same age impression, same skin tone, no face redesign, no identity drift, and no automatic beautification into a different person.

If there are multiple reference images, label each one by role, such as `Image 1: person identity`, `Image 2: side/profile reference`, `Image 3: full-body scale or outfit`, `Image 4: style reference`, `Image 5: product or logo`. Say exactly how references interact. Do not treat a style, costume, pose, product, or lighting reference as evidence for the person's face identity.

When editing an existing output, preserve layout, crop, camera angle, body pose, hand placement, text, product placement, and background unless the user asked to change one of them. If exact text exists in the image and the user did not request replacement, say to preserve the original text verbatim.

## Reference Sufficiency

Run this check before generation when the requested output depends on source information the provided reference does not show well:

- full-body, seated, 9:16 half-body-to-thigh, hand/prop interaction, or complex action output from a face close-up, selfie, screenshot, beautified image, or half-body reference
- side profile, strong head turn, over-the-shoulder pose, or cinematic angle from a frontal-only reference
- specific body build, height impression, outfit, lower body, shoes, or posture that is not visible
- strong expression change when the reference has only one stiff, selfie, screenshot, or neutral expression
- multiple reference images with unclear roles

If the missing information is production-critical and the user has not accepted recommended defaults, ask one options block before generation. Prefer the accuracy-preserving path over natural inference:

```text
I recommend: add the missing reference details before generation, because the current image is enough for visible face identity but not enough to define exact body scale, alternate face angles, or expression range accurately.

Options:
A) I will attach more real reference images (Recommended) - full-body, side/profile, outfit, posture, or expression references for better accuracy
B) I will describe missing details - body build, posture, side/profile features, expression range, outfit, or lower-body details
C) Continue with natural inference - preserve identity anchors, infer realistic body proportions, adapt face angle and expression naturally to the scene; treat inferred details as estimates, not verified identity facts
D) Use a safer composition - half-body or three-quarter crop instead of full-body/action framing

Reply with A, or reply with "B + athletic build + relaxed smile + three-quarter left angle", or reply with "C + use recommended defaults".
```

If the user supplies real references or descriptions, incorporate only the supplied details and keep the original person image as the primary identity reference. If the user chooses natural inference or accepts recommended defaults, continue without further sufficiency questions unless a new missing dimension becomes central to the request. Make the prompt explicit that inferred body scale, angle, and expression are natural estimates, not verified identity facts.

For high-risk source-to-target jumps from close-up selfies, screenshots, beautified images, or single-angle face references into new scenes, complex actions, hand/prop interaction, full-body, or half-body-to-thigh compositions, recommend a conservative identity-first path unless the user explicitly chooses a more ambitious composition or says to generate a first attempt despite risk.

For high-risk source-to-target jumps, offer a staged stability strategy when possible: first generate a conservative half-body or three-quarter composition that locks likeness and natural proportions with reduced action complexity; if the result is close, make one targeted revision for face likeness, proportion, or deformation without reinventing the scene. If the user chooses a riskier first attempt, preserve identity as much as possible and state the accepted risk in the prompt.

The generated result should feel like the same person in a new scene, not a copy of the source screenshot.

## Face Visibility and Performance Integrity

Use `styling-performance.md` for exact pose, action, expression, gaze, hands, props, wardrobe, and role/costume styling. This section defines identity-safe limits for those choices.

Keep both eyes, nose bridge, lips, and face outline clearly visible unless the user asks for a profile or obscured-face concept. Prefer restrained performance over exaggerated posing when identity readability is at risk.

Avoid:

- extreme high angle or low angle
- fisheye or wide-angle closeups of the face
- exaggerated perspective stretching
- unnecessary extreme profile angles when they do not serve the requested concept or identity readability
- forcing a frontal face onto a turned head, side-facing body, or action pose
- face/body perspective mismatch where gaze, jawline, cheek plane, nose bridge, mouth angle, and head turn do not agree
- hair, accessories, props, or shadows covering major facial features
- expressions that fight the requested theme, such as goofy, blank, aggressive, overly seductive, or modern selfie expressions when they do not fit

## Identity Prompt Constraints

Use positive, concrete visual direction first. Choose only negative constraints relevant to the requested output:

- Face and identity: no identity drift, no face redesign, no asymmetrical eyes, no distorted face, no waxy or plastic skin, no over-smoothed skin, no automatic beautification into a different person.
- Hands and body: no extra fingers, fused fingers, malformed hands, broken wrists, extra limbs, distorted anatomy, or prominent hands when the hands are not important to the composition.
- Text, UI, and artifacts: no random text, watermark, fake logo, fake brand, stream UI, stickers, overlays, unreadable microtext, or compression artifacts.
- Composition and camera: no extra people unless requested, no extreme fisheye, no wide-angle face stretching, no cropped face or important headwear, no heavy occlusion of eyes, nose, mouth, or face outline.
- Style-specific finish: for photorealistic requests, avoid cheap CG, anime finish, plastic rendering, and unnatural skin; for CG or key art requests, avoid uncanny face drift and identity-losing stylization.

## Revision

If the result is close, revise surgically. Change one target at a time and repeat identity constraints:

- change only the requested issue
- keep face, pose, composition, crop, palette, text, product placement, and background unchanged unless they are the issue
- preserve original text unless replacement text is supplied
- do not regenerate a new concept when the user asked for a correction
- do not use a style or pose reference to overwrite the primary identity reference

If a revision request is ambiguous and needs user input, ask with the standard lightweight decision format. Do not ask a bare "how should I revise it?" question.

Before generation, check that identity lock names the person's face as the anchor, reference transfer boundaries are explicit, reference roles are labeled when multiple inputs exist, reference sufficiency is resolved when relevant, identity risks from styling/performance are handled, priority order is explicit, and face visibility, natural head-to-body scale, and face/body angle consistency are explicit.

If the generated output is visible in the current thread, review whether the person still looks like the input reference, face anchor features are preserved rather than redesigned, both eyes/nose bridge/lips/face outline remain clear enough for identity, and there are no distorted face/hands or obvious AI tells.
