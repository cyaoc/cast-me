Status: ready-for-agent

# Scoped Option Refresh

## Problem Statement

The identity-image direction flow contains several beginner-facing choice gates, but only Creative Direction currently supports reliable repeated refreshes. A user can reject Finish Directions, shot choices, styling choices, performance choices, or another creative option set and ask for “more,” yet the current coordinator may route any request for another batch into Style Refresh. That can reopen the wrong creative area, disturb decisions the user wanted to keep, or return the same fixed menu with renamed labels.

Lazy users should not need to restate the whole brief or learn the skill's internal production dimensions. They need a predictable way to request new choices at any time while preserving identity, output requirements, Explicit Locks, and every unrelated creative choice. New choices must be visibly different rather than superficial rewrites, but the skill must also be honest when the remaining locked solution space cannot support another complete batch.

## Solution

Add **Scoped Option Refresh** as a conversation behavior shared by existing refreshable creative choice gates. A refresh targets one named or contextually identified creative choice area, replaces only that area's concrete options, and preserves every unrelated decision.

When the user names a creative choice area, that explicit target wins. Otherwise, an unresolved visible gate is the target; if no gate is awaiting an answer, the most recently presented refreshable gate is the target even if its choice was already adopted or the first image was generated. Only when the user gives no target and the conversation contains no reliable recent refreshable gate does the skill ask one compact scope question. An explicit request to change style or creative direction continues to use the existing Style Refresh behavior.

Every visible refreshable gate offers three concrete, image-specific options plus the permanent `D) Custom` option. Each creative choice area keeps its own conversation-local Shown Option history and visible signature. A Fresh Option must be materially different from every Shown Option in the same area. Creative Direction retains its existing stricter Fresh Direction rule; other areas use their own lightweight signatures. If Explicit Locks leave fewer than three Fresh Options, the skill enters Refresh Exhaustion instead of lowering the threshold or inventing superficial variants.

## User Stories

1. As a beginner user, I want to ask for another batch in ordinary language, so that I can keep exploring without learning production terminology.
2. As a user who dislikes the current Finish Directions, I want three new complete Finish Directions, so that I can change the finished feeling without reopening the image concept.
3. As a user who dislikes the current shot choices, I want three new shot relationships, so that I can explore framing and spatial impact while preserving the scene and subject.
4. As a user who dislikes the current styling choices, I want three new styling directions, so that I can explore wardrobe presentation without changing identity or performance.
5. As a user who dislikes the current performance choices, I want three new actions or expressions, so that I can explore how the person inhabits the scene without changing the shot or styling.
6. As a user who dislikes the current Decisive Moment choices, I want new moments within the locked creative direction, so that I can change the story beat without restarting the direction.
7. As a user exploring a poster or editorial layout, I want new layout directions, so that I can change visual organization while preserving exact text and delivery requirements.
8. As a user who explicitly says “give me new shot choices,” I want Shot to refresh even if another creative gate was shown more recently, so that explicit intent wins over conversational inference.
9. As a user who says “these three do not work” immediately after a refreshable gate, I want that gate refreshed, so that I do not need to repeat its name.
10. As a user who selected an option and later says “give me more like the choices from before,” I want the most recently presented refreshable gate reopened, so that adoption does not erase its conversational scope.
11. As a user who already generated the first image and then asks for more Finish choices, I want Finish refreshed without silently starting a revision or generating another image, so that I remain in control of the next action.
12. As a user who says only “give me some more” when no reliable scope exists, I want one compact scope question, so that the skill does not guess the wrong creative area.
13. As a user who asks to “change the direction,” I want the existing Style Refresh behavior, so that a direction request is not mistaken for a local shot or finish refresh.
14. As a user who says “change only the visual style,” I want the existing narrow Style Refresh scope preserved, so that scene, action, composition, and subject placement remain unchanged.
15. As a user who says “pick a new one for me,” I want the skill to choose one Fresh Option internally, so that delegation does not force me through another visible gate.
16. As a user delegating a scoped refresh, I want the chosen option recorded as shown, so that it is not recommended back to me later.
17. As a user viewing any refreshable creative gate, I want three concrete options plus `D) Custom`, so that guided exploration and free-form control remain available together.
18. As a user who adopts a Custom option, I want that concrete result included in later freshness checks, so that the skill does not repackage my own idea as a recommendation.
19. As a user returning for another batch, I want every previously presented A, B, and C option counted as shown, so that rejected options do not quietly return.
20. As a user comparing one batch, I want A, B, and C to be materially different from each other, so that one gate represents three real directions rather than three labels for one idea.
21. As a user requesting repeated batches, I want every new option checked against the complete history for that creative area, so that novelty does not reset after selection or generation.
22. As a user refreshing Creative Direction, I want the existing six-part Direction Signature and three-part difference threshold preserved, so that this feature does not weaken Style Refresh.
23. As a user refreshing Finish, I want changes to the overall feeling, lighting/contrast, color relationship, person or material treatment, or texture, so that a palette swap alone does not count as new.
24. As a user refreshing Shot, I want materially different combinations of subject scale, viewpoint, projection, placement, and spatial/background relationship, so that fixed crop labels do not become a permanent menu.
25. As a user refreshing Styling, I want materially different silhouette, layers, materials, accessories, grooming, or props, so that “keep, simplify, replace” does not remain the only reusable template.
26. As a user refreshing Performance, I want materially different action, body direction, expression, gaze, hands, prop interaction, or energy, so that adjective-only rewrites do not count as new performance.
27. As a user refreshing a Decisive Moment, I want materially different action, tension, story evidence, or first impression, so that the new moment remains concrete and visible.
28. As a user refreshing Layout, I want materially different layout structure, subject/text placement, safe-area use, or variant organization, so that exact text and platform requirements remain locked.
29. As a user who explicitly locks a waist-up crop, I want new Shot options to preserve that crop and vary only unlocked shot relationships, so that local exploration respects my stated boundary.
30. As a user with locked identity, canvas, exact text, wardrobe, action, gaze, or composition, I want unrelated Scoped Option Refreshes to preserve those values, so that asking for ideas does not damage the brief.
31. As a user who accepted recommendation-derived defaults in the target area, I want those Derived Locks eligible to reopen, so that the refreshed area can change meaningfully.
32. As a user who explicitly kept a subfield within the refreshed area, I want that Explicit Lock preserved, so that a scoped refresh changes only what I allowed.
33. As a user answering a safety, reference-coverage, identity-risk, or exact-text gate with “more options,” I want only valid fact-dependent paths, so that creative freshness is not applied to boundaries or evidence.
34. As a user who explicitly names a creative area while a focused risk gate is pending, I want the requested creative area refreshed and the focused gate kept pending before generation, so that changing topic does not waive the unresolved boundary.
35. As a user choosing an Output Type or Role/Costume Version, I want those classifications to remain stable choices rather than novelty menus, so that factual routing is not confused with creative ideation.
36. As a user asking for more spatial impact, I want new Shot expressions within the existing Perspective Intent semantics, so that the skill does not invent new risk categories to simulate novelty.
37. As a user whose Explicit Locks leave too little room for three Fresh Options, I want the skill to identify one most restrictive field, so that I can decide whether to reopen only that field.
38. As a user who keeps every restrictive lock, I want the refresh to stop, so that the skill does not provide fake novelty.
39. As a user in Refresh Exhaustion, I want `D) Custom` to remain available, so that I can supply an intentional exception myself.
40. As a user who explicitly requests an earlier Shown Option, I want it restored, so that freshness limits automatic recommendations rather than my choices.
41. As a user requesting ordinary new options, I want the refresh to stay local and fast without web research, so that basic exploration does not become a research workflow.
42. As a user explicitly requesting current or trending creative directions, I want only Style Refresh to invoke Trend Refresh, so that claims of currentness remain evidence-backed.
43. As a user in a long conversation, I want freshness tracked for as long as the relevant conversation state remains available, so that the skill avoids repeats without pretending to offer permanent memory.
44. As a user starting a new conversation, I want the skill to work without prior refresh history, so that no account storage or setup is required.
45. As a user resolving First-Pass Finish, I want refreshed Finish Directions to remain part of the original generation contract, so that refresh does not create a mandatory second pass.
46. As a user who wants an actual revision after seeing a result, I want revision to begin only when I explicitly request the edit, so that asking for choices never mutates the image by itself.

## Implementation Decisions

- Add Scoped Option Refresh as a conversation behavior over existing creative choice gates; do not add a new mandatory workflow stage.
- Keep the coordinator as the single routing authority. Replace the current broad “another batch means Style Refresh” rule with scoped routing.
- Route a request in this order:
  1. An explicitly named refreshable creative choice area is the target.
  2. Otherwise, an unresolved visible gate is the target. A focused safety, evidence, identity-risk, or exact-text gate remains fact-dependent and does not gain creative freshness behavior.
  3. Otherwise, the most recently presented refreshable gate is the target, even if its option was adopted or generation already occurred.
  4. An explicit style or creative-direction request uses the existing Style Refresh branches.
  5. If no target and no reliable recent refreshable gate exist, ask one compact refresh-scope question. Do not silently default a bare “more options” request to Style Refresh.
- Treat “you decide,” “pick one,” and equivalent wording as delegation modifiers rather than refresh targets. The named, active, or recent creative choice area still determines scope.
- Keep a conversation-local reference to the most recently presented refreshable gate. It is replaced only when another refreshable gate is presented; focused classification or risk gates do not erase it.
- Add one progressively loaded Scoped Option Refresh contract as the single source for routing, per-area Shown Option history, Custom behavior, delegation, lock inheritance, restoration, and Refresh Exhaustion. Owner modules define only their local visible signatures and exceptions.
- Preserve the existing Style Refresh, Trend Refresh, Direction Signature, Fresh Direction, Shown Direction, Direction Atlas, and Direction Gate behavior. Generic option history must not replace or contaminate Creative Direction history.
- Maintain separate conversation-local Shown Option history for each refreshable creative choice area. Record each concrete A, B, and C option when presented, whether selected or generated.
- Keep `D) Custom` present in every visible refreshable creative gate. Never record the placeholder; record an adopted concrete Custom option in the target area's history.
- Every visible scoped gate contains exactly three concrete options plus `D) Custom`. A delegated refresh selects one compatible Fresh Option internally instead of showing the gate.
- A Fresh Option outside Creative Direction must differ from every Shown Option in the same area in at least two visible signature parts. The three options within one batch must also satisfy the threshold against each other.
- Keep Creative Direction's existing stricter rule: a Fresh Direction differs from every Shown Direction in at least three of its six Direction Signature parts.
- Use these owner-specific signatures:
  - Decisive Moment: action/event, before/after tension, story evidence, and first impression.
  - Shot: body cutoff or subject scale, viewpoint/distance/projection, subject placement, and spatial layers or background relationship.
  - First-Pass Finish: overall feeling, lighting/contrast, person-environment color relationship, face or material treatment, and texture/final character.
  - Styling: silhouette/layers, materials, headwear/accessories, makeup/hair/grooming, and props.
  - Performance: action/body direction, expression/mouth, gaze, hands or prop interaction, and energy.
  - Layout/Output Contract: layout structure, subject/text-safe placement, safe areas/readability, and required variants.
- Renaming, palette-only changes, adjective-only changes, equipment vocabulary, creator names, or professional terminology do not by themselves satisfy freshness.
- Treat existing fixed Shot and professional-headshot Styling menus as examples of option shape, not reusable catalogs. Generate choices for the current image, target use, locks, and prior history.
- Keep Perspective Intent as a stable semantic classification. Requests for more perspective creativity produce fresh Shot options within the selected intent rather than new classifications.
- On a scoped refresh, preserve identity, output requirements, every unrelated value, and every Explicit Lock. Reopen only target-area Derived Locks and other target-area values the user explicitly asks to change.
- If the user names a creative target while a focused risk or evidence gate is pending, honor the creative refresh but retain the focused gate as unresolved and require it before generation.
- Output Type, Role/Costume Version, Safety, reference coverage, identity risk, and exact-text verification do not maintain freshness history. They may change only through new facts, explicit user intent, or their existing focused behavior.
- Refresh Exhaustion occurs when Explicit Locks leave fewer than three Fresh Options in the requested area. Do not lower the area's threshold. Ask whether to reopen the single Explicit Lock that most restricts variation, while retaining stop and `D) Custom` paths.
- If the user preserves every restricting lock, stop refreshing. Never silently escalate a scoped refresh into Style Refresh.
- Freshness constrains automatic recommendations only. Honor an explicit request to restore a prior Shown Option.
- Keep history conversation-local. Do not add persistence, a database, user profiles, hooks, scripts, or runtime services.
- Ordinary Scoped Option Refresh does not browse. Only an explicit current, recent, dated, or trending Style Refresh uses the existing Trend Refresh behavior.
- Asking for options never generates or edits an image. First-Pass Finish remains generation-time; targeted revision remains user-initiated.
- Add only the canonical glossary terms needed by the behavior. Do not create an ADR because the contract is localized, reversible, and visible in the skill behavior.

## Testing Decisions

- Use the existing golden-conversation behavior suite as the single highest-level behavioral test seam. Test externally visible routing, option difference, lock preservation, and stopping behavior rather than exact prose, internal state names, or reference-file structure.
- Extend the shared checks so every visible refreshable creative gate presents exactly three concrete options plus `D) Custom`, tracks all presented concrete options in its own area, and preserves unrelated Explicit Locks.
- Add an Active Finish Refresh scenario where “these three do not work; give me another batch” refreshes only First-Pass Finish and preserves scene, Shot, Styling, Performance, canvas, text, and identity.
- Add an Explicit Target Beats Context scenario where a Finish gate is visible but “give me new shot choices” refreshes only Shot.
- Add a Recent Gate After Adoption scenario where the user adopts a choice, proceeds, and later uses an unnamed “another batch”; the most recently presented refreshable gate is reopened.
- Add a No Reliable Scope scenario where a bare “give me more” produces one compact scope question rather than silently entering Style Refresh.
- Add a Pending Focused Gate scenario proving that an unnamed request stays within the focused fact-dependent gate, while an explicitly named creative refresh is honored without resolving or discarding the focused gate.
- Add a Partial Shot Reopen scenario where an Explicit Lock for waist-up framing survives while viewpoint, placement, projection, and background relationship change.
- Add repeated-refresh scenarios for Decisive Moment, Shot, First-Pass Finish, Styling, Performance, and Layout. Each should cover at least three batches, include all presented options in history, and reject renamed or otherwise superficial variants.
- Add a Scoped Custom scenario proving that an adopted Custom option enters the correct area's history while the `D) Custom` placeholder remains available.
- Add a Scoped Delegation scenario proving that “pick a new action yourself” displays no gate, selects and records one Fresh Performance, and changes no unrelated area.
- Add a Scoped Refresh Exhaustion scenario proving that the threshold is preserved, exactly one restricting Explicit Lock is offered for reopening, and keeping all locks stops the refresh.
- Add a Focused Boundary scenario proving that Safety, reference coverage, identity risk, Output Type, Role/Costume Version, and exact-text choices do not receive creative freshness behavior.
- Add a Perspective Boundary scenario proving that requests for more spatial impact refresh Shot expressions while retaining the existing Perspective Intent semantics.
- Keep the existing Style Refresh scenarios as regression coverage for the six-part Direction Signature, 3/6 freshness, narrow style-only refresh, complete direction refresh, Trend Refresh, delegation, restoration, and direction exhaustion.
- Keep the existing First-Pass Finish scenarios as regression coverage for generation-time finish, identity-safe retouching, medium adaptation, and the boundary between choosing a finish and explicitly requesting a revision.
- Run the complete golden-conversation audit and require zero failures. Also run the existing skill-package validator and whitespace validation; these are packaging checks, not additional behavioral seams.
- If the validator requires Python packages, install them only inside a throwaway isolated `uv` environment rather than modifying project or global Python state.

## Out of Scope

- Cross-conversation history, durable deduplication, databases, user profiles, or account preferences.
- A promise of infinite novelty under finite Explicit Locks or limited retained conversation context.
- A fixed global catalog for Shot, Styling, Performance, Finish, Decisive Moment, or Layout.
- Separate refresh workflows, classes, configuration objects, or tools for every creative choice area.
- A new mandatory browser, gallery, filter stage, or second image-generation pass.
- Browsing for ordinary Scoped Option Refreshes.
- Changing existing Style Refresh or Trend Refresh semantics beyond correcting the broad global routing trigger.
- Inventing new Perspective Intent, Safety, reference-coverage, identity-risk, Output Type, or Role/Costume classifications for novelty.
- Automatically changing exact text, platform requirements, identity anchors, or other Explicit Locks.
- Automatically revising, regenerating, or editing an image merely because the user asks to see choices.
- Guaranteeing perfect deduplication after relevant conversation state is no longer available.
- New dependencies, APIs, schemas, storage, background services, or installation behavior.

## Further Notes

- The confirmed ambiguity rule is intentionally narrow: ask one compact scope question only when the user supplies no target and there is no reliable recent refreshable gate. All other common lazy requests should route without another clarification.
- “Perfect” means predictable scope, preservation of unrelated locks, materially fresh choices, conversation-local non-repetition, and honest exhaustion. It does not mean unlimited novelty or permanent memory.
- Scoped Option Refresh is the generic behavior. Style Refresh remains the Creative Direction-specific branch with its existing stronger signature and Trend Refresh capability.
- Shown Direction and Fresh Direction remain precise Creative Direction specializations of the generic Shown Option and Fresh Option language.
- No ADR is required because the change is a reversible skill-contract extension with no schema, API, persistence, or hard-to-reverse architecture decision.
