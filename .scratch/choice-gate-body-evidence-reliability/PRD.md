Status: ready-for-agent

# Choice Gate and Body Evidence Reliability

## Problem Statement

CastMe can guide a user from a partial person reference to a full-body final image, but the latest workflow exposed three connected reliability failures.

First, not every user-visible clarification preserves the permanent `D) Custom` path. The current general contract allows D to be optional, while stronger permanent-D checks apply only to creative and refreshable gates. A focused Reference Coverage gate can therefore present A/B/C without a user-defined resolution even though the rest of the workflow teaches the user that D is always available.

Second, accepting body inference from a half-body reference can be interpreted too broadly. Clearly visible shoulder width, chest volume, torso shape, body build, and head-to-neck-to-shoulder relationships may be discarded together with genuinely unseen waist, hip, leg, foot, and garment-hem evidence. Styling can then replace the person's Visible Body Evidence with a generic costume silhouette, such as flattening a visibly fuller upper torso under layered historical clothing.

Third, Identity Review can still declare a full-body result complete while linked structural problems remain. A slightly oversized head may be improved without being fully corrected, and a simultaneous loss of upper-body volume may not be classified together with it as a Structural Scale Failure. Repeated narrow edits risk preserving the defective body baseline, while unconditional regeneration or unlimited retries would add cost and drift.

The skill needs one consistent Choice Gate contract, a precise Inference Boundary, and a bounded correction rule. It must solve these failures without adding another module, body questionnaire, workflow stage, routine second pass, or hidden anatomy guess.

## Solution

Make every user-visible clarification a four-slot Choice Gate: A, B, and C are valid scoped paths, and D is always the Custom Path. When only two substantive resolutions exist, C is an explicit stop or keep-current path rather than a fabricated option. The Custom Path remains scoped to the gate that presents it, cannot bypass safety or coherence boundaries, creates no lock or history entry as a placeholder, and uses gate-specific wording rather than one copied sentence.

Treat clearly shown body relationships at any source crop as Visible Body Evidence. Preserve them automatically across creative direction and styling changes without asking another body-shape question. Name relevant evidence neutrally and concretely in production prompts, including chest volume when it is clearly visible or explicitly identified, while avoiding measurements, erotic emphasis, or claims about obscured anatomy.

Record accepted inference only through an explicit Inference Boundary. A half-body-to-full-body request may mark visible head, neck, shoulders, chest, torso, and body build as verified while marking only the unseen waist, hips, legs, feet, complete head-to-body continuation, and garment hem as inferred. Accepting one missing region never reclassifies verified evidence or authorizes inference for another region, angle, appearance cue, or performance fact.

Extend Identity Review to compare Protected Identity Cues, Visible Body Evidence, and relevant structural scale relationships. One isolated minor proportion defect in an otherwise coherent unchanged crop receives one surgical edit. Multiple connected body-scale failures, or a repair that expands a partial crop, form a Structural Scale Failure and require regeneration from the Primary Identity Anchor and locked brief without using the defective result as body-scale evidence. Perform at most one automatic correction, review the correction once, and report any remaining failure honestly instead of retrying indefinitely or declaring completion.

## User Stories

1. As a user answering any CastMe clarification, I want `D) Custom` to remain available, so that I can supply a valid answer the suggested paths did not anticipate.
2. As a user moving between creative and focused risk choices, I want the option structure to remain A/B/C/D, so that the interface does not appear to lose a capability midway through the workflow.
3. As a user facing a genuinely binary conflict, I want C to let me keep the current state and stop, so that CastMe does not invent a meaningless third resolution merely to fill the menu.
4. As a user choosing D, I want my custom answer to affect only the current Choice Gate, so that unrelated Explicit Locks are not reopened.
5. As a user choosing D in a safety gate, I want the Custom Path to remain inside the gate's compliant boundary, so that custom wording is not mistaken for an unrestricted bypass.
6. As a user choosing D in a physical-conflict gate, I want CastMe to accept only a coherent custom resolution, so that incompatible locks are not silently retained.
7. As a user viewing D without selecting it, I want the placeholder to create no lock or history entry, so that the mere presence of Custom does not change future routing.
8. As a user adopting a concrete Custom Direction, I want that direction recorded like other shown directions, so that a later refresh does not recommend the same idea again.
9. As a user choosing a custom coverage plan, I do not want that focused answer entered into creative refresh history, so that different gate types keep their ownership boundaries.
10. As a user reading a Choice Gate in my language, I want its Custom Path described for the current decision, so that D is useful rather than a generic label with no guidance.
11. As a user supplying a half-body reference, I want every clearly visible body relationship treated as evidence, so that a wider target does not redesign the part of my body already shown.
12. As a user whose reference clearly shows a fuller chest, I want that volume retained in a full-body result, so that the generated person does not become flat-chested.
13. As a user whose reference shows a particular shoulder width and torso build, I want those proportions retained across a costume change, so that styling does not replace my body with a generic character template.
14. As a user requesting historical or fantasy clothing, I want opaque layered fabric to drape over my preserved body shape, so that costume silhouette does not flatten or narrow verified anatomy.
15. As a user changing wardrobe, I want the wardrobe change kept separate from body-shape change, so that new clothing is not treated as permission to redesign my build.
16. As a user whose body is obscured by loose clothing or framing, I do not want CastMe to claim the hidden shape is verified, so that uncertain anatomy is not fabricated as fact.
17. As a user whose reference has projection distortion, I want body relationships interpreted after accounting for that projection, so that close-camera enlargement is not copied into a full-body image.
18. As a user who has already provided clear Visible Body Evidence, I do not want an extra confirmation question, so that stronger preservation does not make the workflow longer.
19. As a user who explicitly asks to change body shape, I want that request routed through the existing identity-risk behavior, so that intentional transformation remains possible without becoming a silent default.
20. As a user reviewing production wording, I want visible body traits described neutrally and concretely, so that the model receives enough information without sexualizing the person.
21. As a user whose chest volume is clear or explicitly named, I want the prompt to say so directly, so that vague wording such as “keep the build” does not lose the trait.
22. As a user whose body details are ambiguous, I do not want cup sizes, measurements, or other unsupported numbers invented, so that specificity remains evidence-based.
23. As a user asking for a full-body image from a half-body reference, I want verified and inferred regions distinguished, so that accepting inference does not surrender the entire body.
24. As a user accepting lower-body inference, I want only the unseen waist, hips, legs, feet, and garment continuation inferred, so that my visible upper body remains locked.
25. As a user accepting one Inference Boundary, I want a newly relevant missing angle or action to remain unresolved, so that one approval does not become a blanket likeness-risk waiver.
26. As a user who supplies a description for a missing region, I want only that description incorporated, so that CastMe does not invent additional body facts.
27. As a user who selected a full-body shot, I do not want the subsequent coverage gate to suggest changing to a half-body crop or hiding my body unless I reopen the shot, so that a risk choice does not undo an Explicit Lock.
28. As a user who accepts scoped inference, I want the final prompt to preserve verified evidence and label only the approved regions as natural estimates, so that the generation boundary remains explicit.
29. As a user receiving a full-body result, I want Identity Review to compare head, neck, shoulders, chest, torso, hips, and limbs as connected relationships, so that doll-like anatomy is not missed by a face-only review.
30. As a user whose result has only one slightly oversized head unit, I want CastMe to correct the skull, head, hair, and headwear together without shrinking the whole person, so that composition remains unchanged.
31. As a user whose result loses upper-body volume and also has an oversized head, I want the defects treated as one Structural Scale Failure, so that they are not patched against an already incorrect body baseline.
32. As a user whose result has a Structural Scale Failure, I want regeneration anchored in my Primary Identity Anchor and locked brief, so that valid scene and styling intent survive without reusing defective scale evidence.
33. As a user who locked a water stance, camera, costume, lighting, text, and background, I want those locks preserved through structural regeneration, so that a proportion repair does not become a new concept.
34. As a user whose first result clearly fails required identity or structural quality, I want CastMe to attempt one appropriate correction automatically, so that it does not knowingly deliver a failed final image.
35. As a user receiving an automatic correction, I want it reviewed once before completion is claimed, so that the correction is verified rather than assumed.
36. As a user whose correction still fails, I want the unresolved defect reported honestly, so that CastMe does not hide failure behind a completion message.
37. As a user paying generation cost or waiting for results, I do not want unlimited automatic retries, so that quality control remains bounded.
38. As a user whose first result already passes review, I do not want a routine second pass, so that this feature does not introduce unnecessary generation or drift.
39. As a beginner, I want body-evidence preservation, inference scoping, and structural review handled internally, so that I am not asked to understand anatomy or camera terminology.
40. As a maintainer, I want these changes expressed through existing CastMe contracts and golden behavior, so that the fix remains small and reviewable.

## Implementation Decisions

- Centralize the universal Choice Gate and Custom Path invariants in the coordinating Core Rules. Do not create a Custom module, helper workflow, or new reference owner.
- Every user-visible Choice Gate has exactly four labeled slots: A, B, C, and D. D is always the localized Custom Path.
- A through C must remain valid, concrete, gate-scoped paths. When only two substantive resolutions exist, use C as an explicit keep-current or stop path instead of padding the menu with a fake alternative.
- The Custom Path accepts a user-supplied resolution only within the presenting gate's valid scope. It cannot bypass safety, preserve a physical contradiction, or silently reopen unrelated Explicit Locks.
- The `D) Custom` placeholder creates no lock and no history entry. Once the user supplies a concrete answer, the owning gate applies its normal lock, validation, and history semantics.
- Keep Custom wording local to each Choice Gate. Centralize the invariant and scope, not a single literal sentence reused across unrelated decisions.
- Preserve the existing refresh behavior in which an adopted Custom Direction becomes a Shown Direction. Focused custom answers remain owned by their focused gate and do not enter creative history.
- Broaden body preservation from full-body and three-quarter sources to Visible Body Evidence clearly shown at any crop.
- Treat head-to-neck-to-shoulder scale, shoulder width, chest volume, visible torso shape, and body build as verified evidence when clearly visible after accounting for source projection.
- Preserve Visible Body Evidence automatically across shot expansion, creative direction, wardrobe, costume, and styling changes. Do not add a separate body-shape Choice Gate for evidence that is already clear.
- Describe relevant Visible Body Evidence neutrally and concretely in production and revision prompts. When chest volume is clearly shown or explicitly identified, name it directly together with the surrounding upper-torso relationships.
- Do not invent cup sizes, measurements, erotic framing, or structural claims about anatomy hidden by clothing, crop, pose, or projection.
- Require Styling Direction and garment prompt contributions to conform to verified body evidence. A costume change may alter fabric, layers, material, and silhouette treatment but does not authorize flattening, narrowing, enlarging, or otherwise redesigning the body.
- Record Reference Coverage by evidence type and region. For a half-body source, verified upper-body evidence and inferred lower-body continuation must remain separate.
- Replace blanket acceptance such as “body inference accepted” with an explicit Inference Boundary listing only the missing evidence the user authorizes CastMe to estimate.
- Accepting an Inference Boundary never reclassifies verified evidence and never authorizes a different missing region, face or body angle, appearance cue, action, hand interaction, or performance fact.
- A focused coverage Choice Gate should offer three relevant paths such as adding real evidence, describing missing facts, and accepting scoped inference, followed by the Custom Path. It must preserve the locked shot and must not introduce a safer crop or body-obscuring treatment unless the user explicitly reopens that choice.
- Carry the verified-versus-inferred split into the final production prompt. Identity similarity must come from the person's structure rather than local head enlargement or generic costume anatomy.
- Expand Identity Review to compare Protected Identity Cues, Visible Body Evidence, and the relevant structural scale chain across the visible crop.
- Classify one isolated minor proportion deviation in an otherwise coherent unchanged crop as a surgical revision. Reset the affected coherent unit relative to surrounding anatomy without shrinking the whole subject or changing unrelated locks.
- Classify multiple connected body-scale failures, or a correction that must expand a partial crop, as a Structural Scale Failure.
- Resolve a Structural Scale Failure by regenerating from the Primary Identity Anchor and locked brief. Preserve valid scene, camera, projection, pose, styling, lighting, exact text, background, and output locks in the prompt.
- Do not use an output carrying the Structural Scale Failure as supporting body-scale or composition evidence for its regeneration.
- Permit at most one automatic correction for an unambiguous required-quality failure visible after generation. Use the surgical or regeneration path appropriate to the classification, then perform Identity Review once more.
- If the correction remains unresolved, report the concrete failure honestly and stop automatic retrying. Do not declare the result final or complete.
- A passing first result receives no routine second generation, finishing pass, or retry.
- Keep these behaviors inside the existing clarification, prompt-construction, generation, and review flow. Add no new workflow stage, questionnaire, hidden state system, runtime component, or API control.
- Use the newly settled domain vocabulary consistently: Choice Gate, Custom Path, Visible Body Evidence, Inference Boundary, Structural Scale Failure, Identity Review, Primary Identity Anchor, Protected Identity Cue, Explicit Lock, and Shown Direction.
- No ADR is required because these are visible, reversible contract refinements at existing module boundaries rather than an architectural commitment.

## Testing Decisions

- Use the existing golden-conversation suite as the single highest-level behavior seam. Tests should assert user-visible Choice Gates, preserved locks, coverage classification, prompt obligations, correction routing, and truthful completion behavior rather than exact prose or internal loading mechanics.
- Update the shared checks so every user-visible Choice Gate is A/B/C/D, D is always the scoped Custom Path, A through C are not padded, and a stop path occupies C when only two substantive resolutions exist.
- Update the existing high-risk Reference Coverage scenario so it presents real evidence, user description, scoped inference, and Custom paths; preserves the locked full-body shot; distinguishes verified Visible Body Evidence from the Inference Boundary; and does not suggest a fallback crop or body concealment.
- Add one half-body-to-full-body scenario in which the source clearly shows fuller chest volume and upper-torso build while the target uses opaque layered historical or fantasy clothing. The observable result is that verified upper-body evidence is named neutrally and preserved, only unseen lower-body regions are inferred, and the costume follows rather than flattens the body.
- Extend the existing close-crop-to-full-body proportion recovery scenario to cover the agreed revision boundary: one isolated minor head-unit deviation remains surgical, while linked head-scale and Visible Body Evidence failures become a Structural Scale Failure. The skill performs one appropriate correction, reviews once, preserves all unrelated locks, avoids the defective output as scale evidence when regenerating, and reports failure rather than retrying or claiming completion if the correction still misses.
- Reuse the existing high-risk source-to-target and close-crop proportion scenarios as prior art. Do not create a second behavior suite or per-rule unit-test matrix.
- Run the existing structural skill validator after the golden audit. Treat it as a packaging, metadata, and reference-integrity check rather than another behavior seam.
- Run ordinary Markdown and diff checks to catch malformed documents and whitespace without expanding the test surface.

## Out of Scope

- A new Custom Path module, Choice Gate engine, body-analysis agent, review service, or runtime component.
- A separate body-shape questionnaire, confirmation stage, or anatomy form.
- Asking users to reconfirm Visible Body Evidence that is already clear in the source.
- Requiring a full-body reference when the user accepts a precise Inference Boundary.
- Inferring body shape hidden by loose clothing, occlusion, crop, pose, or unsupported camera projection.
- Cup-size estimation, body measurements, biometric scoring, identity percentages, or other unsupported quantification.
- Sexualizing or exaggerating body features while preserving neutral visible evidence.
- Automatic body reshaping, beautification, slimming, enlargement, or flattening that the user did not request.
- Changing a locked shot, crop, camera, pose, costume, text, lighting, or scene as a silent risk fallback.
- Unlimited retries, a routine second pass, automatic candidate batches, or a post-processing workflow.
- Adding image-model parameters, masks, computer-vision measurement, or external editing tools.
- Changing model selection, quality and size controls, output recipes, trend research, or Scoped Option Refresh beyond their interaction with the universal Custom Path.
- Reworking safety policy. The Custom Path remains subject to the existing safety boundary.
- Creating an ADR for these reversible changes.
- Guaranteeing exact physical reconstruction from evidence the reference does not show.

## Further Notes

- The current contract permits D to be optional in the general clarification format, while permanent-D behavior is enforced more narrowly for creative and refreshable gates. This specification makes the invariant universal without introducing a new module.
- The current identity contract already says that half-body references preserve visible torso shape and body build, but an earlier Protected Identity Cue list scopes body silhouette to full-body and three-quarter sources. Visible Body Evidence removes that contradiction.
- The existing close-crop proportion recovery behavior is retained and sharpened rather than replaced. The new Structural Scale Failure rule connects head scale with simultaneous body-evidence drift and bounds correction to one reviewed attempt.
- Earlier final-quality work excluded routine automatic second passes. This specification does not reverse that default: it permits one correction only after a visible result has already failed an explicit required-quality check.
- The agreed glossary changes are part of this feature's design surface. They introduce Choice Gate, Custom Path, Visible Body Evidence, Inference Boundary, and Structural Scale Failure and expand Identity Review.
