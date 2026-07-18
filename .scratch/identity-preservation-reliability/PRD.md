Status: ready-for-agent

# Identity Preservation Reliability Across Generation and Revision

## Problem Statement

CastMe can preserve a person's identity when each production choice is considered alone, yet still produce a result that no longer looks like the referenced person after several valid choices accumulate. Shot, face angle, performance, hair, makeup, lighting, character styling, text, and scene complexity can each be reasonable in isolation while their combination reduces the readability of Protected Identity Cues or depends on evidence the references do not provide.

The current decision flow can worsen this problem by recommending each choice only within its local creative area. A sequence of locally attractive recommendations may therefore keep adding unresolved identity risk even though the user's primary expectation remains that the result depicts the same person. A final prompt can satisfy the selected costume, setting, pose, and finish while facial identity has become a secondary or contradictory objective.

When the first result already has identity-wide drift, treating it as the basis for another ordinary edit can preserve or reinforce the wrong face. A request such as “make the face look more like me” may then be handled like an isolated mouth, hair, or expression correction even though the result is no longer reliable identity evidence. Repeated edits can continue from that failed baseline, and a completion message can be issued without a successful Identity Review.

CastMe already has the necessary domain concepts and workflow seams: Primary Identity Anchor, Protected Identity Cue, Reference Coverage, Inference Boundary, Choice Gate, Identity Review, actual image inputs, and one bounded automatic correction for visible required-quality failures. The missing behavior is to connect them across the whole decision sequence and to distinguish a coherent local defect from identity-wide drift. The solution must remain generic rather than encoding particular characters, hairstyles, poses, lighting setups, genres, error counts, or similarity thresholds.

## Solution

Make every recommendation inherit the current decision state and known identity or geometry risk. Within the active Choice Gate and all existing locks, recommend the valid option that fulfills the requested creative purpose without adding an avoidable unresolved identity risk. Keep the more transformative alternatives available and never silently change an Explicit Lock. This prevents a chain of locally optimized recommendations from drifting away from the person's identity while preserving creative freedom.

After all required choices are resolved and the production prompt is assembled, run one internal combined identity-risk check before generation. Judge the final combination through Protected Identity Cue readability and Reference Coverage rather than a numeric score, cue count, character name, or fixed combination rule. The check creates no new user-visible Gate or workflow stage. It routes only the actual blocking condition to the existing focused behavior: reattach an unavailable Primary Identity Anchor, resolve missing Reference Coverage, or resolve a proposed transformation or occlusion through the existing identity-risk Choice Gate. Re-run the check after the focused answer and do not repeat an already accepted risk.

Extend Identity Review to classify the result by whether it remains reliable identity evidence. A result with one coherent local defect and otherwise intact identity remains eligible for surgical revision. A result whose underlying facial relationships have drifted broadly enough that it is no longer reliable identity evidence is incomplete and requires regeneration from the Primary Identity Anchor and locked brief. Regenerate only when the active generation surface can independently select the Primary Identity Anchor and exclude the failed result. If it cannot, preserve every resolved choice and ask only for the Primary Identity Anchor to be reattached through the existing focused behavior. Never substitute text, pass the failed result, or claim an automatic correction. Preserve valid scene, shot, camera, pose, styling, lighting, exact text, background, output, and accepted-risk locks through the written production brief instead.

When a visible result has an unambiguous identity-wide failure and the active generation surface can execute the required input selection and new generation, perform that regeneration automatically once before claiming completion. Otherwise follow the focused reattachment path above. Run Identity Review once more after a regeneration. If the regenerated result still fails, report the concrete unresolved drift and stop without another retry or completion claim. A passing first result receives no routine second pass, and an output that is not visible or cannot be inspected does not receive an unverified automatic correction.

Keep every accepted identity risk scoped to the exact cue, occlusion, angle, transformation, or missing evidence the user accepted. The accepted change is not itself a failure, but it never becomes a blanket waiver for unrelated facial structure, skin tone, age impression, body evidence, or recognizability. Continue to require the Primary Identity Anchor as an actual image input for every identity-preserving generation and revision.

## User Stories

1. As a user building a complex person-centered image through several choices, I want later recommendations to account for earlier identity risks, so that individually reasonable decisions do not combine into a different person.
2. As a user who has already locked a shot, angle, pose, or styling choice, I want later recommendations to preserve that lock, so that identity protection does not silently rewrite my concept.
3. As a user choosing among several valid creative treatments, I want the recommendation to favor the treatment that does not add avoidable unresolved identity risk, so that the default path remains dependable.
4. As a user who prefers a more transformative option, I want that option to remain available, so that identity-aware recommendations do not become forced conservative styling.
5. As a user who has already selected a demanding face angle, I want later hair and lighting recommendations to work with that angle, so that the workflow does not keep hiding the remaining readable identity cues.
6. As a user who explicitly accepted a particular identity risk, I do not want the same risk asked again in later choices, so that the workflow remains concise.
7. As a user requesting a simple portrait with sufficient reference evidence, I do not want an extra risk question, so that the reliability fix does not lengthen ordinary work.
8. As a user whose selected choices become risky only in combination, I want CastMe to catch the combined problem before generation, so that I do not spend a generation on a predictably weak identity result.
9. As a user encountering a combined risk, I want CastMe to reuse the existing focused Choice Gate, so that I do not have to learn a new “combined identity” workflow.
10. As a user whose target requires an angle or body evidence my references do not show, I want the issue routed to Reference Coverage, so that the question addresses the real missing evidence.
11. As a user whose selected styling would replace or obscure a Protected Identity Cue, I want the issue routed to the existing identity-risk choice, so that styling risk is not confused with missing reference evidence.
12. As a user whose Primary Identity Anchor is unavailable to the image tool, I want only that image requested again, so that my resolved creative choices remain intact.
13. As a user facing more than one unresolved risk, I want CastMe to ask only the currently blocking focused question, so that the fix does not become a multi-part questionnaire.
14. As a user who resolves a focused risk, I want the combined check run again without reopening unrelated decisions, so that the workflow continues from its current state.
15. As a user, I do not want identity risk decided by a hidden score, fixed cue count, or universal threshold, so that the rule remains evidence-based across different faces and image types.
16. As a user requesting a named character, historical role, fashion concept, or fantasy design, I want the same identity rules applied without role-specific exceptions, so that preservation is consistent across genres.
17. As a user requesting identity-preserving generation, I want my Primary Identity Anchor passed as an actual image input, so that identity never depends on a prose description alone.
18. As a user requesting a revision, I want the Primary Identity Anchor passed again, so that later edits do not drift away from the original person.
19. As a user providing supporting angles, I want them treated as additional evidence rather than faces to average, so that they clarify rather than replace my identity.
20. As a user providing another person's costume or style reference, I want only the requested treatment transferred, so that the reference person's face, age impression, and identity do not leak into mine.
21. As a user whose old reference is visible in conversation but unavailable to the active tool, I want CastMe to stop rather than substitute text, so that it does not pretend identity remains anchored.
22. As a user accepting inference for missing body, angle, or performance evidence, I still want my actual identity image included, so that inference never removes the identity anchor.
23. As a user whose result has one isolated mouth-state problem, I want a surgical revision, so that the correct identity, composition, and scene are not discarded.
24. As a user whose result has one coherent face-plane or gaze-coordination problem, I want that coherent unit corrected, so that several symptoms caused by one local defect do not force unnecessary regeneration.
25. As a user whose face width, eye relationship, nose structure, jaw, or age impression have drifted independently, I want the result treated as unreliable identity evidence, so that the wrong face is not used as the repair baseline.
26. As a user receiving an Identity Review, I want the classification based on visible structure and repair scope, so that CastMe does not count errors mechanically.
27. As a user depicted at a three-quarter or profile angle, I want angle-correct asymmetry accepted, so that a valid turned face is not mistaken for identity drift.
28. As a user receiving a stylized or story-driven result, I want Identity Review to respect the accepted treatment while checking the remaining cues, so that creativity and identity are not treated as mutually exclusive.
29. As a user whose result is no longer reliable identity evidence, I do not want it declared final, so that completion means the person remains recognizably anchored.
30. As a user whose output is not visible or is too small to inspect reliably, I want review reported as unavailable or unverified, so that CastMe does not claim evidence it lacks.
31. As a user whose result remains reliable identity evidence with one local defect, I want both the result being edited and the Primary Identity Anchor supplied to the revision, so that the correction preserves layout without losing identity.
32. As a user whose result has identity-wide drift, I want regeneration to start from the Primary Identity Anchor and locked brief, so that it does not inherit the failed face.
33. As a user whose scene, shot, camera, pose, styling, text, lighting, and background are already correct, I want those locks carried into identity regeneration, so that recovery does not become a new concept.
34. As a user whose first visible result has an unambiguous identity-wide failure, I want one automatic regeneration when the active surface can independently use my Primary Identity Anchor and exclude the failed result, or a focused request to reattach only that Anchor otherwise, so that CastMe neither knowingly delivers a failed result nor pretends to control unavailable inputs.
35. As a user receiving an automatic regeneration, I want Identity Review run once more, so that the correction is checked rather than assumed.
36. As a user whose regenerated result still fails, I want the remaining drift reported concretely, so that CastMe stops honestly instead of claiming success.
37. As a user paying generation cost or waiting for results, I do not want more than one automatic correction, so that reliability remains bounded.
38. As a user whose first result passes Identity Review, I do not want a routine second pass, so that the feature does not add needless cost or drift.
39. As a user who accepts hair covering one eye, I want only that occlusion accepted, so that unrelated nose, jaw, skin tone, or age drift still counts as failure.
40. As a user who accepts a strong profile or stylized facial treatment, I want the remaining visible Protected Identity Cues preserved, so that scoped risk does not become a global likeness waiver.
41. As a user, I do not want a vague statement such as “lower likeness is acceptable” to authorize every identity change, so that accepted risk remains understandable and bounded.
42. As a user who explicitly requests a structural identity transformation, I want only the named transformation accepted, so that all unrelated identity evidence remains anchored.
43. As a beginner, I want recommendation inheritance, combined checking, and repair classification handled internally, so that I am not asked to understand facial geometry or risk scoring.
44. As a maintainer, I want this behavior implemented through the existing coordinating and Identity Anchor seams, so that the fix does not create another module, agent, or workflow stage.
45. As a maintainer, I want generic behavioral scenarios across different genres and reference conditions, so that the solution cannot pass by recognizing one character or prompt pattern.
46. As a maintainer, I want existing actual-image, reference-role, coverage, and bounded-correction contracts reused, so that this feature adds only the missing coordination and identity-wide recovery behavior.
47. As a maintainer, I want no biometric matcher, similarity score, face embedding, or fixed risk formula, so that CastMe remains truthful about the evidence and tools it has.
48. As a user, I want identity preservation described as best effort rather than guaranteed matching, so that the workflow improves reliability without promising impossible certainty.

## Implementation Decisions

- Deepen the existing coordinating workflow and Identity Anchor owner. Do not add another module, agent, generation stage, review stage, or persistent risk system.
- Keep the existing decision state of Explicit Locks, Derived Locks, suggested values, unresolved values, accepted risks, and Reference Coverage as the source for recommendation context. Do not introduce a parallel identity-risk state model.
- Require each visible recommendation to inherit current locks and known identity or geometry risk. Within the current Choice Gate's valid scope, prefer a path that satisfies the creative request without adding avoidable unresolved risk.
- Keep every valid creative path available. Recommendation inheritance must not silently reopen or weaken an Explicit Lock, force a close crop, turn the face toward camera, remove a requested occlusion, neutralize a selected perspective, or replace the requested style.
- Use the final combined request rather than individual keywords to judge identity risk. The semantic question is whether the resolved combination materially reduces readable Protected Identity Cues or depends on target-critical evidence that remains missing.
- Do not implement a score, cue counter, risk budget, character list, genre list, pose list, lighting list, or fixed condition such as a particular number of “risky” choices.
- Run the combined identity-risk check internally after production-critical choices are resolved and the production prompt is assembled, immediately before the generation call. It is not a new user-visible Gate or workflow stage.
- Treat actual-image inclusion, failed-result exclusion, and automatic regeneration as verifiable capabilities of the active generation surface, not as effects that prompt wording can guarantee. Claim them only when that surface exposes and executes the required control. If the Primary Identity Anchor cannot be independently selected without the failed result, preserve the complete decision state and route only to the existing focused reattachment behavior; do not substitute text or claim an automatic correction.
- Route an unavailable required Primary Identity Anchor to the existing focused reattachment behavior. Preserve all locks and do not substitute a text description.
- Route missing target-critical face, appearance, body, angle, or performance evidence to the existing Reference Coverage Choice Gate and Inference Boundary behavior.
- Route a proposed transformation, redraw, or occlusion of Protected Identity Cues to the existing identity-risk Choice Gate. Do not create a combined-risk Gate.
- Surface only one currently blocking focused Choice Gate at a time. After the user resolves it, preserve all unrelated decisions and re-evaluate the combined request.
- Do not repeat a risk the user has already accepted within the same explicit boundary. A newly relevant cue, angle, region, or transformation remains separately unresolved.
- Keep the Primary Identity Anchor authoritative and pass it as an actual image input to every identity-preserving generation and revision. Text can state locks and reference roles but never replace the image.
- Continue to label every included image by role. Supporting identity angles add evidence; other-person styling, wardrobe, pose, character, and visual references never supply face identity, age impression, body identity, or a replacement Primary Identity Anchor.
- Extend Identity Review to decide whether a result remains reliable identity evidence. Make this a qualitative structural judgment through Protected Identity Cues, Visible Body Evidence, angle-correct facial planes, and repair scope rather than a score or count.
- Treat a defect as local when the result remains reliable identity evidence and the correction can be expressed as one coherent affected unit while the surrounding identity relationships remain valid.
- Treat a result as identity-wide drift when restoring the person would require rebuilding several underlying facial relationships and the failed result can no longer serve as reliable identity evidence.
- Do not classify every multi-symptom problem as identity-wide drift. Several visible symptoms produced by one coherent face-plane, gaze, mouth, hair, or local styling defect may remain surgical.
- For a surgical revision, pass both the image being edited and the Primary Identity Anchor as actual inputs, change only the coherent defect, repeat the identity invariants, and preserve every unrelated lock.
- For identity-wide drift, regenerate from the Primary Identity Anchor and the locked production brief only after the active generation surface can independently select the required inputs and exclude the failed result. Do not pass the failed result as an image input or use it as identity, face-geometry, pose, composition, or body evidence.
- Preserve valid scene, shot, camera, projection, pose, performance, styling, lighting, finish, exact text, background, output, and accepted-risk locks through the regeneration prompt. Do not silently simplify locked creative intent to make recovery easier.
- Permit one automatic regeneration only when a visible result has an unambiguous identity-wide failure and the active generation surface can verifiably include the required Primary Identity Anchor, exclude the failed result, and initiate a new generation. This is the existing bounded required-quality correction behavior, not a routine second pass.
- Run Identity Review once after the automatic regeneration. If the result remains unreliable identity evidence, report the concrete unresolved drift and stop without another retry or a completion claim.
- Do not perform automatic correction when the output is unavailable, the relevant face region cannot be inspected reliably, the result already passes, or the review is ambiguous. Report the corresponding review boundary truthfully.
- Scope every accepted identity risk to the named cue, occlusion, angle, transformation, or missing evidence. Exclude that accepted change from failure classification while continuing to inspect all unrelated visible identity evidence.
- Do not treat broad wording such as “accept lower likeness” as permission to discard unrelated Protected Identity Cues. Use the existing focused boundary semantics instead of adding a global identity waiver.
- Keep identity a required readable quality constraint without forcing it to become the First Read in every output. Posters, action images, editorials, and key art may still lead with the selected silhouette, action, emotion, product, or message.
- Keep current safety, exact-text, First-Pass Finish, Physical Scene Coherence, Scoped Option Refresh, reference research, quality, and output-control behavior unchanged except where their existing recommendations must inherit current identity or geometry risk.
- Use the existing domain vocabulary. The accepted glossary refinements clarify Protected Identity Cue, Identity Review, and Choice Gate; they do not introduce a new domain term or require a new ADR.

## Testing Decisions

- Use golden conversations as the single highest behavioral testing seam. Assert externally visible routing, recommendations, prompt obligations, image-input roles, review classifications, correction behavior, preserved locks, and truthful completion claims rather than exact prose or internal section-loading mechanics.
- Reuse existing prior art for actual-image identity input, unavailable-reference reattachment, multiple-reference role separation, Reference Coverage and Inference Boundary handling, Identity Review cue reporting, surgical revision, and Structural Scale Failure recovery.
- Add a sequential-choice scenario in which several individually valid creative choices accumulate identity risk. The expected later recommendation inherits the earlier locks and favors a valid path that does not add another unresolved risk while keeping the more transformative alternatives available.
- Add a control scenario with a similarly complex request but sufficient reference evidence and readable Protected Identity Cues. It proceeds without a new Gate, proving that complexity alone is not the trigger.
- Add a combined missing-evidence scenario. The internal check routes to the existing Reference Coverage Choice Gate, preserves all locks, and creates no combined-risk Gate.
- Add a combined transformation or occlusion scenario. The internal check routes to the existing identity-risk Choice Gate and does not misclassify the issue as missing reference evidence.
- Add an unavailable-anchor scenario after all creative choices are resolved. The skill asks only for the Primary Identity Anchor to be reattached and does not reopen the brief or use a text-only fallback.
- Add a surface-limited recovery scenario where the Primary Identity Anchor cannot be independently selected without the failed result. The skill preserves every lock, asks only for the Anchor to be reattached, performs no generation, and makes no automatic-correction claim.
- Add a multi-reference scenario proving that the Primary Identity Anchor owns identity, supporting angles add evidence, and another person's character, costume, pose, makeup, or style reference remains limited to its declared role.
- Add varied named-character, historical, editorial, and fantasy examples to prove that behavior follows reference roles and Protected Identity Cues rather than recognizing one character, genre, hairstyle, pose, or lighting pattern.
- Add a coherent local mouth-state scenario. Identity Review keeps the result eligible for surgical revision, includes both the edited result and Primary Identity Anchor as actual inputs, and preserves every unrelated lock.
- Add a coherent face-plane scenario where several symptoms share one local geometric cause. The result remains surgical, proving that the implementation does not count symptoms mechanically.
- Add an identity-wide drift scenario where independent facial relationships no longer agree with the Primary Identity Anchor. Identity Review marks the result incomplete and regenerates from the Primary Identity Anchor and locked brief without including the failed output.
- In the identity-wide regeneration scenario, assert that correct scene, shot, camera, pose, styling, lighting, finish, exact text, background, and output locks remain represented in the new prompt.
- Add a bounded-correction scenario where the first result fails, the active surface exposes the required input controls, and the regenerated result passes. Assert that the actual inputs include the Primary Identity Anchor and exclude the failed result; the skill performs exactly one new generation and one follow-up Identity Review before completion.
- Add a persistent-failure scenario where the regenerated result remains unreliable. The skill reports concrete remaining drift, performs no third generation, and makes no completion claim.
- Add a passing-first-result scenario proving that no routine second pass or automatic edit occurs.
- Add unavailable-output and insufficient-resolution scenarios proving that the skill neither auto-regenerates nor claims Identity Review it could not perform.
- Add a scoped accepted-risk scenario such as one named occlusion or target-angle limitation. The accepted change is permitted, unrelated visible cues remain protected, and the same risk is not asked again.
- Add a newly introduced risk after an earlier accepted risk. The new cue or evidence gap remains unresolved, proving that acceptance does not become a global waiver.
- Add a vague “lower likeness is acceptable” scenario proving that the skill requires the existing explicit scoped boundary rather than disabling identity preservation globally.
- Test behavior semantically. Do not assert exact option wording, a fixed list of risk factors, an internal score, a specific error count, or a particular implementation layout.
- Run the existing structural skill validator after the golden audit. Treat it as a packaging, metadata, and reference-integrity check rather than a second feature-testing seam.
- Run ordinary Markdown, sequence-count, and diff checks to catch malformed documentation and scenario numbering without adding another test harness.

## Out of Scope

- Character-specific, costume-specific, hairstyle-specific, makeup-specific, pose-specific, lighting-specific, genre-specific, or scene-specific identity rules.
- Fixed formulas such as “full body plus side face plus occlusion means failure,” risk scores, identity budgets, cue counts, similarity percentages, biometric thresholds, or face-shape taxonomies.
- A biometric matcher, face embedding, computer-vision scorer, attractiveness score, identity guarantee, or external verification service.
- A new combined-risk Gate, identity questionnaire, identity-review stage, module, agent, state machine, persistent profile, database, or runtime component.
- Forcing a portrait crop, frontal face, both eyes visible, neutral makeup, soft light, reduced perspective, simplified action, or generic conservative styling.
- Silently changing an Explicit Lock to improve identity or anatomy.
- Requiring extra confirmation when reference evidence is sufficient and no material combined risk exists.
- Treating accepted inference or accepted identity risk as a blanket waiver for unrelated identity drift.
- Using a failed identity-wide result as an image input, identity reference, face reference, pose reference, composition reference, or body reference for its regeneration.
- Unlimited retries, routine second passes, automatic candidate batches, upscaling, post-export editing, or recovery attempts after the one reviewed correction.
- Adding masks, input-fidelity controls, model parameters, API integration, image-tool wrappers, or controls not exposed by the active generation surface.
- Changing model selection, safety handling, trend research, exact-text verification, output recipes, quality and size behavior, or series continuity beyond their interaction with the agreed identity rules.
- Reopening the already implemented Primary Identity Anchor, actual-image input, multiple-reference role, Visible Body Evidence, Inference Boundary, or Structural Scale Failure contracts except for the minimal coordination required here.
- Guaranteeing that GPT Image 2 or human observers will preserve exact identity under every transformation.
- Creating a new ADR or domain term for these reversible refinements.

## Further Notes

- This specification addresses a class of identity-preservation failures, not one character, costume, hairstyle, background, pose, or generated image.
- The existing actual-image input contract remains authoritative: supporting text can preserve locks and describe roles, but identity-preserving generation and revision still require the real Primary Identity Anchor.
- The active-surface capability boundary creates no new Gate. It either permits the existing bounded automatic correction or routes an unavailable independently selectable Anchor to the existing focused reattachment behavior.
- Identity-wide drift is deliberately not introduced as a new capitalized domain term. It is an Identity Review outcome defined by whether the result remains reliable identity evidence.
- The recovery rule parallels the existing bounded Structural Scale Failure recovery without merging facial identity drift and body-scale failure into one concept.
- The recommendation change is preventive, while the combined pre-generation check is a final internal safeguard. Neither creates a user-visible stage.
- The glossary already records the agreed refinements: a Protected Identity Cue acceptance does not waive unrelated cues; Identity Review treats unreliable identity evidence as incomplete; and Choice Gate recommendations inherit current locks and known identity or geometry risk.
- No new ADR is warranted because the refinements deepen existing Identity and coordinating seams, are easy to reverse, and follow the established identity-first decisions.
