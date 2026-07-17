# Identity Image Direction

This context describes how the skill preserves a person's identity while guiding creative image-direction choices across a conversation.

## Language

**Primary Identity Anchor**:
The actual person reference image that authoritatively anchors face identity for generation or editing. Supporting images and text may add evidence but never replace or override it.
_Avoid_: Primary identity reference, text-only identity description

**Protected Identity Cue**:
A visible structural, surface, or external characteristic whose replacement or occlusion could materially reduce recognizability, such as facial relationships, skin tone, age impression, hairline, or a distinctive mark. Risk depends on changing these cues, not on whether styling is labeled light or heavy.
_Avoid_: Makeup intensity, beauty feature

**Visible Body Evidence**:
Clearly shown body relationships at any source crop, such as head-to-neck-to-shoulder scale, shoulder width, chest volume, visible torso shape, and body build; they are preserved by default and named neutrally and concretely across styling changes without a separate Choice Gate. Obscured or off-frame anatomy is not evidence and must not be guessed as if verified.
_Avoid_: Full-body identity, inferred anatomy

**Inference Boundary**:
The explicit set of missing reference evidence that the user permits CastMe to estimate. Accepting inference never reclassifies verified evidence or authorizes guessing a different missing region, angle, appearance cue, or performance fact.
_Avoid_: Blanket body inference, general likeness risk

**Structural Scale Failure**:
A result state in which multiple connected body-scale relationships fail together, or a proportion repair requires expanding a partial crop. It is distinct from one isolated, minor proportion deviation inside an otherwise coherent crop.
_Avoid_: Small local edit, canvas-size problem

**Reference Appearance**:
The visible facial styling, grooming, and hair state shown by a person reference when its makeup status or source is unknown. It may be preserved or explicitly restyled, but it is not evidence of the person's unseen bare-face appearance.
_Avoid_: Natural look, bare face, original makeup

**Appearance Coverage**:
The visible evidence for the Protected Identity Cues needed by the target look. Unknown makeup alone is not a gap; coverage is missing only when styling, filters, or occlusion hide target-critical cues.
_Avoid_: Bare-face requirement, makeup detection

**Delegated Styling**:
A user instruction that asks CastMe to design makeup, hair, wardrobe, or accessories from the story or decide the look. It resolves Styling Direction internally without visible options, while focused identity-risk choices remain available.
_Avoid_: Styling defaults, implicit makeup choice

**Styling Direction**:
A complete character-look choice that coordinates makeup, hair, wardrobe, and accessories across only the unlocked fields that need change. It preserves compatible Reference Appearance and may narrow to one styling field when the user explicitly preserves the others.
_Avoid_: Makeup Gate, separate styling menus, fixed look preset

**Character Read**:
The intended visible impression of the depicted person, supplied by the user or story or proposed as creative direction. It guides styling and performance but is not an inference about the person's actual personality.
_Avoid_: True temperament, personality diagnosis, face-based personality inference

**Story Makeup**:
Intentional visible facial styling or condition that expresses the Character Read, including designed fatigue, weathering, injury, ritual, or cosmetic treatment. It is a Styling lock that First-Pass Finish must render rather than remove as a temporary blemish.
_Avoid_: Retouch target, accidental blemish, finish effect

**Look Continuity**:
The locked base makeup, hair, wardrobe, and accessories that identify one character look across a requested series, together with explicit story-state changes such as wetness, wear, injury, or cosmetic breakdown. It is not exact visual sameness between moments.
_Avoid_: Identical styling state, independent redesign

**Identity Review**:
A structured visual comparison of a result against the Primary Identity Anchor through its Protected Identity Cues, Visible Body Evidence, and relevant structural scale relationships. It reports visible drift and never claims a biometric match, similarity score, or identity guarantee.
_Avoid_: Face score, biometric verification, identity guarantee

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

**Choice Gate**:
A user-visible A/B/C/D decision that resolves one scoped choice or tightly coupled group. A through C are valid concrete paths, with an explicit stop path when only two substantive resolutions exist; D is always the Custom Path.
_Avoid_: Open-ended question, padded preset menu

**Custom Path**:
The permanent `D) Custom` affordance in every Choice Gate. It accepts a user-supplied resolution only within that gate's valid scope; the placeholder itself creates no lock or history entry.
_Avoid_: Fourth preset, unrestricted override

**Custom Direction**:
A concrete Creative Direction supplied through the Custom Path. Once adopted, it is recorded like any other shown direction, while the reusable Custom Path remains available.
_Avoid_: Custom Path, custom option placeholder

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
