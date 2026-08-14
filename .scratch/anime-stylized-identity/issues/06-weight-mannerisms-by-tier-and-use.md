Status: ready-for-agent

# Weight Mannerisms by Deformation Tier and Use

## What to build

Complete the Character Sheet and application-stage performance boundary, then weight characteristic expressions and mannerisms only where they are useful recognition evidence. Strongly deformed sticker sets may use them heavily; avatars and equal-proportion drawn portraits must continue to prioritize source-supported static structure.

Keep the work inside the existing Identity, Composition, and Styling/Performance owners. A mannerism inferred from one photograph is an assumption, never a fact about the person and never a reason for Identity Review to fail.

## Acceptance criteria

- [ ] Keep Character Sheet generation conservative: preserve the source head angle and expression, use even lighting, avoid an extreme viewpoint, and minimize variables while locking the reusable design.
- [ ] Scope those conservative constraints to the Character Sheet only. Application images retain full access to a new expression, gaze, pose, action, face angle, camera angle, and lighting that fit their locked brief.
- [ ] Weight characteristic expressions and mannerisms as recognition evidence for strongly deformed sticker sets, where static structural channels are reduced and the intended audience is likely to know the person.
- [ ] Keep mannerism weight low for social avatars, equal-proportion anime portraits, and other outputs where static structure remains available or the audience may not know the person.
- [ ] Treat any mannerism inferred from a single photograph as an explicit assumption. Do not turn one frozen expression, gaze, posture, or hand position into a claimed habit or personality trait.
- [ ] Never fail Identity Review because an assumed mannerism is absent, different, or rendered imperfectly. Review continues to use the request-wide Medium Contract's open and transferred identity channels and existing silhouette floor.
- [ ] Keep Character Read as user or story intent. Do not infer personality, profession, relationships, or inner traits from appearance while selecting mannerisms.
- [ ] Preserve application-to-application independence, the Character Sheet fixed root, batch/fallback behavior, and all per-image locks while expressions and performances vary.
- [ ] Update Character Sheet stage guidance in `skills/cast-me/references/composition-director.md`, mannerism and performance ownership in `skills/cast-me/references/styling-performance.md`, and the recognition-versus-review boundary in `skills/cast-me/references/identity-anchor.md`. Update `skills/cast-me/SKILL.md` routing only as needed to load those existing sections.
- [ ] Synchronize `docs/architecture.md` with the Character Sheet/application performance split, tier-and-use weighting, review exclusion, current asset sizes, 39 canonical terms, 8 ADRs, and Golden 1–151 coverage.
- [ ] Do not add motion analysis, a mannerism profile, another gate, a personality model, a review score, or video/animation support.

## Verification

- [ ] Add Golden 150, `Character Sheet conservatism does not constrain applications`, and review it directly against `skills/cast-me/references/composition-director.md` and `skills/cast-me/references/styling-performance.md`. Require source-aligned head angle and expression, even light, and no extreme viewpoint on the sheet, then a downstream application with a different expression, gaze, pose, face angle, camera, and lighting from the same sheet.
- [ ] Add Golden 151, `Mannerism weight follows deformation tier and use`, and review it directly against `skills/cast-me/references/styling-performance.md` and `skills/cast-me/references/identity-anchor.md`. Pair a strongly deformed sticker set with an avatar and equal-proportion portrait; mark a single-image mannerism as assumed, weight it only in the sticker set, forbid personality inference, and require that its absence never causes review failure.
- [ ] Preserve Golden 139–141 tier behavior, Golden 147 batch/fallback behavior, and the existing Character Read ownership scenarios, and review them directly against `skills/cast-me/references/identity-anchor.md`, `skills/cast-me/references/composition-director.md`, and `skills/cast-me/references/styling-performance.md`.

## Blocked by

- [`.scratch/medium-aware-identity-contract/issues/02-regenerate-uneven-stylization.md`](../../medium-aware-identity-contract/issues/02-regenerate-uneven-stylization.md) — the entire feature remains blocked by the completed Medium-Aware Identity Contract required by PRD line 23.
- [`05-produce-consistent-sets-and-multi-angle-batches.md`](05-produce-consistent-sets-and-multi-angle-batches.md) — mannerism weighting must operate on the completed Character Sheet, set, and batch/fallback flows rather than define another production path.
