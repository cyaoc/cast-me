Status: ready-for-agent

# Replace Automatic Correction with a Recovery Offer

## What to build

Implement the single-result half of [`../PRD.md`](../PRD.md). When one visible result fails required quality unambiguously, CastMe states the concrete defect, states which recovery operation the existing contracts select for that result and why, states that it has not performed it, and stops without claiming completion. The user decides whether to spend the generation.

Which operation each failure class selects does not change. Identity Review, the completion bar, the freshly-generated test, the fixed-root regeneration contract, and the surface-capability boundary all stay as they are. What is removed is the skill's initiative to run the operation itself, and with it the per-result versus per-request scope question that initiative created.

Land the `Recovery Offer` glossary entry, the new ADR, and the ADR 0008 revision from [`../domain-changes.md`](../domain-changes.md) in this ticket.

Multi-item behavior belongs to tickets 02 and 03. Touch the shared-defect sentence only enough to remove its dead reference to each result's one correction.

## Acceptance criteria

- [ ] On an unambiguous required-quality failure of a visible, inspectable result, state the concrete defect, the recovery operation the existing contracts select for it, why that operation applies, and that it has not been performed. Run no generation or edit, and never call the result final or complete.
- [ ] Move the follow-up Identity Review to the user-requested recovery path, so a repair the user accepts is still reviewed exactly once and still stops with a concrete report of the remaining defect if it fails again.
- [ ] Remove the per-result correction bound, the same-result exhaustion clause, and the cross-result non-consumption clause. Nothing may refer to an attempt, a remaining attempt, or a correction already spent on another result.
- [ ] Keep every condition that already blocks acting: an unavailable output, a face region that cannot be inspected reliably, an ambiguous review, and a passing first result. State the review boundary truthfully and claim no input control, correction, or completion that was not verified.
- [ ] Preserve the freshly-generated test, the fixed-root regeneration contract, the recovery operation table, the Structural Scale Failure route, the Uneven Stylization regeneration-only rule, and the prohibition on editing a locked produced artifact. They now describe what an offer names and what a user-requested repair performs.
- [ ] Preserve the surface-capability boundary. When the active surface cannot select the fixed-root inputs, say so and ask only for the images it cannot select, rather than naming an operation it cannot run.
- [ ] Update the review-and-revise guidance in `skills/cast-me/SKILL.md` so its failure branch produces the offer, a recovery path is invoked by the user rather than by the skill, and its no-claim list drops the automatic correction that no longer exists. Leave the cross-module completion conditions untouched; they name no executor and never mention correction.
- [ ] Reword the shared-defect sentence only enough to remove its reference to each result's one correction. Do not add the non-shared branch or the shared-cause gate.
- [ ] Add `Recovery Offer` to `CONTEXT.md` in the same change as the runtime references, using the entry in `../domain-changes.md`.
- [ ] Add the new ADR and apply the two deletions to ADR 0008, both from `../domain-changes.md`. Do not mark ADR 0008 superseded, and do not replace the deleted clauses with a statement that the constraint on initiative has become total.
- [ ] Append a comment under the existing `## Comments` heading of `.scratch/edit-chain-depth/issues/02-restrict-automatic-correction-to-fresh-results.md` recording that this ticket removes the behavior that landed ticket implemented. Leave its body and its landed work alone.
- [ ] Synchronize `docs/architecture.md`: replace the automatic-execution node in the `F8` flow with the offer, correct the `F8` prose that still describes a per-result bound and a follow-up review, and update the recorded sizes to 41 canonical terms and 9 ADRs.
- [ ] Add no gate, counter, ledger, preference, setting, retry policy, or any other control that restores the automatic behavior.

## Verification

- [ ] Remove the `Shared checks` automatic-recovery entry from `evals/golden-conversations.md` and replace it with one Recovery Offer entry; review it directly against `skills/cast-me/references/identity-anchor.md`. The fixed-root default and the surgical exception it also carried are already stated by the neighbouring likeness-complaint entry and must not be duplicated there.
- [ ] Repurpose Golden 109 as the user-accepted repair path and review it directly against `skills/cast-me/references/identity-anchor.md`. Keep both of its outcomes: the repair completes only after the follow-up review passes, and a still-failing repair reports the remaining concrete drift and stops.
- [ ] Extend Golden 110 case E and review it directly against `skills/cast-me/references/identity-anchor.md`. Assert that a Recovery Offer marks the result incomplete and names a required operation, while offering an optional cosmetic tweak over a result presented as final stays prohibited. This case is the boundary that keeps the offer from becoming the failure mode it replaces; do not flatten it into a plain offer assertion.
- [ ] Convert Golden 118 and Golden 121 case A into offer assertions and review both directly against `skills/cast-me/references/identity-anchor.md`. Golden 121 case B, the surface-limited half, stays as it is.
- [ ] Convert Golden 98 into a selection-and-offer assertion and review it directly against `skills/cast-me/references/identity-anchor.md`. Keep both classifications it exists for: the isolated head-unit deviation selects Surgical Edit and the linked scale drift selects regeneration, with the offer naming the operation rather than performing it. It needs no acceptance turn, and its coverage-matrix row names the proportion recovery rather than an executor and does not change.
- [ ] Give Golden 127, Golden 131 case B, Golden 138 cases A and B, and the applicable cases of Golden 133 through 136 a user-acceptance turn, and review them directly against `skills/cast-me/references/identity-anchor.md`. Each is the only place its contract runs rather than being merely named, so the first turn asserts the offer and the second asserts the operation executing with its required inputs and exclusions.
- [ ] Remove Golden 138 case E, which exists only to exhaust an attempt. Leave case F to ticket 03.
- [ ] Reword Golden 152 case B from the bounded automatic path to the offer and review it directly against `skills/cast-me/references/identity-anchor.md`. Its assertion that no count, tally, safe-edit number, or remaining-edits figure appears must survive unchanged.
- [ ] Preserve Golden 105 and Golden 153, changing only the phrase `do not claim automatic correction`, which loses its subject.
- [ ] Preserve Golden 8, 12, 67, 68, 96, 97, 107, 108, 111, 112, 125, 126, 128, 129, 130, and 142, and confirm each by reading it rather than assuming. Every one is either an explicit user request or a review-and-classify scenario, and none performs a repair on the skill's own initiative.
- [ ] Keep the coverage matrix in `docs/architecture.md` consistent: every Golden number still appears exactly once, and the `F8` rows for 109, 110, 118, 121, 131, 138, and 152 describe what those scenarios now assert.

## Blocked by

- None — can start immediately.

## Supersedes

- [`../../edit-chain-depth/issues/02-restrict-automatic-correction-to-fresh-results.md`](../../edit-chain-depth/issues/02-restrict-automatic-correction-to-fresh-results.md). That ticket has landed; it narrowed which operation the bounded single automatic correction could select. This ticket removes the correction itself, so that operation restriction survives only as the routing a Recovery Offer names and a user-requested repair performs. Its own `## Comments` already records that this proposal would leave it without a subject.
- `.scratch/edit-chain-depth/PRD.md` story 29, superseded by the new ADR. Its story 7 is rewritten and its story 8 is void; `.scratch/identity-preservation-reliability/PRD.md` stories 34 and 35 are rewritten and its story 37 is void. `../domain-changes.md` carries the full disposition table.
