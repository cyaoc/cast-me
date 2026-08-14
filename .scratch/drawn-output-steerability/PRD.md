Status: ready-for-agent

# Drawn output that keeps its locks and returns its vocabulary

Written from one field run: a chibi sticker request taken end to end by a non-specialist user. Three defects surfaced. They are independent — each has its own cause, its own fix, and its own ticket — and they appeared together only because the run combined strong deformation, a full-body crop, and a two-handed action.

## Problem Statement

**Three hands.** The delivered sticker carried two right hands and one left. The negative-constraint vocabulary cannot express either half of that. `identity-anchor.md:226` forbids `extra fingers, fused fingers, malformed hands, broken wrists, extra limbs, unexplained distorted anatomy` — a duplicated-chirality hand violates none of them literally, because its finger count is right and its individual form is normal. The same list is reused as the post-generation check at `identity-anchor.md:297`, so neither generation nor review could catch it.

The count half has a separate cause. The user locked an exaggerated exit with both hands waving. `composition-director.md:205` offers the model `frozen action, natural motion blur, or long-exposure character` — camera vocabulary only. A Drawn Character has no motion vocabulary at all, so the model supplied its own drawing convention for a fast wave, which is repeated limb positions.

Three further conditions made the result likely rather than unlucky. `styling-performance.md:135` treats `hands, props, and follow-through` as one link of the pose chain, so no per-hand position is ever written. The locked action was bilaterally symmetric with no differentiating detail. And the selected proportion simplifies hands, which removes the thumb — the only visual carrier of handedness — while `styling-performance.md:147` independently pushes toward simplification by avoiding poses that need `precise finger articulation`. The skill treats hands as complexity to avoid rather than as countable, sided structures to pin.

**A locked tier that the following gates never read.** After the tier locked at the shortest coherent proportion, two later gates behaved as though it had not.

The crop gate offered waist-up, two-thirds, and full-body. At that proportion the whole figure stands about one and a half heads tall, so those options are not visibly distinguishable. `composition-director.md:148` already requires adapting the options to `the current scene, locks, and Shown Option history`, and the tier is an Explicit Lock, so the rule that should have fired exists. It did not, and the two worked examples immediately below it at `:154` and `:168` are both photographic — waist up, whole body, face and shoulders, camera at eye height. The examples outweighed the rule.

Reference Coverage then asked for a full-body photograph to supply waist, hips, legs, shoes, and weight placement. `identity-anchor.md:139` states that the shortest coherent proportion cannot carry a source-supported figure and forbids restoring it silently. The user was asked to supply evidence the contract had already discarded. The coverage trigger at `identity-anchor.md:169` fires on whether the target reveals body scale, limbs, or posture and never consults the resolved Medium Contract.

The request was also not uniformly illegitimate, which is what makes a blanket suppression wrong. Shoes, stance direction, and weight placement survive at any proportion, and `identity-anchor.md:137` weights characteristic wardrobe *up* as a recognition channel precisely when proportion closes. The gate's error was bundling a closed channel and open ones into one demand.

A third, smaller instance: the stylization-intensity gate offered a path that preserved more facial structure, which the already-locked proportion cannot deliver. `SKILL.md:61` binds the recommendation to the current decision state but says nothing about the other offered paths, and the `Shared checks` entry in `evals/golden-conversations.md` requires only that A through C be `concrete and valid` without defining valid as deliverable.

**A style vocabulary the user cannot speak.** The user reported being unable to say what look they wanted, and named the reason: they can recognize a good image but not describe its style. The six axes at `composition-director.md:34` are production vocabulary, and the named starting looks at `:53` are read as text and imagined before any image exists. Eight serial text gates preceded the first picture, and every one of them asked the person least equipped to answer.

Two apparent escapes are closed. `composition-director.md:67` accepts a supplied artwork as a style reference and extracts its rendering into the axes, but no gate ever offers this, and `D) Custom` consistently asks the user to *describe*. `SKILL.md:76` treats every ordinary generation as a final asset and forbids adding a quality question, so there is no cheap probe to choose from either.

The consequence compounds. `composition-director.md:47` already routes a single named axis through Scoped Option Refresh, so "make the line heavier and change nothing else" is a supported operation. A user who does not know the axis exists, or what it was set to, can never reach it.

## Solution

**Pin the hands positively, and give drawn motion its own decision.** Split the pose chain's single hands link into left and right, each carrying position, orientation, and thumb side, which fixes the count as two by construction. Add one chirality entry to the negative vocabulary and to the post-generation check, drawn into the existing three-to-eight budget only when both hands are visible and active. Add a Drawn Motion Convention as an ordinary visible decision — speed lines, afterimage, repeated limb positions, or a held freeze — so repeated limbs become a path the user chooses rather than a convention the model supplies. That choice is the single carve-out from the two-hand count rule.

**Give the Medium Contract one new authority, and nothing else.** A closed channel is never requested as missing reference evidence. Judge it per channel, so a tier that closes body proportion still permits asking about shoes, stance, and weight placement. The contract does not grow into a general production contract; ADR 0010 records why. Crop vocabulary stays with Shot Direction, whose existing adapt-to-locks rule names the Deformation Tier and gains a drawn worked example to offset its two photographic ones. Extend the inheritance obligation from the recommendation to every offered path, so an option the current locks cannot deliver is not shown.

**Return the vocabulary in the result instead of demanding it in the brief.** Deliver a Style Readout with the first result of each style state: the locked axis values, Deformation Tier, and stylization intensity, in visible language. One readout per style state, not per image, so a set shares one; after a single-axis refresh, report only the axis that moved. It records locked decisions, never the rendered outcome, so it carries no quality claim of its own. Photographic output receives the same mechanism with different content — only the two or three finish controls that actually changed the look, not a full signature.

## User Stories

1. As a user asking for an action sticker, I want exactly two hands with correct handedness, so that the result is usable without a redo.
2. As a user, I want each hand's position and orientation written into the brief, so that a symmetric two-handed gesture does not become one hand mirrored twice.
3. As a user, I want a duplicated-chirality hand to fail the post-generation check, so that a defect I can see in one second is not delivered as finished.
4. As a user requesting a fast gesture in a drawn medium, I want to choose how motion is drawn, so that the model does not add limbs to convey speed.
5. As a user who chooses repeated limb positions deliberately, I want that to remain available, so that a legitimate drawing convention is not banned to fix a defect.
6. As a user who selected the strongest deformation, I do not want to be asked for a full-body photograph to supply a figure that deformation discards, so that I am not sent to find evidence nothing will use.
7. As the same user, I still want to be asked about shoes, stance, and weight placement, so that the details that carry recognition at that proportion are not lost with the ones that cannot survive it.
8. As a user, I want one coverage request to separate what the contract closed from what it left open, so that a single bundled demand does not hide either.
9. As a user who locked a two-and-a-half-head figure, I do not want crop options that differ only in an amount of body that proportion cannot show, so that the question is worth answering.
10. As a user, I want every offered path to be deliverable under what I have already locked, so that choosing one does not silently contradict an earlier choice.
11. As a beginner, I want to be told what rendering treatment my image was actually given, so that I learn the vocabulary from the result instead of being asked for it beforehand.
12. As that beginner on the next round, I want to say "heavier line, everything else the same" and be understood, so that the single-axis refresh that already exists becomes usable.
13. As a user receiving a set, I want one readout for the whole set, so that six stickers do not carry six identical descriptions.
14. As a user who refreshed one axis, I want to be told only what changed, so that I can see the effect of my own instruction.
15. As a user of photographic output, I want the same explanation kept short and limited to what actually changed the look, so that a portrait does not arrive with a rendering essay.
16. As a user, I do not want the readout to claim my image came out right, so that a description of intent is not mistaken for a quality verdict.
17. As a maintainer, I want closed-channel suppression judged per channel rather than per body region, so that the fix does not silently drop evidence the tier never closed.
18. As a maintainer, I do not want the Medium Contract to become a general production contract, so that the identity model stays the one thing it describes.
19. As a maintainer, I want the crop fix expressed as naming the tier in the rule that already exists plus one drawn example, so that a second, competing adaptation rule is not created.
20. As a maintainer, I want the hand fix carried mainly by positive per-hand direction, so that it does not depend on a negative constraint competing for a limited budget.

## Implementation Decisions

- Pose geometry's hands link becomes two links, left and right, each with position, orientation relative to the body, and thumb side. The count of two is asserted positively there rather than as a prohibition.
- The chirality entry joins the existing hands-and-body negative line and the post-generation check. It is selected into the adaptive three-to-eight budget only when both hands are visible and performing, not added universally.
- Drawn Motion Convention is an ordinary production decision resolved through the existing Choice Gate when it is production-critical and unresolved. It is not a new module, stage, or reference file, and it does not resolve Deformation Tier, stylization intensity, or any style axis.
- The two-hand count rule carves out exactly one exception: an explicitly selected repeated-limb motion convention. No other path may add a hand.
- The simplification pressure at `styling-performance.md:147` stays. It is scoped to finger articulation, which is not what carries handedness; the thumb side survives as the minimum chirality anchor at any simplification level.
- The Medium Contract's closed state gains one clause: never requested as missing reference evidence. It also records a Visible Body Evidence carriage state of carried, simplified, or not carried, because body evidence is a category parallel to Protected Identity Cues and never reaches a channel state, so an authority phrased only over closed channels would not fire for the case that motivated it. The Deformation Tier gradient already computes that value; recording it puts the result where a downstream gate can read it. ADR 0010 records both the addition and the decision not to extend the contract to non-identity dimensions.
- Only Reference Coverage reads the carriage state. Identity Review is untouched, because at the shortest proportion it already decides completion through transferred cues and thumbnail-silhouette readability rather than through body-evidence comparison.
- Reference Coverage consults the resolved Medium Contract before constructing its paths. Closed channels are dropped from the request; open and transferred ones in the same body region survive it, and characteristic wardrobe is treated as a channel that gains weight at strong deformation rather than losing it.
- Shot Direction's existing adapt-to-locks sentence names the Deformation Tier explicitly, and a drawn worked example joins the two photographic ones so the examples stop outweighing the rule. When the locked proportion leaves no visibly distinguishable crop choice, the dimension is resolved internally rather than asked.
- The inheritance obligation moves from the recommendation to the full A/B/C set. The `Shared checks` line defining A through C as concrete and valid is amended in the same change so the two statements cannot diverge.
- Style Readout is delivered with the result, not as a gate, and never as a Choice Gate. Its unit is the style state: emitted with the first result under a given combination of axes, tier, and intensity; suppressed while that combination holds; reduced to the changed axis after a single-axis refresh.
- The readout reports the locked decision record. It does not inspect the image, and it does not carry a completion, likeness, or quality claim. Whether the result matches remains with Identity Review and its Uneven Stylization check.
- Photographic output receives a readout limited to the finish controls that materially changed the look. It does not use the six drawn axes and does not reproduce a full Direction Signature.

## Testing Decisions

One seam, already in place: `evals/golden-conversations.md`, reviewed directly against the skill files, with `docs/architecture.md` synchronized for the F-flow coverage and scale baseline. No new seam is proposed. Cross-cutting invariants go to `Shared checks`; scenario behavior goes to numbered Goldens 155 onward.

Good tests here assert visible conversational behavior — which gate appears, what it offers, what the prompt must contain, what the review must catch — never the wording of a rule.

Prior art to follow and to preserve:

- Golden 11 already asserts the pose geometry chain from an upper-body reference. The per-hand split extends it rather than replacing it; its rule against irrelevant chain nodes must survive, so a hand outside the frame still must not be written.
- Golden 102 and Golden 117 are the Reference Coverage scenarios. Both must keep firing for genuinely missing open evidence; the new suppression must be visible as a narrowing of what is asked, never as the gate disappearing.
- Golden 140 already asserts that the shortest proportion cannot carry the figure and must disclose that loss. The suppression rule is its downstream consequence and should be asserted against the same contract.
- Golden 141 case E already covers the four-to-five-head child-reading disclosure. It is correct as scoped and is not touched; the shortest proportion is below any real human proportion and needs no equivalent warning.
- Golden 143 and Golden 144 own the six axes and the starting-look gate. The Style Readout reports their locked values and must not restate, re-resolve, or reorder them.
- Golden 147 and Golden 149 own set delivery. The one-readout-per-set rule is asserted there rather than in a new set scenario.

New scenarios, four rather than the six first sketched, because the merged tickets share assertions:

- Golden 155, `A locked deformation governs the gates that follow it` — one strong-deformation sticker run reaching both the crop gate and Reference Coverage. Assert indistinguishable crop options are not offered, the closed figure channel is not requested, and shoes, stance, and weight placement still are.
- Golden 156, `Every offered path is deliverable under current locks` — a gate whose obvious option contradicts an earlier lock. Assert the unreachable path is absent, the remaining paths stay concrete, and the Custom Path and stop-path conventions are unchanged.
- Golden 157, `Both hands survive a drawn action` — a symmetric two-handed action at strong deformation. Assert per-hand position, orientation, and thumb side in the prompt; a count of two; the chirality entry present in the negatives and in the review; and repeated limbs appearing only under an explicitly selected motion convention.
- Golden 158, `A Style Readout accompanies each style state` — first result, a six-item set, and a single-axis refresh. Assert one readout for the set, changed-axis-only reporting after the refresh, locked values rather than observed ones, and no completion or quality claim.

## Out of Scope

- The number of serial clarification turns before the first image. Serial single-dimension questioning is the skill's core interaction design; changing it is a separate effort and was explicitly excluded.
- Promoting a supplied style-reference image to a first-class path, and adding a cheap low-quality style probe. Both were considered and rejected; ADR 0011 records why.
- Growing the Medium Contract into a general production contract recording which non-identity dimensions remain meaningful. ADR 0010 records the rejection.
- Changing what Identity Review judges, the open/transferred/closed states themselves, Deformation Tier semantics, stylization intensity, the six axes, or the Character Sheet flow. This work reads those results; it does not redefine them. The Medium Contract does gain a Visible Body Evidence carriage state, recorded under Implementation Decisions and ADR 0010; that is an addition beside the channel states, not a change to them, and nothing reads it except Reference Coverage.
- Any anatomy check beyond hand count and chirality. Extra fingers, fused fingers, and extra limbs are already covered and are not being restated.
- A score, counter, ledger, or confidence figure anywhere in the readout or the hand check.

## Further Notes

The three defects were reported as one complaint and are recorded here as three because their fixes do not share a mechanism. Merging them would have produced a single propagation rule that appears to cover the hands and does not: the chirality gap is medium-independent and would survive at any proportion, and the third hand comes from missing drawn motion vocabulary rather than from an unread lock. Only the crop and coverage defects are genuinely one cause.

Two claims in the original diagnosis did not survive checking and are recorded so they are not re-raised. The four-to-five-head child-read disclosure is correctly scoped, because that band matches real child proportions while the shortest proportion does not read as a child at all. And the intensity gate's *recommendation* was consistent with the contract, since recognition legitimately transfers to hairstyle, eye shape, marks, and wardrobe at strong deformation; the defect was in the option set, not the recommendation.

The third-hand cause is a hypothesis. The image was not available for inspection, and the reasoning is that a repeated-limb drawing convention for a fast wave explains the count and the placement together. The motion-vocabulary gap it points at is real regardless of whether it produced this particular result, since a Drawn Character currently has no motion vocabulary at all.

**The carriage state was a spec change, raised rather than back-filled.** The first implementation of the suppression authority phrased it only over closed channels and then hardcoded a list of body measurements to suppress at the shortest proportion. Code review caught that the general clause could never fire, because no body measurement is a Protected Identity Cue, so the hardcoded list was doing all the work — which is the point fix this spec chose against. Rather than adjust the prose and let the spec ratify it afterwards, the gap was raised as a change to this document and to ADR 0010 first, per the rule recorded at `.scratch/cross-spec-defect-provenance/research.md:97`.

The Style Readout's largest effect may be one it was not designed for. Single-axis Scoped Option Refresh has been specified and implemented since the six-axis work, and a user who cannot name an axis or recall its value has no way to invoke it. The readout is the first thing that makes that capability reachable by the users it was built for.
