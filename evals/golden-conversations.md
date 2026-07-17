# Golden Conversations

Use these scenarios to review changes to the skill. They are behavioral checks, not exact scripts: option wording should adapt to the reference image and theme.

## Shared checks

- Keep all eight production dimensions in the internal decision state, but ask only unresolved, relevant choices.
- Ask one owned dimension or truly coupled group per turn; never lock a later dimension from preview text.
- Stop when every user-visible tradeoff that could materially change the result is resolved, irrelevant, or explicitly defaulted; never aim for a question count.
- Describe visible results before professional terminology.
- Do not ask beginners for camera bodies, lens models, ISO, aperture, shutter, Kelvin, light power, or modifiers.
- Do not hardcode an angle, focal length, device, or fixed camera template; generate perspective choices from visible consequences and the user's theme.
- Strong viewpoints, close camera positions, and deliberate projection exaggeration are valid locked intent, not absolute failure modes.
- Identity anchors preserve facial structure, not source face direction, shoulder line, crop scale, or selfie perspective.
- A risk gate handles missing evidence or accepted inference without reopening or silently downgrading locked camera and performance choices.
- Never repeat a locked choice. "Use recommended defaults", "you decide", or equivalent wording ends ordinary clarification.
- Reference-coverage, identity-risk, safety, and exact-text gates remain focused exceptions.
- Every visible Direction Gate contains three concrete A/B/C directions plus the permanent `D) Custom` option.
- Every concrete direction shown or internally chosen remains Shown while it is available in the current conversation context. Before presenting automatic recommendations, apply the three-of-six Direction Signature check against the current batch and every available Shown Direction; do not promise exact deduplication after earlier history is unavailable.
- Treat lighting/color/retouch/finish as one generation-time First-Pass Finish dimension, never as a later mandatory step or automatic second pass.
- When First-Pass Finish is unresolved, the existing lighting/color gate offers exactly three image-specific Finish Directions plus `D) Custom`; each direction describes one coherent visible result rather than a parameter list or palette swap.
- Route a request for replacement choices to the explicitly named creative area, otherwise the unresolved visible gate, otherwise the most recently presented refreshable gate. Ask one compact scope question only when none of those targets exists.
- Every visible refreshable creative gate contains three concrete A/B/C options plus the permanent `D) Custom` option. While history is available in the current conversation context, track all presented concrete options in per-area Shown Option histories; adopted Custom and delegated options count, while the placeholder does not.
- Outside Creative Direction, apply the two-part owner-specific visible-signature check before presenting each Fresh Option, against the current batch and every available Shown Option in the same area. Renaming, palette-only changes, adjective-only changes, equipment vocabulary, or professional terminology alone is not fresh.
- A Scoped Option Refresh preserves identity, output requirements, unrelated values, and every Explicit Lock. It may reopen only target-area Derived Locks and fields the user explicitly asks to change.
- Output Type, Role/Costume Version, Safety, reference coverage, identity risk, Perspective Intent classification, and exact-text verification remain focused or classificatory choices rather than novelty menus.
- Every identity-preserving generation or edit passes each required person reference as an actual image input. Text may explain a reference role but never replaces the Primary Identity Anchor.
- Treat every normal person-centered generation as a final asset across crops and media. Only an explicit preview, draft, exploration, or high-volume batch request permits lower quality for speed or usage.
- For a final asset, request `quality=high` and the highest stable size at or below 3,686,400 total pixels compatible with the chosen aspect ratio only when the active surface exposes those real controls. A controllable request above that threshold gets one concise experimental warning and proceeds without a confirmation gate. Otherwise continue without another gate and never claim an unverified quality setting or pixel size.
- Give every final output one clear First Read at its intended display size. Supporting scene, text, product, effects, and texture reinforce that priority; impact intensity follows the intended use rather than defaulting every medium to cinematic drama.
- Review First Read and overall hierarchy at the intended display size, then inspect only present high-risk face, hand/prop, and exact-text regions at the original available resolution. Never claim a check when the output or sufficient inspection resolution is unavailable.
- Build every final production prompt from concrete brief-specific positive direction, then approximately three to eight observable current failure constraints in the ordinary prompt. Never use a fixed quality suffix, provider-specific negative-prompt field, or universal negative-word dump.

## 1. Vague professional avatar

**Input:** `[selfie] Make this a polished LinkedIn profile photo.`

**Expected:** Use a lightweight route: practical shot/body framing and background, styling only if it materially changes the result, performance, and lighting/finish. Stop as soon as those material choices are resolved. Do not ask for a story-heavy Director Shot Plan, props, equipment, or an avoid-list.

## 2. Explicit delegation

**Input:** `[portrait] Make a natural, premium profile image; keep my clothes; you decide the rest.`

**Expected:** Lock the use, feeling, and wardrobe; accept recommended defaults for every ordinary unresolved dimension and generate without further questions. A genuine reference-coverage, identity-risk, safety, or text conflict may still trigger one focused gate.

## 3. Guided cinematic portrait

**Input:** `[portrait] I want a restrained cinematic image with a sense of story, but I do not know photography.`

**Expected:** Guide the user through distinct visible choices rather than one dense preset: creative direction/decisive moment, shot, styling if material, performance, then motivated lighting/color. A selected action in the decisive moment is locked and must not be asked again; performance asks only its remaining details. Do not ask all eight dimensions mechanically.

## 4. Partial decisions already locked

**Input:** `Keep the hat and silver jewelry, frame from the waist up, turn the body three-quarters, and look beyond the camera.`

**Expected:** Lock wardrobe/accessories, crop, body direction, and gaze. Shot direction may ask only unresolved camera placement and background relationship. Performance may ask only unresolved expression, mouth, hands, or energy. No module may ask for the locked fields again.

## 5. High-risk source-to-target jump

**Input:** `[frontal face close-up] Make a full-body poster of the same person running with a sword and shouting, from a close, wide, high camera position with strong near/far exaggeration.`

**Expected:** Lock the running/sword/shouting performance, close/wide/high camera, and strong near/far exaggeration. Record separate coverage for face identity, body scale, alternate angles, and performance/action. Ask one risk-choice gate generated only from the actual missing coverage. Offer relevant real references, user description, accepted inference, or a staged pass that addresses the gap; do not reopen creative direction or perspective, silently change camera, or replace the action with standing. The final prompt must distinguish underlying human anatomy from projected image proportions.

## 6. Exact-text poster delivery

**Input:** `[portrait] Create a 9:16 character poster titled "归途".`

**Expected:** Resolve direction, shot, styling/version if ambiguous, performance, and lighting without combining them into one package. Reserve a readable title-safe region and verify `归途` character by character. If a targeted text revision still fails, offer to regenerate a clean no-text base rather than claiming exact delivery.

## 7. Series continuity

**Input:** `Use the same person for three connected rainy-night station images; keep the clothes and station consistent.`

**Expected:** Enable a continuity contract only for this series: identity, clothing, hair/makeup, wetness, prop state, light direction, location geography, and color treatment remain locked. Each image may change its decisive moment, performance, and shot. Single-image tasks must not receive this extra workflow.

## 8. Surgical revision

**Input:** `Only fix the left hand; keep everything else unchanged.`

**Expected:** Read only the identity and styling/performance constraints needed for the edit. Repeat the identity lock and preserve face, crop, camera, pose, text, background, lighting, and color. Do not restart creative direction or generate a new concept.

## 9. Frontal identity reference with an angled performance

**Input:** `[frontal chest-up portrait] Keep the same person, but turn the body and head toward the action and look away from camera.`

**Expected:** Preserve facial structure without preserving the source face direction. Lock the selected body direction, head turn, and gaze. Identity readability must be evaluated at that target angle: a three-quarter or profile face may narrow or hide the far eye. Do not rotate the face back toward camera merely to show both eyes, and do not ask for the locked action or gaze again.

## 10. User wants spatial impact without camera vocabulary

**Input:** `[person reference] Make the portrait feel spatially dramatic, but I do not know lenses or camera angles.`

**Expected:** Ask one perspective-intent question using visible outcomes generated for the theme: physically strong near/far exaggeration, strong viewpoint with controlled projected proportions, proportion-first perspective, and optional custom direction. Do not use fixed angles, focal lengths, or equipment. The answer locks viewpoint/distance character, perspective strength, and allowed projection exaggeration without silently locking action, expression, styling, or lighting.

## 11. Dynamic action from an upper-body reference

**Input:** `[upper-body reference; user accepted body inference] Create a full-body action with a strong body turn and the head following the movement.`

**Expected:** Write one coherent pose geometry chain using only the relationships relevant and visible in the chosen action, such as support/contact, weight, pelvis, torso/shoulders, neck/head, facial plane/gaze, and hands/props. Those included must agree with the locked camera and perspective; do not require an off-frame hand, a ground contact for an airborne action, or another irrelevant node. Do not substitute generic "natural dynamic pose", a static torso with decorative limbs, a near-camera gaze, or another risk gate.

## 12. Repair coordination without erasing intentional projection

**Input:** `[result visible] The strong near/far exaggeration is correct, but the turned body has a frontal face and the torso is randomly compressed. Fix only the coordination.`

**Expected:** Preserve camera position, perspective strength, intentional projection exaggeration, action, composition, background, lighting, color, text, and identity anchors. Correct only underlying anatomy discontinuity plus neck/head/facial-plane/gaze alignment. Do not normalize the shot, move the camera, turn the action into standing, or rebuild the concept.

## 13. Three consecutive Style Refreshes

**Input:** `[portrait] Show A/B/C plus D) Custom for a cinematic editorial portrait. I reject the first batch, then request three consecutive new batches.`

**Expected:** Each gate contains exactly three concrete A/B/C directions plus `D) Custom`. The three refreshes add nine Shown Directions; every new Direction Signature differs from every direction shown earlier in the conversation, including options from the same batch, in at least three of production context, medium/era, scene and decisive moment, composition grammar, lighting/color logic, and finish. Renaming, a palette-only change, or equipment vocabulary does not count as fresh.

## 14. Unselected options still become Shown Directions

**Input:** `[portrait] Present a creative-direction gate. I choose none of A/B/C and ask for another batch.`

**Expected:** Record all three presented A/B/C options immediately, not only a selected or generated direction. The next batch must be fresh against all three. Keep the tracking conversation-local and require no persistence or setup.

## 15. Adopted Custom Direction

**Input:** `[portrait] D) Custom: an embossed paper-cut theatre portrait with flat side-on staging. Now refresh the style.`

**Expected:** Derive and record the adopted Custom Direction's six-part Direction Signature, then exclude equivalent automatic recommendations. Every refreshed gate still includes the permanent `D) Custom` placeholder; never record or consume the placeholder itself.

## 16. Style Refresh lock provenance

**Input:** `[portrait] Keep a 4:5 canvas, exact title "NIGHT WALK", black jacket, walking action, leftward gaze, and subject on the right third. Choose direction A and use recommended defaults. Now refresh the style.`

**Expected:** Preserve identity and every Explicit Lock for canvas, exact text, wardrobe, action, gaze, and composition. Reopen the selected creative direction and its direction-owned Derived Locks; values introduced by selected/defaulted direction details must not be misclassified as unrelated Explicit Locks. Preview details that were never repeated or defaulted remain suggested rather than locked.

## 17. Only change the visual style

**Input:** `[portrait] Keep the current scene, action, composition, and subject placement. Only change the visual style.`

**Expected:** Reopen only medium/era, lighting/color, material treatment, and finish. Preserve the scene, action, composition, subject placement, identity, and every other Explicit Lock. Show exactly three Fresh Directions plus `D) Custom` unless the user delegates the choice.

## 18. Completely change the direction

**Input:** `[portrait] Completely change the direction, but keep the same person, 9:16 canvas, exact title "EMBER", and white coat.`

**Expected:** Reopen creative direction plus its derived scene, unlocked composition suggestions, lighting/color, and finish. Preserve identity, output requirements, exact text, wardrobe, and every unrelated Explicit Lock. Do not restart the brief or weaken reference-coverage and identity-risk gates.

## 19. Ordinary refresh versus Trend Refresh

**Input:** `First: give me another batch. Later: make the next batch feel like a 1990s yearbook. Finally: show me current visual directions for 2026.`

**Expected:** The ordinary Style Refresh and the historical-era constraint use the Direction Atlas and conversation history without browsing. The explicit dated/current request triggers live visual research, extracts concrete production anchors, keeps source links available, and applies the same freshness threshold. If research is unavailable, say currentness could not be verified rather than guessing or presenting remembered styles as current.

## 20. Delegated Refresh

**Input:** `[upper-body portrait] I reject the previous directions. Pick a completely different direction yourself and continue; infer the missing full-body and angle evidence.`

**Expected:** Do not display a Direction Gate. Select one compatible Fresh Direction internally, record it as Shown, apply recommended defaults, and continue. The user's accepted inference resolves that coverage gap, while any new focused identity, coverage, safety, or exact-text gate remains available.

## 21. Refresh Exhaustion

**Input:** `[portrait] Keep the exact scene, composition, action, lighting, palette, medium, and finish, but give me three fresh directions after many prior batches.`

**Expected:** If the skill cannot assemble three directions that satisfy both the three-part freshness threshold and every Explicit Lock, declare Refresh Exhaustion. Do not display a partial or padded Direction Gate. Identify the single Explicit Lock most responsible and ask whether to reopen only that dimension, using the standard decision format with stop and `D) Custom` paths. If the user keeps every lock, stop refreshing instead of offering a non-fresh batch.

## 22. Explicitly restore a Shown Direction

**Input:** `Bring back the earlier "Moonlit flooded citadel" direction exactly.`

**Expected:** Honor the explicit request even though the direction is already Shown. Freshness limits automatic recommendations, not deliberate user reuse.

## 23. Defaulted photographic First-Pass Finish

**Input:** `[selfie] Turn this into a polished LinkedIn headshot. Keep my face, age, mole under my left eye, natural skin tone, and current clothes. Use recommended defaults for everything else.`

**Expected:** Generate without another ordinary question. The first prompt includes a coherent lighting/color/retouch/finish treatment and uses Natural Retouch: reduce distracting shine, clearly temporary redness, minor unevenness, and clearly temporary blemishes while preserving pores, fine lines, skin tone, age impression, facial structure, the named mole, every uncertain mark, and natural texture. Do not redesign the face or schedule another generation/editing pass.

## 24. Unresolved beginner Finish Directions

**Input:** `[portrait] Keep the locked 4:5 rainy-station editorial direction, waist-up shot, black jacket, three-quarter turn, quiet expression, and gaze past camera. Everything is resolved except light, color, retouching, texture, and the final finished feeling; I do not know post-production.`

**Expected:** Reuse the existing lighting/color gate rather than adding a post-processing step. Show exactly three image-specific Finish Directions labeled A/B/C plus `D) Custom`, with one recommendation and one short visible-result reason. Each direction makes its overall feeling, light/contrast, person/environment color relationship, identity-safe facial treatment, and relevant texture easy to imagine. Do not ask for LUTs, software, camera, or parameter-by-parameter choices.

## 25. Explicit finish bypasses the gate

**Input:** `[portrait] Make a 4:5 editorial portrait with soft window-like side light, neutral skin, muted warm walls, open shadows, visible pores and fine lines, no grain, and a clean matte finish. Keep my identity and use recommended defaults for everything else.`

**Expected:** Lock the explicit finish, resolve only its materially relevant production controls, and generate without a Finish Direction question. Do not replace the requested treatment with a preset name or ask the user to choose it again.

## 26. No facial retouching

**Input:** `[portrait] Keep my face completely unretouched and preserve the scar over my right eyebrow. You decide the global light, color, contrast, grain, and texture.`

**Expected:** Lock no facial retouching and the named scar. Resolve global lighting/color/retouch/finish internally and keep exposure, contrast, grain, sharpness, and environmental texture available without applying facial cleanup, smoothing, blemish removal, or structural change.

## 27. Stronger retouching follows the existing identity boundary

**Input:** `[portrait] Give me stronger complexion cleanup, tidier flyaway hair, and refined editorial skin texture, but keep the same face. Also make my jaw narrower, skin lighter, and age me down ten years.`

**Expected:** Apply the non-structural complexion, grooming, and texture polish without another beauty-specific gate. Route the narrower jaw, lighter skin, and younger apparent age through the existing identity risk-choice gate because they alter protected identity anchors; do not silently apply, reject, or weaken those requested structural changes.

## 28. Medium-adapted CG First-Pass Finish

**Input:** `[portrait] Make premium dark-fantasy game key art. Keep the identity, 16:9 canvas, full-body stance, bronze lamellar armor, ruined gate, low camera, and amber moonlight. Everything is locked except the final surface, material, and finished look.`

**Expected:** Use the existing lighting/color gate to offer three coherent, image-specific material/medium Finish Directions plus `D) Custom`. Describe face rendering, bronze, cloth, stone, atmosphere, surface detail, and final key-art character in medium-appropriate language; do not turn the choice into photographic skin-retouching, LUT, exposure, or irrelevant editing controls.

## 29. Explicit targeted finish revision

**Input:** `[result visible] The skin looks plastic. Fix only that finish problem.`

**Expected:** Enter the targeted revision flow only because the user explicitly requested it. Restore natural skin texture, repeat the identity invariants, and preserve composition, crop, camera, pose, expression, gaze, wardrobe, text, product placement, background, and every other locked element. Do not restart the concept or perform another unrequested pass after this revision.

## 30. Active Finish Refresh

**Input:** `[portrait at the Finish Direction gate] These three do not work. Give me another batch.`

**Expected:** Refresh only First-Pass Finish. Show three new image-specific Finish Directions plus `D) Custom`; preserve identity, creative direction, scene, Shot, Styling, Performance, canvas, and text. Do not enter Style Refresh, generate an image, or start a targeted revision.

## 31. Explicit refresh target beats the visible gate

**Input:** `[portrait at the Finish Direction gate] Give me three new shot choices instead.`

**Expected:** Refresh only Shot because the user named it explicitly. Keep First-Pass Finish unresolved, preserve every unrelated choice and Explicit Lock, and do not interpret the request as Style Refresh.

## 32. Recent refreshable gate survives adoption and generation

**Input:** `[user adopted a Finish Direction and generated the first image; no later refreshable gate was shown] The choices from before were not right after all. Give me another batch.`

**Expected:** Treat First-Pass Finish as the most recently presented refreshable gate and show three Fresh Finish Directions plus `D) Custom`. Do not edit or regenerate the visible image merely because choices were requested.

## 33. No reliable refresh scope

**Input:** `[new conversation with a person reference but no creative gate yet] Give me some more options.`

**Expected:** Ask one compact localized scope question with concrete choices such as creative direction, Shot, Styling, Performance, or First-Pass Finish. Do not silently default to Style Refresh, create nested menus, or ask several questions.

## 34. Named creative refresh while a focused gate is pending

**Input:** `[reference-coverage gate is unresolved] Before I answer that, give me three new performance choices.`

**Expected:** Refresh only Performance and keep the reference-coverage gate unresolved for return before generation. The topic change does not accept evidence inference, weaken the focused gate, or turn its paths into creative options.

## 35. Partial Shot reopen preserves an Explicit Lock

**Input:** `[waist-up framing is locked] Keep it waist-up, but give me three new shot relationships.`

**Expected:** Preserve the waist-up body cutoff. Generate three Shot options plus `D) Custom` that differ through viewpoint/distance/projection, subject placement, or spatial/background relationship; do not change style, action, expression, or lighting.

## 36. Three consecutive Decisive Moment refreshes

**Input:** `[story-bearing direction locked] Reject the Decisive Moment gate and request three consecutive new batches.`

**Expected:** Each batch contains three concrete moments plus `D) Custom`. Every new moment differs from all prior moments in at least two of event/action, before/after tension, story evidence, and first impression while remaining inside the locked Creative Direction.

## 37. Three consecutive Shot refreshes

**Input:** `[scene and Creative Direction locked] Reject the Shot gate and request three consecutive new batches.`

**Expected:** Each batch contains three concrete Shot options plus `D) Custom`. Every option differs from all prior Shot options in at least two of body cutoff/subject scale, viewpoint/distance/projection, subject placement, and spatial layers/background relationship. Fixed crop labels, equipment tokens, and renamed versions do not count as fresh.

## 38. Three consecutive First-Pass Finish refreshes

**Input:** `[all dimensions except First-Pass Finish locked] Reject the Finish gate and request three consecutive new batches.`

**Expected:** Each batch contains three image-specific Finish Directions plus `D) Custom`. Every option differs from all prior Finish options in at least two of overall feeling, lighting/contrast, person-environment color relationship, face/material treatment, and texture/final character. A palette-only change is not fresh.

## 39. Three consecutive Styling refreshes

**Input:** `[professional portrait with identity, scene, Shot, and Performance locked] Reject the Styling gate and request three consecutive new batches.`

**Expected:** Each batch contains three concrete Styling options plus `D) Custom`. Every option differs from all prior Styling options in at least two of silhouette/layers, materials, headwear/accessories, makeup/hair/grooming, and props. Preserve every named garment or accessory Explicit Lock; do not reuse keep/simplify/replace as a fixed catalog.

## 40. Three consecutive Performance refreshes

**Input:** `[Decisive Moment and Shot locked] Reject the Performance gate and request three consecutive new batches.`

**Expected:** Each batch contains three visible Performance options plus `D) Custom`. Every option differs from all prior Performance options in at least two of action/body direction, expression/mouth, gaze, hands/prop interaction, and energy. Adjective-only changes such as “more natural” or “more powerful” are not fresh.

## 41. Three consecutive Layout refreshes

**Input:** `[poster exact title and platform requirements locked] Reject the Layout gate and request three consecutive new batches.`

**Expected:** Each batch contains three Layout options plus `D) Custom`. Every option differs from all prior Layout options in at least two of layout structure, subject/text-safe placement, safe areas/readability, and required variant organization. Preserve exact text, required aspect ratio, and platform delivery locks.

## 42. Scoped Custom option history

**Input:** `[Shot gate] D) Custom: waist-up, low viewpoint, subject on the far right, deep empty platform to the left. Now give me a new Shot batch.`

**Expected:** Record the adopted Custom Shot in Shot history and exclude equivalent automatic recommendations. Keep the `D) Custom` placeholder available in the next gate; do not add the Custom Shot to Creative Direction or another area's history.

## 43. Scoped Delegated Refresh

**Input:** `[Performance already exists] I do not like that action. Pick a fresh one yourself and continue.`

**Expected:** Do not display a Performance gate. Select and record one compatible Fresh Performance internally, preserve unrelated values and Explicit Locks, then continue; focused risk, coverage, safety, and exact-text gates remain available.

## 44. Scoped Refresh Exhaustion

**Input:** `[waist-up crop, eye-level viewpoint, centered placement, flat background, and proportion-first perspective are all Explicit Locks after many Shot batches] Give me three new Shot options without changing anything.`

**Expected:** If the skill cannot assemble three Shot options that satisfy both the two-part Shot freshness threshold and every Explicit Lock, declare Refresh Exhaustion. Do not display a partial or padded Shot gate. Identify the single Explicit Lock most responsible and ask whether to reopen only that field, while retaining stop and `D) Custom` paths. If every lock stays, stop; do not fabricate a batch or escalate to Style Refresh.

## 45. Focused and classificatory gates do not become novelty menus

**Input:** `[Safety, reference-coverage, identity-risk, Output Type, Role/Costume Version, or exact-text gate is visible] Give me more options.`

**Expected:** Keep the active gate fact-dependent and offer only paths justified by the actual intent, evidence, classification, or text problem. Do not apply Shown Option history, a two-part freshness threshold, or unrelated creative choices.

## 46. Perspective classification stays stable

**Input:** `[strong viewpoint with controlled projected proportions is locked] Give me three more spatially dramatic choices.`

**Expected:** Preserve the selected Perspective Intent and generate Fresh Shot expressions within it. Do not invent a fourth perspective-risk category, weaken the controlled-proportion constraint, or reopen action, Styling, Performance, or First-Pass Finish.

## 47. Full-body final asset keeps the same quality priority

**Input:** `[front and three-quarter full-body references] Create a final 3:2 environmental photograph of me crossing a windy pedestrian bridge at blue hour. Keep my identity, age, skin tone, charcoal coat, full-body walking action, sideward gaze, bridge setting, and natural documentary mood. Use recommended defaults.`

**Expected:** Treat the result as a final asset even though the face occupies less of the frame. If the active surface exposes real controls, request `quality=high` and the highest stable, non-experimental 3:2 size it supports. Preserve identity, clothing, hands, body scale, material texture, and environmental detail; never downgrade quality because the request is full-body or environmental.

## 48. Final quality is shared across media

**Input:** `[person references; all production choices resolved] Prepare one final photographic portrait, cinematic poster, CG key art image, editorial image, social avatar, commercial visual, and illustration in their already locked aspect ratios.`

**Expected:** Treat every output as a final asset and apply the same real `quality=high` default when available, including the avatar and illustration. Use the highest stable supported size compatible with each locked aspect ratio rather than lowering quality based on crop, face size, medium, or display size. Medium-specific prompt language may differ; final-asset priority does not.

## 49. Explicit preview permits the trade-off

**Input:** `[portrait] I am exploring 12 quick 1:1 social-avatar directions. Treat these as previews and favor speed over final fidelity.`

**Expected:** Permit a lower quality setting only because the user explicitly requested previews and a speed trade-off. Preserve identity and thumbnail readability, do not silently promote the previews to final assets, and do not imply a later upscale or automatic finishing pass.

## 50. Generation surface exposes no quality or size controls

**Input:** `[person reference; final 4:5 photographic brief fully resolved] Generate now. The active surface exposes no quality or size control.`

**Expected:** Continue generation without another user question. Keep the final-asset intent concrete through composition, motivated light, believable materials and texture, and First-Pass Finish, but leave exact size and application of the experimental-size rule unverified. Do not claim that `quality=high`, 2K, 4K, or any exact pixel size was applied, and do not insert generic quality words as substitute controls.

## 51. Explicit 4K remains experimental and verifiable

**Input:** `[face, three-quarter, and full-body references; final 16:9 poster brief fully resolved] I need true 4K delivery. The active surface exposes no size control and output dimensions cannot be verified.`

**Expected:** Treat 4K as one example of an explicit experimental-size delivery requirement, not the ordinary default. Continue only with honest capability language: do not claim 4K, set an invented generated resolution, or imply an automatic upscale. A 4K claim is allowed only after a compatible real size was requested and the resulting pixel dimensions were verified.

## 52. Natural photographic First Read stays believable

**Input:** `[portrait and half-body references] Create a final natural 4:5 photograph of me quietly laughing with a friend just outside frame at a bright neighborhood cafe. Keep my identity, age, freckles, blue overshirt, seated pose, and daylight setting. The person and real emotion must register first; keep the cafe supportive and calm, not cinematic or dramatic. Use recommended defaults.`

**Expected:** Make the person's real emotion the First Read through photorealistic capture semantics, a decisive believable moment, motivated daylight, natural exposure and color, and physical skin, hair, fabric, and cafe texture. Keep the environment subordinate. Preserve ordinary imperfections and Natural Retouch; do not add dramatic low-key light, cinematic grading, heavy beauty retouching, artificial HDR halos, or CG sheen.

## 53. Professional impact means trust

**Input:** `[selfie] Create a final LinkedIn headshot. Keep my identity and current navy shirt. I should read as competent, trustworthy, and approachable. Use recommended defaults.`

**Expected:** Make the face and natural expression the First Read. Use clean separation, realistic garment structure, motivated professional lighting, believable skin texture, and calm posture to express competence, trust, and approachability. Do not substitute spectacle, stock-photo posing, an invented blazer, or unrequested dramatic low-key lighting.

## 54. Cinematic poster uses a controlled two-level hierarchy

**Input:** `[person references] Create a final 9:16 cinematic poster with the exact title "ASH HARBOR". Keep my identity, storm-damaged ferry terminal, red rescue coat, and title-safe upper area. Use recommended defaults.`

**Expected:** Make one identity-preserving hero face or silhouette the First Read, then let the damaged terminal and visible conflict form the second read. Use deliberate contrast, atmospheric depth, title-safe composition, and restrained effects that support the person and story. Keep exact text separate from the hero read; do not create equal-weight detail or generic spectacle.

## 55. CG key art keeps effects subordinate

**Input:** `[face, three-quarter, and full-body references] Create final 16:9 dark-fantasy game key art of me defending a ruined hill gate. Keep my identity, age, scar, full-body scale, bronze lamellar armor, forward lunge, low viewpoint, storm setting, and no text. The face and hero silhouette must read first; the ruined army and valley read second. Effects must support the action without covering my face or weapon. Use recommended defaults.`

**Expected:** Build one readable identity-preserving hero silhouette with coherent foreground, hero, gate, army, and deep-valley layers. Differentiate bronze, leather, cloth, stone, rain, and atmosphere through believable material response and controlled contrast. Keep scale and action readable; glow, particles, smoke, rain, and energy remain restrained and never cover the face, silhouette, weapon, or decisive action.

## 56. Editorial, commercial, avatar, and illustration adapt impact

**Input:** `[person reference; each brief otherwise resolved] Prepare four final outputs: a restrained literary-magazine portrait, a bright skincare campaign with supplied product and exact copy, a quiet social avatar, and a hand-cut paper illustration.`

**Expected:** Give each output one brief-specific First Read without inheriting poster or CG drama. The editorial uses pose, gaze, styling, palette, composition, and tactile print-like texture to express a point of view without generic luxury or invented cover text. The commercial visual follows the supplied audience, positioning, product, exact copy, message hierarchy, and negative space without inventing claims or branding. The avatar prioritizes immediate identity readability, simple background structure, and strong separation at thumbnail size while retaining final-asset quality. The illustration names the hand-cut paper medium and uses coherent edges, fibers, layering, ink, and shadow rather than accidental photorealism or plastic 3D treatment.

## 57. Production recipe stays brief-specific

**Input:** `[person references] Create two final photographic environmental portraits with the same identity and 3:2 canvas: one is a quiet winter laundromat goodbye at dawn; the other is a hot afternoon bicycle-repair victory outside a roadside shop. Use recommended defaults.`

**Expected:** Build two distinct production prompts from the actual brief. Each prompt names its own First Read, decisive action, composition, motivated light, color relationship, materials, environmental texture, and First-Pass Finish. Do not reuse a fixed scene, lighting setup, palette, finish, quality-word suffix, or template look merely because both outputs share a medium and canvas.

## 58. Constraints stay short and adaptive

**Input:** `[person reference; final commercial portrait brief fully resolved] The product is a supplied matte ceramic travel mug; no text is requested. Generate now.`

**Expected:** Put concrete positive direction first, then include approximately three to eight observable failures most likely for this image, such as identity drift, malformed product-hand interaction, changed mug shape, random text, or plastic skin. Keep them inside the ordinary prompt. Do not add a provider-specific `negative_prompt` field, copy the full universal identity/anatomy/text/style list, or rely on `4K`, `8K`, `high quality`, `HDR`, `masterpiece`, or `cinematic` as standalone quality mechanisms.

## 59. Unavailable refresh history is not an exact guarantee

**Input:** `[long conversation; early Shot batches are no longer available in the current context] Give me another Shot batch.`

**Expected:** Apply the two-part Shot freshness check against the three candidates in the new batch and every Shown Shot still available in the current conversation context. Do not claim that the new batch is unique against unavailable history, add persistence or setup, or insert a warning or extra clarification into an otherwise successful refresh.

## 60. Accessible identity reference remains an image input

**Input:** `[attached person image; portrait brief fully resolved] Use recommended defaults and generate now.`

**Expected:** Pass the attached person reference to the active generation surface as an actual image input and identify it as the Primary Identity Anchor. A textual identity summary may support the production prompt but must not replace the image.

## 61. Required identity image is no longer tool-accessible

**Input:** `[the person reference is visible in old conversation history but the active image tool cannot include it; all creative choices and accepted risks are resolved] Generate now.`

**Expected:** Stop before generation and ask only for the missing person reference to be reattached. Do not generate from its text description, reopen creative choices, repeat risk gates, or discard Explicit Locks, Derived Locks, and accepted risks.

## 62. Multiple reference roles remain distinct at generation

**Input:** `[Image 1: face identity; Image 2: required profile angle of the same person; Image 3: wardrobe; Image 4: pose; Image 5: style; all choices resolved] Generate the locked profile portrait.`

**Expected:** Pass Images 1 and 2 as required person image inputs and label every included reference by role. Keep Image 1 as the Primary Identity Anchor; wardrobe, pose, and style references guide only their named roles and never overwrite face identity.

## 63. Accepted inference does not permit text-only identity

**Input:** `[attached face image; no body or action reference] Infer the full-body scale, profile angle, and running performance. I accept that risk. Generate now.`

**Expected:** Continue without repeating the accepted coverage gate, but still pass the attached face image as the Primary Identity Anchor. Accepted inference applies only to missing body, angle, and performance evidence; it is not permission to omit the identity image.

## 64. Experimental size uses strict total-pixel area

**Input:** `[final briefs resolved; real size control available] Compare requested outputs of 2560x1440, 2561x1440, 2048x1152, 2048x2048, and 3840x2160.`

**Expected:** Treat exactly 3,686,400 pixels as non-experimental. Treat every larger area as experimental, including 2561x1440, 2048x2048, and 3840x2160; keep 2048x1152 eligible as a stable-size candidate when supported. Classify by total area rather than an edge label such as 2K or 4K.

## 65. Explicit controllable experimental size warns and proceeds

**Input:** `[person reference; final square portrait brief resolved; real size control available] Generate at 2048x2048.`

**Expected:** State concisely that the requested size is experimental, then proceed with the controllable request. Do not ask for confirmation, add a quality questionnaire, substitute a smaller size, or schedule an automatic retry or upscale.

## 66. Exact size is claimed only after inspection

**Input:** `[generated asset requested at 2048x1152] Deliver the result as exactly 2048x1152.`

**Expected:** Claim the exact dimensions only if the generated asset itself was inspected and measured at 2048x1152. A requested control value or prompt phrase alone is not verification; otherwise mark the dimensions unverified.

## 67. Review uses intended and original scales

**Input:** `[visible final poster at original resolution; intended mobile display size known; the face, one hand holding a supplied prop, and exact title "ASH HARBOR" are visible] Review the result.`

**Expected:** Judge First Read, hierarchy, composition, and readability at the intended mobile display size. Then inspect the face and identity geometry, visible hand/prop contact, and every title character at the original available resolution. Skip any high-risk region not present rather than running a fixed checklist.

## 68. Strong-angle review preserves natural asymmetry

**Input:** `[visible profile portrait at original resolution] Review the face before delivery.`

**Expected:** Judge facial coherence against the locked profile angle, projection, head turn, and gaze. Accept angle-correct feature visibility and natural facial asymmetry; do not demand bilateral symmetry, reveal the far eye, rotate the face toward camera, or redesign it as frontal.

## 69. Unavailable evidence limits review claims

**Input:** `[case A: generated result is not visible; case B: a result is visible only as a thumbnail too small to inspect the face and exact text] Report final QA.`

**Expected:** In case A, report visual QA as unavailable. In case B, report First Read only if the thumbnail supports that check and mark face identity, geometry, and exact text unverified because the required inspection resolution is unavailable. Do not claim checks based on the prompt or requested controls.
