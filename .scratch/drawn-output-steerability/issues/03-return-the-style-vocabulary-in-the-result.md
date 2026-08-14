Status: ready-for-agent

# Return the Style Vocabulary in the Result

## What to build

Deliver a Style Readout with the result instead of demanding rendering vocabulary in the brief. A beginner can recognize a good image but cannot name line weight or shading-layer count before seeing one, so today the whole cost of style selection falls on the person least able to pay it.

The readout reports the rendering decisions this result was given, in the visible vocabulary the user can then reopen one axis at a time. It is a disclosure carried by the result, never a gate.

## Acceptance criteria

- [ ] Deliver a Style Readout with the first result of each style state: the locked six axis values, Deformation Tier, and stylization intensity, in visible language rather than production labels.
- [ ] Make the style state its unit. Suppress the readout while the same combination of axes, tier, and intensity holds, so a set carries one readout rather than one per item.
- [ ] After a single-axis Scoped Option Refresh, report only the axis that moved.
- [ ] Report the locked decision record, never an inspection of the image. The readout must carry no completion, likeness, or quality claim of its own.
- [ ] Leave Identity Review and its Uneven Stylization check as the sole authority on whether the result matches those decisions. The readout must not become a second, weaker verdict.
- [ ] Give photographic output the same mechanism with different content: only the two or three finish controls that materially changed the look. Do not use the six drawn axes there and do not reproduce a full Direction Signature.
- [ ] Deliver it as part of the result, not as a Choice Gate, not as an extra turn, and not as process narration about how the image was made.
- [ ] Never pass an artist or school name into the readout, matching the existing prohibition on passing one into the production prompt.
- [ ] Keep the readout's vocabulary identical to the axis names the existing Scoped Option Refresh accepts, so a user can quote it back and be understood.
- [ ] Update `skills/cast-me/SKILL.md` and `skills/cast-me/references/composition-director.md` without creating another reference file.
- [ ] Synchronize `docs/architecture.md` with the Style Readout, its style-state unit, its separation from Identity Review, current asset sizes, 43 canonical terms, 11 ADRs, and Golden 1–158 coverage.
- [ ] Do not add a style-reference-image path, a low-quality style probe, a preview stage, or a quality question. ADR 0011 records why each was rejected.
- [ ] Do not restate, re-resolve, or reorder the six axes, Deformation Tier, or stylization intensity. The readout reads their results.

## Verification

- [ ] Add Golden 158, `A Style Readout accompanies each style state`, and review it directly against `skills/cast-me/SKILL.md` and `skills/cast-me/references/composition-director.md`. Cover a first result, a six-item set, and a single-axis refresh. Require one readout for the set, changed-axis-only reporting after the refresh, locked values rather than observed ones, and no completion or quality claim.
- [ ] Preserve Golden 143 and Golden 144, and review them directly against `skills/cast-me/references/composition-director.md`. The readout reports their locked values without changing how axes are resolved or how the starting-look gate behaves.
- [ ] Preserve Golden 147 and Golden 149, and review them against `skills/cast-me/references/identity-anchor.md` and `skills/cast-me/references/composition-director.md`. Set delivery keeps its existing boundaries, and the one-readout-per-set rule must not weaken any of them.
- [ ] Preserve Golden 142, and review it against the same files. Stylization intensity keeps both failure ends, and reporting the locked intensity must not be mistaken for verifying it.

## Blocked by

- None — can start immediately.
