# Identity Image Direction

This context describes how the skill preserves a person's identity while guiding creative image-direction choices across a conversation.

## Language

**Primary Identity Anchor**:
The actual person reference image that authoritatively anchors face identity for generation or editing. Supporting images and text may add evidence but never replace or override it.
_Avoid_: Primary identity reference, text-only identity description

**First-Pass Finish**:
The generation-time visual finish that resolves lighting/color, identity-safe retouching, texture, and final image character in the original image request. It is not a later edit of an exported file.
_Avoid_: Post-processing, second pass

**Finish Direction**:
A complete beginner-facing option that expresses a First-Pass Finish through visible light, color, person or material treatment, and texture. It is adapted to the current image rather than reused as a fixed filter preset.
_Avoid_: Filter preset, parameter list

**Natural Retouch**:
An identity-safe finish that reduces clearly temporary blemishes, redness, and distracting shine while preserving real skin texture, age impression, distinctive marks, and anything uncertain.
_Avoid_: Automatic beautification, skin replacement

**First Read**:
The one person, face, silhouette, action, emotion, product, or message that must register first at the intended display size. Supporting elements reinforce it rather than compete with it.
_Avoid_: Generic visual impact, universal drama

**Physical Scene Coherence**:
The state in which the resolved setting, time/weather, shot/perspective, performance, styling/materials, and lighting/finish can coexist as one internally coherent scene.
_Avoid_: Cross-dimensional consistency check, consistency review

**Style Refresh**:
A user-requested reopening of creative direction and its derived scene, lighting/color, finish, and unlocked composition suggestions. It preserves identity and output constraints plus every Explicit Lock unless the user reopens them.
_Avoid_: Full restart, reroll

**Trend Refresh**:
A Style Refresh that explicitly asks for current, recent, latest, or trending visual directions, including trends tied to a date. It requires live research; a historical date or era without current/trend intent remains an ordinary creative constraint.
_Avoid_: Regular refresh, fresh batch

**Direction Signature**:
The six-part description of a concrete direction: production context, medium/era, scene and decisive moment, composition grammar, lighting/color logic, and finish.
_Avoid_: Style name

**Fresh Direction**:
A concrete direction whose Direction Signature differs from every Shown Direction still available in the current conversation context in at least three parts. It does not promise exact deduplication after earlier history is no longer available.
_Avoid_: Renamed option, palette swap

**Custom Direction**:
A concrete direction supplied through the permanent `D) Custom` option. The option itself is never consumed or deduplicated, but an adopted Custom Direction is recorded like any other shown direction.
_Avoid_: Custom option

**Shown Direction**:
A concrete A, B, or C option that has been presented to the user, whether or not it was selected or generated. An adopted Custom Direction also becomes a Shown Direction.
_Avoid_: Selected direction, generated direction

**Scoped Option Refresh**:
A user-requested replacement of concrete options within one named or contextually identified creative choice area. It preserves identity, output constraints, Explicit Locks, and every unrelated choice area.
_Avoid_: Full restart, universal reroll

**Shown Option**:
A concrete refreshable option that has been presented to the user, whether or not it was selected. An adopted Custom option counts; the `D) Custom` placeholder does not.
_Avoid_: Selected option, option label

**Fresh Option**:
A concrete option that is materially different from every Shown Option still available in the current conversation context for the same creative choice area, according to that area's visible signature.
_Avoid_: Renamed option, palette swap

**Direction Atlas**:
The internal combination vocabulary for producing concrete directions from production context, medium/era, scene and decisive moment, composition grammar, lighting/color logic, and finish. It includes a few curated quality examples but is not a fixed user-facing catalog.
_Avoid_: Style menu, prompt gallery

**Refresh Exhaustion**:
The state in which the skill cannot assemble a complete three-option batch for the requested creative choice area without violating Explicit Locks or that area's freshness threshold. It stops the batch and asks whether to reopen the single explicit field that most restricts variation.
_Avoid_: Silent deduplication fallback

**Direction Gate**:
The existing creative-direction question enhanced by the Direction Atlas. It always offers three concrete directions plus `D) Custom`; a Style Refresh replaces its three concrete directions without adding a new workflow step.
_Avoid_: Style browser, extra style step

**Delegated Refresh**:
A Scoped Option Refresh in which the user asks the skill to decide. The skill selects and records one Fresh Option internally and proceeds without displaying the choice gate; focused risk gates still apply.
_Avoid_: Reusing the previous recommendation

**Explicit Lock**:
A locked value the user directly specified, selected, or overrode. It is recorded as `locked: explicit` and survives any refresh unless the user explicitly asks to change it.
_Avoid_: User-explicit choice, hard lock

**Derived Lock**:
A locked value introduced by a selected option, preview, or accepted recommended defaults rather than directly supplied by the user. It is recorded as `locked: derived`, and a Scoped Option Refresh may reopen it only when it belongs to the requested creative choice area.
_Avoid_: Derived choice, user requirement
