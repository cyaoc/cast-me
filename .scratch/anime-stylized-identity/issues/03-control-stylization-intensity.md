Status: ready-for-agent

# Control Stylization Intensity Independently

## What to build

Make stylization intensity an explicit drawn-output decision independent of Deformation Tier and the selected rendering look. Keep the change inside existing Creative Direction, finish, prompt, and Identity Review seams; do not invent canonical intensity tiers, a new module, or another workflow stage.

The result must avoid both failure ends: a photograph with a drawing filter and a highly stylized default anime face that no longer preserves the person.

## Acceptance criteria

- [ ] Resolve one explicit stylization-intensity decision before drawn generation and record it separately from Deformation Tier, named look, surface coloring, and optical finish.
- [ ] When intensity remains production-critical and unresolved, use the existing Choice Gate format with visible outcomes adapted to the current brief. Do not create fixed global labels or a preset catalog the PRD does not define.
- [ ] Keep a low-intensity result an actual drawing rather than a filtered photograph. Convert skin, hair, eyes, wardrobe, lighting, shading, and background coherently into the selected medium.
- [ ] Keep a high-intensity result tied to the Primary Identity Anchor and the Medium Contract's open and transferred channels rather than substituting a generic anime face.
- [ ] Treat both ends as failures of the selected intensity or its execution, not as permission to silently change the Deformation Tier or rendering look.
- [ ] Raise intensity progressively in production direction instead of instructing the model to maximize it in one step.
- [ ] Do not ask to preserve every pore or other photographic surface detail that conflicts with the selected drawing medium.
- [ ] Preserve Uneven Stylization as the separate failure where only some visible surfaces convert. A uniformly photographic filter and a uniformly generic drawn face must not be misclassified as that mixed-surface state.
- [ ] Update the existing drawn-output and finish behavior in `skills/cast-me/SKILL.md`, `skills/cast-me/references/composition-director.md`, and `skills/cast-me/references/identity-anchor.md` without creating another reference file.
- [ ] Synchronize `docs/architecture.md` with the independent intensity decision, its two failure ends, current asset sizes, 39 canonical terms, 8 ADRs, and Golden 1–142 coverage.
- [ ] Do not add the six style axes, named-look vocabulary, batch behavior, mannerism weighting, a score, or a model-specific intensity threshold.

## Verification

- [ ] Add Golden 142, `Stylization intensity has two independent failure ends`, and review it directly against `skills/cast-me/references/composition-director.md` and `skills/cast-me/references/identity-anchor.md`. Pair a filtered-photograph result with a generic-anime-face result, require coherent conversion across every visible surface, progressive intensity direction, preserved tier and look, and the correct distinction from Uneven Stylization.
- [ ] Preserve Golden 124, `Surface treatment follows the selected medium`, Golden 127, `Uneven stylization regenerates instead of editing`, and Golden 139–141 tier behavior, and review them directly against `skills/cast-me/references/identity-anchor.md` and `skills/cast-me/references/composition-director.md`.

## Blocked by

- [`.scratch/medium-aware-identity-contract/issues/02-regenerate-uneven-stylization.md`](../../medium-aware-identity-contract/issues/02-regenerate-uneven-stylization.md) — the entire feature remains blocked by the completed Medium-Aware Identity Contract required by PRD line 23.
- [`02-resolve-deformation-tier-and-body-evidence.md`](02-resolve-deformation-tier-and-body-evidence.md) — intensity must remain demonstrably independent of the already-resolved deformation choice.
