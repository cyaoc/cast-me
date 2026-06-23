# Composition Director

Use this reference for creative direction, shot framing, canvas/aspect, lighting, palette, output recipes, and final prompt structure.

## Creative Direction

After the output type is known, infer the design read:

- audience and use case
- mood words from the user
- reference-image role
- platform or crop needs
- shot direction: composition, camera distance/angle, subject blocking, and background relationship
- styling/performance needs routed through `styling-performance.md`
- reference transfer boundaries: what identity anchors to preserve and what temporary reference state to redesign for the theme
- whether the image should feel photographic, editorial, cinematic, commercial, CG, or social-native

Before proposing options or writing a production prompt, form a compact design read: what the image is for, who will view it, what visual language fits, and which defaults must be avoided. Let the design read pick the aesthetic; do not default to generic AI taste.

Resolve one creative-direction follow-up for every output type unless the user's brief is already detailed enough to write a complete production prompt. This applies to portraits, professional headshots, posters, CG/key art, editorial images, avatars, commercial visuals, and custom themes.

If the user gives a precise theme, use it and ask only for missing production-critical choices. If the theme or art direction is under-specified, present 2-4 concrete viable directions for the user to choose. Each option should differ meaningfully in setting, role/archetype, mood, and output use; it may include sample pose, expression, lighting, or palette as preview hints, but those hints are not resolved choices unless the user explicitly accepts defaults. Do not offer generic labels without visual substance.

When asking beginner users for missing creative choices, include suggested answers. Do not ask only open-ended abstract questions like "what mood, scene, and pose do you want?" Offer 2-4 concrete options with different setting, role/archetype, mood, and output use; keep sample pose, expression, lighting, or palette framed as suggestions, not locked decisions. Always allow the user to mix options or describe their own.

Use this pattern and adapt the option contents to the user's image and requested output type:

```text
I recommend: <recommended direction or concept>, because <one short reason tied to the user's request and reference image>.

Options:
A) <direction name> (Recommended) - <setting/world>, <role/archetype>, <mood>, <output use>
B) <direction name> - <setting/world>, <role/archetype>, <mood>, <output use>
C) <direction name> - <setting/world>, <role/archetype>, <mood>, <output use>
D) Custom / mix-and-match - describe your own theme or combine several directions

Reply with A, or reply with "B + use recommended defaults". If you reply with only B, I will ask the next missing dimension, such as styling/performance, aspect ratio, or lighting/color.
```

The visual details inside creative-direction options are previews. If the user replies with only a direction letter/name, continue the serial ladder and ask the next unresolved dimension. Treat preview details as final only if the user accepts defaults or repeats them explicitly.

For practical formats such as LinkedIn, resume, social avatar, or realistic portrait, options should still be concrete, such as different background types, crop, expression, wardrobe treatment, lighting, palette, and polish level. Do not skip the direction follow-up just because the output type is conventional.

Use concrete visual language. Prefer materials, light, camera, location, props, and composition over vague praise like "stunning", "high quality", or "cinematic" alone.

## Shot Direction

Shot direction may resolve composition, crop, camera distance/angle, subject blocking, and background relationship in one decision. Use `styling-performance.md` for exact pose/action, expression, gaze, hands, props, and performance complexity. If shot direction also resolves those choices, skip the later pose/action question unless a production-critical detail remains unresolved.

For realistic portraits, personal photoshoots, lifestyle portraits, social portraits, and beauty/editorial portraits, ask a lightweight portrait shot-direction question unless the user already specified crop, pose, expression, hands, background/props, or accepted recommended defaults. Portraits are common but still need directed composition and performance.

For LinkedIn, resume, professional headshot, business avatar, or simple social avatar requests, keep the gate lightweight: crop and background. Use `styling-performance.md` for expression and wardrobe/accessory treatment. Do not ask a full Director Shot Plan or introduce props unless the user requests them.

```text
I recommend: clean three-quarter portrait direction, because it preserves identity while giving the image a natural, intentional photoshoot feel.

Options:
A) Clean three-quarter portrait (Recommended) - upper body to mid-thigh, relaxed posture, natural gaze, subtle expression, hands calm or out of frame, no unnecessary props
B) Full-body lifestyle portrait - complete body visible, natural proportions, simple stance, environment supports the person without competing
C) Close portrait / beauty-style crop - face and shoulders prioritized, stronger expression, shallow depth, no full-body accuracy needed
D) Custom - specify crop, pose, expression, hands, background, or props

Reply with A, or reply with "B + seated pose + soft smile + no props".
```

For cinematic posters, editorial/magazine images, commercial campaign visuals, CG/game key art, full-body/action outputs, story-heavy concepts, product/prop interaction, or requests for a filmic/editorial/high-fashion/hero image, ask a fuller Director Shot Plan unless already specified:

```text
I recommend: three-quarter hero composition with controlled performance, because it balances identity preservation with a stronger directed image.

Options:
A) Three-quarter hero shot (Recommended) - upper body to mid-thigh, slight natural head turn, controlled gaze, clear hands, one clean background relationship, no unnecessary props
B) Full-body environmental shot - complete body visible, natural proportions, readable stance, background supports the story without competing
C) Cinematic close-medium shot - face and shoulders dominate, stronger emotion, shallow depth, no full-body accuracy needed
D) Custom - specify composition, camera angle, action, expression, hands, props, and background relationship

Reply with A, or reply with "B + walking pose + looking past camera + one umbrella prop".
```

Lighting/color options must cover key/fill/rim light, palette, skin/metal/fabric rendering, and forbidden color mood when relevant.

## Taste Rules

- make one clear hero subject; supporting details must not compete with the person
- use negative space deliberately for posters, covers, avatars, and commercial layouts
- keep one coherent palette with one restrained accent
- define forbidden palette/mood when the theme depends on color discipline
- separate materials, lighting, and palette instead of compressing them into "premium"
- include 5-12 concrete scene details when the background matters
- avoid default AI tells: purple-blue glow, random orbs or blobs, automatic centered hero layouts, generic beige/brass "premium" styling, fake brand logos, unreadable microtext, stock-photo cliches, cheap plastic CG, over-smoothed skin, and template-like card/poster layouts
- use typography only when it has a job and exact user copy exists

## Prompt Craft Rules

Use these cross-output rules when writing the final production prompt:

- Put canvas, aspect ratio, crop, and layout before subject detail when structure matters.
- If required in-image text exists, quote every exact string and specify its hierarchy, such as title, subtitle, CTA, price/date, label, or fine print.
- State scene density with concrete objects, surfaces, spatial layers, and environmental details rather than empty adjectives.
- Keep materials, lighting, palette, and camera/capture context as separate controls.
- For posters, covers, editorials, and commercial visuals, use the three-glance test: first glance reads the hero subject or silhouette, second glance reads the world or message, third glance rewards inspection with texture and detail.
- For layouts with annotations, labels, panels, UI, diagrams, or multi-image boards, define fixed regions, panel roles, labels, spacing, and readability constraints before style detail.
- Use negative constraints only for likely failure modes. Keep avoid lists short, targeted, and tied to the output type.

## Output Recipes

Use these recipes as prompt vocabulary after the relevant choices are resolved. Do not let a recipe silently decide unresolved production-critical choices such as styling/performance, aspect ratio, text, lighting, palette, or avoid-list.

### Realistic Portrait

Use realistic photography language: capture context, 50mm or 85mm portrait lens, natural skin texture, soft light, shallow depth of field, believable wardrobe, ordinary imperfections, and a clean but not empty background.

Avoid CG polish, fantasy styling, poster typography, and unreal materials.

### Professional Headshot

Use a clean background, restrained retouching, confident but natural expression, business/editorial lighting, and realistic face preservation.

Do not default to replacing distinctive original clothing or headwear with a blazer. Use `styling-performance.md` for unresolved wardrobe treatment when visible wardrobe/headwear is distinctive or could affect the output.

Avoid dramatic costume changes, fantasy scenes, and heavy stylization.

### Cinematic Poster

Use strong silhouette, dramatic key light, rim light, atmospheric background, title-safe composition, bold color contrast, and cinematic grading. Pass the three-glance test: the silhouette reads first, the narrative world reads second, and close details reward inspection.

Only include text if the user provides exact text. If text treatment is unresolved and relevant to the output, ask in the aspect/text clarification. If the user accepts defaults or text is not relevant, specify no text. When text exists, define promotional hierarchy and readability distance rather than placing all text at equal weight.

### CG or Game Key Art

Use premium concept-art finish, detailed materials, cinematic environment, dynamic but identity-preserving pose, and stylized lighting. Define the world, camera angle, costume/material system, and readable silhouette.

Do not over-stylize the face until the person becomes unrecognizable.

### Editorial or Magazine Image

Use fashion lighting, refined palette, clean pose direction, luxury styling, negative space, strong typography-safe areas, and cover-like composition.

Only include typography with exact user-provided copy. If text treatment is unresolved and relevant to the output, ask in the aspect/text clarification. If the user accepts defaults or text is not relevant, specify no text. Keep typography-safe negative space and avoid fake magazine cover clutter.

### Social Avatar

Use clear face readability at small size, simple background, strong silhouette, and polished composition. If the crop is unresolved, recommend a square crop for avatars in the aspect/crop clarification rather than silently applying it.

Avoid dense background detail, small text, and complex full-body staging.

### Commercial Campaign Visual

Use the provided product or brand mood if any, controlled composition, premium lighting, simple message hierarchy, and usable negative space.

Do not invent brand names, slogans, logos, or product claims.

## Prompt Structure

Use this structure as flexible scaffolding for generation prompts, not a form to fill.

After the user chooses a direction or supplies enough brief detail, write a complete production prompt for every output type. Complete means all production-critical choices are resolved for the chosen output, not that every possible field is present. Do not use a short generic summary. Do not replace the production prompt with a compact config block unless a complex commercial, product, UI, diagram, or multi-system image would benefit from structured slots. Each relevant dimension must include concrete positive visual direction and necessary negative constraints.

Omit irrelevant dimensions instead of inventing filler. Never keep placeholder rows, empty labels, generic no-op values, or fields that do not help the current request.

Consider these dimensions when relevant:

- identity priority: same person, face anchor, no face redesign
- reference transfer boundaries: identity anchors to preserve; temporary source state not to copy, such as pose, expression, face angle, crop scale, selfie perspective, screenshot artifacts, or lighting
- source sufficiency: whether missing full-body scale, side/profile structure, posture, outfit, or expression range is inferred naturally, described by the user, or supplied by extra real references
- shot direction: portrait or director plan covering composition, camera distance/angle, subject blocking, and background relationship
- styling/performance: wardrobe/accessory structure, hair/makeup, props, pose/action, expression, gaze, hands, and energy level from `styling-performance.md`
- world/setting: location, architecture/nature/props, spatial layers, atmosphere, scale, story context
- composition/camera: crop, subject placement, symmetry/asymmetry, lens feel, distance, angle, perspective limits
- face visibility: eyes, nose bridge, lips, and face outline visible; avoid major occlusion
- lighting: key/fill/rim light, volume light, reflections, how light hits face, hair, wardrobe, and accessories
- palette: main colors, support colors, accent colors, forbidden colors or moods
- texture/detail: skin, hair, fabric, metal, props, environmental surfaces
- negative constraints: no text unless exact copy, no watermark, no fake brands, no random UI, no theme-breaking elements

The expanded prompt should be theme-adaptive. Do not reuse examples such as forests, temples, cyberpunk, saints, warriors, or luxury studios unless the user chose that direction. Delete rows that do not help the specific output.

```text
Use case: identity-preserve
Asset type: <selected output type>
Canvas/aspect: <ratio, crop, platform, or size intent>
Layout contract: <subject placement, negative space, text-safe areas, panel/region structure, or "simple single-image layout">
Input image: reference for the person's visible identity
Primary request: <user request>
Identity and reference transfer: <same person; face anchor details; what identity anchors to preserve; what temporary source state not to copy; whether missing body scale, angle, or expression details are inferred or user-supplied>
Priority order: preserve visible identity likeness first; keep natural non-deformed anatomy second; simplify composition, scene, styling, performance, hands, props, or lighting before sacrificing likeness or anatomy
Creative direction: <style, world/setting, hero hierarchy, mood, and useful scene details>
Shot direction: <portrait shot direction or director shot plan; composition, camera distance/angle, subject blocking, and background relationship>
Subject identity/anatomy: <face visibility, crop, camera, perspective limits, natural adult proportions, realistic head-to-body scale, identity through facial structure instead of enlarged head size, and perspective-aware face angle>
Wardrobe/materials: <from styling-performance.md; preserve / subtly polish / replace because requested; include important materials and accessory constraints>
Performance/props: <pose/action, expression, gaze, mouth state, hands, props, and performance complexity>
Lighting/color/materials: <key light, fill/rim/volume light when useful, palette, material behavior, and forbidden colors or moods>
Text: <exact text in straight quotes; hierarchy and placement; or "no text">
Constraints: no identity drift, no face redesign, no automatic beautification into a different face, no age drift, no ethnicity drift, no extra people unless requested, no watermark, no random text, no fake brands, no distorted face or hands, do not remove original wardrobe/accessories unless requested, do not copy close-up crop scale into full-body output, do not paste a frontal face onto an angled pose, no stiff copied expression, no oversized head or tiny body; add output-adaptive quality negatives and safety framing when relevant
```

Before generation, check that output type, canvas, layout contract, crop, text treatment, portrait shot direction or director shot plan, scene, lighting, palette, materials, quality negatives, and theme-breaking constraints are concrete enough for the output type. Use `styling-performance.md` to check wardrobe, props, pose/action, expression, gaze, hands, and performance complexity.

If the generated output is visible in the current thread, review whether the output matches the requested type, canvas, crop, styling/performance, lighting, palette, and text treatment; whether there is one clear hero subject; whether supporting details do not compete; whether styling, materials, background, props, hands, action, and expression are specific enough and natural; and whether there are unwanted text artifacts or obvious AI tells.
