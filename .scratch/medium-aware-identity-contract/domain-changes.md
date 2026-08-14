Status: ready-for-agent

# Domain Changes for the Medium-Aware Identity Contract

These are the glossary and decision-record changes that `PRD.md` in this directory depends on. They are staged here rather than applied to `CONTEXT.md` and `docs/adr/` directly, because `docs/architecture.md` requires canonical terms to stay consistent with runtime behavior and treats any contradiction between them as drift to be fixed explicitly. The runtime owner modules do not change until the PRD is implemented, so these land as part of that implementation rather than ahead of it.

The change-impact matrix in `docs/architecture.md` lists canonical terms and architecture decisions as requiring updates to every runtime usage, that document, and the golden conversations. All three are covered by the PRD.

## ADR

The ADR test is met on all three counts. It is hard to reverse, because Identity Review's completion rule depends on the resolved channel set once this lands. It is surprising without context, because a future reader will find a medium precondition attached to an anatomy constraint and wonder why the constraint is not simply unconditional. And it is a real trade-off, because relaxing the constraints and exempting drawn media were both available and both rejected.

New file `docs/adr/0007-resolve-identity-constraints-against-selected-medium.md`:

```md
# Resolve identity constraints against the selected medium

Identity constraints resolve against the request's Medium Contract instead of holding as medium-independent constants. Protected Identity Cues resolve per request into channels the medium draws as the person's own quantity, channels whose shape the medium's convention governs but which still carry recognition, and channels it has closed. Per-cue drift comparison against the Primary Identity Anchor applies to the first group; the second is judged as recognition and weighted up; the third is excluded from drift judgment and disclosed before generation. Deformation, apparent age, or surface treatment that the Medium Contract explains is locked intent rather than a defect.

Completion switches at one boundary only: when no structural cue is left in the first group. Until then the existing rule holds unchanged and recognizability alone does not pass. Past it, recognition through the second group decides completion, because nothing else remains to compare, and it carries a floor — the figure must stay identifiable in silhouette at thumbnail size.

CastMe does not weaken the constraints for drawn output and does not exempt non-photographic media as a class. Weakening them would degrade photographic work, and a blanket exemption would accept unexplained deformation, age change, and identity loss in exactly the medium where the fewest structural cues remain to catch them. Adding a medium dimension keeps every constraint at full strength while giving each one an explanation test that a drawing can satisfy.
```

## Glossary

### New term: Medium Contract

Insert after `Protected Identity Cue`, which it modifies:

```md
**Medium Contract**:
The identity channels the selected medium and deformation level can actually express, resolved from the direction already locked rather than asked as a separate choice. It resolves each Protected Identity Cue to one of three states: open, drawn as the person's own quantity and therefore comparable against the Primary Identity Anchor for drift; transferred, shaped by the medium's convention yet still carrying recognition in place of channels the medium has closed, and weighted up accordingly; and closed, not expressible in this medium, excluded from drift judgment, and disclosed before generation.
_Avoid_: Style preset, medium label, drawn-media exemption
```

### New term: Uneven Stylization

Insert after `Structural Scale Failure`, the other named result state it parallels:

```md
**Uneven Stylization**:
A result state in which some features are fully converted to the selected medium while others remain photographic, such as drawn eyes and hair over photographic skin and lighting. It fails completion independently of likeness, so a result that still reads clearly as the person fails on this ground alone.
_Avoid_: Style inconsistency, half-rendered image
```

### Modified term: Protected Identity Cue

The current definition is medium-independent and stops being accurate once the catalog resolves per request. Two sentences are inserted; the rest is unchanged. The second one fixes which cues the structural class contains, because Identity Review's completion rule now turns on that class and a class that resolved per request would let a medium classify its way out of the rule.

```md
**Protected Identity Cue**:
A visible structural, surface, or external characteristic whose replacement or occlusion could materially reduce recognizability, such as facial relationships, skin tone, age impression, hairline, or a distinctive mark. Which characteristics qualify resolves against the request's Medium Contract rather than a fixed catalog, so a characteristic the selected medium cannot express is not protected for that request, while one that carries recognition in its place is weighted more heavily. A cue is structural when it is a bone-structure or facial-geometry relationship; that classification is fixed and medium-independent, and only a cue's state under the Medium Contract varies by request. Risk depends on changing these cues, not on whether styling is labeled light or heavy; accepting a change to one cue does not waive unrelated identity cues.
_Avoid_: Makeup intensity, beauty feature
```

### Modified term: Identity Review

The completion rule changes in two places. The recognizability clause gains the condition under which it holds, and the relaxed criterion that applies past that condition is recorded together with its floor, so that the glossary does not state a relaxation without its bound.

The condition is `any`, not `most`. While the contract leaves even one structural cue open, review still has something it can compare against the anchor, and the existing rule holds unmodified. Only when it leaves none open does recognition through the transferred cues become the criterion, which is what makes the accompanying justification — that nothing else remains to judge — literally rather than approximately true. Both the switch and the floor read the channel record resolved before generation, so silhouette readability, which is judged after generation, cannot feed back into whether the criterion was relaxed.

Current wording: `recognizability alone does not pass`.

Replacement wording: `recognizability alone does not pass while the request's Medium Contract leaves any structural Protected Identity Cue open. Where it leaves none open, recognition through the transferred cues decides completion, and the figure must stay identifiable in silhouette at thumbnail size.`

## Baseline counts

`docs/architecture.md` records asset sizes that these changes invalidate. Update them when the changes land rather than now:

- `CONTEXT.md` moves from 35 canonical terms to 37; recount the word total, which currently reads 1,543 and grows by roughly one hundred and fifty words.
- `docs/adr/` moves from 6 ADRs to 7.
- `golden-conversations.md` currently records 121 scenarios; recount after the PRD's scenarios are added.
