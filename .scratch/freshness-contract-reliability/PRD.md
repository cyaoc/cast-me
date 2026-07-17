Status: ready-for-agent

# Freshness Contract Reliability

## Problem Statement

CastMe's refresh behavior currently describes freshness as an exact guarantee across every Shown Direction or Shown Option in the current conversation. It also defines Refresh Exhaustion as proof that Explicit Locks leave fewer than three possible Fresh Options. Those promises require the model to maintain and compare an unbounded amount of implicit conversation state and to reason about an open-ended creative solution space as though it were finite.

The existing Direction Signature and owner-specific visible signatures are useful because they prevent renamed, palette-only, adjective-only, or equipment-only variants from being presented as fresh. The problem is not the presence of the `3/6` and `2/N` thresholds. The problem is treating those checks as an exact lifetime guarantee after relevant conversation history is no longer available, and treating exhaustion as a count of every option that could theoretically exist.

## Solution

Keep the existing freshness signatures and thresholds as internal checks performed before options are presented. Compare new candidates against other candidates in the same batch and against Shown Directions or Shown Options still available in the current conversation context. Do not promise exact deduplication after earlier history is no longer available, and do not add storage to simulate that promise.

Redefine Refresh Exhaustion as an observable batch-construction failure. If the skill cannot assemble a complete three-option batch without violating Explicit Locks or the target area's freshness threshold, it stops the batch and asks whether to reopen the single Explicit Lock that most restricts variation. It does not display a partial batch, invent superficial variants, relax unrelated locks, or claim to have exhausted the global creative space.

## User Stories

1. As a user requesting new Creative Directions, I want each presented direction to pass the existing `3/6` Direction Signature check, so that a renamed or cosmetically adjusted direction is not presented as fresh.
2. As a user refreshing another creative choice area, I want each presented option to pass the existing `2/N` visible-signature check, so that superficial wording changes do not replace meaningful variation.
3. As a user viewing one refresh batch, I want A, B, and C checked against each other, so that one gate contains three materially different choices.
4. As a user requesting repeated batches, I want new candidates checked against the relevant Shown history still available in the conversation, so that rejected ideas do not immediately return.
5. As a user in a long conversation, I want CastMe to avoid false claims of perfect historical deduplication, so that its guarantees remain honest after earlier context is no longer available.
6. As a user in an ordinary short conversation, I want the existing refresh experience to remain unchanged, so that reliability wording does not add friction to the common path.
7. As a user starting a new conversation, I want refreshes to work without prior-session state, so that no setup or account history is required.
8. As a user who saw but did not select an option, I want it recorded as Shown while it remains available in context, so that rejected options are still considered during later refreshes.
9. As a user who adopts a concrete Custom option, I want it considered during later freshness checks, so that CastMe does not immediately recommend my own idea back to me.
10. As a user viewing `D) Custom`, I want the placeholder to remain permanently available without being treated as a consumed option, so that free-form control is never removed.
11. As a user delegating a refresh, I want the internally selected Fresh Option recorded like a visible choice, so that it is not immediately reused.
12. As a user explicitly requesting an earlier Shown Option, I want that request honored, so that freshness constrains automatic recommendations rather than my intent.
13. As a user with Explicit Locks, I want every generated candidate checked without silently relaxing those locks, so that novelty does not damage the brief.
14. As a user whose locks prevent a complete fresh batch, I want CastMe to recognize that it cannot assemble three valid choices, so that it stops instead of fabricating variety.
15. As a user entering Refresh Exhaustion, I want the skill to withhold an incomplete batch, so that I am not shown one or two valid choices mixed with filler.
16. As a user entering Refresh Exhaustion, I want CastMe to identify one Explicit Lock that most restricts useful variation, so that I can make one focused decision.
17. As a user entering Refresh Exhaustion, I want the stop path and `D) Custom` path retained, so that reopening a lock is not mandatory.
18. As a user who keeps every restricting lock, I want refreshing to stop, so that the skill does not repeat itself or change another creative area.
19. As a user requesting a scoped refresh, I want Refresh Exhaustion to remain scoped to that creative choice area, so that it does not silently escalate into Style Refresh.
20. As a user refreshing Creative Direction, I want the same six Direction Signature parts retained, so that this reliability correction does not weaken the established creative standard.
21. As a user refreshing Shot, Styling, Performance, First-Pass Finish, Decisive Moment, or Layout, I want the existing owner-specific visible signatures retained, so that each area continues to judge visible consequences appropriate to its responsibility.
22. As a user requesting ordinary new options, I want the refresh to remain local and not browse, so that reliability does not become a research workflow.
23. As a user explicitly requesting current or trending Creative Directions, I want Trend Refresh to keep the same freshness checks, so that researched directions do not reintroduce available Shown history.
24. As a user answering a safety, reference-coverage, identity-risk, exact-text, or other fact-dependent gate, I want it excluded from creative freshness, so that this correction does not turn focused decisions into novelty menus.
25. As a user preserving identity and output requirements, I want this correction to change only refresh bookkeeping claims and exhaustion behavior, so that image-direction ownership and generation remain stable.
26. As a maintainer, I want the glossary, refresh contracts, and behavioral checks to use the same definitions, so that future changes do not reintroduce impossible guarantees.
27. As a maintainer, I want the reliability correction implemented without a scratchpad, hook, MCP service, database, or new dependency, so that CastMe remains an instruction-first Skill.

## Implementation Decisions

- Keep Direction Signature, owner-specific visible signatures, Shown Direction, Shown Option, Fresh Direction, Fresh Option, and Refresh Exhaustion as the canonical domain language.
- Keep Creative Direction's `3/6` threshold and other refreshable creative areas' shared `2/N` threshold. Treat both as internal pre-presentation diversity checks rather than proof of permanent global uniqueness.
- Continue generating candidates sequentially. A candidate must pass the applicable threshold against candidates already accepted for the current batch and against relevant Shown history still available in the current conversation context.
- Continue recording presented A, B, and C options, adopted concrete Custom options, and internally selected Delegated Refresh options while that conversation state remains available.
- Keep Shown histories separate by creative choice area. Creative Direction retains its specialized Shown Direction history.
- Do not promise exact deduplication after earlier history is no longer available. The skill does not need to announce this limitation during ordinary successful refreshes; it must simply avoid a stronger contractual guarantee.
- Do not add a hidden scratchpad or any explicit persistence mechanism. Model reasoning output and reasoning summaries are not treated as a state API.
- Do not use local memories, hooks, MCP, scripts, files, databases, user profiles, or runtime services for refresh history.
- Redefine Refresh Exhaustion as failure to assemble a complete three-option batch under the applicable freshness threshold and current Explicit Locks.
- When Refresh Exhaustion occurs, do not present a partial or padded batch. Identify the single Explicit Lock that most restricts variation and use the existing decision format to offer a focused reopening choice, a stop path, and `D) Custom`.
- If the user preserves every restricting lock, stop refreshing. Do not fabricate freshness, relax unrelated locks, or escalate into another refresh area.
- Preserve identity, output requirements, exact text, unrelated values, focused gates, delegation behavior, explicit restoration, Style Refresh routing, and Trend Refresh routing.
- Keep the change within the existing refresh behavior contracts and domain glossary. Do not introduce another workflow stage or coordinator.
- Treat completed PRDs as historical records. Do not rewrite them to mirror this corrective spec.
- Do not create an ADR. This is a localized, reversible clarification of an instruction contract and does not create an architectural commitment.

## Testing Decisions

- Use the existing Golden Conversations suite as the single highest-level behavioral seam. Test externally visible option quality, lock preservation, routing, and stopping behavior rather than hidden reasoning text or an internal ledger shape.
- Update shared refresh checks so freshness is evaluated against the available conversation history and current batch without claiming perfect deduplication after unavailable history.
- Keep the existing consecutive Creative Direction refresh scenario as coverage for three complete batches, nine Shown Directions, and the `3/6` threshold.
- Keep repeated scoped-refresh scenarios as coverage for the `2/N` threshold across Decisive Moment, Shot, First-Pass Finish, Styling, Performance, and Layout.
- Keep scenarios proving that unselected A/B/C choices, adopted concrete Custom choices, and delegated choices enter the appropriate available Shown history while `D) Custom` does not.
- Add or revise a long-conversation scenario so the contract does not promise exact deduplication after earlier history is unavailable. The successful short-conversation path must not add a warning or clarification gate.
- Revise Creative Direction exhaustion coverage so Exhaustion is triggered by inability to assemble three candidates that simultaneously satisfy Explicit Locks and the `3/6` threshold, not by claiming that fewer than three directions exist globally.
- Revise scoped Shot exhaustion coverage so Exhaustion is triggered by inability to assemble three candidates that simultaneously satisfy the Shot locks and `2/N` threshold.
- Exhaustion scenarios must verify that no partial or superficial batch is shown, exactly one restricting Explicit Lock is offered for reopening, and stop plus `D) Custom` remain available.
- Keep regression coverage proving that keeping every lock stops the scoped refresh without escalating to Style Refresh.
- Keep focused-gate boundary coverage so safety, evidence, identity-risk, exact-text, and classificatory choices do not receive freshness histories or thresholds.
- Run the complete Golden Conversations audit and require zero failures.
- Run the existing Skill package validator and whitespace validation. These are verification gates, not new behavioral seams.
- If validation requires Python packages, use only a throwaway isolated `uv` environment and do not modify project or global Python state.

## Out of Scope

- Cross-conversation history or durable deduplication.
- Perfect deduplication after relevant conversation history is no longer available.
- A hidden model scratchpad treated as reliable storage.
- Hooks, MCP services, databases, files, user profiles, account preferences, or background state.
- Removing or weakening the `3/6` or `2/N` freshness thresholds.
- Replacing signatures with an unstructured qualitative instruction.
- Guaranteeing infinite novelty under restrictive Explicit Locks.
- Enumerating or proving the size of an open-ended creative solution space.
- Showing partial refresh batches.
- Adding a new workflow stage, menu, coordinator, or refresh mode.
- Changing the number of concrete A/B/C options or removing `D) Custom`.
- Changing Style Refresh, Trend Refresh, Delegated Refresh, explicit restoration, or focused-gate routing beyond wording needed for the corrected guarantees.
- Changing identity anchoring, image generation, revision, quality, safety, exact-text, or output-delivery behavior.
- Rewriting completed historical PRDs.
- New dependencies, APIs, schemas, installation steps, or runtime services.

## Further Notes

- The originating review was reliable about the risk of implicit long-conversation bookkeeping, but overstated the number of independent quantitative rules. The current design has two shared thresholds, and retaining them gives the model a clearer defense against superficial variation.
- The correction therefore narrows the promise instead of deleting the useful checks: available-context freshness remains required, while unavailable-history uniqueness is not claimed.
- Refresh Exhaustion is deliberately operational. It describes what happens when the next batch cannot be completed, not a mathematical statement about every direction or option that could exist.
- The domain glossary already records the accepted available-history boundary and operational Refresh Exhaustion definition.
