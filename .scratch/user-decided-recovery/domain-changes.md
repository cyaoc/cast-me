Status: ready-for-agent

# Domain Changes for User-Decided Recovery

These are the glossary and decision-record changes that `PRD.md` in this directory depends on. They were staged here rather than applied to `CONTEXT.md` and `docs/adr/` directly, because `docs/architecture.md` requires canonical terms to stay consistent with runtime behavior and treats any contradiction between them as drift to be fixed explicitly. The runtime owner modules did not change until the PRD was implemented, so these landed as part of that implementation rather than ahead of it.

The change-impact matrix in `docs/architecture.md` lists canonical terms and architecture decisions as requiring updates to every runtime usage, that document, and the golden conversations. All three are covered by the PRD.

`PRD.md` is still `Status: proposal` and must be corrected in four places before any of this lands. Its open batch question at `:89` is resolved below and is no longer open. Its `:79-87` conflict inventory overstates the damage to `identity-preservation-reliability` and understates the record burden of `edit-chain-depth` story 29; the classification below replaces it. Its `:87` reading of ADR 0008 describes the constraint as becoming total, when the thing constrained ceases to exist. And its `:15` premise that a one-sentence report and a silent regeneration are equivalent to the user is unevidenced and is dropped in favor of the authority split recorded in the ADR.

## ADR

The ADR test is met on all three counts. It is hard to reverse, because removing the initiative dissolves the per-result versus per-request scope question rather than answering it, and restoring the initiative later would re-open a question that four commits already failed to settle. It is surprising without context, because a future reader will find a skill that detects an unambiguous quality failure and deliberately declines to fix it, while three landed PRDs still on disk ask for exactly that repair, and will read it as a regression. And it is a real trade-off, because keeping the bounded automatic correction, capping corrections per request rather than per result, and reporting only the shared-cause case were all available and all rejected for stated reasons.

New file `docs/adr/0009-let-the-user-decide-whether-to-spend-a-recovery.md`:

```md
# Let the user decide whether to spend a recovery

CastMe no longer repairs its own visibly failed results. On an unambiguous required-quality failure it delivers a Recovery Offer — the concrete defect, the recovery operation the existing contracts select for that result and why, and the statement that it has not been performed — and never claims completion. Two authorities are separated rather than moved together. Whether a result failed stays with Identity Review, which reads the result against the Primary Identity Anchor and is not decided by the user's wording. Whether to spend a generation on the failure moves to the user, who bears that cost and that wait.

The rule being removed had a truthfulness rationale, not a repair rationale: the skill must not hand over an obviously broken image and call it done. A report satisfies that requirement as completely as a repair does, and no document ever argued for acting rather than asking. The choice was expensive to leave unexamined. Deciding what the skill may repair on its own initiative produced a per-result versus per-request scope that the specifications never settled and that four commits adjudicated in place, with the spec amended afterwards to match the implementation. Every contract deciding *how* a repair is performed survives unchanged and applies to the user-requested path: regeneration from the complete fixed root is the default, surgical edit remains the proportionate exception for a freshly generated ordinary result, Uneven Stylization is regeneration-only, and a locked produced artifact is never edited.

A multi-item request produces one Recovery Offer for the whole request, in two branches. When several items fail on the same defect, the cause is attributed to the Character Sheet or locked brief and reported once, together with the operation that cause selects; the attribution is the existing rule and the operation is what the offer adds, because the existing flow stops at attribution and never selects one. Naming that operation exposes a cost the old flow never had to state: repairing a shared cause regenerates the Character Sheet, and a regenerated Sheet is a different Sheet, so rebuilding only the failing items splits the set across two versions of the character while rebuilding every item costs one generation per item. This branch alone therefore ends in the existing Choice Gate, because the trade between them is the same cost-against-quality judgment the decision hands to the user. When they do not, the offer carries one entry per failing item, naming that item's defect and selected operation, and a single user instruction may accept all of them, some of them, or none. The second branch exists because it is the case the evidence actually describes: the only field report on record covers items needing individual redo out of one planned batch, which is the shape shared-cause attribution does not cover. Reporting only the shared case would have left the common failure mode with no answer but item-by-item interrogation.

This supersedes `.scratch/edit-chain-depth/PRD.md` user story 29, which asked for the bounded single automatic correction to be preserved rather than relaxed, on a mechanical rationale about edit-chain depth. Removing the correction satisfies that rationale maximally, because zero automatic corrections is the shortest possible chain, while contradicting the story's literal ask. The contradiction is recorded here because it is otherwise unreadable as anything but a reversal.
```

### Revision to `docs/adr/0008`

ADR 0008 is revised in place rather than superseded. Its subject is the two-stage Character Sheet flow, which survives entirely, as does its round-trip reasoning — that reasoning now governs the user-requested path through the freshness test the PRD keeps. Only two half-sentences lose their subject. In-place revision is this repository's established practice: `0007` was revised three times after landing and `0008` once, and no ADR has ever been superseded or carried a `Status` line.

Two deletions, both in the second paragraph. Nothing else in the file changes.

Delete `, and the automatic correction never edits one on its own initiative` from `Failing applications are therefore regenerated from the sheet and the anchor rather than surgically edited, and the automatic correction never edits one on its own initiative.` The remaining sentence states the routing completely and does not presuppose an executor.

Delete `; only the skill's own initiative over that application is constrained` from `A user who asks for a local fix to an application anyway still gets one; only the skill's own initiative over that application is constrained.` The surviving clause is not merely preserved but becomes more load-bearing, because a user request is now the only path by which an application is repaired at all.

Do not replace the second deletion with a statement that the constraint on initiative has become total. There is no initiative left to constrain, so the sentence would name an empty subject and invite a future reader to ask what is being constrained.

## Glossary

### New term: Recovery Offer

Insert after `Identity Review`, whose failure branch produces it.

The vocabulary names result states such as `Structural Scale Failure` and `Uneven Stylization`, and decision shapes such as `Choice Gate`, but has never named what the skill delivers on failure, because until now that was a behavior rather than an artifact. This change inverts that: the behavior is removed and the artifact is what remains. It becomes load-bearing across the converted golden scenarios, the recovery contracts in `skills/cast-me/references/identity-anchor.md`, the routing in `skills/cast-me/SKILL.md`, and a new branch in the `F8` flow, so leaving it unnamed would let each of those invent its own wording — the drift `docs/architecture.md` requires be fixed explicitly.

The `_Avoid_` line fences it off from `Choice Gate` in particular. The two are adjacent and easy to collapse, and the PRD specifically rules that this is not a gate, because it asks for a decision the user may also ignore.

```md
**Recovery Offer**:
What CastMe delivers in place of a repair when a visible result unambiguously fails required quality: the concrete defect, the recovery operation the existing contracts select for that result and why, and the statement that it has not been performed. It never accompanies a completion claim. A multi-item request receives one offer for the whole request — a single shared cause with the operation it selects where several items inherit one, otherwise one entry per failing item — and a single user instruction may accept all of it, part of it, or none.
_Avoid_: Choice Gate, auto-repair, retry prompt
```

### Unchanged: Identity Review

Recorded so that a later reader does not treat it as an omission. The entry's failure clause reads `On failure, result reliability decides only whether one coherent local correction may reuse the result or identity-wide regeneration is required.` That describes operation selection and names no executor, so it is accurate before and after this change. No canonical term names the automatic correction, which is why the removal costs the glossary nothing and only adds.

## Spec pointers

The supersession and rewrite statements land as pointer lines under the affected stories. The story text itself is not edited, so the original ask stays readable. The `Status:` line is not used for this: `docs/agents/triage-labels.md` has no `superseded` value, and both affected PRDs still read `ready-for-agent` despite having landed, so that line is already unmaintained as a lifecycle marker in this repository.

| Story | Disposition | Pointer |
| --- | --- | --- |
| `identity-preservation-reliability` 34 | Rewritten | Only the automatic regeneration reverses; the focused-reattachment path and the whole rationale survive verbatim |
| `identity-preservation-reliability` 35 | Rewritten | Identity Review still runs once after a correction; the trigger moves to the user-requested path |
| `identity-preservation-reliability` 37 | Void | The bound of one has no subject; the story's own rationale, generation cost and wait, is satisfied more strongly |
| `edit-chain-depth` 7 | Rewritten | The routing rule survives on the user-requested path; its rationale, that the skill never lengthens the chain on its own initiative, becomes unconditional |
| `edit-chain-depth` 8 | Void | Same shape as story 37. This is the story amended after the fact to add `on the same result`, and that scope question disappears with it |
| `edit-chain-depth` 29 | **Superseded** by ADR 0009 | The only true supersession in the set; see the ADR's fourth paragraph |
| `anime-stylized-identity` `:31` | Rewritten | First clause survives; delete `and the bounded automatic correction never edits one on its own initiative` |
| `anime-stylized-identity` `:133` | Rewritten | Routing survives; the executor changes |
| `anime-stylized-identity` `:180` | Rewritten | The scenario asserts the operation was named rather than performed, and must gain a user-acceptance turn |

`identity-preservation-reliability` is not superseded as a whole. Three of its stories are affected and the rest — combined identity-risk checking, recommendation inheritance, accepted-risk scoping — are untouched. Marking the whole document superseded would discard them.

The `:180` note is not cosmetic. The generic contract does keep execution coverage without Golden 138: case A of Golden 129 already asserts regeneration from the complete fixed root including the locked produced artifact and excluding the failed result, and Golden 130 asserts regenerating such an artifact rather than editing it, both on the user-requested path. What only Golden 138 cases A and B assert is that same contract with the two-stage drawn flow named concretely — the Character Sheet as the artifact and the failing application as the result. Converting them to an offer-only assertion would leave that naming asserted nowhere under execution, so each converted case needs a user-acceptance turn. Case E, which exists only to bound automatic attempts, loses its subject entirely and must be removed or repurposed rather than converted.

## Baseline counts

`docs/architecture.md` records asset sizes that these changes invalidate. Update them when the changes land rather than now:

- `CONTEXT.md` moves from 40 canonical terms to 41; recount the word total, which currently reads 1,977 and grows by roughly one hundred words.
- `docs/adr/` moves from 8 ADRs to 9.
- `golden-conversations.md` now grows from 153 to 154 scenarios because ticket 02 adds the unrelated-batch-failure case after the original rewrites. Recount after that scenario lands.
