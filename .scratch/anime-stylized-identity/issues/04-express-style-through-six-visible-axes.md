Status: ready-for-agent

# Express Drawn Style Through Six Visible Axes

## What to build

Replace opaque anime-style labels with six visible, independently controllable axes: line, surface coloring, colour logic, eye rendering, texture, and background. Keep optical finish independently composable with surface coloring, and offer recognizable named looks only as starting points defined by visible features.

Build this through the existing Creative Direction, output-recipe, reference-transfer, prompt, and refresh seams. Do not add a style browser, preset catalog, new reference module, or quality ranking.

## Acceptance criteria

- [ ] Make line, surface coloring, colour logic, eye rendering, texture, and background separately expressible and independently refreshable within their existing owning creative area.
- [ ] Give the line axis concrete visible controls: contour/boundary/detail weight hierarchy, amount of weight variation, tapered or untapered ends, line colour, and full/minimal-coloured/no-line treatment.
- [ ] Give surface coloring a concrete shading-layer count and boundary treatment. Keep it separate from colour logic, which owns shared palette slots, consistency and distinguishability, scene-wide shifts, and overridable shadow-colour derivation defaults.
- [ ] Keep optical finish separate from surface coloring. Light diffusion, bloom, lens-flare shape, bokeh shape, and eye-highlight strength may combine with flat or graduated coloring rather than defining the coloring technique.
- [ ] Give eye rendering visible controls for highlight count and placement, iris gradient direction and optional radial texture, lash colour, and iris-to-sclera boundary treatment.
- [ ] Give texture concrete screentone descriptions for frequency, density, dot shape, and angle without pretending the active surface exposes numeric screen controls. Keep background treatment independent of character rendering.
- [ ] Support flat cel, semi-gradient, thick-painted, watercolour, lineless, monochrome screentone, and toon-shaded three-dimensional looks as non-exclusive starting vocabulary, each defined by its visible features. Do not offer grisaille or an unverified coined term as a finished look.
- [ ] When the user asks only for `anime`, use the existing A/B/C/D Choice Gate to offer three relevant visible-feature starting points plus Custom. Use refresh for other valid directions; do not silently choose one look or build a nested seven-item catalog.
- [ ] Express retro or modern treatment through character palette and optical finish without silently changing the painting technique. Restrict any reduced period palette to the character layer rather than the whole image.
- [ ] Translate an artist, school, unfamiliar, or unsupported style name into concrete visible anchors before production. Do not pass an artist or school name into the production prompt, and do not let an unfamiliar label collapse silently into a default look.
- [ ] Keep another person's artwork or photo reference limited to rendering treatment. It never supplies face identity, age impression, body identity, or a competing person anchor.
- [ ] When dense high-frequency micro-structure is selected, disclose the current model-artifact risk as time-stamped information. Do not describe it as permanent, rank the named looks, or claim which look will produce a better result.
- [ ] Update `skills/cast-me/SKILL.md`, `skills/cast-me/references/composition-director.md`, and the style-reference boundary in `skills/cast-me/references/identity-anchor.md` without creating another owner.
- [ ] Synchronize `docs/architecture.md` with the six axes, optical-finish boundary, named starting vocabulary, reference roles, current asset sizes, 39 canonical terms, 8 ADRs, and Golden 1–146 coverage.
- [ ] Do not add batch production, set delivery, mannerism weighting, a persistent style profile, per-look reachability claims, or numeric quality scores.

## Verification

- [ ] Add Golden 143, `Six visible style axes remain independently controllable`, and review it directly against `skills/cast-me/references/composition-director.md`. Assert all six axes, shading-layer ownership, screentone placement, line and eye parameters, and a background-only change that leaves character rendering unchanged.
- [ ] Add Golden 144, `An unqualified anime request receives visible-feature starting points`, and review it directly against `skills/cast-me/references/composition-director.md`. Require three relevant A/B/C starting points plus Custom, visible definitions rather than labels alone, access to the supported look vocabulary through refresh, no silent default, no nested catalog, and no quality ranking.
- [ ] Add Golden 145, `Surface coloring, colour logic, and optical finish stay orthogonal`, and review it directly against `skills/cast-me/references/composition-director.md`. Pair flat cel with heavy diffusion and with no diffusion, add a period treatment that changes palette and finish without changing technique, and require shared character-colour logic independently of shading-layer count.
- [ ] Add Golden 146, `Style names and references cannot replace identity`, and review it directly against `skills/cast-me/references/composition-director.md` and `skills/cast-me/references/identity-anchor.md`. Cover an artist name, an unfamiliar style term, another person's style reference, dense high-frequency texture, time-stamped artifact disclosure, and the absence of per-look reachability or quality claims.
- [ ] Preserve Golden 142 intensity behavior so no axis or named look silently resolves intensity, and review it directly against `skills/cast-me/references/composition-director.md`.

## Blocked by

- [`.scratch/medium-aware-identity-contract/issues/02-regenerate-uneven-stylization.md`](../../medium-aware-identity-contract/issues/02-regenerate-uneven-stylization.md) — the entire feature remains blocked by the completed Medium-Aware Identity Contract required by PRD line 23.
- [`03-control-stylization-intensity.md`](03-control-stylization-intensity.md) — the axes and named looks must not absorb the independent intensity decision.
