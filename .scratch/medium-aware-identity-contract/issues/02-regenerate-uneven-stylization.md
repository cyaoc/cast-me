Status: ready-for-agent

# Regenerate Uneven Stylization from the Primary Identity Anchor

## What to build

After the Medium Contract is available, make Uneven Stylization an Identity Review completion failure independent of likeness. A result whose features do not share one coherent selected medium must regenerate from the Primary Identity Anchor and locked brief instead of being surgically edited.

Land the corresponding `Uneven Stylization` glossary entry from [`../domain-changes.md`](../domain-changes.md) in this ticket. Do not add a separate ADR; its judgment and routing follow from the Medium Contract decision implemented by ticket 01.

## Acceptance criteria

- [ ] Identity Review fails a visible result when some features are fully converted to the selected medium while others remain photographic, even when the person remains recognizable.
- [ ] Route Uneven Stylization to one new generation from the Primary Identity Anchor and complete locked brief. Include the Anchor and only required reliable supporting references as actual image inputs, and exclude the failed result from every image-input and identity, face, pose, body, composition, or other evidence role.
- [ ] Never route Uneven Stylization through a surgical edit. When Uneven Stylization and identity drift occur together, use the same single regeneration to address both rather than spending the bounded correction on one failure.
- [ ] Restate the selected medium positively for every visible surface: skin, hair, eyes, wardrobe, lighting, and background. Do not name the surfaces that remained photographic or phrase their absence as a negative instruction.
- [ ] Preserve the existing active-surface capability boundary, one-correction limit, one follow-up Identity Review, complete decision state, and stop behavior when required image-input controls are unavailable or the corrected result still fails.
- [ ] Update `skills/cast-me/references/identity-anchor.md` with the failure classification and regeneration route.
- [ ] Update `skills/cast-me/references/composition-director.md` so the non-photographic recipe supplies coherent positive medium language for all visible surfaces during regeneration.
- [ ] Add `Uneven Stylization` to `CONTEXT.md` in the same change as the runtime references. Do not create another ADR.
- [ ] Synchronize `docs/architecture.md` with the named result state, recovery route, recounted sizes for every changed asset, 37 canonical terms, 7 ADRs, and Golden 1–127 coverage.
- [ ] Do not implement deformation tiers, character-sheet generation, edit-chain depth, provenance rules, or any behavior owned by the downstream specifications.
- [ ] Completing this ticket after ticket 01 finishes this feature's prerequisite contract; leave both downstream specifications unimplemented.

## Verification

- [ ] Add Golden 127, `Uneven stylization regenerates instead of editing`, where eyes and hair use the selected drawn medium while skin and lighting remain photographic. Assert failure despite intact likeness, regeneration rather than edit, inclusion of the Primary Identity Anchor, exclusion of the failed result, preservation of the locked brief, positive medium language across every visible surface, and exactly one follow-up Identity Review.
- [ ] Review Golden 127 directly against `skills/cast-me/references/identity-anchor.md` and `skills/cast-me/references/composition-director.md`. Preserve the ticket-01 Medium Contract scenarios and photographic controls unchanged.

## Blocked by

- `01-resolve-medium-contract.md` — the failure state depends on the resolved Medium Contract and its review semantics.
- No external issue or specification blocks this ticket.
