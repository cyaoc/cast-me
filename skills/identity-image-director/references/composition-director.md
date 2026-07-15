# Composition Director

Use this reference for creative direction, Style Refresh, Direction Atlas and freshness tracking, decisive moment, shot framing, perspective intent, camera/capture and projection contracts, art direction, canvas/aspect, lighting/color/finish, delivery, output recipes, and final prompt structure.

## Creative Direction

After the output type is known, infer the design read:

- audience and use case
- mood words from the user
- the decisive moment for story-bearing images: what is happening now, what just happened or may happen next, and what the audience should feel first
- reference-image role
- platform or crop needs
- shot direction: composition, camera distance/angle, subject blocking, and background relationship
- styling/performance needs routed through `styling-performance.md`
- reference transfer boundaries: what identity anchors to preserve and what temporary reference state to redesign for the theme
- whether the image should feel photographic, editorial, cinematic, commercial, CG, or social-native

Before proposing options or writing a production prompt, form a compact design read: what the image is for, who will view it, what visual language fits, and which defaults must be avoided. Let the design read pick the aesthetic; do not default to generic AI taste.

Before asking any composition question, read the coordinating director's decision state. Do not ask for a locked output type, scene concept, aspect ratio, crop, shot distance, camera angle, or text treatment again. If a prior option suggested shot, pose, lighting, or palette details, use those suggestions as the starting point for the next options instead of offering a generic menu.

Resolve creative direction whenever it is still production-critical. Do not force a direction question when a practical use and the user's desired read already define it; posters, editorials, commercial visuals, key art, and story-heavy portraits usually need a distinct direction choice unless already specified.

If the user gives a precise theme, use it and ask only for missing production-critical choices. If the theme or art direction is under-specified, or the user requests a Style Refresh, use the Direction Atlas below. Every visible Direction Gate contains exactly three concrete directions labeled A through C plus the permanent `D) Custom` option.

When asking beginner users for missing creative choices, include suggested answers. Do not ask only open-ended abstract questions like "what mood, scene, and pose do you want?" Offer concrete options with visibly different production choices; keep sample camera, styling, performance, lighting, or palette framed as suggestions, not locked decisions. Always allow the user to mix options or describe their own.

### Direction Atlas and Freshness

Use the Direction Atlas only while creative direction is unresolved or during a Style Refresh. It is an internal combination vocabulary, not a fixed catalog or prompt gallery. Represent every concrete option with a Direction Signature containing:

| Part | What to define |
| --- | --- |
| Production context | The image's use, audience read, and production lane |
| Medium / era | The visible making tradition and period logic |
| Scene and decisive moment | Where the person is and what is happening now |
| Composition grammar | Subject scale, placement, spatial structure, and graphic rhythm |
| Lighting / color logic | Motivated light and the role of color, not a palette name alone |
| Finish | Surface, texture, material rendering, and final image character |

Quality-example shapes only; adapt them to the brief rather than treating them as reusable defaults:

- contemporary documentary editorial + tactile 35mm observation + a public-space transition + layered off-center framing + available mixed light + restrained grain
- mid-century graphic campaign + cut-paper or screen-print construction + one symbolic action + flat poster hierarchy + two-color contrast + imperfect ink texture
- speculative artifact portrait + sculptural digital realism + a ritual or technical threshold + monumental negative space + material-driven glow and shadow + weathered tactile finish

Generate candidates sequentially. A Fresh Direction differs from every Shown Direction, including candidates already chosen for the current batch, in at least three Direction Signature parts. A renamed option, palette-only change, creator name, camera brand, lens token, or minor prompt variation is not fresh.

Track Shown Directions only in the current conversation:

- Record every presented A, B, and C immediately, whether selected or generated.
- Never record or consume the `D) Custom` placeholder. When the user adopts a concrete Custom Direction, derive its Direction Signature and record it.
- Record a direction selected internally during a Delegated Refresh.
- Do not add persistence or require prior-session history.

Freshness limits automatic recommendations, not user intent. If the user explicitly restores a Shown Direction, honor it.

### Style Refresh

A Style Refresh reopens the selected creative direction and may reopen only direction-owned `locked: derived` values. Preserve identity, output requirements, and unrelated `locked: explicit` values such as aspect ratio, exact text, wardrobe, action, gaze, or composition unless the user explicitly reopens them.

Route the user's wording precisely:

- An ordinary request for more or different directions uses the Direction Atlas and conversation-local history without browsing.
- `Only change the visual style` reopens medium/era, lighting/color, material treatment, and finish. Preserve scene, action, composition, subject placement, and every unrelated Explicit Lock.
- `Completely change the direction` reopens creative direction and its derived scene, unlocked composition suggestions, lighting/color, and finish. Preserve identity, output requirements, exact text, and every unrelated Explicit Lock.
- A request that explicitly asks for currentness with words such as current, recent, latest, trending, or this year, or asks for trends tied to a date, is a Trend Refresh. A historical date or era without current/trend intent is an ordinary creative constraint. Use live visual research, extract concrete production anchors, keep source links available, and apply the same freshness threshold. If research is unavailable, say currentness could not be verified; do not guess.
- If the user delegates with `you decide`, `pick one`, or equivalent wording, perform a Delegated Refresh: bypass the visible Direction Gate, select and record one compatible Fresh Direction, apply recommended defaults, and continue. Focused identity, reference-coverage, safety, and exact-text gates still apply.

If Explicit Locks leave fewer than three Fresh Directions, declare Refresh Exhaustion. Keep the three-part threshold, identify the single Explicit Lock most responsible, and ask with the standard decision format whether to reopen only that dimension. Offer bounded ways to reopen that one dimension, plus a path that keeps every lock and stops refreshing; never offer a non-fresh batch or relax unrelated locks.

Use this pattern and adapt the option contents to the user's image and requested output type:

```text
I recommend: <recommended direction or concept>, because <one short reason tied to the user's request and reference image>.

Options:
A) <direction name> (Recommended) - <setting/world>, <role/archetype>, <visible decisive moment when relevant>, <mood and output use>
B) <direction name> - <setting/world>, <role/archetype>, <visible decisive moment when relevant>, <mood and output use>
C) <direction name> - <setting/world>, <role/archetype>, <visible decisive moment when relevant>, <mood and output use>
D) Custom - describe your own theme or combine several directions

Reply with A, or reply with "B + use recommended defaults". If you reply with only B, I will ask the next missing dimension, such as shot direction, styling, performance, aspect/text, or lighting/color.
```

The visual details inside creative-direction options are suggested previews. If the user replies with only a direction letter/name, record the chosen creative direction as `locked: explicit` and continue the adaptive ladder with the next unresolved dimension. Values supplied by the direction itself are `locked: derived` only when the option explicitly makes them part of its premise; camera, styling, performance, lighting, palette, or finish previews remain `suggested`. Accepting recommended defaults converts relevant previews to `locked: derived`; repeating or overriding one converts it to `locked: explicit`.

For LinkedIn, resume, social-avatar, or other practical formats, skip creative direction when the use and desired read already define it. If direction remains ambiguous, offer concrete practical outcomes rather than story-world concepts; later shot, styling, performance, and lighting decisions remain separate.

Use concrete visual language. Prefer materials, light, camera, location, props, and composition over vague praise like "stunning", "high quality", or "cinematic" alone.

## Directorial Intent and Decisive Moment

For story-bearing images, turn mood words into a visible moment: what the person is doing, what just happened or may happen next, the first audience impression, and one or two details that prove the story.

Do not translate cinematic, premium, relaxed, or story-driven into color grading alone. If several moments fit, offer plain visible choices. A selected moment explicitly locks its stated setting, action, and story evidence; camera, styling, lighting, and any unstated expression, gaze, hands, or energy remain suggested for later decisions.

## Shot Direction

Shot direction owns scene framing, subject scale/body cutoff, camera position/distance/viewpoint, perspective strength, allowed projection exaggeration, subject placement, spatial layers, and background relationship. It does not own pose/action, expression, gaze, mouth state, hands, or energy; route those to `styling-performance.md`. Any performance detail previewed here remains suggested until its own dimension is chosen.

If scene concept or creative direction is already locked, shot-direction options must be variants within that direction, not a new style or scene menu. If subject scale/body cutoff, camera distance, or angle is already locked, ask only the unresolved shot part, such as placement or background relationship.

For realistic, lifestyle, social, and beauty/editorial portraits, ask a lightweight shot-direction question unless framing, camera/viewpoint, subject placement, and background relationship are already resolved or accepted through recommended defaults. Performance details alone do not resolve shot direction.

For LinkedIn, resume, professional headshot, business avatar, or simple social avatar requests, keep the gate lightweight: crop and background. Use `styling-performance.md` for expression and wardrobe/accessory treatment. Do not ask a full Director Shot Plan or introduce props unless the user requests them.

```text
I recommend: show the person from the waist up, because the face stays clear while the background can still explain the setting.

Options:
A) Show the person from the waist up (Recommended) - camera around eye height, face easy to read, background still shows where they are
B) Show the whole body - the setting carries more of the story, but more body reference is needed
C) Move closer to the face and shoulders - expression becomes the focus and the background matters less
D) Custom - say how much of the body to show, whether the camera looks from above/level/below, where the person sits in frame, and how much background remains

Reply with A, or reply with "B + camera near eye level + person on the right + deep station background".
```

For cinematic posters, editorial/magazine images, commercial campaign visuals, CG/game key art, full-body/action outputs, story-heavy concepts, product/prop interaction, or requests for a filmic/editorial/high-fashion/hero image, ask a fuller Director Shot Plan unless already specified:

```text
I recommend: show the person from the upper body to mid-thigh, because both the face and the story world remain easy to read.

Options:
A) Upper body to mid-thigh (Recommended) - person reads first, one clear background layer supports the story, and room can remain for a title
B) Whole body in the setting - show something near the camera, the person, and a deeper background; body-reference requirements are higher
C) Move closer to face and shoulders - emotion reads first and only a few background clues remain
D) Custom - say how much body to show, whether the camera looks from above/level/below, where the person sits, and where title or background space should remain

Reply with A, or reply with "B + camera near waist height + long station platform behind + title space above".
```

## Perspective Intent

When perspective materially changes the requested image and remains unresolved, ask one plain-language choice adapted to the theme:

- physically strong perspective - accept pronounced near/far size change and foreshortening as part of the shot
- strong viewpoint with controlled projected proportions - preserve spatial impact while restraining head/body exaggeration
- proportion-first perspective - reduce projection drama to favor stable identity and familiar body scale
- custom - describe which parts should feel nearer, larger, shorter, or more stretched

These are semantic lanes, not fixed presets. Do not use fixed angles, focal lengths, or equipment unless the user supplied them, and still describe their visible consequence. The selection locks viewpoint/distance character, perspective strength, and allowed projection exaggeration; it does not silently lock action, expression, styling, or lighting.

If camera perspective is already locked, skip this question. Preserve it through any later reference-coverage or risk gate.

## Camera and Capture Plan

Translate the selected shot into an internal capture plan using controls that change a visible result:

- camera height, angle, subject distance, and perspective character
- wide environmental feel, natural perspective, or telephoto-like compression
- underlying human anatomy: the person's world-space head, shoulders, torso, hips, limbs, and joints remain structurally valid
- projected image proportions: apparent size and foreshortening follow distance, viewpoint, and the selected perspective strength
- focus placement and shallow, moderate, or deep depth distribution
- frozen action, natural motion blur, or long-exposure character when motion matters

Focal length, aperture, shutter speed, ISO, white balance, format, or equipment names are optional aesthetic vocabulary, not required fields. Tie each one used to a visible consequence. If the user asks for parameter styling, label numbers as approximate visual cues; never claim a physically valid exposure or lighting rig from the generation brief alone.

## Lighting, Color, and Finish

Lighting must be motivated by the scene rather than a generic list of key/fill/rim lights. Resolve the believable source, direction, height, apparent size, softness, falloff, face exposure, fill or negative fill, catchlight, and subject/background separation when relevant.

Name a modifier or shaping method only when it clarifies the visible effect, such as large diffusion, bounce, Fresnel-like hard light, flag/negative fill, grid, or gobo.

Also define skin-tone priority; the warm/cool, brightness, contrast, and saturation relationship between person and environment; and useful finish such as highlight roll-off, shadow detail, grain, halation, sharpness, and material rendering.

Ask in visible outcomes: soft window-like light feels natural and close; motivated side light creates stronger shape and tension; polished frontal beauty light feels cleaner and more commercial. Adapt the actual options to the locked concept.

Do not rely on camera brands, precise light power, empty LUT names, or generic terms such as "8K", "HDR", and "masterpiece" to create professional results.

## Art Direction and Physical World

Treat art direction as internal synthesis of the locked world, shot, styling, and lighting, not as another user gate. If a required choice is unresolved, route it to its owning dimension.

When the setting matters, define time/weather, believable spatial logic, foreground/midground/background roles, surface age and material behavior, one primary story clue, and silhouette/color separation between wardrobe and background.

Prefer two or three details that explain the moment over decorative clutter. Every visible object should support character, action, place, or delivery.

## Taste Rules

- make one clear hero subject; supporting details must not compete with the person
- use negative space deliberately for posters, covers, avatars, and commercial layouts
- keep one coherent palette with one restrained accent
- define forbidden palette/mood when the theme depends on color discipline
- separate materials, lighting, and palette instead of compressing them into "premium"
- include a few concrete, story-bearing scene details when the background matters; do not meet a detail count by adding clutter
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

Use realistic photography language: capture context, the selected natural or compressed perspective, natural skin texture, motivated light, appropriate depth distribution, believable wardrobe, ordinary imperfections, and a clean but not empty background.

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

## Layout and Output Contract

When use or platform is known, form a recommended canvas aspect ratio, safe areas, platform variants, and small-size readability. If these are not locked or accepted through recommended defaults, ask them as one output-contract choice; do not silently lock a platform convention.

Verify exact text character by character. If a targeted revision still fails, offer to regenerate a clean no-text base rather than claiming exact delivery. If the user requests pixel dimensions, transparency, file format, print bleed, DPI, or CMYK, record them as downstream delivery requirements; do not imply that generation-prompt words alone perform file conversion or print color management.

For a requested series, also lock the continuity facts that must not drift: wardrobe, hair/makeup, prop state, weather/wetness, light direction, location geography, and color treatment. Do not add this contract to a single image.

## Prompt Structure

Use this structure as flexible scaffolding for generation prompts, not a form to fill.

After the user chooses a direction or supplies enough brief detail, write a complete production prompt for every output type. Complete means all production-critical choices are resolved for the chosen output, not that every possible field is present. Do not use a short generic summary. Do not replace the production prompt with a compact config block unless a complex commercial, product, UI, diagram, or multi-system image would benefit from structured slots. Each relevant dimension must include concrete positive visual direction and necessary negative constraints.

Omit irrelevant dimensions instead of inventing filler. Never keep placeholder rows, empty labels, generic no-op values, or fields that do not help the current request.

Consider these dimensions when relevant:

- identity priority: same person, face anchor, no face redesign
- reference transfer boundaries: identity anchors to preserve; temporary source state not to copy, such as pose, expression, face angle, crop scale, selfie perspective, screenshot artifacts, or lighting
- reference coverage: which required face, body-scale, angle, and performance facts are verified, described, inferred, or missing
- shot direction: portrait or director plan covering composition, camera distance/angle, subject blocking, and background relationship
- directorial intent: the first audience impression and decisive moment when the image carries a story
- styling/performance: wardrobe/accessory structure, hair/makeup, props, pose/action, expression, gaze, hands, and energy level from `styling-performance.md`
- world/setting: location, time/weather, story evidence, spatial layers, atmosphere, scale, and physical logic
- composition/camera: subject scale/body cutoff, subject placement, camera height/distance, perspective character, allowed projection exaggeration, focus/depth distribution, and motion treatment
- identity readability: facial structure remains recognizable at the target face angle without rotating the person back toward camera
- lighting: motivated source, direction, size/hardness, fill or negative fill, falloff, separation, reflections, and how light reaches face, hair, wardrobe, and accessories
- palette/finish: main, support, and accent colors; skin-tone priority; warm/cool and saturation hierarchy; highlight/shadow treatment; forbidden colors or moods
- texture/detail: skin, hair, fabric, metal, props, environmental surfaces
- output contract: canvas aspect, platform readability, safe areas, exact-text verification, and required variants
- negative constraints: no text unless exact copy, no watermark, no fake brands, no random UI, no theme-breaking elements

The expanded prompt should be theme-adaptive. Do not reuse examples such as forests, temples, cyberpunk, saints, warriors, or luxury studios unless the user chose that direction. Delete rows that do not help the specific output.

```text
Use case: identity-preserve
Asset type: <selected output type>
Canvas/aspect: <ratio, crop, platform, or size intent>
Layout contract: <subject placement, negative space, text-safe areas, panel/region structure, or "simple single-image layout">
Input image: reference for the person's visible identity
Primary request: <user request>
Identity and reference transfer: <same person; face anchors; temporary source pose/angle/crop/perspective not to copy; required face/body-scale/angle/performance coverage marked verified, described, inferred, or missing>
Locked intent and quality constraints: <camera perspective, projection strength, action, head direction, gaze, and other locked choices that cannot change silently; identity, anatomy, projection, and pose quality required inside them>
Creative direction: <style, world/setting, hero hierarchy, mood, and useful scene details>
Directorial intent: <first audience impression; decisive moment; what is happening now; one or two details that carry the story>
Shot direction: <portrait shot direction or director shot plan; composition, camera distance/angle, subject blocking, and background relationship>
Camera/capture plan: <camera height and subject distance, perspective character and strength, allowed projection exaggeration, focus/depth distribution, motion treatment when relevant, and only useful numeric cues tied to visible results>
Perspective contract: <underlying anatomy; projected proportions; which near/far enlargement and foreshortening are intentional; which random or camera-inconsistent deformation is forbidden>
Subject identity/anatomy: <identity readability at the target face angle; angle-correct facial planes; valid world-space head, shoulder, torso, hip, limb, and joint structure>
Wardrobe/materials: <from styling-performance.md; preserve / subtly polish / replace because requested; include important materials and accessory constraints>
Performance/props: <pose/action, expression, gaze, mouth state, hands, props, and performance complexity>
Pose geometry: <coherent relationships among only the relevant visible support/contact, weight, pelvis, torso/shoulders, neck/head, facial plane/gaze, and hands/props; all aligned with the locked camera>
Lighting/color/finish: <motivated source, direction, size/hardness, fill or negative fill, separation, skin/environment relationship, palette, material behavior, and finish>
Text: <exact text in straight quotes; hierarchy and placement; or "no text">
Output contract: <intended platform, canvas aspect, safe areas, small-size readability, exact-text check, and required variants>
Continuity invariants (series only): <identity, wardrobe, hair/makeup, prop state, weather/wetness, light direction, location geography, and color treatment that must not drift>
Constraints: no identity drift, underlying face redesign, age/ethnicity drift, extra people unless requested, watermark, random text, fake brands, target-plane-inconsistent face deformation, malformed hands, copied source crop scale, pasted frontal face, stiff copied expression, invalid underlying anatomy, or random/projection-inconsistent deformation; preserve angle-correct facial appearance and intentional projection exaggeration, and add only output-adaptive negatives
```

Before generation, check that output/canvas, reference coverage, locked intent, shot, perspective contract, target-angle identity, underlying anatomy, projected proportions, pose geometry, styling/performance, lighting/color, text/output contract, and adaptive negatives are concrete enough for the task.

If the generated output is visible, review whether the selected feeling and decisive moment read; identity remains recognizable at the target angle; underlying anatomy is valid; projected proportions match the locked perspective; pose geometry, facial planes, and gaze agree; intentional exaggeration is distinct from random deformation; requested styling/light/text/output match; and there are no competing details or obvious artifacts.
