Status: ready-for-agent

# Keep Both Hands Through a Drawn Action

## What to build

Make a two-handed drawn action deliver exactly two hands of opposite handedness. A field run produced two right hands and one left: the count failed because a Drawn Character has no motion vocabulary and the model supplied a repeated-limb convention for a fast wave, and the handedness failed because the pose chain writes hands as one link and the negative vocabulary has no term for mirroring.

Carry the fix mainly through positive per-hand direction. Add a Drawn Motion Convention as an ordinary visible decision so repeated limbs become a path the user chooses rather than one the model assumes.

## Acceptance criteria

- [ ] Split the pose chain's single `hands, props, and follow-through` link at `styling-performance.md:135` into left and right, each carrying position, orientation relative to the body, and thumb side.
- [ ] Assert the count of two positively in pose geometry rather than only as a prohibition, so a symmetric gesture cannot resolve into one hand mirrored twice.
- [ ] Add one chirality entry to the hands-and-body negative line at `identity-anchor.md:226` and to the post-generation check at `identity-anchor.md:297`, covering duplicated handedness rather than restating extra fingers, fused fingers, or extra limbs.
- [ ] Select that entry into the adaptive three-to-eight negative budget only when both hands are visible and performing. Do not add it universally.
- [ ] Preserve the finger-articulation avoidance at `styling-performance.md:147`. It is scoped to articulation, which does not carry handedness; keep the thumb side as the minimum chirality anchor at any simplification level, including the strongest deformation.
- [ ] Add Drawn Motion Convention as an ordinary production decision covering speed lines, afterimage, repeated limb positions, and a held freeze, resolved through the existing Choice Gate when it is production-critical and unresolved.
- [ ] Keep it distinct from the photographic motion treatment at `composition-director.md:205`, and do not let it resolve Deformation Tier, stylization intensity, or any style axis.
- [ ] Make an explicitly selected repeated-limb convention the single carve-out from the two-hand count rule. No other path may add a hand.
- [ ] Never silently substitute a different action, a simpler gesture, or a safer crop to avoid the risk. The locked action stands.
- [ ] Update `skills/cast-me/references/styling-performance.md`, `skills/cast-me/references/identity-anchor.md`, and `skills/cast-me/references/composition-director.md` without creating another reference file.
- [ ] Synchronize `docs/architecture.md` with the per-hand pose links, the chirality check, Drawn Motion Convention, current asset sizes, 43 canonical terms, 11 ADRs, and Golden 1–157 coverage.
- [ ] Do not add a general anatomy checklist, a limb counter, or any score.

## Verification

- [ ] Add Golden 157, `Both hands survive a drawn action`, and review it directly against `skills/cast-me/references/styling-performance.md` and `skills/cast-me/references/identity-anchor.md`. Use a symmetric two-handed action at strong deformation. Require per-hand position, orientation, and thumb side in the production prompt; a count of two; the chirality entry present in both the negatives and the review; and repeated limbs appearing only under an explicitly selected motion convention.
- [ ] Preserve Golden 11, and review it directly against `skills/cast-me/references/styling-performance.md`. The per-hand split extends its chain without weakening its rule against irrelevant chain nodes, so a hand outside the frame must still not be written.
- [ ] Preserve Golden 12, and review it against the same file. Repairing coordination must not normalize a locked strong perspective or turn a per-hand correction into a whole-image rebuild.

## Blocked by

- None — can start immediately.
