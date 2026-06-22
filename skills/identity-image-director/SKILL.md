---
name: identity-image-director
description: Use when the user provides a person screenshot, selfie, portrait, or photo reference and wants a polished final image while preserving the person's visible identity. Supports portraits, professional headshots, cinematic posters, CG or game key art, magazine/editorial images, social avatars, commercial visuals, and other person-centered outputs.
---

# Identity Image Director

## Goal
Turn a user-provided person image into a polished final image while preserving the person's visible identity as much as possible. First determine the output type and canvas intent, then guide the user through missing creative choices and use Codex built-in image generation/editing.

## Rules

- Resolve clarification gates before any image generation/editing.
- If a gate asks for user input, the complete user-visible response must be only the clarification/options block.
- Match the user's language in user-visible text; translate this skill's English templates before showing them, while preserving exact in-image text, titles, names, and quoted copy. Internal production prompts may use English when useful.
- Treat English labels in examples as semantic placeholders, not literal output. Localize all user-visible scaffolding to the user's language, including labels equivalent to `I recommend`, `because`, `Options`, `Recommended`, `Custom`, `Reply with`, and default-acceptance phrases. Do not mix English scaffolding into non-English clarification blocks unless the user used those exact words.
- Every clarification gate must use the same lightweight gstack-style decision format:
  - start with a localized recommendation sentence: `<localized I recommend>: <recommended path>, <localized because> <one short reason>.`
  - then a localized options label with 2-4 concrete choices using `A)`, `B)`, `C)`, and optional `D)`, with one choice marked by a localized equivalent of `(Recommended)` when a safe default exists
  - end with a localized reply instruction showing how to accept the recommendation and how to override specific fields
- Do not use bare open-ended questions, yes/no-only prompts, or number-only menus for clarification. Give concrete choices, the recommended path, and shorthand examples.
- Ask missing production-critical choices serially, one dimension per turn, with concrete suggestions. Do not hide important choices inside a dense preset when the user has not chosen them.
- Do not create nested menus. A follow-up must ask the next missing decision, not route the user into another category menu.
- A partial answer resolves only the choices it explicitly answers. A bare number, letter, or option name selects that option only; continue to the next missing production-critical choice unless the user also says `default`, `use recommended defaults`, `you decide`, `generate now`, or equivalent wording.
- If the user says `default`, `use recommended defaults`, `you decide`, `generate now`, or equivalent wording, stop asking and generate with recommended defaults for unresolved choices.
- Treat defaults as recommendations, not silent decisions. Use a default only when the user explicitly accepts defaults, asks Codex to decide, or the dimension is irrelevant to the requested output.
- When `imagegen` also triggers, this skill's clarification gates take precedence. Do not call, describe, or proceed with image generation until the user answers.
- Do not hardcode a specific scene, culture, genre, palette, or story world as the default. Adapt all scene, pose, expression, and palette choices to the user's theme.
- For named character cosplay, research the character's visual traits online before writing options or a production prompt unless the user supplies sufficient reference images or details.
- Use Codex built-in image generation/editing only.
- Do not identify the person or infer sensitive traits.
- Do not transform the person into a celebrity or a different identity.
- Use output-adaptive quality negatives; do not dump every negative phrase into every prompt.
- Treat identity preservation as best effort, not guaranteed.
- Preserve identity anchors, not temporary reference-photo state. Do not copy the source pose, expression, face angle, crop scale, selfie perspective, screenshot artifacts, or lighting unless the user explicitly asks for them.

## Step 1: Determine Output Type and Canvas

If the user states the desired output type, use it.

If the user provides a person image but does not specify the final format, ask a compact creative brief question with options as the complete user-visible response:

```text
I recommend: start with the output type closest to your intended use; if you only want to preview results, portrait / headshot / social avatar is the safest starting point because it best preserves recognizability.

Options:
A) Portrait / professional headshot / social avatar (Recommended) - clean portraits, profile images, professional branding, or natural photography
B) Cinematic poster / editorial spread / commercial campaign - stronger narrative, title-safe cover layout, and hero key visual
C) CG or game key art / fantasy / sci-fi / mythic theme - rebuild the world, role, atmosphere, and high-style visual direction
D) Custom - describe the use case, aspect ratio, wardrobe treatment, theme/mood, and any text

Reply with A, or reply with "B + vertical 9:16 + keep wardrobe + title MIDNIGHT SIGNAL".
```

Do not infer the output type from image content or add process narration before the user chooses a format. A recommendation in the clarification block is only guidance; it is not permission to proceed until the user accepts or overrides it.

Supported output types:

- realistic portrait
- professional headshot
- cinematic poster
- CG or game key art
- editorial or magazine image
- social avatar
- commercial campaign visual
- custom themed image

Resolve aspect ratio, crop, and text treatment through the serial clarification ladder when they are not stated. Platform conventions such as square avatar, vertical poster, or no text are recommendations to offer, not silent assumptions. If the user accepts defaults, use the safest platform convention. If there is required in-image text, keep it exact and wrap it in straight quotes.

## Step 2: Resolve Brief and Creative Direction

After the output type is known, infer the design read:

- audience and use case
- mood words from the user
- reference-image role
- platform or crop needs
- shot direction: composition, camera distance/angle, performance, hands, props, and background relationship
- wardrobe/accessory treatment: preserve original, subtly polish, or replace only if requested
- reference transfer boundaries: what identity anchors to preserve and what temporary reference state to redesign for the theme
- whether the image should feel photographic, editorial, cinematic, commercial, CG, or social-native

Resolve one creative-direction follow-up for every output type unless the user's brief is already detailed enough to write a complete production prompt. This applies to portraits, professional headshots, posters, CG/key art, editorial images, avatars, commercial visuals, and custom themes.

If the user gives a precise theme, use it and ask only for missing production-critical choices. If the theme or art direction is under-specified, present 2-4 concrete viable directions for the user to choose. Each option should differ meaningfully in setting, role/archetype, mood, and output use; it may include sample pose, expression, lighting, or palette as preview hints, but those hints are not resolved choices unless the user explicitly accepts defaults. Do not offer generic labels without visual substance.

When asking beginner users for missing creative choices, include suggested answers. Do not ask only open-ended abstract questions like "what mood, scene, and pose do you want?" Offer 2-4 concrete options with different setting, role/archetype, mood, and output use; keep sample pose, expression, lighting, or palette framed as suggestions, not locked decisions. Always allow the user to mix options or describe their own.

Every options block should include a recommended answer so the user can proceed with one letter. Mark one option as recommended when there is a clear best fit. Let the user accept the recommendation, override individual choices, or say the remaining choices should use recommended defaults.

Use this serial clarification ladder for missing production-critical choices. Ask only the next unresolved dimension, and skip a dimension only when it is already specified, irrelevant, or the user has accepted recommended defaults:

1. output type / canvas intent
2. creative direction / scene concept
3. shot direction: composition, camera distance/angle, performance, hands, props, and background relationship
4. wardrobe, headwear, jewelry, and accessory treatment
5. aspect ratio, crop, and text treatment
6. pose/action and expression
7. lighting and color/palette
8. avoid-list and theme-breaking elements

Handle safety as exception handling, not as a creative ladder step. Interrupt the ladder only for high-risk styling, unsafe content, or an actual generation refusal.

Combine tightly coupled dimensions when that reduces friction, such as `pose/action + expression`, or `lighting + color/palette`. Do not combine unrelated dimensions into a dense all-in-one menu unless the user explicitly asks to speed through with recommended defaults.

Shot direction may resolve composition, pose/action, expression, hands, props, and background relationship in one decision. If it does, skip the later pose/action question unless a production-critical detail remains unresolved.

If the output type is known, the user has not specified wardrobe/accessory treatment, and the original clothing, headwear, jewelry, or accessories are visually important or may conflict with the requested format, ask one short follow-up as the complete user-visible response before generation.

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

For all output types, collect enough brief detail before generation to support a detailed production prompt. If multiple important choices are missing, ask them serially using the ladder above. Do not proceed until the user chooses, supplies their own direction, accepts recommended defaults, or explicitly asks Codex to decide.

Use this pattern and adapt the option contents to the user's image and requested output type:

```text
I recommend: <recommended direction or concept>, because <one short reason tied to the user's request and reference image>.

Options:
A) <direction name> (Recommended) - <setting/world>, <role/archetype>, <mood>, <output use>
B) <direction name> - <setting/world>, <role/archetype>, <mood>, <output use>
C) <direction name> - <setting/world>, <role/archetype>, <mood>, <output use>
D) Custom / mix-and-match - describe your own theme or combine several directions

Reply with A, or reply with "B + use recommended defaults". If you reply with only B, I will ask the next missing dimension, such as wardrobe, aspect ratio, pose/expression, or lighting/color.
```

The visual details inside the creative-direction options are previews. If the user replies with only a direction letter/name, continue the serial ladder and ask the next unresolved dimension. Treat those preview details as final only if the user accepts defaults or repeats them explicitly.

For practical formats such as LinkedIn, resume, social avatar, or realistic portrait, the options should still be concrete, such as different background types, crop, expression, wardrobe treatment, lighting, palette, and polish level. Do not skip the direction follow-up just because the output type is conventional.

### Portrait Shot Direction and Director Shot Plan

For realistic portraits, personal photoshoots, lifestyle portraits, social portraits, and beauty/editorial portraits, ask a lightweight portrait shot-direction question unless the user already specified crop, pose, expression, hands, background/props, or accepted recommended defaults. Portraits are common but still need directed composition and performance.

For LinkedIn, resume, professional headshot, business avatar, or simple social avatar requests, keep the gate lightweight: crop, background, expression, and wardrobe/accessory treatment. Do not ask a full Director Shot Plan or introduce props unless the user requests them.

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

Use props only when they support the story, product, role, or user request. If props are unresolved or unnecessary, specify no unnecessary props rather than inventing decorative objects.

Use the same lightweight decision format for later dimensions. Pose/action options must cover body direction, gaze, mouth state, and energy level. Lighting/color options must cover key/fill/rim light, palette, skin/metal/fabric rendering, and forbidden color mood when relevant.

Then wait after each question. Generate only after the required choices are resolved, the user accepts recommended defaults for the remaining choices, supplies overrides, or explicitly says Codex should decide.

Use concrete visual language. Prefer materials, light, camera, location, props, and composition over vague praise like "stunning", "high quality", or "cinematic" alone.

Taste rules:

- make one clear hero subject; supporting details must not compete with the person
- use negative space deliberately for posters, covers, avatars, and commercial layouts
- keep one coherent palette with one restrained accent
- define forbidden palette/mood when the theme depends on color discipline
- separate materials, lighting, and palette instead of compressing them into "premium"
- include 5-12 concrete scene details when the background matters
- avoid default AI tells: purple-blue glow, random orbs or blobs, fake brand logos, unreadable microtext, stock-photo cliches, cheap plastic CG, over-smoothed skin, and template-like card/poster layouts
- use typography only when it has a job and exact user copy exists

### Character Cosplay Research

When the user asks for a named character cosplay, do online research before writing the character-specific options or prompt unless the user provides sufficient reference images or a detailed character brief.

Use reliable visual sources first: official character pages, publisher/studio/game pages, official art, production stills, or reputable character wikis with images. Extract only visual production anchors:

- character version or outfit variant
- hair shape, color, length, bangs, and silhouette
- outfit silhouette, layers, materials, color blocking, armor or fabric details
- signature accessories, symbols, props, weapons, or motifs
- makeup, facial styling, posture, and recognizable attitude
- palette, lighting genre, world context, and details that must not be added

If the character has multiple major variants, ask the user to choose the version with the standard decision format before generation. Do not rely on memory for niche, current, or visually complex characters. If online research is unavailable or inconclusive, ask the user for reference images or a character brief instead of guessing. If web research was used, keep source links available for the response.

### Quality Negative Constraints

Use positive, concrete visual direction first. Negative constraints support the direction; they do not replace it.

Choose only the negative constraints relevant to the requested output:

- Face and identity: no identity drift, no face redesign, no asymmetrical eyes, no distorted face, no waxy or plastic skin, no over-smoothed skin, no automatic beautification into a different person.
- Hands and body: no extra fingers, fused fingers, malformed hands, broken wrists, extra limbs, distorted anatomy, or prominent hands when the hands are not important to the composition.
- Text, UI, and artifacts: no random text, watermark, fake logo, fake brand, stream UI, stickers, overlays, unreadable microtext, or compression artifacts.
- Composition and camera: no extra people unless requested, no extreme fisheye, no wide-angle face stretching, no cropped face or important headwear, no heavy occlusion of eyes, nose, mouth, or face outline.
- Style-specific finish: for photorealistic requests, avoid cheap CG, anime finish, plastic rendering, and unnatural skin; for CG or key art requests, avoid uncanny face drift and identity-losing stylization.

### Safety Handling

Treat safety as exception handling, not as a normal creative dimension.

- Light-risk styling: resort swimwear, beachwear, bare shoulders, fitted fashion, normal stagewear, athletic activewear, dancewear, or non-sexual cosplay. Continue the normal ladder, preserve the user's stated fashion/editorial/performance intent, and add at most one relevant qualifier when useful: public/editorial setting, natural non-erotic pose, age-appropriate styling, opaque or non-transparent fabric. Do not change the wardrobe category, such as swimwear to rashguard or stagewear to formalwear, unless the user chooses it.
- High-risk styling: nudity, transparent/sheer/micro clothing, lingerie/underwear focus, undressing, bedroom/boudoir/private-room intimacy, wet-look plus seductive framing, fetish framing, explicit sexual language, erotic gaze, sexualized body-part closeups, minors, or non-consensual intimate imagery. Ask an early compliant-intent option, refuse, or redirect to a compliant editorial/fashion/sport/performance alternative.
- Clear benign intent matters. If the user says the goal is fashion swimwear editorial, resort lookbook, stage performance styling, athletic progress, dance portfolio, or character costume accuracy, do not over-constrain it unless high-risk signals are also present.
- If generation is blocked or refused, say the model/tool blocked it, do not silently switch wardrobe/crop/pose/concept, and offer revisions that preserve the original setting, role, wardrobe category, and visual style as much as safely possible.
- Keep safety handling tool-agnostic. Do not make platform-specific policy claims, and do not silently rewrite the user's requested wardrobe, crop, pose, concept, or visual style.
- Use `user-provided self-reference image` only when the user explicitly says the image is them, a selfie, or their own image. Otherwise use `user-provided person reference image`. Do not claim consent, ownership, age, or relationship details that the user did not provide.

When a safety option is necessary, use the standard options format:

```text
I recommend: keep as much of your original concept as possible in a compliant editorial version, because the current request is high-risk or was blocked by the generation tool.

Options:
A) Preserve the original fashion/editorial intent (Recommended) - keep the chosen setting, role, wardrobe category, and visual style; adjust only unsafe pose, transparency, nudity, or body-part emphasis
B) More conservative variation - more coverage, restrained pose, face identity and styling accuracy prioritized
C) Custom compliant framing - describe your safe intent while keeping it non-sexual, age-appropriate, and free of nudity, transparent clothing, fetish framing, or intimate/private-room framing

Reply with A, or reply with "B + use recommended defaults".
```

## Step 3: Identity Lock and Reference Transfer Boundaries

Do not treat every visible detail in the reference image as fixed.

Preserve after the user requests it, accepts recommended defaults, or when the detail is not a production-critical creative choice:

- visible identity
- selected or distinctive wardrobe, headwear, jewelry, and accessories
- user-specified props, text, product, or brand elements

Redesign temporary reference-photo state after the relevant choice is resolved and when useful for the requested theme:

- expression
- gaze direction
- face angle
- pose/action
- crop scale and head size in frame
- background
- lighting
- camera angle
- selfie, livestream, screenshot, or casual capture perspective
- screenshot UI, stickers, comments, stream overlays, clutter, and original low-quality capture artifacts

Use the input image as the identity reference.

Preserve:

- face outline and bone structure
- facial proportions, forehead proportion, and overall recognizability
- brow and eye relationship
- eyebrow shape
- eye shape, size, eyelid structure, and eye distance
- nose bridge, nose root, nose tip, and nostril/alar width
- lip thickness, cupid's bow, mouth corners, and philtrum length
- chin shape and jawline
- skin tone and age impression
- hairstyle and hairline
- recognizability across different theme-appropriate expressions
- original wardrobe, headwear, jewelry, and accessories unless the user asks to replace them, including style, color, material, pattern, cut, layers, wearing method, headwear outline, dangling elements, and major structure
- visible body silhouette and stance when a full-body or three-quarter source provides them
- distinctive visible styling details

Avoid:

- face drift
- age drift
- ethnicity drift
- celebrity resemblance
- extra people unless requested
- removing distinctive wardrobe, headwear, jewelry, or accessories unless requested
- redesigning the face
- beautifying into a different face
- changing face width, eye shape, nose structure, lips, chin, jawline, skin tone, or age impression
- random text
- watermarks
- distorted face or hands
- copying the source close-up crop scale into a full-body image
- oversized head, tiny body, doll-like proportions, chibi proportions, compressed torso, or miniature limbs unless explicitly requested
- pasting a frontal face onto an angled head, side-facing body, or action pose
- stiff copied expression, selfie gaze, frozen reference-photo mouth shape, or unnatural face/body mismatch

When the target image needs a different pose, expression, camera angle, crop, or full-body composition, preserve the identity anchors while adapting the face and body naturally to the new state. The source image is not a template for pose, expression, face angle, camera distance, or head-to-body scale unless the user says to copy those details.

For close-up or half-body references used in full-body outputs, state that the input is only a face/visible-styling reference. Do not preserve the source image's close-up head scale. Use natural human proportions, camera distance appropriate for a complete standing or seated figure, balanced head-to-body scale, realistic shoulder width, torso length, legs, and feet.

For full-body and three-quarter outputs, require natural adult human proportions: realistic head-to-body scale, shoulder width, torso length, leg length, and limb size. Identity similarity must come from facial structure and visible styling anchors, not from enlarging the head.

For frontal references used in angled, side-facing, action, poster, or cinematic outputs, do not force a frontal face onto the new pose. Adapt the same facial structure to the target head turn and camera perspective so the gaze, jawline, cheek plane, nose bridge, mouth angle, and face outline match the selected direction.

For reference edits, be surgical: state the target transformation first, then name what must remain unchanged. If there are multiple reference images, label each one by role, such as `Image 1: person identity`, `Image 2: side/profile reference`, `Image 3: full-body scale or outfit`, `Image 4: style reference`, `Image 5: product or logo`.

When reference information is missing, do not create extra generated references and treat them as factual identity evidence. If exact accuracy may matter, ask for real additional reference images or user-described details before generation. Use clearly labeled natural inference only when the user accepts defaults, asks Codex to decide, or says exact body scale, angle, posture, outfit, or expression details do not need to be verified. The original user-provided person image remains the primary identity reference.

### Reference Sufficiency Check

Run this check before generation when the requested output depends on source information the provided reference does not show well:

- full-body, seated, or complex action output from a face close-up or half-body reference
- side profile, strong head turn, over-the-shoulder pose, or cinematic angle from a frontal-only reference
- specific body build, height impression, outfit, lower body, shoes, or posture that is not visible
- strong expression change when the reference has only one stiff, selfie, screenshot, or neutral expression
- multiple reference images with unclear roles

If the missing information is production-critical and the user has not accepted recommended defaults, ask one options block before generation. Prefer the accuracy-preserving path over natural inference:

```text
I recommend: add the missing reference details before generation, because the current image is enough for visible face identity but not enough to define exact body scale, alternate face angles, or expression range accurately.

Options:
A) I will attach more real reference images (Recommended) - full-body, side/profile, outfit, posture, or expression references for better accuracy
B) I will describe missing details - body build, posture, side/profile features, expression range, outfit, or lower-body details
C) Continue with natural inference - preserve identity anchors, infer realistic body proportions, adapt face angle and expression naturally to the scene; treat inferred details as estimates, not verified identity facts
D) Use a safer composition - half-body or three-quarter crop instead of full-body/action framing

Reply with A, or reply with "B + athletic build + relaxed smile + three-quarter left angle", or reply with "C + use recommended defaults".
```

If the user supplies real references or descriptions, incorporate only the supplied details and keep the original person image as the primary identity reference. If the user chooses natural inference or accepts recommended defaults, continue without further sufficiency questions unless a new missing dimension becomes central to the request. Make the prompt explicit that inferred body scale, angle, and expression are natural estimates, not verified identity facts.

The generated result should feel like the same person in a new scene, not a copy of the source screenshot.

## Step 4: Pose, Expression, and Face Visibility

Pose and expression should serve the requested theme, not blindly copy the screenshot.

Use theme-appropriate action and expression while keeping identity readable. Prefer natural, restrained direction over exaggerated posing. Keep both eyes, nose bridge, lips, and face outline clearly visible unless the user asks for a profile or obscured-face concept.

Avoid:

- extreme high angle or low angle
- fisheye or wide-angle closeups of the face
- exaggerated perspective stretching
- unnecessary extreme profile angles when they do not serve the requested concept or identity readability
- forcing a frontal face onto a turned head, side-facing body, or action pose
- face/body perspective mismatch where gaze, jawline, cheek plane, nose bridge, mouth angle, and head turn do not agree
- hair, accessories, props, or shadows covering major facial features
- expressions that fight the requested theme, such as goofy, blank, aggressive, overly seductive, or modern selfie expressions when they do not fit

## Step 5: Output Recipes

Use these recipes as prompt vocabulary after the relevant choices are resolved. Do not let a recipe silently decide unresolved production-critical choices such as wardrobe, aspect ratio, text, pose/expression, lighting, palette, or avoid-list.

### Realistic Portrait

Use realistic photography language: capture context, 50mm or 85mm portrait lens, natural skin texture, soft light, shallow depth of field, believable wardrobe, ordinary imperfections, and a clean but not empty background.

Avoid CG polish, fantasy styling, poster typography, and unreal materials.

### Professional Headshot

Use a clean background, restrained retouching, confident but natural expression, business/editorial lighting, and realistic face preservation.

Do not default to replacing distinctive original clothing or headwear with a blazer. If the user requests professional use but does not specify wardrobe treatment, ask when the visible wardrobe/headwear is distinctive or could affect the output; use preserve-as-is only after the user accepts defaults or when wardrobe is not a meaningful creative choice.

Avoid dramatic costume changes, fantasy scenes, and heavy stylization.

### Cinematic Poster

Use strong silhouette, dramatic key light, rim light, atmospheric background, title-safe composition, bold color contrast, and cinematic grading. Pass the three-glance test: the silhouette reads first, the narrative world reads second, and close details reward inspection.

Only include text if the user provides exact text. If text treatment is unresolved and relevant to the output, ask in the aspect/text clarification. If the user accepts defaults or text is not relevant, specify no text.

### CG or Game Key Art

Use premium concept-art finish, detailed materials, cinematic environment, dynamic but identity-preserving pose, and stylized lighting. Define the world, camera angle, costume/material system, and readable silhouette.

Do not over-stylize the face until the person becomes unrecognizable.

### Editorial or Magazine Image

Use fashion lighting, refined palette, clean pose direction, luxury styling, negative space, strong typography-safe areas, and cover-like composition.

Only include typography with exact user-provided copy. If text treatment is unresolved and relevant to the output, ask in the aspect/text clarification. If the user accepts defaults or text is not relevant, specify no text.

### Social Avatar

Use clear face readability at small size, simple background, strong silhouette, and polished composition. If the crop is unresolved, recommend a square crop for avatars in the aspect/crop clarification rather than silently applying it.

Avoid dense background detail, small text, and complex full-body staging.

### Commercial Campaign Visual

Use the provided product or brand mood if any, controlled composition, premium lighting, simple message hierarchy, and usable negative space.

Do not invent brand names, slogans, logos, or product claims.

## Step 6: Prompt Structure

Use this structure as flexible scaffolding for generation prompts, not a form to fill.

After the user chooses a direction or supplies enough brief detail, write a complete production prompt for every output type. Complete means all production-critical choices are resolved for the chosen output, not that every possible field is present. Do not use a short generic summary. Do not replace the production prompt with a compact config block. Each relevant dimension must include concrete positive visual direction and necessary negative constraints.

Omit irrelevant dimensions instead of inventing filler. Never keep placeholder rows, empty labels, generic no-op values, or fields that do not help the current request.

Consider these dimensions when relevant:

- identity priority: same person, face anchor, no face redesign
- reference transfer boundaries: identity anchors to preserve; temporary source state not to copy, such as pose, expression, face angle, crop scale, selfie perspective, screenshot artifacts, or lighting
- source sufficiency: whether missing full-body scale, side/profile structure, posture, outfit, or expression range is inferred naturally, described by the user, or supplied by extra real references
- shot direction: portrait or director plan covering composition, camera distance/angle, subject blocking, performance, hands, props, and background relationship
- wardrobe/accessory structure: style, color, material, pattern, cut, layers, wearing method, headwear outline, dangling elements, and major structure
- world/setting: location, architecture/nature/props, spatial layers, atmosphere, scale, story context
- pose/action: theme-appropriate body language, hand placement, motion, restraint or dynamism
- expression: theme-appropriate emotion, gaze, mouth state, intensity, forbidden expressions
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
Input image: reference for the person's visible identity
Primary request: <user request>
Identity and reference transfer: <same person; face anchor details; what identity anchors to preserve; what temporary source state not to copy; whether missing body scale, angle, or expression details are inferred or user-supplied>
Creative direction: <style, world/setting, hero hierarchy, mood, and useful scene details>
Shot direction: <portrait shot direction or director shot plan; composition, camera distance/angle, subject blocking, performance, hands, props, and background relationship>
Subject direction: <pose/action, expression, face visibility, crop, camera, perspective limits, natural adult proportions, realistic head-to-body scale, identity through facial structure instead of enlarged head size, and perspective-aware face angle>
Wardrobe/materials: <preserve / subtly polish / replace because requested; include important materials and accessory constraints>
Lighting/color: <key light, fill/rim/volume light when useful, palette, and forbidden colors or moods>
Text: <exact text in straight quotes or "no text">
Constraints: no identity drift, no face redesign, no automatic beautification into a different face, no age drift, no ethnicity drift, no extra people unless requested, no watermark, no random text, no fake brands, no distorted face or hands, do not remove original wardrobe/accessories unless requested, do not copy close-up crop scale into full-body output, do not paste a frontal face onto an angled pose, no stiff copied expression, no oversized head or tiny body; add output-adaptive quality negatives and safety framing when relevant
```

## Step 7: Revision and Quality Gates

If the result is close, revise surgically. Change one target at a time and repeat identity constraints:

- change only the requested issue
- keep face, pose, composition, crop, palette, and text unchanged unless they are the issue
- preserve original text unless replacement text is supplied
- do not regenerate a new concept when the user asked for a correction

If a revision request is ambiguous and needs user input, ask with the same lightweight gstack-style decision format: recommendation, concrete options, and direct reply examples. Do not ask a bare "how should I revise it?" question.

Before generation, check the production prompt:

- identity lock names the person's face as the anchor and forbids face redesign
- reference transfer boundaries say what identity anchors to preserve and what temporary source state not to copy
- reference sufficiency is resolved when the output depends on missing full-body scale, side/profile structure, posture, outfit, or expression range
- portrait shot direction or director shot plan is resolved when the output is a portrait/photoshoot, poster, editorial, commercial, CG/key art, full-body/action image, or prop/product/story-heavy scene
- named character cosplay has researched or user-provided visual anchors, with the character version resolved when relevant
- wardrobe/accessory treatment is explicit
- output type, canvas, crop, and text treatment are explicit
- pose and expression fit the chosen direction
- face visibility, perspective limits, natural head-to-body scale, and face/body angle consistency are explicit
- scene, shot direction, lighting, palette, materials, props, and negative constraints are concrete enough for the output type
- quality negative constraints are output-adaptive rather than a dumped generic list
- safety handling is applied only when relevant, stays tool-agnostic, and does not silently rewrite the user's concept
- the prompt avoids generic AI tells, fake brands, random UI, random text, and theme-breaking elements

If the generated output is visible in the current thread, review it before final response:

- whether the person still looks like the input reference
- whether face anchor features are preserved rather than redesigned
- whether the output matches the requested type, canvas, crop, pose, expression, lighting, palette, and text treatment
- whether both eyes, nose bridge, lips, and face outline remain clear enough for identity
- whether there is one clear hero subject and supporting details do not compete
- whether materials, background, and props are specific enough
- whether there are unwanted text artifacts, distorted face/hands, or obvious AI tells

If the result is visibly close but has a specific issue, run one targeted revision and repeat the identity lock. If the output is not visible to Codex, do not claim visual QA; report the prompt and ask the user to request a revision if the rendered result misses the target.
