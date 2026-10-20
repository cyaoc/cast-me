Status: ready-for-agent

# Anchor Two Applications to One Character Sheet

## What to build

Implement the thinnest end-to-end Character Sheet slice from [`../PRD.md`](../PRD.md): one recurring drawn character and two application images that visibly remain the same character. Generate one Character Sheet from the Primary Identity Anchor, then generate both applications independently from that sheet together with the Anchor.

Treat the Character Sheet as an ordinary generated artifact carried by the existing fixed-root and recovery contracts, not as a new module, agent, gate, or persistent character library. Land the Character Sheet glossary entry and the two-stage ADR from [`../domain-changes.md`](../domain-changes.md) in this same ticket so the canonical term never gets ahead of runtime behavior.

## Acceptance criteria

- [ ] For a request that explicitly needs a reusable drawn character or at least two images of the same drawn character, generate one Character Sheet before either application image.
- [ ] Generate the Character Sheet from the Primary Identity Anchor as an actual image input, on a clean background, and lock its proportions, face construction, hair, eye rendering, wardrobe, palette, line treatment, and shading treatment.
- [ ] Supply both `Primary Identity Anchor` and `Character Sheet` as actual, explicitly labeled image inputs to each application. State that the Anchor governs who the person is, while the Character Sheet governs how that person is drawn and never serves as identity evidence.
- [ ] Tell every application not to redesign the character. Generate both applications independently from the same sheet and Anchor; never pass application 1 into application 2 or otherwise grow the image-input chain.
- [ ] Preserve application-specific scene, expression, gaze, pose, camera, and output locks rather than forcing the two applications to be duplicates.
- [ ] Add the Character Sheet to the request's fixed root as a locked produced artifact for every application built from it. Regeneration of an application carries the Anchor, the sheet, and the complete locked brief while excluding the failed application.
- [ ] Regenerate a failing Character Sheet from its own fixed root rather than editing it. Regenerate a failing application automatically rather than surgically editing it because a generated image was among its inputs.
- [ ] When the user explicitly insists on a local edit to one application, preserve the existing direct-edit boundary: recommend regeneration, but allow the edit with the application plus the Primary Identity Anchor and do not add the Character Sheet again.
- [ ] Do not introduce a Character Sheet for an unrelated one-off drawn image in this slice, and do not add Deformation Tier, style axes, batch behavior, mannerism weighting, or a new workflow component.
- [ ] Update the owning runtime seams in `skills/cast-me/SKILL.md`, `skills/cast-me/references/identity-anchor.md`, and `skills/cast-me/references/composition-director.md` without creating another reference module.
- [ ] Add `Character Sheet` to `CONTEXT.md` and add `docs/adr/0008-anchor-drawn-characters-to-a-locked-character-sheet.md` in the same change as the runtime behavior. Do not add `Deformation Tier` yet.
- [ ] Synchronize `docs/architecture.md` with the Character Sheet input roles, fixed-root routing, two-application flow, current asset sizes, 38 canonical terms, 8 ADRs, and Golden 1–138 coverage.

## Verification

- [ ] Add Golden 137, `One Character Sheet anchors two independent applications`, and review it directly against `skills/cast-me/references/identity-anchor.md` and `skills/cast-me/references/composition-director.md`. Assert sheet-first generation from the Anchor, the locked design fields, labeled Anchor and Sheet inputs for both applications, explicit role separation, no redesign, no application-to-application input, and different application-level expression, pose, and camera choices.
- [ ] Add Golden 138, `Character Sheet recovery stays on the fixed root`, and review it directly against `skills/cast-me/references/identity-anchor.md`. Cover a failing application, a failing Character Sheet, and a user-requested local application edit; require the two regeneration routes and preserve the explicit-edit input boundary.
- [ ] Preserve Golden 127, `Uneven stylization regenerates instead of editing`, and Golden 135–136 fixed-root automatic-correction behavior as prerequisite controls, and review them directly against `skills/cast-me/references/identity-anchor.md`.

## Blocked by

- [`.scratch/medium-aware-identity-contract/issues/02-regenerate-uneven-stylization.md`](../../medium-aware-identity-contract/issues/02-regenerate-uneven-stylization.md) — completing this ticket completes the Medium-Aware Identity Contract specification required by PRD line 23.
- [`.scratch/edit-chain-depth/issues/02-restrict-automatic-correction-to-fresh-results.md`](../../edit-chain-depth/issues/02-restrict-automatic-correction-to-fresh-results.md) — Character Sheet applications and the sheet itself depend on its fixed-root, generated-input freshness, and locked-produced-artifact recovery rules.
