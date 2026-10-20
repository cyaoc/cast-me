Status: needs-triage

# Restrict Automatic Correction to Fresh Results

## What to build

After ticket 01 establishes fixed-root recovery and the Medium Contract specification finishes changing when the bounded single automatic correction triggers, narrow what that same correction may do. It may choose surgical edit only for a visible, inspectable, freshly generated ordinary result with one coherent local defect. Every other eligible failure must use one regeneration from the request's fixed root and locked brief.

This changes only the operation selected by the existing automatic correction. Preserve its trigger, one-correction limit, verified active-surface controls, one follow-up Identity Review, and stop behavior as established by the Medium Contract work.

## Acceptance criteria

- [ ] Restrict automatic surgical edit to a result produced in the current exchange, still visible to CastMe, produced with no generated image among its inputs, terminal rather than reused as a locked produced artifact, reliable as identity evidence, and failing in one coherent local unit.
- [ ] Automatically regenerate from the complete request fixed root when the failed result was already edited, was produced with any generated image input, is a locked produced artifact, or has indeterminate provenance.
- [ ] Exclude the failed result from every regeneration image-input and identity, face, pose, body, composition, or other evidence role. Carry the complete locked brief and every fixed-root input, including any required locked produced artifact.
- [ ] Treat the Primary Identity Anchor appearing among an operation's inputs as insufficient to make the output freshly generated when another input was generated.
- [ ] Keep the correction bounded to exactly one operation followed by exactly one Identity Review. If the corrected result still fails, report the concrete unresolved defect and stop without another edit, generation, retry, final claim, or completion claim.
- [ ] Preserve the existing requirements for visible, inspectable evidence and verified active-surface input controls. When those requirements fail, preserve the decision state and use the existing focused reattachment or review-boundary behavior.
- [ ] Preserve a passing first result's no-routine-second-pass behavior and every correction trigger introduced by `.scratch/medium-aware-identity-contract/issues/02-regenerate-uneven-stylization.md`.
- [ ] Update only the bounded automatic-correction contract in `skills/cast-me/references/identity-anchor.md`; do not reopen its trigger conditions or modify unrelated composition guidance.
- [ ] Do not add another correction, retry, counter, provenance store, noise review item, numeric threshold, glossary term, ADR, module, workflow stage, or runtime component.

## Verification

- [ ] Modify the `Shared checks` automatic-recovery entry and Golden 109, `Automatic identity recovery is bounded and reviewed`, in `evals/golden-conversations.md`; review both directly against `skills/cast-me/references/identity-anchor.md` so the existing trigger and bound remain intact while the operation obeys freshness and fixed-root routing.
- [ ] Add Golden 134, `Automatic correction does not re-edit an edited result`, and review it directly against `skills/cast-me/references/identity-anchor.md`; assert one regeneration from the fixed root, exclusion of the failed result, one follow-up Identity Review, and no second correction.
- [ ] Add Golden 135, `Automatic correction carries generated fixed-root artifacts`, and review it directly against `skills/cast-me/references/identity-anchor.md`; cover a result produced from the Primary Identity Anchor plus a locked produced artifact and require regeneration carrying that artifact rather than surgical edit.
- [ ] Add Golden 136, `Automatic correction regenerates reusable artifacts`, and review it directly against `skills/cast-me/references/identity-anchor.md`; cover a freshly generated locked produced artifact with one coherent local defect and require regeneration because downstream images will reuse it.
- [ ] Extend Golden 131, `Unknown provenance defaults to regeneration`, and review it directly against `skills/cast-me/references/identity-anchor.md`; assert that an otherwise eligible automatic correction regenerates without inventing provenance or tracking history.
- [ ] Preserve Golden 107, `Coherent local identity defects stay surgical`, as the freshly generated terminal-result control and review it directly against `skills/cast-me/references/identity-anchor.md`.
- [ ] Preserve Golden 127, `Uneven stylization regenerates instead of editing`, and review it directly against `skills/cast-me/references/identity-anchor.md`; its Medium Contract trigger must remain unchanged while using the same bounded correction and fixed-root regeneration contract.

## Blocked by

- `01-establish-fixed-root-recovery.md` — this ticket applies the fixed-root and freshness definitions to the bounded automatic correction.
- `.scratch/medium-aware-identity-contract/issues/02-regenerate-uneven-stylization.md` — that A-spec ticket first changes when the same bounded automatic correction triggers; this B-spec ticket then changes which operation that correction may select. The order prevents this ticket from overwriting A's trigger semantics.

## Comments

This ticket narrows what the bounded single automatic correction may do. `.scratch/user-decided-recovery/PRD.md` proposes removing that correction entirely, which would leave this ticket without a subject. Do not implement until that proposal is accepted or rejected.

`.scratch/user-decided-recovery/issues/01-replace-automatic-correction-with-a-recovery-offer.md` removes the automatic correction this landed ticket constrained. Its freshness and fixed-root routing remain as the operation a Recovery Offer names and a user-requested repair performs.
