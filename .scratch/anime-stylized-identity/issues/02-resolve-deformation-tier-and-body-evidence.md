Status: ready-for-agent

# Resolve Deformation Tier and Visible Body Evidence

## What to build

Add Deformation Tier as the user-facing proportion decision for drawn characters. Keep three semantic labels in a stable order while adapting their concrete drawing proportions to the intended use, retain the permanent Custom path, and feed the selected deformation into the existing request-wide Medium Contract.

Make the tier own the Visible Body Evidence gradient and its disclosures. Land the Deformation Tier glossary entry from [`../domain-changes.md`](../domain-changes.md) with this runtime behavior; do not add another ADR or a separate body-shape question.

## Acceptance criteria

- [ ] Present `conservative`, `standard`, and `strong` in that stable semantic order through the existing A/B/C Choice Gate mechanics, plus `D) Custom`. Localize the visible labels while preserving their order and meaning.
- [ ] Adapt the concrete head-to-body proportions behind those labels to the stated use. Show concrete values and visible consequences in the gate, but treat them as drawing conventions rather than measured model thresholds or a universal fixed table.
- [ ] Describe tier differences through visible shape roundness, simplification, feature placement, hand treatment, and body-curvature treatment rather than a ratio alone.
- [ ] Pass only the explicitly selected tier or Custom deformation into the existing Medium Contract. Do not infer deformation from `anime`, `chibi`, a named look, the source image, or a generated result, and do not resolve a second contract for later images in the same request.
- [ ] As deformation increases, weight hairstyle outline, eye shape, distinctive marks, and characteristic wardrobe as transferred recognition channels while preserving their existing Styling ownership.
- [ ] Keep structural cues such as nose bridge and upper-lip thickness open and reviewable when the selected equal-proportion treatment can express them.
- [ ] Resolve Visible Body Evidence as a tier property: equal proportion carries it unchanged, intermediate proportions carry it in simplified form, the second-shortest proportion offers chest/waist/hip curvature explicitly with its more-mature read disclosed, and the shortest proportion discloses before generation that it cannot carry the shown figure.
- [ ] When the selected tier would drop body evidence that the source visibly supports, disclose that consequence before generation. Offer a less-deformed tier when the user wants both strong deformation and that figure; do not silently add the figure to a proportion that cannot carry it.
- [ ] Do not combine emphasized adult body characteristics with a proportion that reads as a child. Resolve the conflict by moving the tier rather than silently moderating the body request.
- [ ] Wherever body evidence remains expressible, keep the existing neutral prompt contract: concrete relationships, including supported chest volume with shoulders and upper torso, without measurements, cup sizes, or erotic emphasis.
- [ ] Treat the accepted younger read of an explicitly chosen strong deformation as locked intent, while unexplained age drift outside that contract still fails.
- [ ] Update `skills/cast-me/SKILL.md`, `skills/cast-me/references/identity-anchor.md`, `skills/cast-me/references/styling-performance.md`, and the non-photographic prompt guidance in `skills/cast-me/references/composition-director.md` through their existing ownership boundaries.
- [ ] Add `Deformation Tier` to `CONTEXT.md` in the same change. Synchronize `docs/architecture.md` with the tier-to-Medium-Contract flow, body-evidence gradient, current asset sizes, 39 canonical terms, 8 ADRs, and Golden 1–141 coverage.
- [ ] Do not add stylization intensity, style axes, batch production, mannerism weighting, a separate body gate, a new module, or a persistent proportion profile.

## Verification

- [ ] Add Golden 139, `Deformation Tier keeps stable labels across uses`, and review it directly against `skills/cast-me/references/identity-anchor.md`. Pair two different uses, require the same three semantic labels in the same order plus Custom, and require use-appropriate concrete proportions and visible consequences without asserting one universal table.
- [ ] Add Golden 140, `Deformation Tier resolves identity channels and body evidence`, and review it directly against `skills/cast-me/references/identity-anchor.md` and `skills/cast-me/references/styling-performance.md`. Cover equal, intermediate, second-shortest, and shortest proportion families; assert open structural cues, transferred recognition channels, the complete body-evidence gradient, pre-generation loss disclosure, and no separate body question.
- [ ] Add Golden 141, `Child-reading proportions cannot carry adult body emphasis`, and review it directly against `skills/cast-me/references/identity-anchor.md` and `skills/cast-me/references/styling-performance.md`. Pair an accepted younger read, the explicit more-mature consequence at the second-shortest proportion, a shortest-tier preservation conflict resolved by moving tiers, and neutral body language without measurements or erotic emphasis.
- [ ] Preserve Golden 122–126 Medium Contract boundaries and Golden 137–138 Character Sheet behavior, and review them directly against `skills/cast-me/references/identity-anchor.md` and `skills/cast-me/references/composition-director.md`.

## Blocked by

- [`.scratch/medium-aware-identity-contract/issues/02-regenerate-uneven-stylization.md`](../../medium-aware-identity-contract/issues/02-regenerate-uneven-stylization.md) — the entire feature remains blocked by the completed Medium-Aware Identity Contract required by PRD line 23.
- [`01-anchor-two-applications-to-one-character-sheet.md`](01-anchor-two-applications-to-one-character-sheet.md) — the tier must resolve one contract shared by the Character Sheet and both downstream applications.
