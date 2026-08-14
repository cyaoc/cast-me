Status: ready-for-agent

# Gate the Rebuild Scope for a Shared Cause

## What to build

Finish the multi-item Recovery Offer with its shared-cause branch. When several items of one set fail on the same defect, the cause is attributed to the Character Sheet or locked brief and reported once, as it already is — and the offer now also names the operation that cause selects, which the current flow never reaches because it stops at attribution.

Naming that operation exposes a cost the old flow never had to state. Repairing a shared cause regenerates the Character Sheet, and a regenerated Sheet is a new Sheet rather than a patched one, so rebuilding only the failing items leaves the set carrying two versions of the character, while rebuilding every item costs one generation per item. The skill has no basis for choosing between those, because the trade is the same cost-against-quality judgment this feature hands to the user. This branch alone therefore ends in a Choice Gate.

A throwaway prototype of both branches produced this finding; the shared branch turned out to be the harder one, not the easier one.

## Acceptance criteria

- [ ] Keep the existing attribution unchanged: several items failing on one defect are a Character Sheet or locked-brief failure reported once, not a per-item failure.
- [ ] Name the operation that cause selects — regenerate the Character Sheet from its own fixed root and Sheet brief, then regenerate items from the new Sheet — and state that neither has been performed.
- [ ] Disclose that a regenerated Character Sheet is a new Sheet rather than a patched one, so items still built from the old Sheet no longer share its locks.
- [ ] Present the rebuild scope through one localized Choice Gate, in the shape the convention already prescribes when only two substantive resolutions exist: rebuild every item from the new Sheet, rebuild only the failing items and accept two versions of the character in the set, an explicit stop path that delivers the passing items unchanged, and the permanent Custom Path.
- [ ] State the cost of each path concretely in terms of the current request rather than as a general rule, and do not recommend one by default.
- [ ] Do not let the gate reopen creative choices, unrelated Explicit Locks, or the resolved Medium Contract, and do not let any of its paths restore automatic repair.
- [ ] Keep the gate scoped to a shared cause. A request whose failing items share no cause still ends at the offer, per ticket 02.
- [ ] Accommodate the absent default in the general Choice Gate format in `skills/cast-me/SKILL.md`, which currently opens every gate with a recommendation sentence, tells the user how to accept that recommendation, and lists the recommended path among what a clarification must give. Add only the exception: when an owning contract forbids a default, the gate states the concrete tradeoff, marks no path as recommended, and its reply instruction shows how to select a path. Leave the requirement intact wherever a safe default exists.
- [ ] Synchronize `docs/architecture.md`: the shared-defect branch in `F8` no longer terminates at attribution but continues through operation selection and the offer node into the gate.

## Verification

- [ ] Extend Golden 138 case F and review it directly against `skills/cast-me/references/identity-anchor.md` and `skills/cast-me/references/composition-director.md`. Assert the single shared-cause report, the operation named for that cause, the disclosure that a regenerated Sheet is a new Sheet, and the four-path gate including its stop path and its Custom Path.
- [ ] Extend Golden 154 with a case that does have a shared cause and assert that it reaches the gate while the unrelated-failure case does not, so the two branches are distinguished in one place and neither can silently take the other's route.
- [ ] Confirm the new gate against the `Shared checks` Choice Gate entries in `evals/golden-conversations.md`: exactly four scoped paths, `D) Custom` as a localized custom path that cannot bypass safety or reopen unrelated Explicit Locks, and no padded menu.
- [ ] Keep the coverage matrix row for Golden 138 in `docs/architecture.md` accurate about the shared-cause branch and its gate, and leave every other row untouched.

## Blocked by

- [`02-report-unrelated-batch-failures-in-one-offer.md`](02-report-unrelated-batch-failures-in-one-offer.md) — the shared branch is one arm of the request-wide offer that ticket establishes, and both tickets edit the same recovery paragraph and the same `F8` flow.
