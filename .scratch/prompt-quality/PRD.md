Status: ready-for-agent

# Person-Centered Final-Image Quality

## Problem Statement

The skill exists primarily to turn a person's reference image into a polished final image, but its current output recipes do not establish one explicit quality and resolution default for every final person-centered output. A close portrait may receive strong skin and face treatment while a full-body, environmental, poster, CG, illustration, or avatar request can still lose identity, material, edge, clothing, hand, and environment detail when the generated asset is treated like a lower-quality preview.

Generic prompt phrases such as `4K`, `8K`, `high quality`, `HDR`, `masterpiece`, or `cinematic` do not set real output parameters and do not reliably create believable texture, composition, or visual hierarchy. At the same time, forcing experimental 4K output onto every generation would trade away reliability and would not solve weak art direction.

The skill needs a final-image quality contract that defaults every normal person-centered generation to the strongest available quality and a stable high-resolution target, gives every image a clear First Read, and adapts visible quality to the selected medium. It must do this without adding a quality questionnaire, a fixed magic-word suffix, a universal negative-prompt list, an Image API integration, or an automatic second pass.

## Solution

Treat every normal person-centered generation as a final asset unless the user explicitly asks for a preview, draft, exploration, or high-volume batch. All final person-centered outputs default to `quality=high` when the active generation surface exposes a real quality control, regardless of crop, face size, or medium. They also default to the highest stable, non-experimental resolution compatible with the selected aspect ratio when the generation surface exposes a real size control.

When the built-in generation surface does not expose quality or size controls, continue generation without another user gate. Preserve the same final-asset intent through concrete composition, lighting, material, texture, and First-Pass Finish direction, but never claim that an unverified quality setting or pixel size was applied.

Require a clear First Read for every output: one person, face, silhouette, action, emotion, product, or message must register first at the intended display size, and supporting elements must reinforce rather than compete with it. Cinematic posters and CG or game key art default to stronger dramatic impact; photographic, professional, editorial, avatar, commercial, and illustrative outputs adapt intensity to their intended use.

Keep output recipes dynamic. Each recipe defines its medium-specific success criteria and likely failure modes, while the current identity, scene, action, framing, lighting, palette, materials, and First-Pass Finish determine the actual production prompt. Photographic outputs use explicit photorealistic capture language and believable physical texture. CG and game key art use readable identity-preserving silhouette, scale, material response, spatial depth, and controlled effects. Negative constraints remain short, output-adaptive, and inside the ordinary prompt.

## User Stories

1. As a user generating an image from my reference photo, I want the ordinary workflow to assume I need a final asset, so that my result is not silently treated as a low-quality preview.
2. As a user generating a full-body or environmental image, I want the same final quality priority as a close portrait, so that identity, clothing, hands, and scene detail do not degrade merely because my face occupies less of the frame.
3. As a user generating a photographic portrait, I want the final request to default to high quality, so that skin, hair, fabric, and lighting have enough fidelity for direct use.
4. As a user generating a professional headshot, I want the final request to default to high quality, so that the result looks trustworthy and polished without becoming a generic stock portrait.
5. As a user generating a cinematic poster, I want the final request to default to high quality, so that the person, silhouette, atmosphere, text-safe composition, and story detail remain coherent.
6. As a user generating CG or game key art, I want the final request to default to high quality, so that identity, surfaces, material response, spatial depth, and effects remain convincing.
7. As a user generating an editorial or magazine image, I want the final request to default to high quality, so that skin, styling, textiles, pose, and print-like texture support the intended point of view.
8. As a user generating a social avatar, I want the source asset to default to high quality even if the final display is small, so that my identity remains clear and the image can be reused at larger sizes.
9. As a user generating a commercial visual, I want the final request to default to high quality, so that the person, product, packaging, wardrobe, and message hierarchy feel production-ready.
10. As a user generating an illustration or another non-photographic image, I want the final request to default to high quality, so that identity and medium-specific line, brush, paper, print, or painted texture remain intentional.
11. As a user who explicitly asks for a preview, draft, exploration, or large batch, I want the skill to permit a lower quality setting, so that iteration can favor speed and usage when I actually requested that trade-off.
12. As a user who did not ask for a preview, I want the skill to avoid downgrading quality based on its own guess about face size, output type, or display size.
13. As a user choosing an aspect ratio, I want the output to target the highest stable resolution compatible with that ratio, so that the pixel budget is used for the composition I actually requested.
14. As a user requesting a normal final image, I want stable output preferred over experimental 4K, so that nominal pixel count does not reduce generation reliability.
15. As a user explicitly requesting 4K, I want that treated as an experimental delivery target, so that the skill does not misrepresent it as the ordinary stable default.
16. As a user explicitly requesting 4K, I want the skill to claim 4K only when the active surface can request and verify the actual pixel dimensions.
17. As a user working through the built-in image generator, I want generation to continue when quality and size controls are unavailable, so that the workflow does not stop at a technical limitation.
18. As a user working through a surface without exposed controls, I want the skill not to claim `quality=high`, 2K, or 4K as a verified result, so that I can trust its delivery statements.
19. As a beginner, I want final quality and stable resolution to be internal defaults, so that I am not asked to choose technical settings on every image.
20. As a user with an explicit quality or delivery requirement, I want that requirement honored when the active surface can control it, so that my direct instruction overrides the default.
21. As a viewer of any generated image, I want one clear First Read, so that I immediately understand the intended person, emotion, action, product, or message.
22. As a viewer of any generated image, I want background, props, text, effects, and texture to support the First Read, so that equal-weight detail does not create visual clutter.
23. As a user requesting a natural photograph, I want visual impact to mean believable presence, emotional connection, or a decisive real moment, so that the image is not forced into cinematic drama.
24. As a user requesting a professional image, I want visual impact to mean competence, trust, and approachability, so that dramatic lighting does not undermine the use case.
25. As a user requesting a cinematic poster or CG key art, I want stronger dramatic impact by default, so that silhouette, scale, story stakes, lighting, and color create an immediate impression.
26. As a user requesting an editorial, commercial, avatar, or illustrative output, I want impact intensity to follow my intended use, so that the skill can be bold or restrained without losing clarity.
27. As a user requesting a photographic output, I want the prompt to establish photorealistic capture, motivated light, believable exposure, natural color, and real physical texture, so that the result feels photographed rather than rendered.
28. As a user whose visible identity matters, I want photographic quality to preserve pores, fine lines, skin tone, age impression, hair, distinctive marks, and ordinary imperfections, so that polish does not replace my face.
29. As a user requesting photographic polish, I want Natural Retouch to remain the default identity-safe finish, so that distracting temporary issues can be reduced without plastic skin or structural beautification.
30. As a user requesting CG or game key art, I want one readable identity-preserving hero silhouette, coherent foreground-to-background depth, believable materials, and controlled effects, so that spectacle does not obscure the person.
31. As a user requesting CG or game key art, I want dramatic effects to support the face, silhouette, and action, so that glow, particles, smoke, or energy do not become the subject.
32. As a user requesting any output type, I want its recipe adapted to my actual brief, so that repeated generations do not share the same fixed scene, lighting, palette, or template look.
33. As a user requesting a different medium, I want the skill to change its quality language with the medium, so that photographic skin vocabulary is not forced into illustration and CG effects are not forced into natural photography.
34. As a user receiving a production prompt, I want concrete subject, composition, light, color, material, texture, and finish direction, so that broad praise words do not stand in for visible decisions.
35. As a user receiving a production prompt, I want only a short set of likely failure constraints for the current output, so that the prompt remains focused rather than carrying a universal negative-word dump.
36. As a user using OpenAI image generation, I want negative constraints written in the ordinary prompt, so that the skill does not assume a provider-specific `negative_prompt` field.
37. As a user expecting a strong first result, I want these quality rules included in the existing First-Pass Finish and production prompt, so that quality does not become another workflow stage.
38. As a user expecting a one-pass workflow, I want no automatic second generation, upscale, or editing pass, so that the skill does not hide extra processing behind the quality default.
39. As a user reviewing a nearly correct result, I want the existing targeted revision flow to remain available, so that I can correct one visible failure without reopening unrelated decisions.
40. As a maintainer, I want quality behavior tested at the conversation and production-prompt boundary, so that tests protect user-visible results without depending on exact prose or an unavailable tool parameter.

## Implementation Decisions

- Reuse the existing coordinating workflow, output recipes, prompt craft rules, First-Pass Finish, and targeted revision flow. Do not add a quality stage, quality gate, or post-processing workflow.
- Treat a normal person-centered generation as a final asset. Only an explicit preview, draft, exploration, or high-volume batch request changes that assumption.
- Apply the final-asset quality default to every supported person-centered medium and crop, including photographic, poster, CG, editorial, avatar, commercial, and illustrative outputs.
- When the active generation surface exposes a real quality control, request `high` for every final asset. A preview, draft, exploration, or high-volume batch may use a lower setting.
- Never infer that a social avatar, wide shot, full-body image, illustration, or non-close-up composition needs less quality merely because the face or final display is smaller.
- When the active generation surface exposes a real size control, request the highest stable, non-experimental resolution compatible with the selected aspect ratio and the model's supported dimension rules.
- Do not make experimental 4K the default. Treat an explicit 4K request as a delivery requirement that can be claimed only after a compatible size was actually requested and the output dimensions were verified.
- When quality or size controls are unavailable, continue generation without another user question. Do not insert generic quality words as substitutes and do not claim an unverified setting or pixel size.
- Keep quality and resolution defaults internal. Ask no new user-facing question unless an existing delivery conflict genuinely requires a choice.
- Require a First Read for every final output. Resolve the intended audience effect, the one primary readable person, face, silhouette, action, emotion, product, or message, and the supporting hierarchy inside the existing direction and prompt flow.
- Do not equate First Read with universal drama. Natural photography, professional imagery, social avatars, editorial work, commercial work, and illustration adapt intensity to use; cinematic posters and CG or game key art default to stronger dramatic impact unless the brief says otherwise.
- Keep output recipes dynamic rather than creating fixed prompt suffixes or a user-facing style catalog. Recipes own only medium-specific quality criteria and likely failure modes.
- Photographic recipes must use `photorealistic` or equivalent real-capture semantics, motivated light, believable exposure and color, and concrete skin, hair, fabric, object, and environmental texture.
- Photographic recipes must preserve ordinary imperfections and Natural Retouch identity safeguards. Avoid plastic or waxy skin, heavy beauty retouching, CG sheen, artificial HDR halos, and glamorization that conflicts with the brief.
- Professional headshots must favor trust, competence, approachability, clean separation, natural expression, and realistic garments rather than stock-photo posing or unrequested dramatic low-key lighting.
- Cinematic posters must favor a single identity-preserving hero read, a second-read story world or conflict, title-safe composition when needed, deliberate color contrast, atmospheric depth, and restrained supporting effects.
- CG or game key art must favor one identity-preserving hero silhouette, readable action, coherent foreground/hero/deep-world layers, environmental scale, differentiated material response, controlled contrast, and effects that do not cover the face or action.
- Editorial and magazine imagery must express a brief-specific point of view through pose, gaze, styling, composition, palette, and tactile texture rather than generic luxury cues or invented cover text.
- Social avatars must preserve immediate identity readability at thumbnail size through face or silhouette priority, simple background structure, and strong separation, while retaining the same final-asset quality default.
- Commercial visuals must follow the supplied audience, positioning, brand mood, product, message hierarchy, exact copy, and negative-space needs. Do not invent brands, slogans, claims, or logos.
- Illustration and other non-photographic outputs must state the intended medium and use medium-coherent line, brush, paper, print, painted, or collage characteristics rather than accidental photorealism or plastic 3D treatment.
- Build every final production prompt from concrete positive direction first: intended use, identity and reference boundaries, First Read, composition and action, medium-specific quality, materials, motivated lighting and color, First-Pass Finish, text and delivery constraints, then likely failure constraints.
- Keep negative constraints in the ordinary prompt. Select approximately three to eight observable, output-specific failure constraints; do not add a provider-specific negative-prompt field or a universal long word list.
- Do not depend on `4K`, `8K`, `high quality`, `best quality`, `HDR`, `masterpiece`, `cinematic`, or `impactful` as standalone quality mechanisms. A term may appear only when it describes a concrete visible or delivery intent and never as a substitute for actual controls.
- Preserve every existing identity, anatomy, projection, styling, performance, text, layout, continuity, and safety contract. This feature strengthens output quality without weakening those locks.
- Keep First-Pass Finish generation-time. Do not schedule an automatic second generation, edit, upscale, or finishing pass.
- Keep the existing explicit targeted revision path for a visible failure. Preserve all unrelated locks during that revision.
- Do not add an Image API integration, API key requirement, custom backend, or new dependency in this scope.

## Testing Decisions

- Use the existing golden-conversation behavior suite as the single high-level testing seam. It already covers identity preservation, adaptive clarification, output recipes, First-Pass Finish, prompt completeness, and targeted revision behavior.
- Test externally visible routing and production-prompt behavior rather than exact prose, internal labels, a specific prompt serialization, or a generation parameter that the built-in tool does not expose.
- Add a normal full-body or environmental photographic request proving that it is treated as a final asset, receives the same high-quality intent as a close portrait, and does not get downgraded because the face occupies less of the frame.
- Add a cross-medium final-output scenario proving that photographic, poster, CG, editorial, avatar, commercial, and illustrative outputs share the final-asset quality default while adapting their visible quality language to the medium.
- Add an explicit preview or exploration scenario proving that lower quality is permitted only because the user requested the speed or batch trade-off.
- Add a no-control-surface scenario proving that generation continues without another gate and that the skill does not claim verified `quality=high`, 2K, or 4K.
- Add an explicit 4K scenario proving that 4K remains an experimental delivery requirement and is not claimed without real size control and output-dimension verification.
- Add a natural photographic scenario proving that First Read is strong without unrequested dramatic lighting, cinematic grading, heavy retouching, or CG sheen.
- Add a professional headshot scenario proving that impact is expressed as competence, trust, and approachability rather than spectacle.
- Add a cinematic poster scenario proving that a hero read, story-world read, title-safe composition, atmosphere, and controlled drama form a coherent hierarchy.
- Add a CG or game key-art scenario proving that identity-preserving silhouette, depth, scale, material response, and effects remain readable and that effects do not obscure the face or action.
- Add an editorial, commercial, avatar, or illustration scenario proving that impact intensity follows the brief rather than inheriting the poster or CG dramatic default.
- Add a dynamic-recipe scenario proving that the prompt contains concrete brief-specific scene, lighting, palette, material, and finish decisions rather than a fixed universal suffix.
- Add an adaptive-constraints scenario proving that the ordinary prompt contains only a short set of current high-risk failures and does not contain a generic negative-word dump.
- Preserve all existing First-Pass Finish tests, including Natural Retouch, explicit finish, no retouch, medium adaptation, no automatic second pass, and targeted revision preservation.

## Out of Scope

- OpenAI Image API integration, API keys, a custom generation backend, or a new dependency.
- Guaranteed runtime enforcement of quality or size on a built-in generation surface that does not expose those controls.
- Making experimental 4K the default for every image.
- 8K generation, deterministic upscaling, super-resolution, resizing, sharpening, denoising, compression, format conversion, DPI, CMYK, bleed, or print-production processing.
- A quality or resolution questionnaire for ordinary users.
- A fixed quality-word suffix, prompt gallery, style preset catalog, or universal negative-prompt list.
- A separate post-processing stage or automatic second generation, editing, or upscale pass.
- Changes to the existing identity anchor, reference sufficiency, risk, anatomy, projection, styling, performance, continuity, or safety models.
- Exact text-rendering guarantees or other delivery guarantees already outside the generation surface's verified capabilities.

## Further Notes

- `quality=high` and pixel size are real generation controls when a surface exposes them; prompt adjectives are not equivalent controls.
- The current stable default is intentionally described as the highest non-experimental size compatible with the selected aspect ratio rather than as a universal fixed canvas. The current GPT Image 2 guidance treats output above the `2560x1440` pixel envelope as experimental, but the implementation should preserve the stable-versus-experimental distinction if supported limits change.
- First Read is the canonical term for universal immediate readability. It does not mean universal dramatic treatment.
- No ADR is required because the decisions are confined to an existing skill contract, introduce no hard-to-reverse architecture, and can evolve with future generation surfaces.
- If a future built-in generation surface exposes quality and size controls, the skill can enforce the same contract directly without redesigning the user workflow.
