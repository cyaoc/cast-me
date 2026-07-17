# Scoped Option Refresh

This module owns refresh-target routing, per-area option history and freshness, Delegated Refresh, lock inheritance, and Refresh Exhaustion.

## Scope

Refreshable creative areas are:

- Creative Direction, using the existing Style Refresh contract
- Decisive Moment
- Shot
- Styling
- Performance
- First-Pass Finish
- Layout / Output Contract, excluding exact text and hard delivery requirements

Output Type, Role/Costume Version, Safety, reference coverage, identity risk, exact-text verification, and Perspective Intent classification are focused or classificatory choices, not novelty menus. New facts or explicit user intent may change them, but do not maintain Shown Option history or apply creative freshness to them.

## Route the Target

Resolve one target in this order:

1. If the user names a refreshable creative area, refresh it. An explicit style or creative-direction target uses the Style Refresh rules in `composition-director.md`.
2. Otherwise, use the unresolved visible gate. If it is focused or classificatory, keep its options tied to the actual intent, evidence, classification, or text problem rather than applying creative freshness.
3. Otherwise, use the most recently presented refreshable gate, even if its option was adopted or an image was generated afterward.
4. If no reliable target exists, ask one compact localized scope gate with concrete choices drawn only from relevant creative areas. Do not silently default a bare request for more options to Style Refresh.

Track the most recently presented refreshable gate in the conversation decision state. Replace it only when another refreshable gate is presented; a focused or classificatory gate does not erase it.

If the user names a creative target while a focused gate is pending, honor the creative refresh but keep the focused gate unresolved and return to it before generation. Changing topic never accepts missing evidence, identity risk, safety tradeoffs, or exact-text uncertainty.

Treat `you decide`, `pick one`, and equivalent wording as delegation modifiers, not targets. Resolve the target first, then select and record one compatible Fresh Option internally without displaying the choice gate.

## Visible Gate and History

Every visible refreshable creative gate contains exactly three concrete options labeled A through C plus the permanent `D) Custom` option. Use the standard decision format and describe visible outcomes before professional vocabulary.

Maintain separate Shown Option history for each creative area while it remains available in the current conversation context:

- Record every presented A, B, and C immediately, whether selected or generated.
- Never record or consume the `D) Custom` placeholder. Record an adopted concrete Custom option in the target area's history.
- Record an option selected internally during a Delegated Refresh.
- Keep Creative Direction's Shown Direction history separate; do not mix another area's options into it.
- Do not add persistence or require prior-session history.

Generate candidates sequentially. Before presenting a candidate outside Creative Direction, use the owner's visible signature as an internal diversity check: it must differ from every available Shown Option in the same area, including candidates already chosen for the current batch, in at least two parts. Creative Direction keeps its existing three-of-six Direction Signature rule. Do not promise exact deduplication after earlier conversation history is unavailable.

A renamed option, palette-only change, adjective-only change, creator name, equipment token, professional term, or minor prompt rewrite is not fresh by itself. Freshness limits automatic recommendations, not user intent; restore a prior Shown Option when the user explicitly requests it.

## Locks and Continuity

A Scoped Option Refresh preserves identity, output requirements, exact text, every unrelated value, and every Explicit Lock. Reopen only the target area's Derived Locks and target fields the user explicitly asks to change. An Explicit Lock inside the target area remains locked unless the user reopens it.

Asking for choices does not generate, regenerate, or edit an image. First-Pass Finish remains generation-time, and targeted revision begins only after an explicit request to change a visible result.

Ordinary Scoped Option Refresh does not browse. Only a Style Refresh that explicitly asks for current, recent, latest, or trending directions, including trends tied to a date, uses Trend Refresh. A historical date or era without current/trend intent remains an ordinary creative constraint.

## Refresh Exhaustion

If the skill cannot assemble a complete three-option batch in the target area without violating Explicit Locks or that area's freshness threshold, declare Refresh Exhaustion. Do not display a partial or padded gate. Identify the single Explicit Lock that most restricts variation and ask with the standard decision format whether to reopen only that field; retain a `D) Custom` path and a path that keeps every lock and stops refreshing. Do not claim that the global creative space is exhausted.

If the user keeps every restricting lock, stop. Do not fabricate a new batch, relax unrelated locks, or silently escalate the request into Style Refresh.
