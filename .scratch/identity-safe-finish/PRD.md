Status: ready-for-agent

# Identity-Safe First-Pass Finish

## Problem Statement

Beginner users can describe the kind of image they want but usually cannot translate “make it look finished” into lighting, grading, retouching, texture, and material decisions. The current workflow can resolve lighting and color without giving the user a complete, easy-to-imagine finishing choice, so the first generation may feel technically polished but visually unfinished or mismatched to the intended use.

The solution must not turn this gap into a parameter form, a fixed filter catalog, a separate mandatory post-processing step, or an automatic second generation pass. The user should be able to choose by visible feeling, while the skill translates that choice into a complete generation-time finish without weakening identity preservation.

## Solution

Extend the existing adaptive lighting/color dimension into a generation-time **First-Pass Finish** contract covering lighting, color, identity-safe retouching, texture, and final image character. The selected finish is included in the first generation prompt.

When First-Pass Finish is unresolved, reuse the existing lighting/color gate to show three complete, image-specific **Finish Directions** plus `D) Custom`. Each direction describes a coherent finished feeling in beginner-friendly visual language, one direction is recommended for the current use and locked creative intent, and the user chooses the complete result rather than individual technical parameters.

Photographic outputs use **Natural Retouch** as the recommended identity-safe baseline when defaults are accepted. CG, game key art, illustration, and other non-photographic outputs adapt the same contract to face, surface, material, and medium-specific finish without importing inappropriate photography vocabulary.

## User Stories

1. As a beginner requesting a person-centered image, I want the first generation to include a complete finished look, so that I do not need to understand professional post-production.
2. As a beginner choosing by feeling, I want complete Finish Directions rather than individual parameters, so that I can imagine the result before generation.
3. As a user with an unresolved finish, I want three concrete Finish Directions plus `D) Custom`, so that I receive guidance without losing free-form control.
4. As a user viewing Finish Directions, I want each one adapted to my current image, output type, and creative direction, so that the options are relevant rather than generic filter presets.
5. As a user who usually follows recommendations, I want one Finish Direction recommended using my intended use, locked creative direction, scene light, and identity priorities, so that the recommendation is meaningful.
6. As a beginner reading the recommendation, I want one short visible-result reason, so that I understand why it fits without learning technical jargon.
7. As a user who already specified a finish, I want that finish honored directly, so that the skill does not ask me to choose it again.
8. As a user who accepted recommended defaults or asked the skill to decide, I want First-Pass Finish resolved internally, so that ordinary clarification stops as requested.
9. As a user who selected only a creative direction, I want previewed finish details to remain suggestions until resolved, so that selecting a premise does not silently choose the final treatment.
10. As a user moving through the normal workflow, I want Finish Directions inside the existing lighting/color gate, so that this feature does not add another mandatory step.
11. As a user requesting a photographic portrait, headshot, avatar, or editorial image, I want Natural Retouch to reduce distracting shine, minor unevenness, and clearly temporary blemishes, so that the result feels polished but real.
12. As a user whose identity matters, I want Natural Retouch to preserve pores, fine lines, skin tone, age impression, facial structure, and distinctive marks, so that polish does not redesign me.
13. As a user whose facial mark may be a mole, freckle, scar, or temporary blemish, I want uncertain marks preserved, so that the skill does not erase identity evidence by guessing.
14. As a user who explicitly requests no facial retouching or preservation of a named mark, I want that choice locked while global light, color, contrast, and texture remain available.
15. As a user requesting stronger complexion, grooming, or texture polish, I want it applied without another gate when protected identity anchors remain unchanged.
16. As a user requesting changes to face or body structure, intrinsic features, skin tone, ethnicity impression, or apparent age, I want the existing identity risk choice used, so that the likeness tradeoff is explicit.
17. As a user requesting CG, game key art, illustration, or another non-photographic output, I want First-Pass Finish adapted to the selected medium, so that photographic retouching language does not distort the intended style.
18. As a user selecting a Finish Direction, I want its overall feeling, light and contrast, color relationship, person or material treatment, and relevant texture to form one coherent result.
19. As a user who does not understand LUTs or editing controls, I want the skill to translate my selected direction into only the controls that materially affect this image, so that the prompt stays complete without becoming a checklist.
20. As a user expecting a one-pass workflow, I want no automatic second generation or editing pass, so that First-Pass Finish remains part of the original generation.
21. As a user reviewing a nearly correct result, I want to request a targeted finish revision, so that a visible flaw can be corrected without restarting the concept.
22. As a user requesting a targeted finish revision, I want identity, composition, crop, camera, pose, expression, gaze, wardrobe, text, product placement, and background preserved unless I explicitly reopen them.

## Implementation Decisions

- Reuse the existing adaptive lighting/color step and extend its owned dimension and final prompt slot to `lighting/color/retouch/finish`; do not add a post-processing step.
- The coordinating director resolves First-Pass Finish in this order: honor an explicit finish; resolve it internally after accepted recommended defaults or delegated choices; otherwise route the unresolved choice to the existing lighting/color gate.
- An unresolved lighting/color gate presents exactly three image-specific Finish Directions labeled A through C plus `D) Custom`, with one direction marked recommended.
- A Finish Direction is a complete outcome bundle. It makes the overall finished feeling, light and contrast, color and person/environment relationship, identity-safe retouch or face/material treatment, and relevant texture easy to imagine.
- Finish Direction names and contents are generated for the current image. Do not create a fixed catalog, reuse preset names as a menu, or treat a palette-only change as a complete direction.
- Choose the recommended Finish Direction by fit with intended use, output type, locked creative direction, motivated scene light, and identity preservation. Do not always favor the most natural or most dramatic option.
- Explain the recommendation with one short reason describing the visible result, not camera, LUT, software, or editing terminology.
- Translate the selected Finish Direction into only production controls that materially affect the output. Exposure, white balance, highlight/shadow behavior, local contrast, grain, halation, sharpness, and material rendering are optional controls rather than mandatory fields.
- Preserve the existing `locked: explicit`, `locked: derived`, `suggested`, and `unresolved` decision behavior. A bare creative-direction choice does not silently lock previewed retouching or finish.
- For realistic portraits, professional headshots, social avatars, and photographic editorials, recommend Natural Retouch when the user accepts defaults: reduce distracting shine, minor unevenness, and clearly temporary blemishes while preserving pores, fine lines, skin tone, age impression, and distinctive moles, freckles, or scars. Preserve any uncertain mark.
- Natural Retouch must not change face outline, bone structure, intrinsic eye shape, nose, lips, chin, jawline, ethnicity impression, body shape, skin tone, or apparent age.
- An explicit `no retouch`, preservation request, or named facial mark is a lock. Global exposure, color, contrast, grain, and sharpness remain separately controllable.
- Stronger complexion, grooming, or texture polish may proceed without another gate while protected identity anchors remain unchanged. Requested changes to face or body structure, intrinsic features, skin tone, ethnicity impression, or apparent age use the existing identity risk-choice gate; do not create a beauty-specific workflow.
- For CG, game key art, illustration, and other non-photographic outputs, adapt finish to the selected medium and material system while preserving identity and natural face structure. Do not force photographic skin-retouching vocabulary onto those outputs.
- A filter or grading treatment must follow the locked creative direction and motivated lighting/color logic. Empty LUT names and one-size-fits-all presets are insufficient.
- Never run an automatic second generation or editing pass. Only an explicit user request may enter the existing targeted revision flow after generation.
- A targeted finish revision addresses one concrete visible failure, such as plastic skin, a color cast, crushed shadows, clipped highlights, excessive smoothing, or oversharpening, and repeats the identity invariants.
- A targeted finish revision preserves every unrelated locked element, including composition, crop, camera, pose, expression, gaze, wardrobe, text, product placement, and background.

## Testing Decisions

- Use the existing golden-conversation behavior suite as the single testing seam. It already tests adaptive question depth, decision inheritance, recommended defaults, identity-risk gates, Style Refresh behavior, and targeted revisions.
- Test externally visible conversation and prompt behavior rather than exact prose, internal labels, or a particular data representation.
- Add a defaulted photographic portrait or professional headshot scenario proving that accepted recommended defaults produce a complete First-Pass Finish with Natural Retouch, natural skin texture, and no face redesign, without another question.
- Add an unresolved beginner scenario proving that the existing lighting/color gate presents three complete, image-specific Finish Directions plus `D) Custom`, recommends the option that best fits the locked intent with a visible-result reason, and does not add a post-processing step.
- Add an explicit-finish scenario proving that an already specified finish is honored without another gate.
- Add a `no retouch` scenario proving that facial treatment remains off while global light, color, contrast, and texture remain available.
- Add a stronger beauty-retouch scenario proving that non-structural polish proceeds directly while identity-changing treatment uses the existing identity risk-choice gate.
- Add one CG or key-art scenario proving that finish adapts to its medium without photographic retouching vocabulary or irrelevant controls.
- Add a targeted revision scenario proving that correcting plastic skin or a color cast requires an explicit user request and preserves every unrelated locked element.

## Out of Scope

- Photoshop, Lightroom, LUT-file, or third-party editor integration.
- Deterministic pixel operations such as ICC or CMYK conversion, resizing, denoising, output sharpening, compression, metadata editing, or file-format conversion.
- A fixed filter catalog, preset browser, or universal cinematic grade.
- A separate mandatory post-processing or finish question.
- A parameter-by-parameter beginner questionnaire.
- An automatic second generation or editing pass.
- A beauty-specific risk workflow separate from existing identity safeguards.
- Broader changes to identity anchors, reference coverage, creative direction, styling, performance, or generation tooling.

## Further Notes

- First-Pass Finish is generation-time direction, not literal post-production on an exported file.
- Finish Direction is the beginner-facing choice; the production prompt remains detailed and professional internally.
- No ADR is required because this feature extends an existing skill-contract dimension, introduces no hard-to-reverse architecture, and remains easy to revise.
