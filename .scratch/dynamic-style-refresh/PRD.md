Status: ready-for-agent

# Dynamic Style Refresh

## Problem Statement

The current identity-image direction flow offers only three concrete creative directions plus a custom option. When a user rejects those directions, asks for more, or wants to try a new style after making a selection, later choices can repeat the same underlying ideas with renamed labels, palette changes, or minor prompt variations. The user cannot reliably explore a broader range of genuinely different directions without restarting the brief or restating constraints that should remain locked.

## Solution

Enhance the existing Direction Gate with a lightweight Direction Atlas and conversation-local freshness tracking. Every visible gate continues to offer three concrete directions plus the permanent `D) Custom` option. A Style Refresh replaces the three concrete directions with Fresh Directions while preserving identity, output constraints, and Explicit Locks. Derived Locks belonging to the previous creative direction may reopen. Ordinary refreshes guarantee novelty within the conversation; only an explicit request for current or trending directions triggers a Trend Refresh with live research.

## User Stories

1. As a user exploring an identity-preserving image, I want three concrete directions plus a custom option, so that I have guided choices without losing the ability to describe my own idea.
2. As a user who dislikes the current directions, I want to ask for another batch, so that I can continue exploring without restarting the brief.
3. As a user requesting another batch, I want all three concrete choices to be Fresh Directions, so that I do not see renamed versions of rejected ideas.
4. As a user refreshing repeatedly, I want every previously presented A, B, and C direction to count as shown, so that rejected choices do not return later.
5. As a user choosing `D) Custom`, I want that entry to remain available in every batch, so that guided exploration never removes free-form control.
6. As a user who adopts a Custom Direction, I want that concrete direction included in later freshness checks, so that the skill does not recommend my own recent idea back to me.
7. As a user who explicitly chose an aspect ratio, exact text, wardrobe, action, gaze, or composition, I want those Explicit Locks preserved during a Style Refresh, so that exploring style does not erase my requirements.
8. As a user who accepted recommended defaults, I want direction-derived scene, lighting, color, finish, and unlocked composition suggestions to be replaceable during a Style Refresh, so that the new direction is meaningfully different.
9. As a user selecting a direction without accepting all defaults, I want preview details to remain suggestions, so that choosing a premise does not silently lock later production decisions.
10. As a user who says “only change the visual style,” I want the scene, action, composition, and subject placement preserved, so that only medium, lighting/color, material treatment, and finish change.
11. As a user who asks for a completely different direction, I want the creative direction and its derived choices reopened while identity and other Explicit Locks remain, so that the result can change substantially without becoming a new brief.
12. As a user asking for ordinary new directions, I want fast conversation-local freshness without mandatory web research, so that simple exploration stays lightweight.
13. As a user explicitly asking for current, recent, dated, or trending styles, I want a Trend Refresh based on live research, so that “current” is evidence-backed rather than guessed.
14. As a user receiving a Trend Refresh, I want the three researched directions to obey the same freshness rules, so that current references do not reintroduce ideas already shown in the conversation.
15. As a user who delegates with “you decide,” I want the skill to select one Fresh Direction internally and continue, so that I am not forced through a Direction Gate I explicitly waived.
16. As a user delegating a refresh, I want the internally selected direction recorded as shown, so that it is not recommended again later.
17. As a user who asks for many batches, I want the skill to maintain a meaningful difference threshold, so that it never fills the list with superficial variations.
18. As a user whose Explicit Locks prevent three Fresh Directions, I want the skill to identify the single most restrictive dimension and ask whether to reopen it, so that I can continue without losing unrelated choices.
19. As a user who intentionally asks to restore an earlier direction, I want to be allowed to do so, so that freshness rules constrain recommendations rather than my explicit choices.
20. As a user moving through the normal image-direction workflow, I want Style Refresh to reuse the existing Direction Gate, so that the feature does not add another mandatory question.
21. As a user with incomplete reference coverage, I want existing identity, anatomy, perspective, and performance risk gates to remain active, so that broader style exploration does not weaken identity protection.
22. As a user in a new conversation, I want the skill to behave normally even without prior-session history, so that this feature does not require persistent tracking or setup.
23. As a user reviewing different batches, I want directions to differ in visible production terms rather than creator names or camera-brand tokens, so that I can understand what will actually change in the image.
24. As a user who requests an older Shown Direction by name, I want the skill to honor that request, so that deduplication does not block deliberate reuse.

## Implementation Decisions

- Reuse the existing creative-direction dimension and Direction Gate. Do not add a separate style-browser step or another mandatory question.
- Every visible Direction Gate contains exactly three concrete directions, labeled A through C, plus the permanent `D) Custom` option.
- Add a lightweight Direction Atlas used only when creative direction is unresolved or a Style Refresh is requested. It is an internal combination vocabulary with a few curated quality examples, not a fixed user-facing catalog or a copied prompt gallery.
- The Direction Atlas combines six parts: production context, medium/era, scene and decisive moment, composition grammar, lighting/color logic, and finish.
- Represent each concrete option with a Direction Signature covering those six parts.
- A Fresh Direction must differ from every Shown Direction in at least three Direction Signature parts. Renaming an option, changing only its palette, or swapping equipment vocabulary does not satisfy freshness.
- Add conversation-local tracking for Shown Directions. Each presented A, B, and C direction is recorded immediately, whether selected or generated.
- Keep `D) Custom` permanently available and never record the placeholder itself. When the user adopts a concrete Custom Direction, derive its Direction Signature and record it as a Shown Direction.
- Preserve the existing `locked`, `suggested`, and `unresolved` states while distinguishing lock provenance as `locked: explicit` and `locked: derived`.
- A Style Refresh explicitly reopens the selected creative direction and may reopen direction-owned Derived Locks. It preserves all unrelated Explicit Locks unless the user explicitly reopens them.
- A direction selection locks only the fields explicitly stated by that option. Previewed camera, styling, performance, lighting, or palette details remain suggested unless the user repeats them or accepts recommended defaults.
- “Only change the visual style” reopens only medium/era, lighting/color, material treatment, and finish. Scene, composition, action, and subject placement remain unchanged.
- “Completely change the direction” reopens creative direction and its derived scene, composition suggestions, lighting/color, and finish while preserving identity, output requirements, exact text, and other Explicit Locks.
- An ordinary Style Refresh uses the Direction Atlas and conversation history without browsing. A Trend Refresh occurs only for explicit requests such as “latest,” “current,” “this year,” or a dated trend request.
- A Trend Refresh uses live visual research, extracts concrete production anchors, keeps source links available, and does not claim currentness when research is unavailable.
- A Delegated Refresh bypasses the visible Direction Gate, selects one compatible Fresh Direction internally, records it, applies recommended defaults, and continues. Existing focused identity, coverage, safety, and exact-text gates still apply.
- Refresh Exhaustion occurs when Explicit Locks leave fewer than three Fresh Directions. Do not silently relax freshness; identify the single explicit dimension most responsible and ask whether to reopen only that dimension.
- Deduplication limits automatic recommendations, not explicit user intent. A user may restore any prior Shown Direction.
- Freshness is conversation-local. Do not add cross-conversation storage or persistence.
- The feature must remain identity-first. New direction generation cannot borrow identity from style references, weaken reference-coverage checks, or silently downgrade locked camera and performance choices.

## Testing Decisions

- Use the existing golden-conversation behavior suite as the single highest-level test seam. Tests should evaluate externally visible dialogue, decision inheritance, and prompt behavior rather than internal wording or data representation.
- Add a scenario where the first Direction Gate presents A/B/C plus `D) Custom`, then three consecutive refreshes produce nine concrete Shown Directions with no pair violating the three-part freshness threshold.
- Add a scenario proving that all presented A/B/C options are recorded even when the user selects none of them.
- Add a scenario where a user adopts a Custom Direction, refreshes, and does not receive an equivalent recommendation while `D) Custom` remains present.
- Add a scenario where Style Refresh reopens direction-owned Derived Locks but preserves Explicit Locks for identity, canvas, exact text, wardrobe, action, gaze, and composition.
- Add separate scenarios for “only change the visual style” and “completely change the direction” to verify their different reopen scopes.
- Add a scenario where an ordinary refresh does not browse and a clearly requested Trend Refresh does perform research or reports that currentness could not be verified.
- Add a Delegated Refresh scenario proving that no Direction Gate is shown, one Fresh Direction is recorded, recommended defaults are applied, and focused risk gates remain available.
- Add a Refresh Exhaustion scenario proving that the skill does not relax freshness and asks to reopen exactly one constraining Explicit Lock.
- Add a scenario proving that the user can explicitly restore a Shown Direction even though the skill may not recommend it automatically.
- Reuse existing identity-risk, strong-perspective, decision-inheritance, and explicit-default scenarios as prior art. The new feature must not change their expected behavior except where a Style Refresh explicitly reopens creative direction.

## Out of Scope

- Importing or maintaining the external repository's full prompt gallery.
- A fixed set of six user-visible composition cards or a finite style menu.
- A separate mandatory style-browser step.
- Showing more than three concrete directions in one Direction Gate.
- Removing or replacing `D) Custom`.
- Cross-conversation persistence, databases, or user profiles for direction history.
- Browsing on every ordinary refresh.
- New CLI, model-selection, quality, billing, or API controls.
- Refactoring existing identity anchors, reference-coverage gates, safety handling, or generation tooling beyond the integration required for Style Refresh.
- Guaranteeing that subjective style trends remain current without live research.

## Further Notes

- The external GPT Image prompt gallery informed the value of category routing and concrete visual anchors, but this feature adopts only a lightweight, identity-centered Direction Atlas. It must not copy the external gallery wholesale or make runtime availability depend on it.
- The project glossary defines Style Refresh, Trend Refresh, Direction Signature, Fresh Direction, Custom Direction, Shown Direction, Direction Atlas, Refresh Exhaustion, Direction Gate, Delegated Refresh, Explicit Lock, and Derived Lock. Implementation and tests should use those terms consistently.
- No ADR is required: these behavior rules are visible in the skill contract, remain easy to revise, and do not create an irreversible architectural commitment.
