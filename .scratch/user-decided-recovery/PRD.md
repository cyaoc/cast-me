Status: ready-for-agent

# Recovery decided by the user, not by the skill

Written so the cost of the change could be read before it was approved. Tickets 01 through 03 in `issues/` have since landed it. The term and decision-record conclusions it depends on were staged in `domain-changes.md` in this directory and now live in `CONTEXT.md` and `docs/adr/`.

## Problem Statement

CastMe repairs its own visibly failed results before showing them. `skills/cast-me/references/identity-anchor.md:299` performs exactly one automatic correction operation for each visible result under review, then runs Identity Review once more, then stops.

The reason on record is narrow. `.scratch/identity-preservation-reliability/PRD.md:23` says to perform the regeneration `automatically once before claiming completion`. The rule exists so the skill cannot hand over an obviously broken image and call it done. That is a truthfulness requirement, not a repair requirement, and reporting the defect satisfies it exactly as well as repairing it does.

No document argues for repairing rather than reporting. Four PRDs, two research notes, and eight ADRs were searched. The bound has a rationale — generation cost and edit-chain depth. The trigger has a rationale — do not claim completion over a visible failure. The choice to act rather than ask has never been written down.

That unexamined choice is expensive. Deciding what the skill may repair on its own initiative, and how often, has produced: a per-result versus per-request scope question the specifications never settled, adjudicated in place across `ec7f666`, `86a6577`, `69dbbbb`, and `dd48c64`, with the spec amended afterwards to match the implementation; a freshly-generated provenance test; a fixed-root regeneration contract; a shared-defect attribution guard; and sixteen coverage rows under `F8` in `docs/architecture.md`. `.scratch/cross-spec-defect-provenance/research.md:90` records the pattern: `faced with a question the specs left open, it adjudicated in place, flip-flopped once, and then edited the PRD so the spec ratified the implementation`.

Two authorities are in play, and the specifications only ever settled one. `identity-anchor.md:245` states that a likeness complaint `triggers this review but does not determine its outcome`, and `SKILL.md:214` makes the user's report a first-class trigger. Read together they fix the verdict with the skill: Identity Review compares the result against the Anchor, and the user's wording does not classify it. This proposal leaves that untouched. What it moves is the separate question of whether to spend a generation on that verdict, which no document ever assigned. The closest thing to an assignment on record is the rationale of `.scratch/identity-preservation-reliability/PRD.md` story 37, `As a user paying generation cost or waiting for results`, which grants that the user bears the cost while leaving the skill the decision to incur it.

The skill is already forbidden from acting when the call is close: `identity-anchor.md:301` blocks automatic correction when `the review is ambiguous`. The automatic path therefore only ever covers unambiguous, inspectable defects — the band where the defect can be stated concretely. It does not follow that a report and a repair are equivalent to the user. The repair delivers a corrected image; the report delivers a description and a round trip. The claim here is narrower: the trade between them, latency and interaction against cost and control, belongs to whoever pays for it.

## Solution

Keep Identity Review, the completion bar, and every recovery contract that decides *how* a repair must be performed. Remove only the skill's initiative to perform one.

On an unambiguous required-quality failure, the skill delivers a Recovery Offer: the concrete defect, the recovery operation the existing contracts select for that result and why, and the statement that it has not been performed. It then stops, and never claims completion. The user decides whether to spend the generation.

A multi-item request receives one Recovery Offer for the whole request, in two branches. Where several items fail on the same defect, the cause is attributed to the Character Sheet or locked brief and reported once, together with the operation that cause selects — the attribution is the existing rule, the operation is what the offer adds to it. Where they do not, the offer carries one entry per failing item naming that item's defect and selected operation, and one instruction may accept all of them, some of them, or none.

Every existing recovery rule survives unchanged in content and changes only in mood: from what the skill does, to what the skill offers. Surgical edit remains the proportionate exception for a freshly generated ordinary result. Regeneration from the complete fixed root remains the path for everything else. Uneven Stylization remains regeneration-only. A Character Sheet is still never edited. What disappears is the question of how many repairs the skill may initiate, because it initiates none.

## User Stories

1. As a user whose result has a visible unambiguous defect, I want to be told what is wrong before anything else is generated, so that I decide whether the fix is worth the wait and the cost.
2. As a user, I want the skill to tell me which recovery operation it would use and why, so that I can accept it, ask for a different one, or accept the result as is.
3. As a user who is happy with a result the skill considers defective, I do not want it regenerated, so that my judgement is not overridden by a rule.
4. As a user requesting a twelve-item set, I do not want up to twelve regenerations started on the skill's own initiative, so that cost stays under my control.
5. As a user, I want a shared defect across several items attributed to its common cause in one report, so that I am not told the same thing twelve times. I also want to be told that repairing that cause rebuilds the Character Sheet, and therefore either splits my set across two versions of the character or costs a rebuild of every item, so that I choose between them instead of discovering the mismatch after delivery.
6. As a user whose failing items do not share a cause, I want one report listing each item's defect and its selected operation, and one instruction to be enough to approve all of them, some of them, or none, so that the ordinary batch outcome does not become an item-by-item interrogation.
7. As a user, I still do not want a defective result described as finished, so that completion claims stay truthful.
8. As a user who says the result looks wrong, I want Identity Review run against the Anchor rather than a verdict read from my wording, so that the existing review discipline is unchanged.
9. As a user who asks for a repair, I want the same operation the skill would have chosen, so that removing the initiative does not degrade the repair.
10. As a maintainer, I want the per-result versus per-request question to disappear rather than be answered, so that a scope the specifications never settled stops accumulating machinery.
11. As a maintainer, I want no counter, ledger, or remaining-attempts figure anywhere, so that the existing prohibition survives the change.

## Implementation Decisions

- `identity-anchor.md:299` loses the initiative and keeps the routing. The paragraph states which operation the contracts select, that the skill has not performed it, and that completion is not claimed. `Then run Identity Review exactly once for that corrected result` moves to the user-requested path, which already exists.
- `identity-anchor.md:301` loses the per-result bound, the same-result exhaustion clause, and the cross-result non-consumption clause, because none has a subject once nothing is automatic. It keeps the truthfulness requirements and the shared-defect attribution, and extends that attribution to carry the operation the shared cause selects. It also gains the attribution rule's complement: when the failing items of one set do not share a cause, one report lists each item's defect and selected operation, and one instruction may accept any subset of them.
- The freshly-generated test at `identity-anchor.md:251` stays. It still selects the operation, and the user-requested recovery path at `:253` already depends on it.
- The fixed-root regeneration contract at `:249` stays unchanged.
- The surface-capability boundary stays. When the surface cannot select the fixed-root inputs, the skill still says so rather than pretending, per `.scratch/identity-preservation-reliability/PRD.md:87`.
- `SKILL.md:210` gains the Recovery Offer on its failure branch, where the result has already been classified. `:212` changes who invokes a recovery path, from the skill to the user. `:216` drops `or automatic correction` from its no-claim list, which has no subject once nothing is automatic, and keeps its explicit-revision half and its truthful-boundary requirement unchanged. `:201` is not touched: it states a completion condition in actor-neutral terms and never mentions correction.
- `docs/architecture.md` `F8` becomes two stages. Every failing result runs the existing `SCOPE` and `FRESH` classification through to a selected operation — including the shared-defect branch, which currently terminates at attribution and therefore has no operation to name — and the outcomes are then collected into one Recovery Offer node. The `ONCE` node disappears and the follow-up Identity Review moves behind the user's acceptance. The shared-defect branch continues past the offer node into the Choice Gate described below; every other branch ends at it.
- No new gate on the ordinary path or the non-shared branch. The offer rides the existing report, not a Choice Gate, because it asks for a decision the user can also ignore.
- The shared-cause branch is the one exception, and it uses the existing Choice Gate rather than a new construct. Repairing the cause regenerates the Character Sheet; a regenerated Sheet is a different Sheet, so rebuilding only the failing items splits the set across two versions of the character, and rebuilding every item costs one generation per item. Two substantive resolutions exist, so the gate takes the shape the convention already prescribes for that case: rebuild every item, rebuild only the failing ones, an explicit stop path that delivers the passing items unchanged, and the permanent Custom Path.

## Testing Decisions

Scenarios touching automatic recovery, found by search and then read individually. They do not share one disposition, and converting them uniformly would weaken two of them. The coverage-matrix re-read at the end of this section adds four more that the search missed, one of them outside `F8`.

**Deleted and replaced.** The `Shared checks` automatic-recovery entry, `evals/golden-conversations.md:44`, is removed rather than converted. Everything in it that survives — the fixed-root default and the surgical exception for a freshly generated ordinary result — is already stated for the user-requested path at `:43`. What is left is the per-result bound, the follow-up review, the cross-result non-consumption clause, and the no-counter rule, none of which has a subject. One Recovery Offer entry replaces it.

**Unchanged.** Golden 105 and Golden 153 are already user-requested, at `Make the face look like me again.` and `Correct the result.` Golden 105 asserts that the skill performs no generation at all when the surface cannot select the inputs; only the phrase `do not claim automatic correction` in its expectation loses its subject. Golden 153 keeps the surgical row for a one-off drawn result and is untouched.

**Gains a user-acceptance turn.** Golden 127, Golden 131 case B, Golden 138 cases A and B, and the applicable cases of Golden 133 through 136. Each is the only place its contract is exercised rather than merely named, so the first turn asserts the Recovery Offer and the second asserts the operation actually running with the required inputs and exclusions.

**Repurposed or removed.** Golden 109 is the only scenario whose entire subject is the bound. It becomes the user-accepted repair path, keeping both outcomes — case A completes only after the follow-up review passes, case B reports the remaining drift and stops — and losing only the word `automatic` and its title. Golden 138 case E, which exists solely to exhaust an attempt, is removed.

**Strengthened.** Golden 110 case E forbids presenting a failed result as final and forbids framing its repair as an optional `make the face more like the reference` tweak. That is the closest thing on record to a test against this proposal's own worst failure mode, because a Recovery Offer has the outward shape of what case E prohibits. It is not converted. It is extended to pin the boundary: a Recovery Offer marks the result incomplete and names a required operation, while an optional cosmetic tweak offered over a result presented as final stays prohibited. Cases A through D survive with `automatic correction` adjusted as in Golden 105.

Golden 138 case F asserts the shared branch, which survives, but it must now also assert that the shared cause carries the operation it selects and that the branch ends in the Choice Gate between rebuilding every item and rebuilding only the failing ones, with its stop path and Custom Path intact. Golden 152's no-count assertion survives unchanged; only case B's framing moves from the bounded automatic path to the offer.

**The remaining `F8` rows were read rather than assumed.** All nineteen — 8, 12, 67–68, 96–97, 107–108, 111–112, 118, 121, 125–126, 128–131, 142 — were checked individually against `evals/golden-conversations.md`. Sixteen survive unchanged and three do not, so the earlier expectation that every one of them classifies rather than repairs was wrong.

Surviving unchanged: 8, 12, 97, 107, and 108, whose inputs are user requests — `Only fix the left hand`, `Fix only the coordination`, a named list of drifted cues to restore, `Correct the result`, and a pose change reported together with a distorted face. 67, 68, 96, 125, 126, and 142, which review or classify and never repair; Golden 126's `do not add ... correction for an absent closed cue` stays literally true. 111 and 112, which scope accepted risk and refuse a guarantee. 128, 129, and 130, whose every case is an explicit user request.

Changing, and none of the three was in the conversion list above:

- Golden 118 takes the input `Review and deliver the result.` and ends by routing to `the existing bounded recovery or reattachment path according to active-surface capability` on the skill's own initiative. It becomes an assertion that the offer names that path's operation.
- Golden 121 case A asserts `perform exactly one new generation from the Anchor and complete locked brief ... before one follow-up Identity Review`, after an input that asked only to `Generate and review the portrait`. It becomes an offer assertion. Its case B, the surface-limited half, survives exactly as Golden 105 does.
- Golden 131 case B performs a regeneration for an unambiguous failure before delivery. Its case A only recommends, so case B is that scenario's sole execution coverage and it gains a user-acceptance turn.

Golden 118 and Golden 121 need no acceptance turn, because Golden 108 already exercises identity-wide regeneration from the Anchor under execution on the user-requested path.

**The re-read above is scoped by the coverage matrix, and one scenario sits outside `F8`.** Golden 98 is filed under `F4` as the close-crop proportion recovery, so the `F8` re-read never reached it and it appears in no list above, yet its expectation ends `Perform at most one automatic correction, run Identity Review once more across the connected head-to-limb scale chain, and report any remaining concrete failure without another retry or a completion claim`. Left alone it would keep asserting the initiative this proposal removes. It becomes a selection-and-offer assertion and keeps both classifications it exists for: the isolated head-unit deviation selects Surgical Edit, and linked head-scale and Visible Body Evidence drift or an expanded partial crop selects regeneration. It needs no acceptance turn either, because Golden 107 exercises the surgical row and Golden 108 the regeneration row under execution on the user-requested path. Its matrix row names the proportion recovery rather than an executor and does not change.

Preserve unchanged: every scenario asserting that the user's likeness complaint triggers review without deciding it; every scenario asserting no biometric score or guarantee; every scenario asserting a passing first result gets no second pass.

## Out of Scope

- Changing what Identity Review judges, or the open/transferred/closed channel model.
- Changing which operation each failure class selects. This proposal moves the initiative, not the routing.
- Relaxing the edit-chain depth constraint. A user-requested repair still obeys the freshness and fixed-root rules.
- Adding a confirmation gate, a preference, or a setting that restores the automatic behavior.
- Batch generation itself, which remains specified elsewhere. The multi-item Recovery Offer is claimed here rather than deferred, because deferring it to a spec that never picked it up is how the batch recovery budget went unowned the first time.

## Further Notes

**This touches three landed specifications. The dispositions are decided; `domain-changes.md` in this directory carries them story by story, together with the ADR that records them.**

Nine items are affected across the three specifications — six user stories and three specification lines — and exactly one is superseded. `.scratch/edit-chain-depth/PRD.md` story 29 asks for `the existing bounded single automatic correction preserved rather than relaxed`, on a mechanical rationale about edit-chain depth. Removing the correction satisfies that rationale maximally, because zero automatic corrections is the shortest possible chain, while contradicting the literal ask. That contradiction reads as a plain reversal unless it is written down, so it is.

`.scratch/identity-preservation-reliability/PRD.md` is not superseded as a whole. Its story 34 keeps its focused-reattachment path and its entire rationale, and reverses only the automatic regeneration. Its story 35 keeps its requirement and moves the trigger to the user-requested path. Only its story 37, and `edit-chain-depth` story 8 with it, loses its subject; both are the bound of one, and the intent behind them — `As a user paying generation cost or waiting for results` — is satisfied more strongly by zero. Everything else in that PRD is untouched, and marking it superseded wholesale would discard work this proposal does not reach.

`.scratch/anime-stylized-identity/PRD.md:31` and `:133` keep their routing and lose only the clause naming the executor. `:180` keeps its scenario and changes what it asserts, and it must also gain a user-acceptance turn. Golden 129 and 130 already assert the fixed-root and no-edit contracts generically on the user-requested path, but Golden 138 cases A and B are the only place the two-stage drawn flow is named concretely under execution.

`docs/adr/0008` is revised in place rather than superseded, which is this repository's established practice for ADRs. Its subject, the two-stage flow, survives entirely, as does its round-trip reasoning, which now governs the user-requested path. Two half-sentences lose their subject and are deleted. Do not replace them with a statement that the constraint on initiative has become total: no initiative remains to constrain, so that sentence would name an empty subject.

**The batch case was the open question, and the evidence turned out to answer a different one.** `.scratch/anime-stylized-identity/research.md:118` reports roughly five or six usable images out of eight with two or three needing individual redos, flags itself as single-source, and sits at `:111` under a batch produced as one planned group. Items needing *individual* redo out of one planned batch is the non-shared shape, while the shared-defect rule at `identity-anchor.md:301` fires only for defects attributable to the Character Sheet or locked brief. The only evidence on record therefore describes the branch that rule does not reach. `.scratch/cross-spec-defect-provenance/research.md:74` chose per-result for the mirror-image reason: a request-wide cap of one means `the other eleven ship defective`. This proposal takes neither horn. The shared branch reports once; the non-shared branch reports each failing item's defect and selected operation in one report, and one instruction accepts any subset. Neither branch depends on shared-cause attribution succeeding.

**A throwaway prototype drafted both branches as literal conversations and found the assumed difficulty reversed.** The non-shared branch reads acceptably, for a structural reason rather than a stylistic one: every failing item in a drawn set routes to the same operation, because ADR 0008 makes an application never freshly generated, so a local defect, Uneven Stylization, a scale failure, and identity-wide drift all land on regeneration from the Character Sheet and the Anchor. The per-item operation this proposal imagines enumerating is a constant, and the report carries one operation against several defect descriptions. What length remains does not scale with the number of failing items, because the disclosures — that no shared cause is claimed, and that individually rebuilt items sit outside the planned batch — are per-request. Three of twelve and six of twelve differ by three sentences, and even twelve of twelve stays one message and one instruction.

The shared branch is the harder one, which this document had assumed was the easy one. Repairing a shared cause regenerates the Character Sheet, and a regenerated Sheet is a different Sheet rather than a patched one, so rebuilding only the failing items leaves the set carrying two versions of the character while rebuilding every item costs one generation per item. The skill has no basis for choosing between those, because the trade is precisely the cost-against-quality judgment this proposal hands to the user. That is why the shared branch, alone, ends in a gate.

What the prototype could not settle is whether the user's answer is usually yes. If it is, the report is added latency over a repair they would have accepted. That part of the premise stays unevidenced, and this proposal rests on the authority argument rather than on it.

**Process.** `.scratch/cross-spec-defect-provenance/research.md:97` states the rule this document follows: `When implementation hits a question the spec never decided, raise it as a spec change before writing prose, rather than deciding and back-filling.`
