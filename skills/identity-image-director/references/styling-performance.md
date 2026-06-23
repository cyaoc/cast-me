# Styling and Performance Director

Use this reference for wardrobe, headwear, jewelry, accessories, props, makeup, hair styling, role/costume research, pose, action, expression, gaze, hand direction, and performance energy.

## Ownership

This module owns what the person wears, holds, does, and performs. It must respect `identity-anchor.md`: visible likeness and natural non-deformed anatomy are the default recommendation above styling ambition, props, complex actions, expression intensity, and beautification.

When styling or performance conflicts with identity likeness or natural anatomy, simplify wardrobe changes, props, hand work, action complexity, head turn, expression intensity, or beautification before sacrificing likeness or body structure unless the user explicitly chooses a riskier level.

## Risk and Beauty Levels

Use these levels when the coordinating director needs to ask a risk-choice gate or write the accepted tradeoff into the production prompt:

- Stable identity-first: preserve likeness and natural proportions; use subtle expression, simple body direction, calm hands, low prop complexity, and natural retouching.
- Generate one version now: keep the user's requested direction, accept moderate likeness/proportion risk, reduce only the highest-risk variable, and plan for targeted revision if needed.
- Stronger beauty polish: improve skin finish, lighting, complexion, grooming, styling, and photo polish while preserving original facial structure and face proportions.
- Bold attempt: keep strong action, strong expression, obvious beauty retouching, complex hands, or ambitious camera direction; explicitly accept lower likeness or proportion stability.

Beauty retouching should be specific:

- Natural cleanup: remove screenshot/capture artifacts, improve light and skin tone, keep pores/texture and original facial structure.
- Refined editorial polish: cleaner skin, better complexion, stronger grooming/makeup/styling, but no change to face width, eyes, nose, lips, chin, jawline, or age impression.
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

If hand/prop interaction is complex and the reference is a close-up selfie, screenshot, beautified image, or single-angle face reference, prefer simpler hand placement or a safer crop unless the user explicitly chooses a complex action.

## Performance Direction

Pose/action options must cover body direction, gaze, mouth state, and energy level. Keep performance theme-appropriate while preserving identity readability.

Pose and expression should serve the requested theme, not blindly copy the screenshot. Prefer natural, restrained direction over exaggerated posing. Keep both eyes, nose bridge, lips, and face outline clearly visible unless the user asks for a profile or obscured-face concept.

For high-risk source-to-target jumps, reduce performance complexity first:

- prefer calm standing, seated, or slight turn over complex action
- prefer hands calm, lightly posed, or out of frame over intricate finger work
- prefer subtle expression over extreme emotion
- prefer three-quarter or half-body framing over full-body action when body information is missing
- prefer gaze near camera or gently off-camera over extreme profile when identity readability matters
- prefer natural cleanup or refined editorial polish over obvious beautification unless the user explicitly chooses stronger beauty retouching

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
- pose/action, body direction, gaze, mouth state, expression intensity, and energy level
- forbidden styling, props, expressions, or performance notes

For fashion, costume, uniform, or character work, name the visible production anchors rather than writing only a label such as "luxury", "cyberpunk", "old money", "warrior", or "professional". Include what is actually visible: silhouette, garment layers, fabric behavior, closures, trims, accessories, makeup/grooming, and how the person performs the role.

Before generation, check that styling/performance choices are explicit enough for the output type, do not contradict identity preservation, and do not overload the composition with unnecessary wardrobe changes, props, or action complexity.

If the generated output is visible, review whether wardrobe/accessories were preserved or changed as requested, props support the concept without competing, hands/action are natural, expression fits the brief, and styling does not make the person look like a different identity.
