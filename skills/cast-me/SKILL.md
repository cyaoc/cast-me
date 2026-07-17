---
name: cast-me
description: Use when the user provides a person screenshot, selfie, portrait, or photo reference and wants a polished final image while preserving the person's visible identity. Supports portraits, professional headshots, cinematic posters, CG or game key art, magazine/editorial images, social avatars, commercial visuals, and other person-centered outputs.
---

# CastMe

## Goal

Turn a user-provided person image into a polished final image while preserving the person's visible identity as much as possible. Act as the coordinating director: resolve the output type and missing creative choices, route identity, composition, and styling/performance work to the right reference modules, then use Codex built-in image generation/editing.

## Reference Modules

Route reference reading by stable Markdown heading. Prefer reading only the named sections when the active file tools support targeted reads; otherwise read the complete owning file. Do not maintain a read-state tracker, but avoid knowingly rereading material already present in the current task context.

| Active condition | Read |
| --- | --- |
| Normal person-centered generation | `references/identity-anchor.md`: `Priority`, `Reference Transfer`, and `Reference Coverage` |
| Before writing the final generation prompt | `references/identity-anchor.md`: `Identity Prompt Constraints`; `references/composition-director.md`: `Final-Asset Quality`, `First-Pass Finish`, and `Prompt Structure` |
| Creative direction, First Read, or decisive moment | `references/composition-director.md`: `Creative Direction` and `Directorial Intent and Decisive Moment`; add `Direction Atlas and Freshness` when options are needed and `Style Refresh` when that branch is active |
| Shot, perspective, camera, or projection | `references/composition-director.md`: `Shot Direction`; add `Perspective Intent` and `Camera and Capture Plan` when relevant. For side-facing identity, action, or strong perspective, also add identity `Face Visibility and Performance Integrity` and styling/performance `Pose Geometry` as relevant |
| Physical world, taste, prompt craft, or medium-specific output guidance | `references/composition-director.md`: the relevant `Art Direction and Physical World`, `Taste Rules`, `Prompt Craft Rules`, or matching subsection under `Output Recipes` |
| Wardrobe, headwear, jewelry, accessories, makeup, hair, or props | `references/styling-performance.md`: the relevant `Ownership`, `Risk and Facial Treatment`, `Category Routing`, `Styling Direction`, or `Props` |
| Pose, action, expression, gaze, hands, or performance | `references/styling-performance.md`: `Performance Direction` and, for non-trivial action, `Pose Geometry`; add identity `Face Visibility and Performance Integrity` when the face angle or performance affects identity readability |
| Named character, uniform, historical dress, or other canon-dependent styling | `references/styling-performance.md`: `Role, Costume, and Visual Research` |
| Exact text, layout, platform delivery, variants, or a requested series | `references/composition-director.md`: `Layout and Output Contract`; add `Prompt Craft Rules` when the prompt needs text or structured regions |
| Presenting or replacing a refreshable creative gate | `references/scoped-option-refresh.md`: `Scope` and `Visible Gate and History`; add `Route the Target`, `Locks and Continuity`, or `Refresh Exhaustion` when active, plus the section that owns the target creative area |
| Reviewing a visible result | Read identity `Revision` first, then only the owner sections that contributed to generation or revision and their final review checks; composition review checks are in `Prompt Structure`, and styling/performance review checks are in `Prompt Contributions` |
| Narrow revision to a visible result | Bypass the normal-generation core. Read identity `Revision` plus the section that owns the requested correction. Add identity `Priority` and `Identity Prompt Constraints` for a likeness or face correction; add other core sections only when the correction actually touches reference transfer or coverage, composition, final quality, or finish |

Read any other section only when its choice, risk, research branch, output requirement, or revision concern is active. Section-level reading is an optimization, never a correctness dependency.

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
- Do not create nested menus. A follow-up must ask the next missing decision, not route the user into another category menu. The only exception is one compact refresh-scope gate when the user asks for more choices without an explicit, unresolved, or recent refreshable target.
- Keep the eight production dimensions as an internal completeness checklist, not as eight mandatory user questions. Adapt the route to the task: simple headshots and avatars usually need fewer choices than portraits, while posters, key art, full-body action, exact text, or series work may need more. Skip dimensions that are already stated, irrelevant, or accepted through recommended defaults.
- Preserve detail without turning the interaction into a professional form. Ask users to choose visible outcomes in plain language; translate those choices internally into camera, lighting, color, material, and delivery decisions. Do not ask beginners to choose camera bodies, lens models, ISO, aperture, shutter speed, Kelvin values, light power, or modifiers. If the user explicitly asks for parameter styling, use only approximate aesthetic cues tied to visible results, not a claimed physical exposure plan.
- Do not compress creative direction, shot direction, styling, performance, lighting, and delivery into one production package when several of those dimensions are still unresolved. A direction option may preview later details, but selecting it locks only the dimension being asked unless the user explicitly accepts the whole recommendation or recommended defaults.
- Maintain a decision state after every user response:
  - `locked: explicit`: the user directly specified, selected, or overrode this value; preserve it through any refresh unless the user explicitly reopens it
  - `locked: derived`: a selected option or accepted recommended defaults supplied this value; a Scoped Option Refresh may reopen it only when it belongs to the requested creative area
  - `suggested`: a prior option or recommendation previewed this value, but the user has not explicitly locked it
  - `unresolved`: the value is still missing and production-critical
- Every clarification must ask exactly one unresolved dimension or tightly coupled decision group and inherit all locked and suggested prior decisions. Do not ask a locked dimension again unless the user reopens it, contradicts it, or asks to change it.
- Suggested details are not final choices, but later questions must refine or adapt from them instead of restarting with generic menus. When the user accepts recommended defaults, convert relevant suggested details into `locked: derived` decisions; a repeated or overridden value becomes `locked: explicit`.
- Route any request for more, different, replacement, or new choices through `references/scoped-option-refresh.md`; it owns target priority, recent-gate tracking, delegation, and the no-target fallback. A target resolved as Creative Direction uses Style Refresh, while a precise first-time style request simply locks that theme.
- A partial answer resolves only the choices it explicitly answers. A bare number, letter, or option name selects that option only; continue to the next missing production-critical choice unless the user also says `default`, `use recommended defaults`, `generate now`, or an unscoped equivalent of `you decide`. A `you decide` or `pick one` attached to a Scoped Option Refresh delegates only that target area.
- If the user says `default`, `use recommended defaults`, `generate now`, or an unscoped global equivalent of `you decide`, stop ordinary clarification and use recommended defaults for unresolved creative choices. A focused coverage/risk, safety, or exact-text gate may still be required; defaults do not accept an unstated evidence or inference risk.
- Treat defaults as recommendations, not silent decisions. Use a default only when the user explicitly accepts defaults, asks Codex to decide, or the dimension is irrelevant to the requested output.
- A creative-direction preview does not resolve First-Pass Finish; it remains `suggested` until resolved, defaulted, or delegated.
- When identity or geometry constraints conflict with requested camera, composition, styling, pose, expression, hands, or beautification, trigger a risk-choice gate instead of silently rejecting or weakening the user's intent. Recommend the most accurate path that preserves locked choices, explain the risk in one short reason, and let the user choose how to handle missing evidence or accepted inference.
- Do not repeat a risk-choice gate when the user clearly accepted that specific risk, such as `try one version with inferred body and angle`, `I accept lower likeness`, `stronger beauty retouch`, or `bold attempt with the missing evidence inferred`. Continue with the chosen risk and make the prompt explicit about the tradeoff.
- When `imagegen` also triggers, this skill's clarification gates take precedence. Do not call, describe, or proceed with image generation until the user answers.
- Use Codex built-in image generation/editing only.
- Do not hardcode a specific scene, culture, genre, palette, or story world as the default. Adapt all scene, pose, expression, and palette choices to the user's theme.
- Treat normal person-centered generation as a final asset across every crop and medium; only an explicit preview, draft, exploration, or high-volume batch request permits a lower-quality trade-off. Do not add a quality question.

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

Resolve canvas aspect ratio, safe areas, and text treatment through the adaptive clarification ladder when they are not stated. Shot direction owns how much of the person appears in frame. Platform conventions such as square avatar, vertical poster, or no text are recommendations to offer, not silent assumptions. If the user accepts defaults, use the safest platform convention. If there is required in-image text, keep it exact and wrap it in straight quotes.

## Step 2: Resolve Brief and Creative Direction

After the output type is known, infer the design read and ask one creative-direction follow-up unless the user's brief is already detailed enough to write a complete production prompt. Use the Direction Atlas, freshness tracking, and lock-reopening rules whenever creative direction is unresolved or the user requests a Style Refresh.

Use this adaptive clarification ladder as an internal routing order for missing production-critical choices. It is not a requirement to ask eight questions. Ask only the next unresolved dimension or tightly coupled decision group, skip anything locked, irrelevant, or accepted through recommended defaults, and carry suggested values forward as the basis for later options:

1. output type / canvas intent
2. creative direction / scene concept
3. shot/perspective direction: composition, camera position/distance/angle, projection character, subject blocking, and background relationship
4. wardrobe, headwear, jewelry, accessory, makeup, hair, and prop treatment
5. canvas aspect ratio, safe areas, variants, and text treatment
6. performance direction: pose/action, expression, gaze, hands, and energy level
7. lighting/color/retouch/finish
8. avoid-list and theme-breaking elements

Route by production complexity rather than a turn-count target. Simple practical images omit story-world decisions that do not affect the result; directed portraits keep each material visual choice; posters, key art, full-body/action, exact text, or series work add only their relevant decisions and focused risk gates.

Stop asking as soon as every user-visible tradeoff that could materially change intent, identity, or use is locked, irrelevant, or accepted through recommended defaults. Resolve remaining professional implementation details internally. Question count is an outcome of the brief, never a quota.

Keep ownership clear while routing:

- creative direction owns the visual premise, world, mood, audience read, decisive moment, Direction Signature, and conversation-local Shown Directions
- shot direction owns scene framing, subject scale/body cutoff, camera position/viewpoint/distance, perspective strength, allowed projection exaggeration, subject placement, spatial layers, and background relationship
- styling owns wardrobe, hair, makeup, accessories, and props
- performance owns pose/action, expression, gaze, mouth state, hands, and energy
- lighting/color/retouch/finish owns motivated light, contrast, palette, identity-safe facial or material treatment, texture, and final image character
- art direction internally reconciles the locked world, shot, styling, and lighting into one physical scene; it is not a separate user gate
- output contract owns canvas aspect ratio, safe areas, platform variants, exact text, and platform readability

Prefer one owned dimension per question. Combine across modules only when the visible choice is genuinely inseparable, such as a full-body walking frame or a decisive moment defined by a specific action. Name every field the option resolves, record direction-supplied values as `locked: derived`, and skip them later; the dimension or override the user directly chooses is `locked: explicit`. Never silently lock performance from shot text or lock shot, styling, performance, or First-Pass Finish from a preview. Keep `pose/action + expression + gaze`, `lighting/color/retouch/finish`, and `canvas aspect + safe areas + text treatment` as normal coupled groups. Ask the avoid-list only for user exclusions, real theme ambiguity, or a likely theme-breaking element that output-adaptive constraints cannot safely handle.

For all output types, collect enough brief detail before generation to support a detailed production prompt. If multiple important choices are missing, ask them serially. Do not proceed until the user chooses, supplies their own direction, accepts recommended defaults, or explicitly asks Codex to decide.

If a required focused section flags missing coverage or a conflict, follow its one risk-choice gate unless the user already accepted that specific risk. Inherit every locked decision and never restart, reopen, or silently downgrade the brief.

Then wait after each question. Generate only after focused gates are resolved and ordinary choices are resolved, defaulted, overridden, or delegated to Codex.

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

Before generation, load the mandatory final-prompt sections and every active conditional section from the routing table. Build a complete, concrete production prompt from their results.

Complete means all production-critical choices are resolved for the chosen output, not that every possible field is present. Do not use a short generic summary. Do not replace the production prompt with a compact config block. Omit irrelevant dimensions instead of inventing filler.

Include the image being edited and every person reference required by the resolved Reference Coverage as actual image inputs; text never substitutes for a required identity image. If one is unavailable, follow the focused reattachment rule in `identity-anchor.md`.

Generation and review are complete only when:

- every required focused gate is resolved
- every required identity image is included as an actual image input
- locked user intent is unchanged
- the results of every module whose sections contributed to generation or revision are represented in the production prompt or revision
- claims about tool controls, output quality, size, text, and visual review are truthful and verified where required

## Step 4: Review or Revise

If the generated output is visible in the current conversation, review identity first, then only the modules whose sections contributed to generation or revision. Apply the cross-module completion conditions above; do not load or review unrelated composition, styling, performance, text, quality, finish, or delivery guidance.

If the user explicitly requests a targeted revision to a visibly close result, change only the named issue and repeat the identity lock. If the output is not visible to Codex, do not claim visual QA; report the prompt and ask the user to request a revision if the rendered result misses the target.
