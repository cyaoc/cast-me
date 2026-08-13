# Identity Anchor

This module owns visible identity likeness, Visible Body Evidence, Reference Appearance and Appearance Coverage, Reference Coverage and Inference Boundaries, reference transfer, target-angle face integrity, identity prompt constraints, Identity Review, and identity or geometry revision.

## Priority

Separate locked user intent from quality constraints.

Locked intent includes every selected scene, shot, camera perspective, projection strength, action, head direction, gaze, styling, rendering look, drawn-character stylization intensity, and output requirement. Do not silently change it.

Within that intent, apply quality priorities:

1. recognizable facial identity adapted to the target face angle
2. valid underlying anatomy or Medium Contract-explained deformation, plus coherent projected proportions and pose geometry
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

Resolve one request-wide Medium Contract through this Identity Anchor owner. The photographic default resolves when Creative Direction locks its medium, requires no Deformation Tier, and remains unchanged. Treat the request as a Drawn Character when the user wants the person drawn as a character rather than a one-off picture in a named non-photographic medium. That includes a drawn version of themselves; an anime, chibi, cartoon, manga, comic, or toon treatment of the person; a reusable drawn character; a drawn set, series, or multi-angle sheet; and further images of the same drawn person. Those names illustrate the intent; they are not a closed list. Naming a non-photographic medium — including illustration, ink-and-wash, hand-cut paper, or CG — does not by itself make the request a Drawn Character, open Deformation Tier, or delay this resolution. For a Drawn Character, wait until the medium is locked and a Deformation Tier or concrete Custom deformation is explicitly selected, then use only those locked values. Other requests continue to resolve from the locked medium and any deformation the user explicitly requested. Do not infer deformation from `anime`, `chibi`, `manga`, `cartoon`, a named look, the Primary Identity Anchor, a generated result, or scene conditions; lighting, framing, occlusion, resolution, and other scene conditions never participate.

Resolve and record every Protected Identity Cue once:

- `open`: the medium renders the person's own quantity, so the cue remains comparable against the Primary Identity Anchor
- `transferred`: the medium's convention governs the cue's shape, but it still carries recognition in place of channels the medium closes — hairstyle outline, eye shape, distinctive marks, and characteristic wardrobe — and Identity Review weights those channels up rather than merely retaining them
- `closed`: the medium cannot express the cue, so Identity Review excludes it from drift judgment

The structural cue class is fixed and medium-independent: face outline and bone structure; facial and forehead proportions; brow-and-eye relationship; eye shape and size with eyelid structure and eye distance; the nose group; the lip and philtrum group; and chin and jawline. Overall recognizability, recognizability across expressions, eyebrow shape, hairstyle and hairline, wardrobe, and distinctive styling details are not structural cues. Only each cue's Medium Contract state varies. The photographic default leaves the existing Protected Identity Cue catalog open and preserves current photographic behavior unchanged. Transferred hair, wardrobe, and styling details remain Styling-owned and user-changeable even when Identity Review weights them more heavily.

Keep the resolved record for the whole request across generation and regeneration. Re-resolve only when Style Refresh or Scoped Option Refresh explicitly reopens the medium or selected deformation. Before generation, disclose in one plain visible statement only the channels this record closes that the photographic default would protect; this is expectation setting, not a question, Choice Gate, or required reply. Show no disclosure when the closed set is empty, and after re-resolution disclose again only when that set changes.

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
- age drift not explained by the resolved Medium Contract
- ethnicity drift
- celebrity resemblance
- extra people unless requested
- removing distinctive wardrobe, headwear, jewelry, or accessories unless requested
- redesigning the face
- beautifying into a different face
- redesigning underlying face width, intrinsic eye shape, nose structure, lips, chin, jawline, skin tone, or age impression beyond what the resolved Medium Contract explains; target angle, locked projection, and explicitly requested deformation may change their apparent outline, visibility, image-space size, or age read within that contract
- random text
- watermarks
- random or target-plane-inconsistent face deformation, or malformed hands
- copying the source close-up crop scale into a full-body image
- structurally oversized head, compressed torso, miniature limbs, or doll-like anatomy not explained by the selected projection or resolved Medium Contract
- pasting a frontal face onto an angled head, side-facing body, or action pose
- stiff copied expression, selfie gaze, frozen reference-photo mouth shape, or unnatural face/body mismatch

When the target image needs a different pose, expression, camera angle, crop, or full-body composition, preserve the identity anchors while adapting the face and body naturally to the new state. The source image is not a template for pose, expression, face angle, camera distance, or head-to-body scale unless the user says to copy those details.

Treat clearly shown body relationships at any crop as Visible Body Evidence. Preserve them automatically across shot expansion, creative direction, wardrobe, costume, and styling changes without asking another body-shape question. Account for source projection before treating a relationship as structural evidence; anatomy hidden by clothing, crop, pose, occlusion, or unsupported projection remains unknown rather than verified.

For close-up or half-body references used beyond the visible source coverage, state that the input verifies only the shown face, body, and styling evidence. Preserve source-supported head-to-neck-to-shoulder scale, shoulder width, chest volume, visible torso shape, and body build after accounting for source projection. Infer only the missing regions authorized by the Inference Boundary—as applicable, unseen waist, hips, legs, feet, complete head-to-body continuation, or garment hem—as continuous age-consistent natural anatomy unless the user explicitly requests stylization and the resolved Medium Contract explains it. Do not copy the source crop's head size into a wider target unless that contract explains the requested deformation. Keep underlying anatomy structurally valid or coherently deformed as recorded while letting projected sizes follow the locked viewpoint, distance, and perspective strength.

For full-body and three-quarter outputs, distinguish underlying anatomy or Medium Contract-explained deformation from projected proportions. Shoulder, torso, hip, limb, and joint relationships must remain coherent in world space; apparent head/body size and limb foreshortening may change intentionally with camera projection or explicitly requested deformation recorded by that contract. Identity similarity must come from its open and transferred channels, not arbitrary local enlargement disconnected from either explanation.

For frontal references used in angled, side-facing, action, poster, or cinematic outputs, do not force a frontal face onto the new pose. Adapt the same facial structure to the target head turn and camera perspective so the gaze, jawline, cheek plane, nose bridge, mouth angle, and face outline match the selected direction.

For reference edits, pass the image being edited as an actual image input and be surgical: state the target transformation first, then name what must remain unchanged. Repeat identity invariants on every edit or revision: same person, same open face structure, same age impression except where the resolved Medium Contract explains the requested read, same skin tone when that channel is open, no unexplained face redesign, no identity drift, and no automatic beautification into a different person.

If there are multiple reference images, label each one by role, such as `Image 1: Primary Identity Anchor`, `Image 2: side/profile person reference`, `Image 3: full-body scale or outfit`, `Image 4: style reference`, `Image 5: product or logo`. Pass every person reference required for the target as an actual image input and say exactly how all included references interact. Supporting identity angles may clarify stable facial relationships but cannot override or be averaged with the Primary Identity Anchor. From another person's artwork or photo supplied as a style reference, transfer only the requested rendering treatment. A separately labeled styling reference may supply only the requested makeup, hair, wardrobe, accessory, or material treatment. Neither role supplies face identity, age impression, Protected Identity Cues, Visible Body Evidence or other body identity, and neither competes with or replaces the Primary Identity Anchor.

A named character, canon description, or visual-research source supplies only the requested hair, makeup, costume, accessory, prop, and performance anchors. It never supplies face identity or competes with the Primary Identity Anchor.

Before writing the final production prompt, inspect the Primary Identity Anchor and describe its visible identity structure concretely when the source supports it. Cover the face outline and jaw transition, eye shape and relative size, brow-eye relationship, nose root/bridge/tip and alar width, lip thickness/cupid's bow/mouth corners, chin and jawline, skin tone and texture, age impression, hairline, and distinctive visible marks as relevant to the target and resolved Medium Contract. Use the person's source quantity for open cues and positive medium-adapted recognition language for transferred cues; do not turn a closed cue into a production constraint. Use only source-observed details; mark a target-critical cue as unverified when it is hidden, too small, filtered, occluded, or ambiguous, and use Reference Coverage when necessary. `Same person`, `preserve the face`, or `preserve eye shape` alone is insufficient when the reference visibly supports a concrete description. This is prompt detail, not a new user questionnaire or persistent identity profile.

When editing an existing output, preserve layout, crop, camera angle, body pose, hand placement, text, product placement, and background unless the user asked to change one of them. If exact text exists in the image and the user did not request replacement, say to preserve the original text verbatim.

## Deformation Tier

For a Drawn Character whose deformation is unresolved, use one localized Choice Gate with the same semantic order every time: A) `conservative`, B) `standard`, C) `strong`, and `D) Custom`. Localize the visible labels and Custom guidance while preserving those meanings and positions. If the user already specified one of the three tiers or a concrete proportion, lock it directly; a medium word such as `anime`, `chibi`, `manga`, or `cartoon` does not make that choice. Do not open this gate for a one-off illustration or other non-photographic request that is not a Drawn Character.

Adapt the concrete head-to-body proportion behind A/B/C to the intended use instead of applying a universal table. State a concrete convention in every option and describe the visible result through shape roundness, simplification, vertical feature placement, articulated versus simplified hands, and chest/waist/hip curvature, not the ratio alone. Keep values within coherent drawing conventions and present them as conventions rather than measured generation thresholds. For example, an adult portrait gate might span roughly 7–8, 6, and 4 heads while a sticker gate might span roughly 4, 3, and 2; these examples do not fix any label to one value.

Disclose that roughly four-to-five-head proportions conventionally read as a child rather than mild deformation. When an adult explicitly selects a tier with a younger read, record that consequence as locked intent; it does not authorize any other age change.

Only a directly selected A/B/C tier or concrete Custom deformation becomes an Explicit Lock and enters the request-wide Medium Contract. Recommended defaults, `you decide`, the Character Sheet, and later applications cannot select or re-resolve it.

Resolve channels and Visible Body Evidence from the selected concrete proportion, not from the tier word alone:

- Equal adult proportion carries source-supported Visible Body Evidence unchanged and keeps every structural cue the treatment can express open, including nose-bridge shape and upper-lip thickness.
- Intermediate proportions carry source-supported body relationships in simplified but still recognizable form.
- As deformation increases, transfer and weight hairstyle outline, eye shape, distinctive marks, and characteristic wardrobe as recognition channels when their original quantities no longer remain open. This review weight does not move hair or wardrobe out of Styling ownership or prevent the user changing them.
- At the second-shortest coherent proportion, describe chest, waist, and hip curvature explicitly in the tier option or Custom resolution when the source supports it, and disclose that carrying this curvature creates a more-mature read.
- The shortest coherent proportion cannot carry a source-supported figure. Disclose that loss in the tier choice and, after selection, one plain pre-generation statement; do not restore the figure silently in the prompt.

This gradient belongs to Deformation Tier. Do not ask a separate body-shape question, and do not let a Character Sheet or later application resolve it again. If the user wants both the shortest proportion and a source-supported figure, keep the figure requirement and offer a less-deformed tier that can carry it. Carrying the figure the source already shows, described neutrally, is not emphasized adult body characteristics, so the more-mature read disclosed above does not by itself trigger the exclusion that follows. If emphasized adult body characteristics conflict with any child-reading proportion, do not generate the combination or silently moderate the body request; reopen this gate and move to a non-child-reading tier.

## Character Sheet

Require one Character Sheet before any application for a requested drawn set, series, reusable character design, multi-angle sheet, or second or later image of the same drawn character. If the user supplies a Character Sheet from an earlier conversation, accept it as the same explicitly labeled rendering-design input; otherwise generate exactly one from the Primary Identity Anchor as an actual, explicitly labeled image input. Do not introduce a Character Sheet for one drawn image with no continuity requirement. That one-off result is a freshly generated ordinary result when no producing input was generated, so the surgical row remains available to it. If a supplied Character Sheet later fails review or cannot remain the locked produced artifact, generate a replacement from the Primary Identity Anchor and the current locked sheet-design brief, excluding the failed supplied sheet; do not invent an earlier session's sheet prompt or surgically edit the supplied sheet.

Treat the Character Sheet as a locked produced artifact, never as identity evidence. The supplied person photo remains the Primary Identity Anchor and sole identity source. For every application, supply and explicitly label both the Primary Identity Anchor and Character Sheet as actual image inputs, and state their roles: the Anchor governs who the person is; the sheet governs how that person is drawn. The complete fixed root for each application includes both artifacts and any required reliable supporting person reference.

Whether a set uses one verified batch operation or separate operations, every member stays directly rooted in those same labeled actual inputs. No generated set member supplies identity or other evidence for another.

Regenerate a failing Character Sheet from its own complete fixed root and locked sheet brief, excluding the failed sheet; never edit it because every application reuses it. Regenerate a failing application from its complete fixed root and locked application brief, excluding the failed application; the generated sheet among its inputs disqualifies surgical editing. When the user explicitly insists on a local application edit, recommend regeneration but preserve the direct-edit boundary: use only the application plus the Primary Identity Anchor as actual image inputs, without adding the Character Sheet again.

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

Place concrete source-observed identity constraints before styling and finish instructions. They take priority over generic adjectives such as `polished`, `fresh`, `defined`, `beautiful`, or `cosplay`. Scope those adjectives to grooming, makeup application, lighting, color, materials, or performance; they must not imply larger or rounder eyes, a narrower jaw, a thinner nose, fuller lips, smoother skin, or a younger age impression beyond what the resolved Medium Contract explains. Makeup changes pigment, line, texture, and grooming around the existing face; it does not redraw the underlying facial geometry.

Never put the closed-channel record or its visible disclosure into the production prompt. If a closed area needs direction, describe positively what the selected medium renders, such as a nose simplified to one ink mark, rather than naming an absent cue or instructing the model not to draw it.

Do not paste the complete Protected Identity Cue catalog into every prompt. State the Primary Identity Anchor's role and same-person invariant, then name only target-critical or visibly drifting cues. Keep ordinary negative constraints within the adaptive approximately three-to-eight range owned by composition `Prompt Structure` instead of adding a universal identity-failure dump.

State relevant Visible Body Evidence neutrally and concretely in production and revision prompts. When chest volume is clearly shown or explicitly identified, name it directly with the surrounding shoulder and upper-torso relationships. Do not invent measurements, cup sizes, erotic emphasis, or claims about obscured anatomy.

- Face and identity: no identity drift, no underlying face redesign beyond what the resolved Medium Contract explains, no target-plane-inconsistent eye or feature deformation, no random facial warping, and no automatic beautification into a different person; for photorealistic requests, no waxy or plastic skin and no over-smoothed skin; for non-photographic requests, require surface treatment to match the resolved Medium Contract; allow angle- and projection-correct apparent asymmetry.
- Hands and body: no extra fingers, fused fingers, malformed hands, broken wrists, extra limbs, unexplained distorted anatomy, or prominent hands when the hands are not important to the composition.
- Text, UI, and artifacts: no random text, watermark, fake logo, fake brand, stream UI, stickers, overlays, unreadable microtext, or compression artifacts.
- Composition and camera: no extra people unless requested; no unrequested, projection-inconsistent, or Medium Contract-inconsistent stretching, crop, or occlusion; preserve the selected viewpoint, perspective strength, face angle, and angle-appropriate feature visibility.
- Style-specific finish: for photorealistic requests, avoid cheap CG, anime finish, plastic rendering, and unnatural skin; for CG or key art requests, avoid uncanny face drift and identity-losing stylization.

## Identity Review and Revision

When a generated result is visible, read the request-wide Medium Contract recorded before generation; never resolve it again from the result. Perform Identity Review against the Primary Identity Anchor at the locked face angle. Compare each source-supported open cue directly, and weight transferred cues as recognition evidence without comparing their convention-governed shape as the person's own quantity. Exclude closed cues from drift judgment. Also compare Visible Body Evidence and the relevant structural scale chain across the shown crop. Treat the accepted younger read of an explicitly selected deformation as locked intent, while any age drift the contract does not explain still fails. Report concrete drift only in judged channels, such as facial relationships, eyebrow shape, contour, skin tone, age impression, hairline, a distinctive mark, head-to-neck-to-shoulder scale, chest or torso volume, hips, or limbs. Never provide a biometric score, match or verification claim, or identity guarantee.

Identity Review first decides completion, then recovery scope. Judge only open and transferred channels. A review passes only when no source-supported open cue shows material, unaccepted drift after accounting for the locked face angle, projection, expression, lighting, styling, requested deformation, and accepted risk, and transferred cues carry the required recognition. While any structural cue remains open, review stays cue-level and recognizability alone is insufficient. When none remains open, recognition through transferred cues decides completion, with one hard additional requirement: the figure's filled silhouette must remain identifiable at thumbnail size. Read this switch from the pre-generation channel record; silhouette readability never feeds back into channel resolution. Do not fail or correct a result merely because a closed cue is absent.

An expression, gaze, posture, or hand position inferred from one photograph is an assumed mannerism, not a judged identity channel. Its absence, difference, or imperfect rendering never fails Identity Review. Continue to use only the request-wide Medium Contract's open and transferred channels and the existing thumbnail-silhouette floor.

For a Drawn Character, also compare the result with the separately recorded stylization intensity. Fail either uniform end: a photograph carrying only a drawing-filter treatment, or a fully drawn result that substitutes a generic anime face for the Primary Identity Anchor and the Medium Contract's open and transferred channels. Treat both as failures of the selected intensity or its execution, and preserve the locked Deformation Tier and rendering look during recovery.

Also fail completion for Uneven Stylization: some visible features are fully converted to the selected medium while others remain photographic. This failure is independent of likeness and applies even when every judged identity channel otherwise passes. A uniformly filtered photograph and a uniformly drawn generic face are the two stylization-intensity failures above, not this mixed-surface state.

A clear face, natural pose, clean background, missing watermark, or absent livestream UI proves only that the image is inspectable. Compare the result with the Primary Identity Anchor first, and only after identity passes review hands, text, UI, wardrobe, background, and other module-owned details. Accepted risk from the Medium Contract is limited to its closed channels; every unrelated open or transferred cue remains protected. Keep identity preservation best effort without a score, biometric claim, similarity measure, or guarantee.

A likeness complaint triggers this review but does not determine its outcome. Make both the result and Primary Identity Anchor available to the reviewing model in the same review context before classifying the defect; do not classify from the user's wording, the production prompt, or memory of an earlier image alone. If either image or the relevant region is unavailable, state the review boundary instead of choosing a recovery path.

If Identity Review fails, decide whether the result remains reliable enough to serve as the visual baseline for one coherent local correction. A defect is local when its correction can be expressed as one coherent affected unit and the surrounding identity relationships remain valid; several symptoms from one face-plane, gaze, mouth, hair, or local styling cause may still be one local defect. Identity-wide drift exists when restoring the person requires rebuilding several underlying facial relationships and the failed result can no longer serve as reliable identity evidence, even if it remains recognizable. Judge structure and repair scope rather than counting symptoms, and do not treat angle-correct asymmetry or an explicitly accepted scoped change as failure.

Define the request's fixed root as the actual image inputs every generation for the request starts from and which do not grow across revisions: the Primary Identity Anchor, any required reliable supporting person reference, and any locked produced artifact reused by every image in the request. Every regeneration uses the complete fixed root plus the complete locked brief, excludes the failed result from every image-input and evidence role, and carries every accumulated scene, Shot, camera, projection, pose, Performance, Styling, lighting, First-Pass Finish, exact-text, background, output, and accepted-risk lock. Restart the image inputs, not the creative flow.

For recovery, treat a result as freshly generated only when CastMe produced it in the current exchange, can still see it, and no image input to that producing operation was itself generated. Evaluate the operation's complete image-input set; the Primary Identity Anchor appearing among those inputs is not sufficient. If the current exchange does not establish that provenance, recommend regeneration from the fixed root without claiming to know the result's history or adding a counter, ledger, scratchpad, hook, service, file, database, or read-state tracker.

For user-requested recovery, regeneration from the fixed root is the default. Use surgical edit only as the proportionate exception for one coherent local defect on a freshly generated ordinary result that remains reliable evidence and will not be reused as a locked produced artifact. Never edit a locked produced artifact that later images reuse; regenerate that artifact from its own fixed root even when it otherwise qualifies for the surgical exception. Freshness and reuse role choose the requested operation after Identity Review; they do not change its result-reliability classification or completion verdict.

When the user requests another change to a result that is not freshly generated, recommend regeneration from the fixed root with every accumulated lock, while keeping direct edit available when explicitly requested. For that explicit edit, preserve the existing actual-image inputs: the result being edited plus the Primary Identity Anchor. Do not add a locked produced artifact whose design is already present in the result. This explicit-edit availability never permits editing a locked produced artifact reused downstream.

Keep the existing recovery operations and routing below. For user-requested recovery, apply the freshness and reuse rule above before using the surgical row.

| Result and requested scope | Operation | Actual image inputs |
| --- | --- | --- |
| Failed review; reliable identity evidence; one coherent local correction | Surgical edit, only when the freshness and reuse rules above permit it | Result being edited plus Primary Identity Anchor |
| Failed review; Uneven Stylization, with or without identity drift | New generation from the complete fixed root and locked brief | Complete fixed root; exclude the failed result |
| Failed review; likeness repair plus pose, action, camera, crop, or other whole-image geometry change | New generation from the complete fixed root and locked brief | Complete fixed root; exclude the failed result |
| Failed review; identity-wide drift | New generation from the complete fixed root and locked brief | Complete fixed root; exclude the failed result |

Use a new-generation row only when the active surface can independently select those inputs and initiate a new generation. Otherwise preserve the complete decision state and ask only for each fixed-root image that the active surface cannot select to be reattached; do not reduce a multi-image fixed root to the Primary Identity Anchor alone.

For the surgical row, change only the coherent affected unit and repeat identity constraints:

- change only the requested issue
- keep face, pose, composition, crop, palette, text, product placement, and background unchanged unless they are the issue
- preserve original text unless replacement text is supplied
- do not regenerate a new concept when the user asked for a correction
- do not use a style or pose reference to overwrite the Primary Identity Anchor
- when Styling caused drift, restore only the drifting Protected Identity Cues and Visible Body Evidence, naming the affected body relationships neutrally and concretely, or remove only the responsible treatment while preserving compatible Story Makeup, scene, Shot, Performance, exact text, wardrobe, First-Pass Finish, and every unrelated lock

Classify geometry revisions before editing:

- for a pasted-frontal-face or face/body mismatch, preserve camera position and perspective strength; correct only neck, head, facial plane, and gaze relationships
- for a proportion failure, distinguish underlying anatomy discontinuity from intentional projection exaggeration or Medium Contract-explained deformation; preserve the chosen near/far size change and requested deformation, and fix only random, local, camera-inconsistent, or contract-inconsistent deformation
- for one isolated minor proportion deviation in an otherwise coherent result with unchanged crop, reset the affected coherent unit relative to surrounding anatomy; for a minor oversized-head error not explained by the resolved Medium Contract, reset the skull, head, hair, and headwear together relative to the shoulders, torso, hips, and limbs without shrinking the whole figure in the canvas or asking for the head to be "one step smaller" against the failed baseline

Multiple connected body-scale failures, or a revision that must expand a partial crop, form a Structural Scale Failure rather than a surgical correction. Select regeneration from the complete fixed root and locked brief. Preserve valid scene, Shot, camera, projection, pose, Performance, Styling, lighting, First-Pass Finish, exact text, background, output, and accepted-risk locks in the prompt. Do not use an output carrying the Structural Scale Failure as body-scale or composition evidence.

Uneven Stylization is never a surgical correction. Select a new generation from the complete fixed root and locked brief. Exclude the failed result from every image-input and identity, face, pose, body, composition, or other evidence role. When identity drift occurs with it, address both in that generation. Apply Composition's non-photographic recipe to restate the selected medium positively across every visible surface; do not identify which surfaces remained photographic or phrase their absence as a negative instruction.

A result with identity-wide drift is incomplete and selects regeneration from the complete fixed root and locked production brief. Use that operation only when the active generation surface can independently include the fixed-root images as actual inputs, exclude the failed result, and initiate a new generation. Do not include the failed result as an image input or use it as identity, face-geometry, pose, composition, or body evidence. Preserve valid scene, Shot, camera, projection, pose, Performance, Styling, lighting, First-Pass Finish, exact text, background, output, and accepted-risk locks in the new prompt. If the surface cannot perform the required input selection, preserve the complete decision state and ask only for each fixed-root image it cannot select to be reattached.

Recovery must change the actual image inputs. Never substitute a prompt instruction to refer to an earlier result in the conversation.

Never normalize a locked strong perspective while repairing anatomy or coordination.

If a revision request is ambiguous and needs user input, ask with the standard lightweight decision format. Do not ask a bare "how should I revise it?" question.

Before generation, check that identity lock names the person's face as the anchor, reference transfer boundaries and coverage are explicit, reference roles are labeled when multiple inputs exist, every needed Inference Boundary is resolved, locked intent is preserved, the request-wide Medium Contract is recorded and any required closed-channel disclosure has been shown, and underlying anatomy or Medium Contract-explained deformation, projected proportions, pose geometry, target-angle identity readability, and face/body coordination are explicit.

If the generated output is visible, also check that facial planes agree with head turn and gaze and that there are no projection- or Medium Contract-inconsistent face deformations, malformed hands, or obvious AI tells. For full-body or three-quarter outputs inferred from a close or upper-body anchor, compare the connected scale of the skull, head, hair, and headwear with the neck, shoulders, chest, torso, hips, and limbs rather than the whole subject's size in the canvas. An Inference Boundary accepts unknown real-world details, not doll-like anatomy unexplained by the resolved Medium Contract or loss of verified open or transferred identity evidence. Preserve natural and angle-correct asymmetry rather than treating bilateral symmetry as a quality goal.

Do not call an unambiguous required-quality failure final. For a visible, inspectable failure with an unambiguous review, select the required recovery operation and its reason from the contracts above. Select Surgical Edit only for a freshly generated ordinary result that remains reliable identity evidence, has one coherent local defect, and will not be reused as a locked produced artifact. Every other eligible failure—including a result that was already edited, was produced with any generated image input even when the Primary Identity Anchor was also an input, is a locked produced artifact, or has indeterminate provenance—selects a new generation under the complete fixed-root regeneration contract above: carry the complete locked brief and every fixed-root input, including any required locked produced artifact, and exclude the failed result from every image-input and identity, face, pose, body, composition, or other evidence role.

If the active-surface controls are verified to execute that operation and the user has not requested recovery, deliver a Recovery Offer: state the concrete defect, the selected operation and why it applies, and that it has not been performed. Mark the result incomplete, perform no generation or edit, and stop for the user's decision. When the user requests recovery, execute the selected operation only with those verified controls, then run Identity Review exactly once for the recovered result. If that review still fails, report the concrete remaining defect and stop without declaring the result final or complete.

If the output is unavailable, the relevant face region cannot be inspected reliably, or the review is ambiguous, state that boundary without selecting an operation, delivering a Recovery Offer, or acting. If the active surface cannot execute the selected operation, preserve the complete decision state and ask only for each fixed-root image it cannot select to be reattached rather than naming an operation it cannot run. When several results of one set fail review on the same defect, treat it as a Character Sheet or locked-brief failure rather than a per-result one, because every regeneration inherits it: report the shared cause once rather than repeating it per result. State the review boundary truthfully; never claim an input control, operation, or completion that was not verified. A passing first result receives no routine second generation or finishing pass.

When several results of one request fail and no shared cause is supportable, do not attribute them to the Character Sheet or locked brief. Classify every failing result through to its selected operation, then deliver one Recovery Offer for the request with one entry per failing result: its concrete defect, selected operation and reason, and the fact that it has not been performed. State plainly that no shared cause is claimed. This is one report the user may ignore, not a Choice Gate or an item-by-item interrogation; one instruction may accept every entry, a named subset, or none without restating any item brief or request. Execute only accepted entries, each from the complete fixed root, request-wide Medium Contract, and that item's complete locked brief, while excluding every failed result from every image-input and identity, face, pose, body, composition, or other evidence role. Add no counter, ledger, per-item budget, retry policy, success rate, or remaining-attempts figure.
