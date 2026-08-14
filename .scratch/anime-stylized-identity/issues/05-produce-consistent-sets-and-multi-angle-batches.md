Status: ready-for-agent

# Produce Consistent Sets and Multi-Angle Batches

## What to build

Extend the Character Sheet slice to complete sets, series, and multi-angle work. Prefer one planned batch when the active surface actually supports it; otherwise generate each image independently from the same Character Sheet and Primary Identity Anchor without claiming batch consistency.

Keep one-off drawn images direct, accept a user-supplied Character Sheet from an earlier conversation, and make set delivery truthful about dimensions and transparency.

This slice owns the shared-defect recovery case for a multi-image request: when several items fail on the same inherited cause, report it once rather than correcting each item. The per-result automatic-correction bound itself stays with [`../../edit-chain-depth/PRD.md`](../../edit-chain-depth/PRD.md).

## Acceptance criteria

- [ ] Introduce or require a Character Sheet for a requested set, series, reusable character design, multi-angle sheet, or second image of the same drawn character. Skip it for one drawn image with no continuity requirement.
- [ ] Accept a user-supplied Character Sheet as the same labeled rendering-design input, while retaining the supplied person photo as the Primary Identity Anchor and sole identity source.
- [ ] Detect batch production as an active-surface capability. When it is available, plan and produce a sticker set or multi-angle sheet as one coherent batch rather than as generated images that reference each other.
- [ ] When batch production is unavailable, generate every item independently from the same Character Sheet, Primary Identity Anchor, request-wide Medium Contract, and per-image locked brief. Never feed one application into the next.
- [ ] When several items of one set fail on the same defect, attribute it to the Character Sheet or locked brief rather than to each item, report the shared cause once, and do not correct the items individually.
- [ ] State truthfully which path was used. Do not claim batch consistency, paid-mode behavior, a success rate, or a number of usable images when the active operation did not verify it.
- [ ] Carry one shared character palette and other Character Sheet locks across every item while preserving legitimate per-image expression, pose, angle, and story-state changes.
- [ ] Verify that delivered set members use the required matching dimensions and output organization; do not let an automatic crop silently leave one item at a different size.
- [ ] When transparent stickers are requested, state before generation that the active model does not produce transparency and record downstream cutout as a delivery requirement. Do not promise an alpha channel or implement automated cutout.
- [ ] Keep multi-person drawn output unsupported and state that boundary before generation rather than producing a blended identity.
- [ ] Keep drawn likeness best effort without a similarity score, identity guarantee, batch-consistency guarantee, or persistent character library.
- [ ] Update the routing and generation checkpoint in `skills/cast-me/SKILL.md`, the actual-image and Character Sheet roles in `skills/cast-me/references/identity-anchor.md`, and batch, series, layout, dimension, and delivery behavior in `skills/cast-me/references/composition-director.md`.
- [ ] Synchronize `docs/architecture.md` with the Character Sheet trigger boundary, batch/fallback routes, multi-angle and set delivery, current asset sizes, 39 canonical terms, 8 ADRs, and Golden 1–149 coverage.
- [ ] Do not add a batch service, retry policy, output success-rate promise, alpha-generation workflow, style gallery, or character library.

## Verification

- [ ] Add Golden 147, `Sets use a verified batch capability or the Character Sheet fallback`, and review it directly against `skills/cast-me/references/composition-director.md` and `skills/cast-me/references/identity-anchor.md`. Pair a batch-capable surface with a surface that lacks the capability; require one planned batch in the first case, independent Sheet-rooted generations in the second, shared character locks in both, and no false batch-consistency claim.
- [ ] Add Golden 148, `Character Sheet activation follows continuity need`, and review it directly against `skills/cast-me/references/identity-anchor.md`. Pair a one-off image, a second image of the same character, a reusable or multi-angle request, and a user-supplied Character Sheet; assert the correct trigger and input roles in each case.
- [ ] Add Golden 149, `Drawn-set delivery states its real boundaries`, and review it directly against `skills/cast-me/references/composition-director.md`. Cover matching dimensions, a transparency request recorded for downstream cutout, truthful best-effort language without rates or guarantees, and a multi-person request stopped before blended output.
- [ ] Preserve Golden 137–138 Character Sheet input and recovery contracts and Golden 145 shared colour logic, and review them directly against `skills/cast-me/references/identity-anchor.md` and `skills/cast-me/references/composition-director.md`. Golden 138 case F asserts the shared-defect set recovery this slice owns: several applications failing on the same defect report the shared Character Sheet or locked-brief cause once and do not spend each application's one correction reproducing it.

## Blocked by

- [`.scratch/medium-aware-identity-contract/issues/02-regenerate-uneven-stylization.md`](../../medium-aware-identity-contract/issues/02-regenerate-uneven-stylization.md) — the entire feature remains blocked by the completed Medium-Aware Identity Contract required by PRD line 23.
- [`04-express-style-through-six-visible-axes.md`](04-express-style-through-six-visible-axes.md) — set production must carry the already-resolved Character Sheet design, style axes, optical finish, and palette rather than inventing a batch-specific look.
