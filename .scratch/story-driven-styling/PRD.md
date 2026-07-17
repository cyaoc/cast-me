Status: ready-for-agent

# Identity-Safe Story-Driven Styling

## Problem Statement

Users sometimes want CastMe to design makeup, hair, wardrobe, and accessories from a person's intended Character Read and the needs of a story. The current Styling Direction can resolve those fields, but it does not explicitly handle the fact that a person reference may already contain unknown makeup, grooming, filters, or styling. CastMe can see the Reference Appearance but cannot know which visible details are intrinsic, cosmetic, temporary, or representative of an unseen bare face.

Without a clearer contract, story styling can fail in opposite directions. It may preserve every visible cosmetic detail so rigidly that the requested character transformation never happens, or it may treat all makeup and hair as disposable and produce a well-styled stranger. Natural-looking contouring can replace Protected Identity Cues without triggering concern, while bold color that preserves facial relationships can be rejected merely for looking heavy. First-Pass Finish may also erase intentional Story Makeup as if fatigue, weathering, injury, or cosmetic breakdown were accidental blemishes.

The user should experience the result as the same visible person styled for a story. They should not need to know whether the source photograph contains makeup, understand professional makeup terminology, answer a makeup questionnaire for every image, or accept silent identity loss. CastMe must remain honest about what the reference actually verifies, use story and user input rather than face-based personality inference, and keep ordinary portraits lightweight.

## Solution

Deepen the existing Styling Direction and Identity Anchor modules instead of adding a makeup agent, Makeup Gate, or makeup-specific module. Styling Direction remains the single character-look interface and coordinates makeup, hair, wardrobe, and accessories across only the unlocked fields that need change. It preserves compatible Reference Appearance and may narrow to one field when the user explicitly locks the others.

Treat the visible styling, grooming, and hair state in a person reference as Reference Appearance whose makeup status and source may be unknown. Unknown makeup alone is not an Appearance Coverage gap. CastMe asks for additional evidence, user description, or accepted inference only when filters, styling, face paint, hair, accessories, or occlusion hide Protected Identity Cues required by the target look. It never claims to reconstruct an unseen bare face.

When the user asks CastMe to design the look from the story or decide it, treat that instruction as Delegated Styling and resolve one recommended Styling Direction internally without a visible option gate. When the user wants choices and styling is material, use the existing visible Styling Direction gate to present three complete, story-specific looks plus `D) Custom`; do not split makeup, hair, wardrobe, and accessories into separate menus. Story-driven styling preserves identity by default, and the existing identity-risk choice appears only when the proposed look would replace, redraw, or obscure Protected Identity Cues.

Intentional Story Makeup remains a Styling lock through First-Pass Finish. Natural Retouch and other finish handling may render the designed facial state coherently but cannot remove story-required fatigue, weathering, injury, grooming, cosmetic treatment, or breakdown as defects. Generated results receive an Identity Review based on visible cues rather than an automatic face score, and any likeness failure enters the existing targeted revision flow so that only the drifting styling details are corrected.

## User Stories

1. As a user uploading a person reference, I want CastMe to avoid assuming whether the person is wearing makeup, so that the workflow does not invent facts about the source image.
2. As a user whose reference may contain subtle makeup, I want the visible face treated as valid Reference Appearance, so that I am not forced to provide a bare-face photo for an ordinary task.
3. As a user whose reference contains makeup of unknown origin, I want CastMe to avoid claiming that it knows my unseen bare-face appearance, so that the result remains evidence-based.
4. As a user requesting story-driven makeup, I want the same visible person restyled for the story, so that the output reads as me in character rather than a newly designed face.
5. As a user requesting a no-makeup or bare-face result from a made-up reference, I want CastMe to expose the missing Appearance Coverage, so that hidden facial information is not silently fabricated.
6. As a user with missing Appearance Coverage, I want relevant choices to add a clearer person reference, describe the missing facts, or accept inference risk, so that I control the tradeoff.
7. As a user whose visible Protected Identity Cues remain clear despite unknown makeup, I want CastMe to proceed without another evidence question, so that normal styling stays lightweight.
8. As a user whose source contains face paint, a strong beauty filter, obscuring hair, or heavy contouring, I want CastMe to notice when the target depends on hidden cues, so that it does not treat altered evidence as verified identity.
9. As a user providing several person references, I want one Primary Identity Anchor to remain authoritative, so that different makeup states are not averaged into a new face.
10. As a user providing supporting identity angles, I want them to clarify stable facial relationships across appearances, so that strong story styling has better identity evidence.
11. As a user providing another person's makeup, hair, costume, or fashion reference, I want it used for styling only, so that its face, age, body, or identity does not transfer to me.
12. As a user describing the intended Character Read, I want that description to guide the look, so that the styling communicates the person I want the image to portray.
13. As a user saying that the look should fit my temperament, I want CastMe to treat temperament as creative intent rather than a factual personality inference, so that one photograph is not used to diagnose my character.
14. As a user who explicitly describes myself as calm, restrained, warm, severe, playful, or another visible impression, I want that self-description honored as a lock, so that the styling follows my stated intent.
15. As a user who provides only a story, I want the story to supply the Character Read, so that CastMe does not infer profession, personality, or inner traits from facial appearance.
16. As a user whose current appearance already supports the story, I want CastMe to preserve and deepen it, so that professional styling does not require gratuitous change.
17. As a user whose current appearance conflicts with the story, I want only the conflicting or missing styling fields redesigned, so that compatible identity and personal style remain intact.
18. As a user requesting a simple professional headshot, avatar, or ordinary portrait, I want Styling Direction skipped when the current appearance already fits, so that I do not answer unnecessary makeup questions.
19. As a user asking for an unrelated background, text, hand, or composition revision, I want styling left closed, so that a surgical edit does not reopen my look.
20. As a user requesting a role, period, ceremony, fashion editorial, stage look, special-effects look, or other story-dependent transformation, I want Styling Direction activated even if I did not list makeup and hair explicitly, so that the character is visually complete.
21. As a user saying that CastMe should design the look from the story, I want that instruction recognized as Delegated Styling, so that I am not asked to choose after already delegating.
22. As a user using Delegated Styling, I want CastMe to select one story-appropriate and identity-preserving look internally, so that generation can continue without a visible Styling gate.
23. As a user using Delegated Styling, I want focused identity-risk choices to remain available, so that delegation does not silently accept major likeness loss.
24. As a user who asks to see styling choices, I want three complete story-specific Styling Directions plus `D) Custom`, so that I can choose a whole visible result or describe my own.
25. As a beginner reviewing Styling Directions, I want each option to explain the Character Read, makeup, hair, wardrobe, accessories, preserved identity, and material risk in visible language, so that I do not need makeup artistry vocabulary.
26. As a user reviewing a recommendation, I want one Styling Direction recommended with a short visible-result reason, so that the recommendation is understandable and specific to my story.
27. As a user selecting a Styling Direction, I want only the fields actually stated by the option locked, so that preview details do not silently decide unrelated production dimensions.
28. As a user who locks my hair and wardrobe but asks for makeup choices, I want the same Styling Direction interface narrowed to makeup, so that no separate Makeup Gate or unrelated redesign appears.
29. As a user who locks my makeup but asks for clothing and accessories, I want the locked facial styling preserved, so that the system coordinates only the open fields.
30. As a user asking for refreshed Styling choices, I want the existing Scoped Option Refresh behavior to preserve Explicit Locks and unrelated dimensions, so that exploring looks does not restart the brief.
31. As a user receiving a bold but structure-preserving look, I want it allowed without an identity-risk choice merely because its colors are intense, so that story expression is not confused with identity loss.
32. As a user receiving natural-looking contouring or grooming that would redraw my face, I want it treated as identity-sensitive, so that subtle beautification cannot silently replace me.
33. As a user whose proposed look would change facial relationships, skin tone, age impression, hairline, or a distinctive mark, I want the existing identity-risk choice used, so that the likeness tradeoff is explicit.
34. As a user whose proposed look would cover important cues with hair, headwear, face paint, injury, prosthetics, or accessories, I want the visibility risk surfaced, so that the story does not erase the available identity evidence by accident.
35. As a user choosing the safer identity-preserving path, I want CastMe to keep the story through clothing, material, props, grooming, and localized makeup, so that safety does not collapse the creative concept.
36. As a user explicitly accepting a story transformation and its likeness risk, I want CastMe to proceed without repeating the same gate, so that an informed decision remains respected.
37. As a user requesting strong age, injury, ritual, theatrical, or special-effects styling, I want the story impact available after explicit risk acceptance, so that identity preservation does not become an absolute ban.
38. As a user whose story needs fatigue, weathering, injury, ritual marks, or cosmetic breakdown, I want those details recorded as Story Makeup, so that they are treated as intentional design rather than defects.
39. As a user receiving First-Pass Finish, I want Story Makeup preserved through light, color, texture, and Natural Retouch, so that polishing the image does not erase the narrative.
40. As a user requesting Natural Retouch alongside Story Makeup, I want unrelated shine or temporary distraction reduced while intentional fatigue, scars, dirt, or cosmetic treatment remains, so that polish and story can coexist.
41. As a user selecting only a Styling Direction, I want First-Pass Finish to remain separately unresolved or suggested, so that choosing makeup and clothes does not silently choose grading and retouching.
42. As a user selecting only a Finish Direction, I want Story Makeup and all other Styling locks preserved, so that changing the final surface does not redesign the character.
43. As a user expecting a coherent final image, I want makeup, hair, wardrobe, accessories, setting, performance, and finish to pass Physical Scene Coherence, so that every production choice belongs to the same story world.
44. As a user requesting a series, I want the base makeup, hair, wardrobe, and accessories recorded as Look Continuity, so that the same character look persists across images.
45. As a user showing the character before and after rain, conflict, travel, or injury, I want explicit story-state changes layered onto Look Continuity, so that continuity means believable evolution rather than exact sameness.
46. As a user creating only one image, I want no Look Continuity state added, so that single-image work does not acquire a series workflow.
47. As a user reviewing a generated result, I want CastMe to perform an Identity Review against the Primary Identity Anchor, so that it checks whether the styling still reads as the same person.
48. As a user receiving an Identity Review, I want concrete visible drift reported through Protected Identity Cues, so that feedback identifies what changed rather than saying only that similarity is low.
49. As a user receiving an Identity Review, I want no biometric score or identity guarantee, so that CastMe does not claim evidence or tools it does not have.
50. As a user creating an action image, environmental portrait, poster, or key art, I want identity to remain readable without being forced to become the First Read, so that the selected action, emotion, silhouette, or message may still lead the composition.
51. As a user creating a headshot or identity-centered portrait, I want the face and recognizable person to become the First Read when appropriate, so that the image serves its identity-centered use.
52. As a user whose result tells the right story but no longer looks like me, I want a targeted revision of only the drifting styling details, so that correct scene, shot, performance, text, wardrobe, and finish remain intact.
53. As a user whose eyebrow, contour, skin tone, hairline, or distinctive mark drifted, I want those cues restored without removing all Story Makeup, so that the repair preserves both identity and narrative.
54. As a user requesting only a makeup correction, I want unrelated scene and production locks preserved, so that revision does not regenerate a new concept.
55. As a user working with a named character, historical period, uniform, ceremonial system, or visual canon, I want existing visual-research rules reused, so that story styling is based on reliable visual anchors rather than stereotypes or memory.
56. As a user requesting culturally specific styling, I want concrete clothing, hair, makeup, material, and symbol evidence used carefully, so that a broad label does not substitute for accurate design.
57. As a user refreshing Styling options, I want new choices to differ in meaningful visible styling fields while preserving my locks, so that refreshed looks are genuinely different rather than renamed.
58. As a user who accepted recommended defaults for styling, I want the resolved values recorded as Derived Locks, so that a later scoped refresh can reopen only the styling-owned defaults.
59. As a user who explicitly selected or overrode a makeup, hair, wardrobe, or accessory detail, I want it recorded as an Explicit Lock, so that future refreshes preserve it until I reopen it.
60. As a maintainer, I want story-driven makeup implemented through existing Styling and Identity modules, so that behavior remains local and the coordinating director stays small.
61. As a maintainer, I want the highest existing golden-conversation seam to verify the feature, so that tests exercise user-visible behavior rather than documentation structure.
62. As a maintainer, I want no makeup detector, bare-face reconstruction system, biometric scorer, or persistent look database, so that the feature remains evidence-based and proportionate to the problem.

## Implementation Decisions

- Deepen the existing Styling Direction and Identity Anchor modules. Do not add a makeup agent, Makeup Gate, makeup-specific module, separate workflow stage, or new runtime system.
- Keep the coordinating director's existing routing: makeup, hair, wardrobe, accessories, grooming, and props continue to route to Styling; identity evidence, coverage, risk, and revision continue to route to Identity Anchor.
- Treat Reference Appearance as the visible facial styling, grooming, and hair state shown by a person reference when its makeup status or source is unknown. Do not classify the source as made-up or bare-faced unless the user provides that fact.
- Reference Appearance is valid visible evidence but not proof of an unseen bare-face appearance. Final prompts for restyling must state the target transformation without claiming to remove makeup to a verified natural baseline.
- Define Appearance Coverage in terms of Protected Identity Cues needed by the target look. Unknown makeup alone is not a coverage gap.
- Trigger the existing coverage choice only when source styling, filters, face paint, hair, accessories, occlusion, or image quality hide target-critical Protected Identity Cues.
- Coverage choices remain derived from the actual missing evidence and may offer a clearer person reference, user description, accepted inference, or a staged strategy only when it materially addresses the gap.
- Keep the Primary Identity Anchor as the authoritative actual image input. Supporting identity angles may add evidence but cannot override or be averaged with it into a new face.
- Label non-person references and other-person styling references by role. Transfer only the requested makeup, hair, wardrobe, accessory, material, or visual treatment; never borrow their face, age impression, body, or identity.
- Treat Character Read as creative intent supplied by the user or story or proposed as a creative direction. Visible appearance may inform formal compatibility and identity preservation but cannot establish real personality, profession, relationship, or inner traits.
- Treat explicit wording equivalent to "design the styling from the story," "you decide the makeup and look," or "styling according to the character" as Delegated Styling for that owned dimension.
- Delegated Styling selects one compatible Styling Direction internally, records its resolved values as Derived Locks, and continues without a visible Styling gate. Focused coverage, identity-risk, safety, and exact-text choices remain available.
- A user request for options, an unresolved material Styling choice, or a rejected Styling batch uses the existing visible gate: exactly three complete story-specific Styling Directions plus `D) Custom`, with one recommendation and one short visible-result reason.
- Do not create independent makeup, hair, wardrobe, and accessory menus. One Styling Direction coordinates all currently unlocked styling fields; explicit locks may narrow the same interface to one field.
- Each visible Styling Direction describes the intended Character Read, concrete makeup/grooming, hair, wardrobe/accessories, Protected Identity Cues to preserve, and any material likeness risk in beginner-facing visual language.
- Preserve compatible Reference Appearance and apply the minimum story-required change. Entering Styling does not require a conspicuous makeover or prove value through visible alteration.
- Activate Styling when it materially changes intended use, story, role, era, fashion, ceremony, performance context, canon, or identity risk, including when those needs are implicit in the brief rather than named as makeup or hair.
- Skip ordinary Styling clarification for compatible headshots, avatars, lifestyle portraits, explicit keep-current-look requests, accepted defaults, already complete styling briefs, and unrelated targeted revisions.
- Use Protected Identity Cues rather than visual intensity labels to classify risk. Bold color or texture may proceed when facial relationships and visible cues remain intact; natural-looking contour, grooming, hair, or coverage changes are risky when they replace, redraw, or obscure those cues.
- Reuse the existing identity-risk choice when a proposed look would materially change facial relationships, face or body structure, skin tone, age impression, ethnicity impression, hairline, distinctive marks, or the visibility of important cues.
- Default to identity preservation when story treatment conflicts with likeness. Story impact becomes the priority only after the user explicitly accepts the corresponding risk; do not repeat a clearly accepted risk choice.
- Preserve the story on safer paths by shifting narrative work to wardrobe, silhouette, material, accessories, props, localized makeup, grooming, and other unlocked non-identity details rather than collapsing the concept.
- Treat intentional fatigue, weathering, injury, ritual marks, cosmetic design, grooming, and breakdown as Story Makeup owned by Styling Direction.
- Story Makeup is a Styling lock through First-Pass Finish. Natural Retouch and other finish handling may render it coherently but cannot remove it as redness, unevenness, a blemish, flyaway hair, or another accidental defect.
- Keep physical or depicted makeup, hair, wardrobe, and accessories in Styling. Keep generation-time lighting, color, identity-safe retouching, texture, and final image character in First-Pass Finish.
- A Styling Direction does not silently resolve First-Pass Finish, and a Finish Direction does not reopen Styling. Preserve the existing explicit, derived, suggested, and unresolved state semantics.
- Require Physical Scene Coherence between resolved story/time/weather, Shot and perspective, Performance, Styling and materials, and First-Pass Finish. Reconcile suggested or derived conflicts internally and use the existing focused conflict choice only for incompatible Explicit Locks.
- Create Look Continuity only for a requested series. Lock the base makeup, hair, wardrobe, and accessories while recording explicit story-state changes such as wetness, wear, injury, dirt, cosmetic breakdown, or costume damage for each moment.
- Look Continuity represents coherent evolution, not identical styling state in every image. Single-image tasks do not receive continuity state.
- Build the final production prompt from concrete story-specific styling details and reference roles. State that the source makeup status is unknown when relevant, preserve the same visible person and Protected Identity Cues, describe the intended target look, and forbid identity borrowing from styling references.
- Keep identity as a required quality constraint for every person-centered result without forcing it to be the First Read in every output. The selected person, face, silhouette, action, emotion, product, or message may lead according to the intended use.
- When a result is visible, perform Identity Review through a structured comparison of Protected Identity Cues against the Primary Identity Anchor. Report specific visible drift and never claim biometric verification, a similarity score, or guaranteed identity.
- If Styling causes identity drift, use the existing targeted revision flow. Restore only the drifting cues or remove only the responsible styling treatment while preserving every unrelated lock and as much Story Makeup as remains compatible.
- Do not run an automatic second generation or edit. A visible result changes only after an explicit targeted revision request.
- Reuse existing role, costume, historical, cultural, occupational, ceremonial, sports/team, and named-character research behavior. Do not infer a specific canon or culturally specific system from a broad label when evidence is required.
- Reuse existing Scoped Option Refresh behavior and Styling visible signature. Styling refreshes may reopen only Styling-owned Derived Locks and explicitly requested fields while preserving identity, output requirements, unrelated dimensions, and all other Explicit Locks.
- Keep the feature conversational and document-driven. Do not add schemas, APIs, persistent storage, model-selection controls, or external integrations.

## Testing Decisions

- Use the existing golden-conversation behavior suite as the single highest testing seam. It already verifies adaptive question depth, reference coverage, identity-risk choices, decision inheritance, Styling refreshes, First-Pass Finish, series continuity, and targeted revision.
- Test externally visible conversation, decision inheritance, final-prompt obligations, and revision preservation. Do not test exact prose, internal section names, a particular state representation, or the number of implementation lines.
- Treat the existing structural validator as a packaging/documentation gate rather than a second feature-testing seam. The feature's behavioral acceptance lives in golden conversations.
- Add an unknown-makeup professional-headshot scenario proving that clear Protected Identity Cues do not trigger a bare-face request or an unnecessary Styling gate.
- Add an unknown-makeup story-styling scenario proving that Reference Appearance is restyled without claiming to reconstruct an unseen bare face.
- Add a source-face-paint or beauty-filter scenario proving that a bare-face or substantially different target exposes the actual missing Appearance Coverage and offers only relevant evidence or inference paths.
- Add a multi-reference scenario proving that the Primary Identity Anchor remains authoritative, supporting angles add evidence, and another person's makeup or costume reference remains styling-only.
- Add a Character Read scenario proving that user/story intent drives the visible impression while the skill makes no factual personality inference from expression, clothing, face shape, or other appearance.
- Add a Delegated Styling scenario proving that story-based delegation selects one complete look internally, asks no ordinary Styling question, records Derived Locks, and preserves focused risk choices.
- Add a visible-choice scenario proving that a user who requests options receives exactly three complete story-specific Styling Directions plus `D) Custom`, one recommendation, and no separate makeup, hair, or wardrobe menus.
- Add a locked-scope scenario proving that a user who preserves hair and wardrobe receives makeup-only Styling choices without reopening those locks or unrelated production dimensions.
- Add a compatible-appearance scenario proving that an already suitable look is preserved and deepened through minimum necessary change rather than redesigned for its own sake.
- Add an implicit-story-need scenario proving that role, era, ceremony, fashion, or character requirements activate Styling even when the user does not say "makeup" or "hair."
- Add a simple or unrelated-edit scenario proving that ordinary Styling remains closed when the current look fits or the requested correction does not touch it.
- Add paired bold-safe and natural-risky scenarios proving that identity risk follows Protected Identity Cues rather than light/heavy makeup labels.
- Add an occlusion or transformation scenario proving that changing or hiding target-critical cues triggers the existing identity-risk choice, while explicit accepted risk is not asked twice.
- Add a Story Makeup versus Natural Retouch scenario proving that intentional fatigue, weathering, injury, dirt, cosmetic treatment, and wet hair survive First-Pass Finish while unrelated distractions may still be reduced.
- Add a Styling-versus-Finish ownership scenario proving that selecting or refreshing one does not silently resolve or reopen the other.
- Add a Physical Scene Coherence scenario proving that story time/weather, makeup condition, hair/material state, wardrobe, and finish cannot contradict one another without the existing focused conflict handling.
- Add a three-image Look Continuity scenario proving that base makeup, hair, wardrobe, and accessories remain recognizable while rain, wear, injury, and cosmetic breakdown evolve by story moment.
- Add a single-image scenario proving that Look Continuity is not created for an ordinary one-off output.
- Add a non-identity First Read scenario proving that action, silhouette, emotion, or message may lead a poster or key art while identity remains a required readable constraint.
- Add an Identity Review scenario proving that visible drift is reported through specific Protected Identity Cues without a biometric score, verification claim, or identity guarantee.
- Add a targeted styling revision scenario proving that restoring eyebrow shape, contour, skin tone, hairline, or a distinctive mark preserves correct story, scene, Shot, Performance, text, wardrobe, and First-Pass Finish.
- Reuse existing prior art for vague professional avatars, guided cinematic portraits, high-risk source-to-target jumps, series continuity, multi-reference role separation, stronger retouching, consecutive Styling refreshes, and surgical revision.

## Out of Scope

- Human makeup artist, hair stylist, costume designer, or wardrobe-stylist marketplace integration.
- A new makeup agent, Makeup Gate, makeup-specific module, or mandatory styling stage.
- Automatic makeup detection or classification of a reference as bare-faced, lightly made-up, or heavily made-up.
- Reconstructing, claiming, or guaranteeing the person's unseen bare-face appearance.
- Automatic makeup removal, digital de-makeup, or restoration of hidden facial details.
- Biometric face matching, face embeddings, similarity thresholds, identity scores, or identity guarantees.
- A fixed light/medium/heavy makeup scale, universal identity budget, beauty score, attractiveness ranking, or face-shape taxonomy.
- A parameter questionnaire for foundation, brow products, eyeliner, lipstick, contour, hair products, or professional application techniques.
- Fixed user-facing makeup presets, style catalogs, or separate makeup, hair, wardrobe, and accessory menus.
- Inferring personality, profession, social class, relationship, sensitive attributes, or real temperament from facial appearance.
- Automatic or silently inferred structural beautification, skin-tone change, age change, ethnicity-impression change, face-shape redesign, or body-shape redesign. Explicitly requested, risk-accepted story transformations remain governed by the existing identity-risk flow.
- Weakening existing safety handling for sexualized styling, minors, nudity, transparent clothing, intimate imagery, or other high-risk requests.
- Replacing the existing reference-coverage, identity-risk, role/costume research, Scoped Option Refresh, First-Pass Finish, Physical Scene Coherence, or targeted revision workflows.
- Cross-conversation persistence, user profiles, a look database, or automatic continuity state for single images.
- Automatic second-pass generation or post-export editing.
- Changes to image-model selection, quality/size controls, API contracts, billing, storage, deployment, or generation tooling.
- Guaranteeing that human observers or GPT Image 2 will preserve identity under every transformation.

## Further Notes

- The supporting research found directional evidence that heavy makeup and large hairstyle changes can reduce human recognition, while clothing can carry strong story information with less facial risk. Those studies do not provide a universal cross-cultural makeup threshold and do not measure GPT Image 2 identity retention directly.
- The product contract therefore judges risk by replacement or occlusion of Protected Identity Cues rather than makeup intensity, attractiveness, or a numeric score.
- The six accepted ADRs record identity-first unconfirmed transformation, makeup ownership within Styling Direction, cue-based risk, Character Read as creative intent, Story Makeup preservation through First-Pass Finish, and deepening the existing Styling and Identity modules.
- The glossary is the canonical source for Primary Identity Anchor, Protected Identity Cue, Reference Appearance, Appearance Coverage, Delegated Styling, Styling Direction, Character Read, Story Makeup, Look Continuity, Identity Review, First-Pass Finish, Natural Retouch, First Read, locks, and refresh terminology.
- The test seam was confirmed during design grilling: golden conversations remain the single highest behavioral acceptance surface, with no new test harness or biometric evaluator.
- The research note remains useful background for evidence and limitations, but the accepted domain glossary and ADRs govern implementation decisions.
