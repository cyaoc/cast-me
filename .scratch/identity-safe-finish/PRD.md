Status: ready-for-human

# Identity-Safe First-Pass Finish

## Problem Statement

The skill already directs lighting, color, and finish, but it does not state a complete first-pass finishing contract for person-centered images. As a result, a prompt may describe a palette without resolving skin-tone priority, highlight and shadow treatment, natural texture, sharpening, grain, or restrained retouching. Adding a separate mandatory post-processing stage would duplicate the existing lighting/color decision, lengthen the conversation, and create another opportunity for identity drift.

## Solution

Expand the existing `lighting/color/finish` dimension into one adaptive `lighting/color/retouch/finish` contract. The first generation should contain the intended finished look. Photographic outputs use natural, identity-safe retouching by default when the user accepts recommended defaults; non-photographic outputs adapt the same contract to face, surface, and material rendering. Do not add a new mandatory question or an automatic second generation pass.

## User Stories

1. As a user requesting a polished person-centered image, I want the first generation to resolve exposure, color, skin rendering, texture, and finish together, so that the result does not look like an unfinished capture.
2. As a user who wants the same person, I want natural retouching to preserve facial structure, skin tone, age impression, skin texture, and distinctive marks, so that polish does not redesign the face.
3. As a user who has already selected a creative direction or accepted recommended defaults, I do not want another mandatory post-processing question.
4. As a user whose desired finish would materially change the result, I want visible outcome choices in the existing lighting/color question instead of technical LUT, camera, or editing jargon.
5. As a user who requests no facial retouching, I want that choice preserved while still allowing global exposure, color, contrast, and texture treatment.
6. As a user requesting stronger beauty retouching, I want identity risk exposed rather than having the skill silently weaken my request or change my face.
7. As a user reviewing a nearly correct result, I want a targeted finish revision to preserve identity, composition, pose, text, and background.

## Implementation Decisions

- Reuse the existing adaptive lighting/color step. Rename its owned dimension and final prompt slot to `lighting/color/retouch/finish`; do not add a post-processing step.
- Resolve the following together when relevant: exposure and white-balance intent, person/environment brightness and saturation relationship, skin-tone priority, highlight roll-off, shadow detail, local contrast, texture, grain or halation, sharpness, and material rendering.
- For realistic portraits, professional headshots, social avatars, and photographic editorials, recommend natural retouching: reduce distracting shine, minor unevenness, and transient-looking surface blemishes while preserving pores, fine lines, skin tone, age impression, and distinctive moles, freckles, or scars. When uncertain whether a mark is distinctive, preserve it.
- Natural retouching must not change face outline, bone structure, intrinsic eye shape, nose, lips, chin, jawline, ethnicity impression, body shape, or apparent age.
- For CG, game key art, illustration, or other non-photographic outputs, adapt finish to the chosen medium and material system. Do not force photographic skin-retouching vocabulary onto those outputs, but keep identity and natural face-structure constraints.
- A filter or grading treatment is never a universal default. It must follow the locked creative direction and motivated lighting/color logic; empty LUT names and one-size-fits-all presets are insufficient.
- If the user has specified the finish, accepted recommended defaults, or delegated remaining choices, resolve professional details internally. Ask within the existing lighting/color gate only when competing visible finishes would materially change intent.
- A bare creative-direction selection does not silently lock previewed retouching or finish. Preserve the existing `locked: explicit`, `locked: derived`, `suggested`, and `unresolved` behavior.
- An explicit `no retouch`, preservation request, or named facial mark is a lock. Global exposure, color, contrast, grain, and sharpness remain separately controllable.
- If stronger beauty retouching may change protected identity anchors, use the existing identity risk-choice gate. Do not create a second beauty-specific workflow.
- Do not run a second generation pass by default. After generation, revise only a concrete visible failure such as plastic skin, color cast, crushed shadows, clipped highlights, excessive smoothing, or oversharpening.
- A targeted finish revision repeats the identity invariants and preserves composition, crop, camera, pose, expression, gaze, wardrobe, text, product placement, and background unless one of them is explicitly reopened.

## Testing Decisions

- Use the existing golden-conversation behavior suite as the test seam.
- Add a realistic portrait or professional headshot scenario proving that accepted recommended defaults produce a complete first-pass finish with natural skin texture and no face redesign.
- Add a scenario proving that the feature reuses the existing lighting/color gate and does not add a mandatory post-processing question.
- Add a `no retouch` scenario proving that facial treatment stays off while global color and finish remain available.
- Add a stronger beauty-retouch scenario proving that identity-changing treatment uses the existing risk-choice gate.
- Add a targeted revision scenario proving that correcting plastic skin or a color cast preserves every unrelated locked element.

## Out of Scope

- Photoshop, Lightroom, LUT-file, or third-party editor integration.
- Deterministic pixel operations such as ICC or CMYK conversion, resizing, denoising, output sharpening, compression, metadata editing, or file-format conversion.
- A fixed filter catalog, preset browser, or universal cinematic grade.
- A separate mandatory post-processing question.
- An automatic second generation or editing pass.
- Broader changes to identity anchors, reference coverage, creative direction, styling, performance, or generation tooling.

## Further Notes

- This feature defines generation-time finish, not literal post-production on an exported file.
- No ADR is required because the change extends an existing skill-contract dimension and remains easy to revise.
