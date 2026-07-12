# Styling and Performance Director

Use this reference for wardrobe, headwear, jewelry, accessories, props, makeup, hair styling, role/costume research, pose geometry, action, expression, gaze, hand direction, and performance energy.

## Ownership

This module owns what the person wears, holds, does, and performs. It does not own framing, crop, camera position, subject placement, spatial layers, or background relationship; those belong to `composition-director.md`. Inside locked user intent, it must respect the identity and geometry quality constraints in `identity-anchor.md`.

When styling or performance conflicts with identity or geometry, first simplify only unresolved, unsupported, non-story-critical details. Never alter a locked action, head direction, gaze, hand interaction, or styling choice without a risk-choice gate.

Before asking about wardrobe, props, pose, expression, gaze, hands, or beauty level, read the coordinating director's decision state. Do not ask for locked composition, crop, camera angle, scene, action, expression, wardrobe, or beauty level again. If earlier composition or creative-direction options suggested pose, expression, hands, lighting, or styling, refine within those suggestions instead of reopening a generic performance menu.

## Risk and Beauty Handling

When a risk gate is needed, derive its options from the actual unsupported fields and locked intent. Relevant options add evidence or description, accept labeled inference, or stage the work around the actual gap. Do not use a universal stable/bold ladder, and do not treat intentional projected size change under a locked camera as anatomy instability.

Beauty retouching should be specific:

- Natural cleanup: remove screenshot/capture artifacts, improve light and skin tone, keep pores/texture and original facial structure.
- Refined editorial polish: cleaner skin, better complexion, stronger grooming/makeup/styling, but no redesign of intrinsic face width, eyes, nose, lips, chin, jawline, or age impression.
- Obvious beautification: idealized face shape or features may reduce likeness; require explicit user acceptance before using this level.

## Category Routing

When the requested image has a clear genre, route styling and performance through the closest category instead of using generic fashion or cinematic language:

- Photography / lifestyle: capture context, ordinary imperfections, real-world wardrobe behavior, believable hand placement, and natural expression.
- Fashion editorial: garment silhouette, fabric behavior, styling concept, accessory logic, grooming, pose line, and how the body relates to space.
- Cinematic poster or film still: role, silhouette, readable attitude, restrained expression, prop symbolism, and performance that supports the story world.
- Character design or game key art: costume system, layers, material motifs, signature props, stance, expression range, and silhouette readability.
- Professional headshot or avatar: identity readability, restrained grooming, calm expression, simple wardrobe decision, and no unnecessary props.

Use the category only as a production lens. Do not let a category override the user's stated wardrobe, identity anchors, safety handling, or natural anatomy.

## Styling Direction

Resolve wardrobe, headwear, jewelry, accessories, makeup, hair styling, and props when they are production-critical or visually important.

Do not replace distinctive clothing, headwear, jewelry, accessories, hairstyle, or makeup unless the user requests replacement, accepts defaults that include replacement, or the chosen concept makes replacement unavoidable.

If the output type is known, the user has not specified wardrobe/accessory treatment, and the original clothing, headwear, jewelry, or accessories are visually important or may conflict with the requested format, ask one short follow-up before generation.

If a creative direction already suggested a styling lane, such as lifestyle, street photo, editorial, professional, cinematic, or character design, wardrobe/accessory options must stay inside that lane unless the user reopens the direction.

Do not combine wardrobe/accessory treatment into the creative-direction question unless the user already specified it or it is inseparable from the requested concept. If wardrobe/accessory treatment is still missing after the direction is chosen, ask it as the next serial clarification.

For LinkedIn, professional headshot, resume, or business-avatar requests, do not assume the outfit or headwear should be replaced. If distinctive wardrobe, headwear, jewelry, or accessories are visible and the user did not say whether to keep or change them, ask:

```text
I recommend: keep the original outfit, headwear, and accessories, then polish them for the professional context, because these are the strongest visual identity cues in the reference and replacing them can shift the final image too far.

Options:
A) Keep as-is and elevate the finish (Recommended) - remove livestream elements; preserve clothing, headwear, jewelry, and wearing method; make the background and lighting LinkedIn-ready
B) Simplify moderately - keep the most recognizable headwear or silver jewelry while reducing strong stage styling for a more business-appropriate avatar
C) Replace with a new professional look - use a blazer, shirt, or simple business outfit while preserving the same face identity
D) Custom - specify which outfit, headwear, or accessories to keep or replace

Reply with A, or reply with "B + square 1:1 + no text + avoid overly corporate styling".
```

Do not add process narration, explain skill/tool usage, or describe why the follow-up is needed.

## Props

Use props only when they support the story, product, role, task, or user request. If props are unresolved or unnecessary, specify no unnecessary props rather than inventing decorative objects.

When props are used, define:

- prop identity and purpose
- whether the person holds, wears, touches, points to, or stands near it
- hand visibility and hand complexity
- whether the prop should be foreground, background, or secondary
- what must not appear, such as fake logos, random text, unreadable labels, or extra products

If hand/prop interaction is complex and unsupported by the reference, expose that coverage gap. Offer simpler hand placement or a safer crop only when those fields remain unresolved or the user voluntarily chooses the tradeoff.

## Performance Direction

Pose/action options must cover body direction, gaze, mouth state, and energy level. Keep performance theme-appropriate while preserving identity readability.

Describe performance choices as visible behavior, not acting jargon: where the body turns, what the hands do, where the eyes land, whether the mouth is relaxed or active, and how restrained or forceful the moment feels. For example, distinguish a quiet pause with gaze beyond camera from an engaged task with hands occupied or a stronger action with accepted identity/anatomy risk. Adapt the behavior to the locked decisive moment.

Selecting performance does not lock framing, camera, background, lighting, or color. If those dimensions are unresolved, keep any previewed details suggested for their own later questions.

If the user already chose an action, do not ask "what action" again. Ask only the unresolved performance detail, such as expression intensity, gaze, hand simplification, or risk level. If an action was suggested but not locked, offer refinements that inherit it, such as lighter, more dynamic, or safer variations.

Pose and expression should serve the requested theme, not blindly copy the screenshot. Apply the angle-aware identity rules from `identity-anchor.md`: never turn the face back toward camera merely to expose both eyes. Prefer restrained direction only when the user has not locked a stronger performance.

## Pose Geometry

For non-trivial action, write one coherent chain using only the links relevant and visible in the chosen frame:

- ground contact and support point
- weight-bearing leg, seat, or contact surface
- pelvis and hip direction
- torso/ribcage and shoulder rotation
- neck, head turn, and tilt
- facial plane and gaze
- hands, props, and follow-through

Every link must agree with the locked camera and perspective. Do not write only "natural dynamic pose", attach decorative limbs to a static torso, or turn the head independently of neck and shoulders.

For high-risk source-to-target jumps, simplify only unresolved, unsupported, and non-story-critical performance details. Never change a locked action, head direction, gaze, framing, or camera intent without a risk-choice gate. Prefer simpler hands, props, or expression only when those fields remain unresolved or the user selects that tradeoff.

Avoid:

- stiff copied expression, selfie gaze, or frozen reference-photo mouth shape
- expressions that fight the theme, such as goofy, blank, aggressive, overly seductive, or modern selfie expressions when they do not fit
- extreme head turns or profiles when they do not serve the requested concept or identity readability
- hands, props, hair, accessories, or shadows covering major facial features
- hand poses that require precise finger articulation unless the hands are central to the request

## Role, Costume, and Visual Research

Use visual research when the requested styling depends on named or specific visual canon, such as named character cosplay, recognizable occupational uniforms, historical dress, sports/team gear, ceremonial dress, fantasy archetypes, or culturally specific costume systems.

For named character cosplay, research the character's visual traits online before writing character-specific options or a production prompt unless the user provides sufficient reference images or a detailed character brief.

Use reliable visual sources first: official character pages, publisher/studio/game pages, official art, production stills, or reputable character wikis with images. Extract only visual production anchors:

- character, role, profession, or costume version
- hair shape, color, length, bangs, and silhouette
- outfit silhouette, layers, materials, color blocking, armor or fabric details
- signature accessories, symbols, props, weapons, tools, or motifs
- makeup, facial styling, posture, and recognizable attitude
- palette, lighting genre, world context, and details that must not be added

If the character, uniform, role, or costume has multiple major variants, ask the user to choose the version with the standard decision format before generation. Do not rely on memory for niche, current, or visually complex characters. If online research is unavailable or inconclusive, ask the user for reference images or a styling brief instead of guessing. If web research was used, keep source links available for the response.

## Prompt Contributions

When writing the production prompt, include styling/performance details only when relevant:

- wardrobe/headwear/jewelry/accessories: preserve, simplify, polish, or replace because requested
- hair/makeup/grooming constraints, especially if visible identity depends on them
- beauty level: natural cleanup, refined editorial polish, or obvious beautification with accepted likeness risk
- materials, color, pattern, layers, cut, fit, silhouette, wearing method, weathering, and distinctive details
- prop purpose, hand relationship, and hand complexity
- pose/action plus relevant support, weight, pelvis, torso/shoulder, neck/head, facial-plane, gaze, mouth, hand/prop, and energy relationships
- forbidden styling, props, expressions, or performance notes

For fashion, costume, uniform, or character work, name the visible production anchors rather than writing only a label such as "luxury", "cyberpunk", "old money", "warrior", or "professional". Include what is actually visible: silhouette, garment layers, fabric behavior, closures, trims, accessories, makeup/grooming, and how the person performs the role.

Before generation, check that styling/performance choices are explicit enough for the output type, do not contradict identity preservation, and do not overload the composition with unnecessary wardrobe changes, props, or action complexity.

If the generated output is visible, review whether wardrobe/accessories changed as requested, props support the concept, all relevant visible pose relationships are coherent with the camera and action, expression fits the brief, and styling does not change identity.
