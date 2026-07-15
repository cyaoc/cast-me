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
- Every concrete direction shown or internally chosen is tracked for the current conversation; automatic recommendations differ from every Shown Direction in at least three of the six Direction Signature parts.
- Treat lighting/color/retouch/finish as one generation-time First-Pass Finish dimension, never as a later mandatory step or automatic second pass.
- When First-Pass Finish is unresolved, the existing lighting/color gate offers exactly three image-specific Finish Directions plus `D) Custom`; each direction describes one coherent visible result rather than a parameter list or palette swap.
- Route a request for replacement choices to the explicitly named creative area, otherwise the unresolved visible gate, otherwise the most recently presented refreshable gate. Ask one compact scope question only when none of those targets exists.
- Every visible refreshable creative gate contains three concrete A/B/C options plus the permanent `D) Custom` option. Track all presented concrete options in conversation-local, per-area Shown Option histories; adopted Custom and delegated options count, while the placeholder does not.
- Outside Creative Direction, every Fresh Option differs from every Shown Option in the same area, including options in the current batch, in at least two owner-specific visible signature parts. Renaming, palette-only changes, adjective-only changes, equipment vocabulary, or professional terminology alone is not fresh.
- A Scoped Option Refresh preserves identity, output requirements, unrelated values, and every Explicit Lock. It may reopen only target-area Derived Locks and fields the user explicitly asks to change.
- Output Type, Role/Costume Version, Safety, reference coverage, identity risk, Perspective Intent classification, and exact-text verification remain focused or classificatory choices rather than novelty menus.

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

**Expected:** Do not weaken the three-part freshness threshold or silently relax locks. Identify the single Explicit Lock most responsible for leaving fewer than three Fresh Directions and ask whether to reopen only that dimension, using the standard decision format. If the user keeps every lock, stop refreshing instead of offering a non-fresh batch.

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

**Expected:** Keep the two-part Shot freshness threshold. Identify the single Explicit Lock most responsible for leaving fewer than three Fresh Options and ask whether to reopen only that field, while retaining stop and `D) Custom` paths. If every lock stays, stop; do not fabricate a batch or escalate to Style Refresh.

## 45. Focused and classificatory gates do not become novelty menus

**Input:** `[Safety, reference-coverage, identity-risk, Output Type, Role/Costume Version, or exact-text gate is visible] Give me more options.`

**Expected:** Keep the active gate fact-dependent and offer only paths justified by the actual intent, evidence, classification, or text problem. Do not apply Shown Option history, a two-part freshness threshold, or unrelated creative choices.

## 46. Perspective classification stays stable

**Input:** `[strong viewpoint with controlled projected proportions is locked] Give me three more spatially dramatic choices.`

**Expected:** Preserve the selected Perspective Intent and generate Fresh Shot expressions within it. Do not invent a fourth perspective-risk category, weaken the controlled-proportion constraint, or reopen action, Styling, Performance, or First-Pass Finish.
