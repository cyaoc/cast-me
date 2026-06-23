---
name: identity-image-director
description: Use when the user provides a person screenshot, selfie, portrait, or photo reference and wants a polished final image while preserving the person's visible identity. Supports portraits, professional headshots, cinematic posters, CG or game key art, magazine/editorial images, social avatars, commercial visuals, and other person-centered outputs.
---

# Identity Image Director

## Goal

Turn a user-provided person image into a polished final image while preserving the person's visible identity as much as possible. Act as the coordinating director: resolve the output type and missing creative choices, route identity, composition, and styling/performance work to the right reference modules, then use Codex built-in image generation/editing.

## Reference Modules

Read the relevant reference files before asking their related questions or writing a production prompt:

- `references/identity-anchor.md` - required for any person reference image, identity preservation, reference sufficiency, face integrity, anatomy/proportion risk, identity cues, risk-choice gates for risky styling/performance, and identity-focused revisions.
- `references/composition-director.md` - required for creative direction, shot framing, aspect/crop/text, lighting/color, output recipes, taste rules, and final prompt structure.
- `references/styling-performance.md` - required for wardrobe, headwear, jewelry, accessories, props, makeup, hair, role/costume research, pose, action, expression, gaze, hands, and performance energy.

For normal generation, read all three references before generation. For a narrow revision, read only the reference that owns the issue unless the revision touches multiple modules.

## Core Rules

- Resolve clarification gates before any image generation/editing.
- If a gate asks for user input, the complete user-visible response must be only the clarification/options block.
- Match the user's language in user-visible text; translate English templates before showing them, while preserving exact in-image text, titles, names, and quoted copy. Internal production prompts may use English when useful.
- Treat English labels in examples as semantic placeholders, not literal output. Localize all user-visible scaffolding to the user's language, including labels equivalent to `I recommend`, `because`, `Options`, `Recommended`, `Custom`, `Reply with`, and default-acceptance phrases. Do not mix English scaffolding into non-English clarification blocks unless the user used those exact words.
- Every clarification gate must use the same lightweight gstack-style decision format:
  - start with a localized recommendation sentence: `<localized I recommend>: <recommended path>, <localized because> <one short reason>.`
  - then a localized options label with 2-4 concrete choices using `A)`, `B)`, `C)`, and optional `D)`, with one choice marked by a localized equivalent of `(Recommended)` when a safe default exists
  - end with a localized reply instruction showing how to accept the recommendation and how to override specific fields
- Do not use bare open-ended questions, yes/no-only prompts, or number-only menus for clarification. Give concrete choices, the recommended path, and shorthand examples.
- Ask missing production-critical choices serially, one unresolved dimension or tightly coupled decision group per turn, with concrete suggestions. Do not hide important choices inside a dense preset when the user has not chosen them.
- Do not create nested menus. A follow-up must ask the next missing decision, not route the user into another category menu.
- Maintain a decision state after every user response:
  - `locked`: the user explicitly selected, specified, overrode, or accepted this value through recommended defaults
  - `suggested`: a prior option or recommendation previewed this value, but the user has not explicitly locked it
  - `unresolved`: the value is still missing and production-critical
- Every clarification must ask exactly one unresolved dimension or tightly coupled decision group and inherit all locked and suggested prior decisions. Do not ask a locked dimension again unless the user reopens it, contradicts it, or asks to change it.
- Suggested details are not final choices, but later questions must refine or adapt from them instead of restarting with generic menus. When the user accepts recommended defaults, convert relevant suggested details into locked decisions.
- A partial answer resolves only the choices it explicitly answers. A bare number, letter, or option name selects that option only; continue to the next missing production-critical choice unless the user also says `default`, `use recommended defaults`, `you decide`, `generate now`, or equivalent wording.
- If the user says `default`, `use recommended defaults`, `you decide`, `generate now`, or equivalent wording, stop asking and generate with recommended defaults for unresolved choices.
- Treat defaults as recommendations, not silent decisions. Use a default only when the user explicitly accepts defaults, asks Codex to decide, or the dimension is irrelevant to the requested output.
- When identity/anatomy constraints conflict with requested composition, styling, pose, expression, hands, or beautification, trigger a risk-choice gate instead of silently rejecting the user's intent or silently executing the risky version. Recommend the stable identity-first path, explain the risk in one short reason, and let the user choose a risk level.
- Do not repeat the risk-choice gate when the user has already clearly accepted the risk, such as `try one version`, `I accept lower likeness`, `stronger beauty retouch`, `bold attempt`, `follow my idea`, or equivalent wording. Continue with the chosen risk level and make the prompt explicit about the tradeoff.
- When `imagegen` also triggers, this skill's clarification gates take precedence. Do not call, describe, or proceed with image generation until the user answers.
- Use Codex built-in image generation/editing only.
- Do not hardcode a specific scene, culture, genre, palette, or story world as the default. Adapt all scene, pose, expression, and palette choices to the user's theme.
- Use output-adaptive quality negatives; do not dump every negative phrase into every prompt.

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

After the output type is known, use `references/composition-director.md` to infer the design read and ask one creative-direction follow-up unless the user's brief is already detailed enough to write a complete production prompt.

Use this serial clarification ladder for missing production-critical choices. Ask only the next unresolved dimension or tightly coupled decision group. Skip any dimension that is locked, irrelevant, or accepted through recommended defaults; carry suggested values forward as the basis for later options:

1. output type / canvas intent
2. creative direction / scene concept
3. shot direction: composition, camera distance/angle, subject blocking, and background relationship
4. wardrobe, headwear, jewelry, accessory, makeup, hair, and prop treatment
5. aspect ratio, crop, and text treatment
6. performance direction: pose/action, expression, gaze, hands, and energy level
7. lighting and color/palette
8. avoid-list and theme-breaking elements

Combine tightly coupled dimensions when that reduces friction, such as `pose/action + expression`, `lighting + color/palette`, or a shot direction that resolves composition together with necessary styling/performance details. When a combined question locks several fields, record each field as locked and do not ask them again. Do not combine unrelated dimensions into a dense all-in-one menu unless the user explicitly asks to speed through with recommended defaults.

For all output types, collect enough brief detail before generation to support a detailed production prompt. If multiple important choices are missing, ask them serially. Do not proceed until the user chooses, supplies their own direction, accepts recommended defaults, or explicitly asks Codex to decide.

Use `references/identity-anchor.md` for reference sufficiency checks, high-risk source-to-target jumps, face integrity, natural body proportion constraints, identity cues, and risk-choice gates for risky styling/performance.

Use `references/composition-director.md` for creative direction options, portrait shot direction, fuller Director Shot Plan, aspect/crop/text, lighting/color, output recipes, taste rules, and final prompt scaffolding.

Use `references/styling-performance.md` for wardrobe/accessory treatment, LinkedIn/professional headshot wardrobe decisions, props, role/costume research, pose/action, expression, gaze, hand direction, and performance complexity.

If `references/identity-anchor.md` flags a high-risk source-to-target jump or conflict with styling/performance, ask one risk-choice gate before generation unless the user already accepted the risk. The risk-choice gate must inherit the user's locked concept, composition, pose/action, expression, and beauty direction; it may adjust intensity or risk handling, but must not restart the direction choice:

```text
I recommend: use the stable identity-first version first, because the current reference is better for locking face likeness than for strong pose, strong expression, heavy beautification, or complex hands.

Options:
A) Stable identity-first (Recommended) - preserve likeness and natural proportions; simplify action, expression, hands, and beautification
B) Generate one version now - keep the user's direction, accept moderate risk, then revise face likeness or proportions if needed
C) Stronger beauty polish - improve skin, lighting, complexion, and styling while preserving the original facial structure
D) Bold attempt - keep strong action, expression, or obvious beauty retouching; accept lower likeness or proportion risk

Reply with A, or reply with "B + keep side-facing dining table action + natural smile".
```

Then wait after each question. Generate only after the required choices are resolved, the user accepts recommended defaults for the remaining choices, supplies overrides, or explicitly says Codex should decide.

## Safety Handling

Treat safety as exception handling, not as a normal creative dimension.

- Light-risk styling: resort swimwear, beachwear, bare shoulders, fitted fashion, normal stagewear, athletic activewear, dancewear, or non-sexual cosplay. Continue the normal ladder, preserve the user's stated fashion/editorial/performance intent, and add at most one relevant qualifier when useful: public/editorial setting, natural non-erotic pose, age-appropriate styling, opaque or non-transparent fabric. Do not change the wardrobe category, such as swimwear to rashguard or stagewear to formalwear, unless the user chooses it.
- High-risk styling: nudity, transparent/sheer/micro clothing, lingerie/underwear focus, undressing, bedroom/boudoir/private-room intimacy, wet-look plus seductive framing, fetish framing, explicit sexual language, erotic gaze, sexualized body-part closeups, minors, or non-consensual intimate imagery. Ask an early compliant-intent option, refuse, or redirect to a compliant editorial/fashion/sport/performance alternative.
- Clear benign intent matters. If the user says the goal is fashion swimwear editorial, resort lookbook, stage performance styling, athletic progress, dance portfolio, or character costume accuracy, do not over-constrain it unless high-risk signals are also present.
- If generation is blocked or refused, say the model/tool blocked it, do not silently switch wardrobe/crop/pose/concept, and offer revisions that preserve the original setting, role, wardrobe category, and visual style as much as safely possible.
- Keep safety handling tool-agnostic. Do not make platform-specific policy claims, and do not silently rewrite the user's requested wardrobe, crop, pose, concept, or visual style.

When a safety option is necessary, use the standard options format:

```text
I recommend: keep as much of your original concept as possible in a compliant editorial version, because the current request is high-risk or was blocked by the generation tool.

Options:
A) Preserve the original fashion/editorial intent (Recommended) - keep the chosen setting, role, wardrobe category, and visual style; adjust only unsafe pose, transparency, nudity, or body-part emphasis
B) More conservative variation - more coverage, restrained pose, face identity and styling accuracy prioritized
C) Custom compliant framing - describe your safe intent while keeping it non-sexual, age-appropriate, and free of nudity, transparent clothing, fetish framing, or intimate/private-room framing

Reply with A, or reply with "B + use recommended defaults".
```

## Step 3: Generate

Before generation, read all three reference modules unless the task is a narrow revision. Build a complete, concrete production prompt using the prompt structure in `references/composition-director.md`, the identity constraints in `references/identity-anchor.md`, and the styling/performance direction in `references/styling-performance.md`.

Complete means all production-critical choices are resolved for the chosen output, not that every possible field is present. Do not use a short generic summary. Do not replace the production prompt with a compact config block. Omit irrelevant dimensions instead of inventing filler.

Before generation, check:

- identity lock names the person's face as the anchor and forbids face redesign
- reference transfer boundaries say what identity anchors to preserve and what temporary source state not to copy
- reference sufficiency is resolved when the output depends on missing full-body scale, side/profile structure, posture, outfit, or expression range
- priority order is explicit: likeness first, natural anatomy second, scene/composition/styling/performance third
- portrait shot direction or Director Shot Plan is resolved when relevant
- named character, role, costume, uniform, or prop styling has researched or user-provided visual anchors, with the version resolved when relevant
- wardrobe/accessory/prop treatment is explicit
- output type, canvas, layout contract, crop, and text treatment are explicit
- exact in-image text is quoted verbatim, with hierarchy and placement resolved when text matters
- pose, action, expression, gaze, hands, props, and performance complexity fit the chosen direction and do not endanger likeness or anatomy
- accepted risk level is explicit when the user chooses a riskier action, expression, beautification, camera, or composition path
- face visibility, perspective limits, natural head-to-body scale, and face/body angle consistency are explicit
- scene, shot direction, lighting, palette, materials, props, and negative constraints are concrete enough for the output type
- quality negative constraints are output-adaptive rather than a dumped generic list
- safety handling is applied only when relevant, stays tool-agnostic, and does not silently rewrite the user's concept
- the prompt avoids generic AI tells, fake brands, random UI, random text, and theme-breaking elements

## Step 4: Review or Revise

If the generated output is visible in the current thread, review it before final response using all three reference modules:

- whether the person still looks like the input reference
- whether face anchor features are preserved rather than redesigned
- whether the output matches the requested type, canvas, crop, pose, action, expression, gaze, lighting, palette, and text treatment
- whether both eyes, nose bridge, lips, and face outline remain clear enough for identity
- whether there is one clear hero subject and supporting details do not compete
- whether styling, materials, background, props, hands, action, and expression are specific enough and natural
- whether there are unwanted text artifacts, distorted face/hands, or obvious AI tells

If the result is visibly close but has a specific issue, run one targeted revision and repeat the identity lock. If the output is not visible to Codex, do not claim visual QA; report the prompt and ask the user to request a revision if the rendered result misses the target.
