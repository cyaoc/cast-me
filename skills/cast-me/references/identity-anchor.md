# Identity Anchor

This module owns visible identity likeness, Visible Body Evidence, Reference Appearance and Appearance Coverage, Reference Coverage and Inference Boundaries, reference transfer, target-angle face integrity, identity prompt constraints, Identity Review, and identity or geometry revision.

## Priority

Separate locked user intent from quality constraints.

Locked intent includes every selected scene, shot, camera perspective, projection strength, action, head direction, gaze, styling, and output requirement. Do not silently change it.

Within that intent, apply quality priorities:

1. recognizable facial identity adapted to the target face angle
2. valid underlying anatomy plus coherent projected proportions and pose geometry
3. nonessential scene, styling, prop, hand-detail, lighting, and finish complexity

If locked intent conflicts with identity or geometry, present a risk-choice gate. Recommend improving missing evidence or simplifying only unresolved, nonessential variables first. Change a locked camera, action, head direction, or gaze only when the user explicitly reopens it, never as an automatic fallback.

Use `styling-performance.md` for the performance decision itself. This module vetoes silent high-risk execution, not the user's chosen direction.

Treat identity preservation as best effort, not guaranteed. Do not identify the person, infer sensitive traits, transform the person into a celebrity, or claim consent/ownership/age/relationship details the user did not provide.

Identity is a required readable quality constraint for every person-centered result, but it is not always the First Read. Let the locked use determine whether the face, person, silhouette, action, emotion, product, or message leads the composition.

Use `user-provided self-reference image` only when the user explicitly says the image is them, a selfie, or their own image. Otherwise use `user-provided person reference image`.

Use the user's person reference as the Primary Identity Anchor and pass it to every identity-preserving generation or revision as an actual image input. Text may describe visible evidence or disambiguate roles, but it never replaces that image. An Inference Boundary for missing body, angle, or performance evidence does not permit omitting the Primary Identity Anchor.

If any person reference required by the resolved Reference Coverage is no longer available to the active image tool, stop before generation and ask only for that image to be reattached. Preserve all Explicit Locks, Derived Locks, accepted risks, and resolved creative choices.

## Reference Transfer

Do not treat every visible detail in the reference image as fixed.

Preserve after the user requests it, accepts recommended defaults, or when the detail is not a production-critical creative choice:

- visible identity
- selected or distinctive wardrobe, headwear, jewelry, and accessories
- user-specified props, text, product, or brand elements

Treat the target-critical subset of these visible identity anchors as Protected Identity Cues:

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
- distinctive visible styling details

Track clearly shown head-to-neck-to-shoulder scale, shoulder width, chest volume, visible torso shape, body build, silhouette, and stance separately as Visible Body Evidence at any source crop.

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
- redesigning underlying face width, intrinsic eye shape, nose structure, lips, chin, jawline, skin tone, or age impression; target angle and locked projection may change their apparent outline, visibility, or image-space size
- random text
- watermarks
- random or target-plane-inconsistent face deformation, or malformed hands
- copying the source close-up crop scale into a full-body image
- structurally oversized head, compressed torso, miniature limbs, or doll-like anatomy not explained by the selected projection
- pasting a frontal face onto an angled head, side-facing body, or action pose
- stiff copied expression, selfie gaze, frozen reference-photo mouth shape, or unnatural face/body mismatch

When the target image needs a different pose, expression, camera angle, crop, or full-body composition, preserve the identity anchors while adapting the face and body naturally to the new state. The source image is not a template for pose, expression, face angle, camera distance, or head-to-body scale unless the user says to copy those details.

Treat clearly shown body relationships at any crop as Visible Body Evidence. Preserve them automatically across shot expansion, creative direction, wardrobe, costume, and styling changes without asking another body-shape question. Account for source projection before treating a relationship as structural evidence; anatomy hidden by clothing, crop, pose, occlusion, or unsupported projection remains unknown rather than verified.

For close-up or half-body references used beyond the visible source coverage, state that the input verifies only the shown face, body, and styling evidence. Preserve source-supported head-to-neck-to-shoulder scale, shoulder width, chest volume, visible torso shape, and body build after accounting for source projection. Infer only the missing regions authorized by the Inference Boundary—as applicable, unseen waist, hips, legs, feet, complete head-to-body continuation, or garment hem—as continuous age-consistent natural anatomy unless the user explicitly requests stylization. Do not copy the source crop's head size into a wider target. Keep underlying anatomy structurally valid while letting projected sizes follow the locked viewpoint, distance, and perspective strength.

For full-body and three-quarter outputs, distinguish underlying anatomy from projected proportions. Shoulder, torso, hip, limb, and joint relationships must remain valid in world space; apparent head/body size and limb foreshortening may change intentionally with camera projection. Identity similarity must come from facial structure, not arbitrary local enlargement disconnected from that projection.

For frontal references used in angled, side-facing, action, poster, or cinematic outputs, do not force a frontal face onto the new pose. Adapt the same facial structure to the target head turn and camera perspective so the gaze, jawline, cheek plane, nose bridge, mouth angle, and face outline match the selected direction.

For reference edits, pass the image being edited as an actual image input and be surgical: state the target transformation first, then name what must remain unchanged. Repeat identity invariants on every edit or revision: same person, same face structure, same age impression, same skin tone, no face redesign, no identity drift, and no automatic beautification into a different person.

If there are multiple reference images, label each one by role, such as `Image 1: Primary Identity Anchor`, `Image 2: side/profile person reference`, `Image 3: full-body scale or outfit`, `Image 4: style reference`, `Image 5: product or logo`. Pass every person reference required for the target as an actual image input and say exactly how all included references interact. Supporting identity angles may clarify stable facial relationships but cannot override or be averaged with the Primary Identity Anchor. Transfer only the requested makeup, hair, wardrobe, accessory, material, or visual treatment from another person's styling reference; never borrow that person's face, age impression, body, or identity.

A named character, canon description, or visual-research source supplies only the requested hair, makeup, costume, accessory, prop, and performance anchors. It never supplies face identity or competes with the Primary Identity Anchor.

When editing an existing output, preserve layout, crop, camera angle, body pose, hand placement, text, product placement, and background unless the user asked to change one of them. If exact text exists in the image and the user did not request replacement, say to preserve the original text verbatim.

## Reference Coverage

Treat visible facial styling, grooming, and hair whose makeup status or source is unknown as Reference Appearance. It is valid evidence for the visible person, but it does not verify an unseen bare-face appearance. Unknown makeup alone is not an Appearance Coverage gap, and final prompts must describe the target transformation without claiming makeup removal to a known natural baseline.

Define Appearance Coverage by the Protected Identity Cues needed for the target. Ask for more evidence or an Inference Boundary only when source styling, filters, face paint, hair, accessories, occlusion, or image quality hide a target-critical cue; clear visible cues require no additional appearance question.

Before generation, record only the coverage needed by the target as `verified`, `described`, `inferred`, or `missing`, separated by evidence type and visible region:

- face identity coverage: visible facial structure and which face angles are actually shown
- appearance coverage: target-critical Protected Identity Cues visible through the Reference Appearance
- body-scale coverage: visible head-to-neck-to-shoulder scale, shoulder width, chest volume, torso shape, body build, hip, limb, height, stance, and outfit information; keep verified regions separate from missing or inferred continuation
- angle coverage: frontal, three-quarter, profile, high/low viewpoint, and perspective evidence
- performance coverage: expression range, weight-bearing pose, action, hands, and prop interaction

The source image remains evidence only for what it shows. A face or upper-body reference can verify face identity and visible styling without verifying full-body scale, alternate angles, or action geometry.

Run this check before generation when the requested output depends on source information the provided reference does not show well:

- the target reveals body scale, limbs, feet, posture, support, hands, or prop interaction outside the visible source coverage
- the target requires face, head, body, or camera angles not shown by the source
- the target depends on body build, height impression, outfit, or movement facts that are not visible
- the target requires expression or performance range not demonstrated by the source
- multiple reference images with unclear roles

If production-critical coverage is missing and the user has not explicitly accepted an Inference Boundary for those gaps, ask one Choice Gate before generation. Construct its paths from the actual coverage gaps and inherit every locked scene, camera, Shot, action, expression, and styling choice. A bare-face or substantially different facial-styling target may expose missing Appearance Coverage when the source hides cues that target requires; never promise automatic de-makeup or reconstruction.

Present exactly four relevant paths: A) add real references for the listed missing evidence, B) describe those missing facts, C) accept an explicit Inference Boundary for only those gaps, and D) supply another coherent resolution inside this coverage gate. Preserve the locked Shot, camera, action, styling, and scene; do not introduce a safer crop, body concealment, or other lock change unless the user explicitly reopens it.

An Inference Boundary lists the exact missing regions or evidence the user permits CastMe to estimate. Accepting it never reclassifies Visible Body Evidence and never authorizes a different missing region, face or body angle, appearance cue, action, hand interaction, or performance fact.

Recommend the most accurate path that preserves locked intent. Change camera, crop, or action only if the user explicitly reopens it; never introduce that change as a fallback inside the coverage gate.

If the user supplies real references or descriptions, incorporate only the supplied details and keep the original person image as the Primary Identity Anchor. If the user explicitly accepts an Inference Boundary, continue without another coverage question unless a new missing dimension becomes central to the request. Make the prompt explicit about which evidence remains verified and which authorized regions or facts are natural estimates.

For high-risk source-to-target jumps, preserve every locked camera and performance choice while exposing the missing coverage. Recommend added evidence or user description first; if the user accepts an Inference Boundary, keep the selected Shot and label only the authorized body, angle, and performance facts as inferred.

Use a staged stability strategy only when the user explicitly requests it or supplies it as a coherent Custom Path. It does not reopen a locked Shot, framing, angle, or action, and all synthetic intermediate evidence remains inferred rather than verified.

The generated result should feel like the same person in a new scene, not a copy of the source screenshot.

Trigger the existing identity-risk choice when Styling would replace, redraw, or obscure Protected Identity Cues such as facial relationships, skin tone, age impression, hairline, or a distinctive mark. Judge the proposed change by cue replacement or visibility, not by whether makeup looks light, natural, bold, or heavy. Preserve identity by default; after explicit risk acceptance, scope it to the named cue, occlusion, angle, or transformation and proceed without repeating that same gate. Keep unrelated cues protected, treat a newly introduced risk as unresolved, and keep the story through compatible non-identity styling details.

## Face Visibility and Performance Integrity

Use `styling-performance.md` for exact pose, action, expression, gaze, hands, props, wardrobe, and role/costume styling. This section defines identity-safe limits for those choices.

Keep identity readable at the target face angle instead of turning the person back toward camera. A frontal face can show both eyes; a three-quarter face may naturally narrow the far eye; a profile may hide it. Preserve angle-correct brow, eye, nose, cheek, mouth, jaw, ear, and outline relationships. Prefer restrained performance only when the user has not locked a stronger direction.

A selected camera perspective is locked user intent. Strong high/low viewpoints, close wide perspective, fisheye-like treatment, and deliberate stretching remain available when chosen. If they threaten identity or anatomy, use the risk-choice gate; do not silently reduce the angle, increase camera distance, narrow the perspective, or turn the face back toward camera.

Avoid:

- unrequested extreme viewpoints or lens distortion
- accidental face/body stretching that does not follow the selected camera perspective
- unnecessary extreme profile angles when they do not serve the requested concept or identity readability
- forcing a frontal face onto a turned head, side-facing body, or action pose
- face/body perspective mismatch where gaze, jawline, cheek plane, nose bridge, mouth angle, and head turn do not agree
- hair, accessories, props, or shadows covering major facial features
- expressions that fight the requested theme, such as goofy, blank, aggressive, overly seductive, or modern selfie expressions when they do not fit

## Identity Prompt Constraints

Use positive, concrete visual direction first. Choose only negative constraints relevant to the requested output:

Do not paste the complete Protected Identity Cue catalog into every prompt. State the Primary Identity Anchor's role and same-person invariant, then name only target-critical or visibly drifting cues. Keep ordinary negative constraints within the adaptive approximately three-to-eight range owned by composition `Prompt Structure` instead of adding a universal identity-failure dump.

State relevant Visible Body Evidence neutrally and concretely in production and revision prompts. When chest volume is clearly shown or explicitly identified, name it directly with the surrounding shoulder and upper-torso relationships. Do not invent measurements, cup sizes, erotic emphasis, or claims about obscured anatomy.

- Face and identity: no identity drift, no underlying face redesign, no target-plane-inconsistent eye or feature deformation, no random facial warping, no waxy or plastic skin, no over-smoothed skin, no automatic beautification into a different person; allow angle- and projection-correct apparent asymmetry.
- Hands and body: no extra fingers, fused fingers, malformed hands, broken wrists, extra limbs, distorted anatomy, or prominent hands when the hands are not important to the composition.
- Text, UI, and artifacts: no random text, watermark, fake logo, fake brand, stream UI, stickers, overlays, unreadable microtext, or compression artifacts.
- Composition and camera: no extra people unless requested; no unrequested or projection-inconsistent stretching, crop, or occlusion; preserve the selected viewpoint, perspective strength, face angle, and angle-appropriate feature visibility.
- Style-specific finish: for photorealistic requests, avoid cheap CG, anime finish, plastic rendering, and unnatural skin; for CG or key art requests, avoid uncanny face drift and identity-losing stylization.

## Identity Review and Revision

When a generated result is visible, perform Identity Review against the Primary Identity Anchor at the locked face angle. Compare visible Protected Identity Cues, Visible Body Evidence, and the relevant structural scale chain across the shown crop. Report concrete drift, such as facial relationships, eyebrow shape, contour, skin tone, age impression, hairline, a distinctive mark, head-to-neck-to-shoulder scale, chest or torso volume, hips, or limbs. Never provide a biometric score, match or verification claim, or identity guarantee.

A likeness complaint triggers this review but does not determine its outcome. Make both the result and Primary Identity Anchor available to the reviewing model in the same review context before classifying the defect; do not classify from the user's wording, the production prompt, or memory of an earlier image alone. If either image or the relevant region is unavailable, state the review boundary instead of choosing a recovery path.

First decide whether the result remains reliable identity evidence. A defect is local when its correction can be expressed as one coherent affected unit and the surrounding identity relationships remain valid; several symptoms from one face-plane, gaze, mouth, hair, or local styling cause may still be one local defect. Identity-wide drift exists when restoring the person requires rebuilding several underlying facial relationships and the failed result can no longer serve as reliable identity evidence. Judge structure and repair scope rather than counting symptoms, and do not treat angle-correct asymmetry or an explicitly accepted scoped change as failure.

Choose the operation from both result reliability and the total requested change:

| Result and requested scope | Operation | Actual image inputs |
| --- | --- | --- |
| Reliable identity evidence; one coherent local correction | Surgical edit | Result being edited plus Primary Identity Anchor |
| Likeness repair plus pose, action, camera, crop, or other whole-image geometry change | New generation from the locked brief | Primary Identity Anchor plus only required reliable supporting person references; exclude the result |
| Identity-wide drift | New generation from the locked brief | Primary Identity Anchor plus only required reliable supporting person references; exclude the failed result |

Use either new-generation row only when the active surface can independently select those inputs and initiate a new generation. Otherwise preserve the complete decision state and ask only for the Primary Identity Anchor to be reattached.

For the surgical row, change only the coherent affected unit and repeat identity constraints:

- change only the requested issue
- keep face, pose, composition, crop, palette, text, product placement, and background unchanged unless they are the issue
- preserve original text unless replacement text is supplied
- do not regenerate a new concept when the user asked for a correction
- do not use a style or pose reference to overwrite the Primary Identity Anchor
- when Styling caused drift, restore only the drifting Protected Identity Cues and Visible Body Evidence, naming the affected body relationships neutrally and concretely, or remove only the responsible treatment while preserving compatible Story Makeup, scene, Shot, Performance, exact text, wardrobe, First-Pass Finish, and every unrelated lock

Classify geometry revisions before editing:

- for a pasted-frontal-face or face/body mismatch, preserve camera position and perspective strength; correct only neck, head, facial plane, and gaze relationships
- for a proportion failure, distinguish underlying anatomy discontinuity from intentional projection exaggeration; preserve the chosen near/far size change and fix only random, local, or camera-inconsistent deformation
- for one isolated minor proportion deviation in an otherwise coherent result with unchanged crop, reset the affected coherent unit relative to surrounding anatomy; for a minor oversized-head error, reset the skull, head, hair, and headwear together relative to the shoulders, torso, hips, and limbs without shrinking the whole figure in the canvas or asking for the head to be "one step smaller" against the failed baseline

Multiple connected body-scale failures, or a revision that must expand a partial crop, form a Structural Scale Failure rather than a surgical correction. Regenerate from the Primary Identity Anchor and locked brief. Preserve valid scene, Shot, camera, projection, pose, Performance, Styling, lighting, First-Pass Finish, exact text, background, output, and accepted-risk locks in the prompt. Do not use an output carrying the Structural Scale Failure as body-scale or composition evidence.

A result with identity-wide drift is incomplete. Regenerate from the Primary Identity Anchor and locked production brief only when the active generation surface can independently include the Anchor as an actual image input, exclude the failed result, and initiate a new generation. Do not include the failed result as an image input or use it as identity, face-geometry, pose, composition, or body evidence. Preserve valid scene, Shot, camera, projection, pose, Performance, Styling, lighting, First-Pass Finish, exact text, background, output, and accepted-risk locks in the new prompt. If the surface cannot perform the required input selection, preserve the complete decision state and ask only for the Primary Identity Anchor to be reattached.

Never normalize a locked strong perspective while repairing anatomy or coordination.

If a revision request is ambiguous and needs user input, ask with the standard lightweight decision format. Do not ask a bare "how should I revise it?" question.

Before generation, check that identity lock names the person's face as the anchor, reference transfer boundaries and coverage are explicit, reference roles are labeled when multiple inputs exist, every needed Inference Boundary is resolved, locked intent is preserved, and underlying anatomy, projected proportions, pose geometry, target-angle identity readability, and face/body coordination are explicit.

If the generated output is visible, also check that facial planes agree with head turn and gaze and that there are no projection-inconsistent face deformations, malformed hands, or obvious AI tells. For full-body or three-quarter outputs inferred from a close or upper-body anchor, compare the connected scale of the skull, head, hair, and headwear with the neck, shoulders, chest, torso, hips, and limbs rather than the whole subject's size in the canvas. An Inference Boundary accepts unknown real-world details, not visible doll-like anatomy or loss of verified evidence. Preserve natural and angle-correct asymmetry rather than treating bilateral symmetry as a quality goal.

Do not call an unambiguous required-quality failure final. Perform one automatic correction, and never more than one, using the appropriate path above only when the result is visible and inspectable and the active surface can execute the required input selection and generation or edit. Then run Identity Review once more. If the correction still fails, report the concrete unresolved defect and stop; do not retry again or declare the result final or complete.

Do not automatically correct when the output is unavailable, the relevant face region cannot be inspected reliably, the review is ambiguous, or the first result passes. State the review boundary truthfully; never claim an input control, correction, or completion that was not verified. A passing first result receives no routine second generation or finishing pass.
