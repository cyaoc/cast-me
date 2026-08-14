Status: ready-for-agent

# Report Unrelated Batch Failures in One Offer

## What to build

Extend the Recovery Offer to a request that produced several items, for the case where the failing items do not share a cause. Three failing items out of twelve produce one report rather than three conversations: each failing item's concrete defect together with the operation selected for it, gathered into a single offer that one user instruction may accept in full, in part, or not at all.

This is the shape the only field evidence on record describes — items needing individual redo out of one planned batch — and it is exactly the case the existing shared-defect rule does not reach, because that rule fires only for a cause attributable to the Character Sheet or locked brief. The shared-cause branch is ticket 03.

## Acceptance criteria

- [ ] When several items of one request fail review and no shared cause is supportable, produce one Recovery Offer for the whole request, carrying one entry per failing item: that item's concrete defect and the operation the existing contracts select for it.
- [ ] Say plainly that no shared cause is claimed, rather than attributing the failures to the Character Sheet or locked brief on thin evidence.
- [ ] Accept a single user instruction that approves every listed item, a named subset, or none of them. Do not ask item by item, and do not require the user to restate the request for each one.
- [ ] Disclose that items regenerated individually were not part of the planned batch, so their consistency with the passing items is best effort. Never claim batch consistency for them.
- [ ] Carry the Character Sheet, the Primary Identity Anchor, the request-wide Medium Contract, and each item's own locked brief into every accepted repair, and exclude each failed item from every image-input and identity, face, pose, body, composition, or other evidence role.
- [ ] Keep the offer a report rather than a Choice Gate, because it asks for a decision the user may also ignore.
- [ ] Add no counter, ledger, per-item budget, retry policy, success rate, or remaining-attempts figure.
- [ ] Synchronize `docs/architecture.md`: `F8` runs its existing classification through to a selected operation for every failing item and then collects the outcomes into one offer node, rather than routing a single result.

## Verification

- [ ] Add Golden 154, `Unrelated batch failures report once and repair on one instruction`, and review it directly against `skills/cast-me/references/identity-anchor.md` and `skills/cast-me/references/composition-director.md`. Cover a twelve-item set with three items failing for unrelated reasons — a mixed-surface item, an item whose head scale is unexplained by the locked Deformation Tier, and an item that substitutes a generic face — and assert one report rather than three exchanges, one entry per failing item with its own defect, the operation named for each, an explicit statement that no shared cause is claimed, the best-effort disclosure about items rebuilt outside the batch, and a single instruction accepting a named subset.
- [ ] Preserve Golden 138 case F unchanged in this ticket. The shared branch belongs to ticket 03, and a change here would let the two branches blur.
- [ ] Preserve Golden 147 and Golden 149 and review them directly against `skills/cast-me/references/composition-director.md`. Batch capability detection and truthful set delivery are unaffected by how failures are reported.
- [ ] Update the coverage matrix in `docs/architecture.md` from `Golden 1–153` to `Golden 1–154`, place the new scenario under `F8`, and correct the golden count recorded in [`../domain-changes.md`](../domain-changes.md), which currently predicts the count will hold.

## Blocked by

- [`01-replace-automatic-correction-with-a-recovery-offer.md`](01-replace-automatic-correction-with-a-recovery-offer.md) — the offer must exist for one result before it can gather several.
