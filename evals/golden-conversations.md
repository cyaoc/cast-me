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
- A risk gate handles missing evidence or an explicit Inference Boundary without reopening or silently downgrading locked camera and performance choices.
- A broad statement such as `I accept lower likeness` or `infer the missing evidence` does not define an Inference Boundary; list the exact missing regions or facts before generation.
- Never repeat a locked choice. "Use recommended defaults", "you decide", or equivalent wording ends ordinary clarification.
- Reference-coverage, identity-risk, safety, and exact-text gates remain focused exceptions.
- Every user-visible Choice Gate contains exactly four scoped paths labeled A/B/C/D. A through C are concrete and valid; when only two substantive resolutions exist, C keeps the current state and stops instead of padding the gate. D is always a localized, gate-specific Custom Path that cannot bypass safety, preserve a physical contradiction, or silently reopen unrelated Explicit Locks.
- The `D) Custom` placeholder creates no lock or history entry. A concrete custom answer receives the presenting gate's normal validation, lock, and history treatment; only an adopted creative Custom Direction becomes a Shown Direction.
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
- For a final asset, request `quality=high` when a real quality control exists and, independently, the highest stable size at or below 3,686,400 total pixels compatible with the chosen aspect ratio when a real size control exists. A controllable request above that threshold gets one concise experimental warning and proceeds without a confirmation gate. Continue when either control is absent and never claim its unverified setting.
- Give every final output one clear First Read at its intended display size. Supporting scene, text, product, effects, and texture reinforce that priority; impact intensity follows the intended use rather than defaulting every medium to cinematic drama.
- Review First Read and overall hierarchy at the intended display size, then inspect only present high-risk face, hand/prop, and exact-text regions at the original available resolution. Never claim a check when the output or sufficient inspection resolution is unavailable.
- Build every final production prompt from concrete brief-specific positive direction, then approximately three to eight observable current failure constraints in the ordinary prompt. Never use a fixed quality suffix, provider-specific negative-prompt field, or universal negative-word dump.
- For exact copy, derive ordinary missing typography internally. The production prompt must enumerate the complete allowed-text set and give every string a role/hierarchy, compatible type character, color, relative size, and precise region/alignment; forbid additional text when the set is complete.
- Before generation, require Physical Scene Coherence across setting and time/weather, Shot and perspective, Performance, Styling/materials, and lighting/finish. Reconcile Suggested and Derived conflicts internally, honor clear later Explicit overrides, and ask once only for incompatible Explicit Locks with no override relationship.
- Every recommendation inherits the current locks, accepted risks, and known identity or geometry risk. Prefer the valid path that adds no avoidable unresolved identity risk without hiding alternatives or silently weakening locked creative intent.
- After the production prompt is assembled, check the resolved combination once for target-critical missing evidence or materially reduced Protected Identity Cue readability. Route only the current blocker through the existing Reference Coverage, identity-risk, or reattachment behavior; do not add a combined-risk gate, score, cue count, or risk budget.
- Identity Review first decides completion: recognizability is insufficient when any source-supported Protected Identity Cue has material, unaccepted drift after accounting for locked target conditions and accepted risk. Only after failure does result reliability choose one coherent local correction versus identity-wide regeneration from the Primary Identity Anchor and locked brief without the failed result.
- When the Primary Identity Anchor visibly supports them, the final prompt describes concrete source-observed facial relationships before styling and finish. Generic identity phrases do not replace those details, and character references contribute only hair, makeup, wardrobe, accessories, props, and performance.
- Before generation, every Explicit wardrobe/body-cutoff requirement must be visible, intentionally off-frame, or resolved through the existing Physical Scene Coherence confirmation. `Where the crop allows` is not a resolution; expanding the crop can trigger Reference Coverage for newly exposed evidence.
- A likeness complaint triggers Identity Review but does not prove a local defect. Compare the visible result directly with the Primary Identity Anchor before choosing edit versus regeneration; when likeness repair is combined with a non-local pose, action, camera, crop, or whole-image geometry change, regenerate from reliable identity evidence instead of calling the operation surgical.
- Automatic identity-wide regeneration requires visible, inspectable failure plus active-surface controls that can include the Primary Identity Anchor and exclude the failed result. Perform at most one new generation and one follow-up Identity Review; never claim review, correction, or completion when those controls or visual evidence are unavailable.
- An accepted identity risk applies only to the named cue, occlusion, angle, transformation, or missing evidence. It neither repeats within that boundary nor waives a newly introduced or unrelated identity risk.

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

**Expected:** Lock the running/sword/shouting performance, close/wide/high camera, strong near/far exaggeration, and full-body Shot. Record coverage by evidence type and region: the visible face and upper-body relationships remain verified Visible Body Evidence, while unseen lower body, alternate angles, and performance/action remain missing. Ask one Choice Gate with A) add relevant real evidence, B) describe the missing facts, C) accept a precise Inference Boundary, and D) supply another valid coverage resolution. Preserve the locked full-body Shot; do not offer a fallback crop, body concealment, standing pose, or weaker perspective. Selecting inference authorizes only the listed missing evidence and never reclassifies verified evidence. The final prompt must distinguish verified anatomy from inferred regions and projected image proportions.

## 6. Exact-text poster delivery

**Input:** `[portrait] Create a 9:16 character poster titled "归途".`

**Expected:** Resolve direction, shot, styling/version if ambiguous, performance, and lighting without combining them into one package. Do not add a routine typography question. In the production prompt, preserve `归途` verbatim as the complete allowed-text set; identify it as the title; derive a direction-compatible type character, color, dominant relative size, and precise title-safe region/alignment; and forbid all other text. Verify `归途` character by character without applying Latin-only capitalization or spelling advice. If a targeted text revision still fails, offer to regenerate a clean no-text base rather than claiming exact delivery.

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

**Input:** `[upper-body reference; user accepted an Inference Boundary for the missing lower-body and action evidence] Create a full-body action with a strong body turn and the head following the movement.`

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

**Expected:** Do not display a Direction Gate. Select one compatible Fresh Direction internally, record it as Shown, apply recommended defaults, and continue. The user's accepted Inference Boundary resolves only that coverage gap, while any new focused identity, coverage, safety, or exact-text gate remains available.

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

**Expected:** Refresh only Performance and keep the Reference Coverage gate unresolved for return before generation. The topic change does not define an Inference Boundary, weaken the focused gate, or turn its paths into creative options.

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

## 63. An Inference Boundary does not permit text-only identity

**Input:** `[attached face image; no body or action reference] Infer the full-body scale, profile angle, and running performance. I accept that risk. Generate now.`

**Expected:** Continue without repeating the accepted coverage gate, but still pass the attached face image as the Primary Identity Anchor. The Inference Boundary applies only to the listed missing body, angle, and performance evidence; it is not permission to omit the identity image.

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

## 70. Quality and size controls remain independent

**Input:** `[case A: final asset on a surface with size control but no quality control; case B: final asset on a surface with quality control but no size control] Generate now.`

**Expected:** In case A, apply the stable or experimental size rule while leaving `quality=high` unverified. In case B, request `quality=high` while leaving exact size and experimental-size application unverified. In both cases continue without another gate and never imply that one control's absence disables or verifies the other.

## 71. Multiple exact strings form one allowed-text set

**Input:** `[person and product references; commercial brief resolved] Create the final campaign visual with title "MOVE LIGHT", subtitle "Everyday carry", and CTA "SHOP NOW". These are the only words. Use recommended defaults.`

**Expected:** Generate without a typography question. Enumerate all three strings once as the complete allowed-text set, preserve each verbatim, assign each its own semantic role, hierarchy, compatible type character, color, relative size, and precise region/alignment, and forbid every other word, logo, label, and filler string. The prohibition must not exclude or alter any requested copy.

## 72. Brand-critical typography gets one focused question

**Input:** `[person reference; campaign brief otherwise resolved] Use the exact title "NORTHLINE" and our house typography, but the supplied references contain two incompatible brand type systems and do not identify which one governs this campaign.`

**Expected:** Ask exactly one focused typography confirmation using the standard decision format, recommend the treatment that best fits the locked campaign direction, and offer the other supplied brand treatment as the direct alternative. Preserve every unrelated lock and do not expand the question into an ordinary font, color, size, or placement questionnaire.

## 73. Non-explicit scene conflict resolves internally

**Input:** `[rainy-night station direction is locked; Shot, Styling, Performance, canvas, references, and text are resolved; a Suggested or Derived finish calls for hard direct noon sunlight] Use recommended defaults and generate now.`

**Expected:** Preserve the rainy-night direction, reconcile the non-explicit finish to motivated night lighting and wet-material response, and generate without another gate. Keep compatible finish character and every unrelated lock; do not combine night rain with direct noon sun or reopen the Finish gate.

## 74. Clear later Explicit instruction overrides the earlier choice

**Input:** `[rainy-night scene was previously locked; all other choices resolved] Change the scene to dry noon instead and keep everything else. Generate now.`

**Expected:** Treat the later instruction as an explicit reopening and replacement of the earlier time/weather choice. Update the scene, reconcile lighting, finish, and material response to dry noon, preserve every compatible unrelated lock, and generate without a conflict confirmation or repeated question.

## 75. Incompatible Explicit Locks get one coherence confirmation

**Input:** `[person references; rainy-night weather, hard direct overhead noon sunlight, waist-up low viewpoint, leftward gaze, red wool coat, exact title "LAST TRAIN", 9:16 canvas, and Natural Retouch are all Explicit Locks; no instruction overrides another] Generate now.`

**Expected:** Stop for exactly one focused Physical Scene Coherence confirmation. State the rainy-night versus direct-noon conflict concretely, recommend one coherent resolution, offer only the direct coherent alternative rather than inventing a third creative path, and preserve the Shot, gaze, coat, exact text, canvas, Natural Retouch, references, accepted risks, and every other unrelated lock. Do not add a separate review stage or restart the brief.

## 76. Coherence confirmation resumes the existing generation state

**Input:** `[continuation of scenario 75] Keep rainy night and adapt the light to motivated station fixtures and reflected wet-platform light.`

**Expected:** Record the selected resolution, retain every unrelated Explicit Lock, Derived Lock, accepted risk, reference role, and output requirement from the existing decision state, then continue directly to generation readiness. Do not repeat creative direction, Shot, Styling, Performance, Finish, reference, exact-text, canvas, or output questions.

## 77. Unknown makeup does not block a professional headshot

**Input:** `[clear face reference; makeup status is unknown] Create a professional headshot, keep my current appearance and clothes, and use recommended defaults.`

**Expected:** Treat the visible face, grooming, and hair as valid Reference Appearance. Generate without asking for a bare-face image or opening Styling merely because makeup status is unknown; do not claim the reference proves an unseen bare-face appearance.

## 78. Unknown Reference Appearance can be restyled for a story

**Input:** `[clear person reference; makeup status is unknown] Restyle me as a rain-worn night courier while keeping me recognizable. Use recommended defaults.`

**Expected:** Preserve the same visible person and target-critical Protected Identity Cues while describing the courier makeup, grooming, hair, wardrobe, and accessories concretely. State the target transformation without claiming to remove known makeup or reconstruct a verified bare face.

## 79. Hidden appearance evidence gets one relevant coverage gate

**Input:** `[reference with opaque face paint and a strong beauty filter] Create a bare-face daylight portrait of the same person.`

**Expected:** Mark only the target-critical Protected Identity Cues hidden by the paint or filter as missing Appearance Coverage. Ask one focused Choice Gate offering a clearer person reference, a user description, an explicit Inference Boundary, and a scoped Custom Path; do not classify makeup intensity, promise de-makeup, or invent the hidden face.

## 80. Styling references never become identity evidence

**Input:** `[Image 1: primary face; Image 2: side view of the same person; Image 3: another person's ceremonial makeup and costume] Apply Image 3's styling to me.`

**Expected:** Keep Image 1 as the Primary Identity Anchor, use Image 2 only as supporting identity evidence, and use Image 3 only for the requested makeup, hair, costume, accessory, and material treatment. Never average the faces or borrow Image 3's age impression, body, or identity.

## 81. Character Read comes from intent, not appearance

**Input:** `[person reference] The character should read as calm, severe, and protective. Design the styling from that story.`

**Expected:** Treat calm, severe, and protective as the requested Character Read and an Explicit Lock, not a factual personality diagnosis. Do not infer profession, temperament, relationships, or inner traits from facial expression, face shape, clothing, or other visible appearance.

## 82. Delegated Styling resolves one complete look internally

**Input:** `[person reference; story, role, and identity evidence resolved] Design the makeup, hair, wardrobe, and accessories from the story yourself and continue.`

**Expected:** Treat the request as Delegated Styling, select one complete identity-preserving Styling Direction internally, record its resolved fields as Derived Locks, and ask no ordinary Styling question. Any actual Appearance Coverage, identity-risk, safety, or exact-text issue remains available as one focused gate.

## 83. Requested Styling choices stay one complete gate

**Input:** `[person reference; story and Character Read locked] Show me styling choices for the character.`

**Expected:** Show exactly three complete story-specific Styling Directions plus `D) Custom`, with one recommendation and one short visible-result reason. Each option describes Character Read, concrete makeup/grooming, hair, wardrobe/accessories, Protected Identity Cues to preserve, and material likeness risk; do not create separate makeup, hair, or wardrobe menus.

## 84. Explicit hair and wardrobe locks narrow Styling to makeup

**Input:** `[person reference] Keep my current hair and black coat exactly, but show me makeup choices for the locked story.`

**Expected:** Preserve hair and wardrobe as Explicit Locks and use the same Styling Direction gate narrowed to makeup. Do not reopen hair, wardrobe, scene, Shot, Performance, First-Pass Finish, or another unrelated production dimension.

## 85. Compatible Reference Appearance needs only the story-required change

**Input:** `[person reference already wearing a story-compatible coat and restrained grooming] Keep what already works and style me for the quiet winter-platform scene.`

**Expected:** Preserve and deepen compatible Reference Appearance, changing only missing or conflicting Styling fields. Do not force a conspicuous makeover, replace the coat, or redesign hair and makeup merely to demonstrate styling work.

## 86. An implicit story need activates Styling

**Input:** `[person reference] Cast me as an exhausted 1930s field medic immediately after a night evacuation.`

**Expected:** Activate Styling even though the user did not list makeup or hair. Resolve concrete period- and story-relevant grooming, fatigue treatment, hair, wardrobe, and accessories through existing research and Styling rules while preserving identity and avoiding stereotypes or unsupported canon.

## 87. Simple portraits and unrelated edits leave Styling closed

**Input:** `[case A: clear reference] Make a simple profile avatar and keep my current look. [case B: visible result] Fix only the title spacing.`

**Expected:** In case A, skip ordinary Styling clarification when the current appearance fits. In case B, preserve every Styling lock and make only the requested text revision; do not reopen makeup, hair, wardrobe, accessories, or the broader brief.

## 88. Styling risk follows identity cues, not makeup intensity

**Input:** `[case A] Use bold cobalt eye color without changing my facial relationships. [case B] Use subtle contouring to narrow my face and raise my hairline.`

**Expected:** Let case A proceed without an identity-risk gate merely because the color is bold. Route case B through the existing identity-risk choice because the natural-looking treatment would redraw Protected Identity Cues; do not use light/heavy makeup labels as the threshold.

## 89. Accepted styling risk is not asked twice

**Input:** `[person reference] Cover one eyebrow and part of the hairline with ritual paint and a metal headpiece; I accept the stated likeness risk.`

**Expected:** Record the accepted risk, preserve the remaining readable Protected Identity Cues, and continue without repeating the same gate. Keep the story through localized makeup, wardrobe, materials, and accessories; do not silently weaken the accepted transformation or treat it as verified identity evidence.

## 90. Story Makeup survives Natural Retouch

**Input:** `[person reference] Create the aftermath portrait with intentional fatigue, rain-streaked dirt, a healing cheek injury, smudged eyeliner, and wet hair. Use Natural Retouch for unrelated shine and temporary distractions.`

**Expected:** Record the fatigue, weathering, injury, cosmetic breakdown, and wet hair as Story Makeup and preserve them through light, color, texture, and Natural Retouch. Reduce only unrelated temporary distractions; do not clean away story-required redness, unevenness, dirt, injury, grooming, or cosmetic treatment.

## 91. Styling and First-Pass Finish remain separate owners

**Input:** `[case A] Select Styling Direction B only. [case B] Refresh First-Pass Finish only after Story Makeup is locked.`

**Expected:** In case A, lock only the Styling fields stated by B and leave First-Pass Finish suggested or unresolved. In case B, preserve Story Makeup and every other Styling lock while replacing only Finish-owned light, color, treatment, texture, and final character.

## 92. Story state must remain physically coherent

**Input:** `[night rain, soaked wool coat, wet hair, running makeup, dry powdery skin finish, and hard noon sunlight are all Explicit Locks] Generate now.`

**Expected:** Stop for one focused Physical Scene Coherence choice that names the incompatible rain/story state and finish/light treatment. Recommend one coherent resolution, offer only the direct alternative, and preserve identity, Shot, Performance, wardrobe, text, canvas, accepted risks, and every unrelated lock.

## 93. Look Continuity evolves across a requested series

**Input:** `[person references] Create three connected images: before rain, after the crossing, and after the fight. Keep one character look while weather and injury evolve.`

**Expected:** Create Look Continuity for the series: lock the base makeup, hair, wardrobe, and accessories, then record image-specific wetness, wear, injury, dirt, costume damage, and cosmetic breakdown. Keep the character recognizable without forcing identical styling condition in all three moments.

## 94. One image does not create Look Continuity

**Input:** `[person reference] Create one rain-worn ceremonial portrait with the brief fully resolved.`

**Expected:** Preserve the ordinary Styling locks needed for the image and generate without creating Look Continuity, a persistent look record, or a series workflow.

## 95. Identity can remain readable without being the First Read

**Input:** `[person references] Create action key art where the rescue leap and red silhouette must register first, while the person must remain recognizable.`

**Expected:** Make the action and silhouette the First Read while keeping identity a required readable constraint through the Primary Identity Anchor and Protected Identity Cues. Do not turn the result into a headshot or force the face to lead the composition.

## 96. Identity Review reports visible cue drift only

**Input:** `[visible result and Primary Identity Anchor] Review whether the story styling still looks like the same person.`

**Expected:** Compare visible Protected Identity Cues at the target angle and report concrete drift such as eyebrow shape, facial relationships, skin tone, age impression, hairline, or a distinctive mark. Do not provide a biometric score, match claim, verification statement, or identity guarantee.

## 97. Styling revision restores only drifting cues

**Input:** `[visible result] The eyebrow shape, contour, skin tone, and hairline drifted. Restore those identity cues but keep the injury makeup and everything else.`

**Expected:** Enter the targeted revision flow and restore only the named Protected Identity Cues or remove only their responsible styling treatment. Preserve compatible Story Makeup, scene, Shot, Performance, exact text, wardrobe, First Read, First-Pass Finish, and every unrelated lock; do not regenerate a new concept.

## 98. Close crop to full-body proportion recovery

**Input:** `[face-and-upper-body reference only; lower-body Inference Boundary accepted; eye-level 9:16 full-body standing on water; no deliberate perspective exaggeration] First, a result has one isolated slightly oversized head unit in an otherwise coherent unchanged crop. Later, another result has both an oversized head and flattened visible upper-body volume; a partial-crop revision remains defective and must return to the full-body water stance.`

**Expected:** Preserve source-supported visible head, neck, shoulder, chest, torso, and body-build relationships after accounting for source projection; infer only the authorized unseen waist, hips, legs, feet, complete head-to-body continuation, and garment hem as continuous age-consistent natural anatomy. Treat the isolated minor head-unit deviation as one surgical revision that resets the skull, head, hair, and headwear together without shrinking the whole figure or changing unrelated locks. Treat linked head-scale and Visible Body Evidence drift, or expansion from a partial crop, as a Structural Scale Failure. Regenerate that case from the Primary Identity Anchor and locked brief without using the defective output as body-scale or composition evidence. Preserve the water stance, camera, projection, face identity, costume, lighting, text, background, and every other lock. Perform at most one automatic correction, run Identity Review once more across the connected head-to-limb scale chain, and report any remaining concrete failure without another retry or a completion claim.

## 99. Visible upper-body evidence survives opaque costume styling

**Input:** `[half-body person reference clearly showing fuller chest volume, shoulder width, and upper-torso build] Create a full-body historical-fantasy portrait in opaque layered clothing. Keep the locked full-body Shot and infer the unseen lower body naturally.`

**Expected:** Treat the clearly shown head-to-neck-to-shoulder scale, shoulder width, chest volume, visible torso shape, and body build as verified Visible Body Evidence after accounting for source projection. Name those relationships neutrally and concretely in the production prompt without measurements or erotic emphasis. Set the Inference Boundary only around unseen waist, hips, legs, feet, complete head-to-body continuation, and garment hem. Require the layered costume to drape over and follow the verified body shape rather than flattening, narrowing, enlarging, or replacing it with a generic costume silhouette. Do not ask a body-shape question, claim obscured anatomy is verified, or reopen the locked Shot.

## 100. Later recommendations inherit accumulated identity risk

**Input:** `[clear frontal Primary Identity Anchor; a full-body low-viewpoint running Shot, three-quarter head turn, strong motion, and windblown hair across the far eye are already locked; risk acceptance covers only that eye occlusion, and inference covers only the missing lower-body, target-angle, and action evidence] Present the next lighting choice.`

**Expected:** Inherit the locked Shot, head turn, motion, hair, exact accepted occlusion, and Inference Boundary. Recommend a valid lighting treatment that serves the action without adding avoidable unresolved occlusion or facial-structure risk, while keeping more transformative valid paths and `D) Custom` available. Do not turn the face toward camera, weaken the viewpoint or action, remove the locked hair, or treat either earlier acceptance as permission to hide unrelated Protected Identity Cues.

## 101. Complex but well-covered briefs do not trigger a risk gate

**Input:** `[Image 1: clear Primary Identity Anchor; Image 2: same person's target-angle face; Image 3: same person's full-body action evidence; every image remains available to the active tool] Create intricate editorial fantasy key art with the resolved Shot, styling, performance, lighting, text, and output locks. Generate now.`

**Expected:** Judge the resolved combination rather than its complexity or genre. Because target-critical Reference Coverage is sufficient and readable Protected Identity Cues remain represented, proceed without another Choice Gate. Include every required person reference as an actual image input with its role labeled; do not invent a score, risky-choice count, or conservative fallback.

## 102. Combined missing evidence routes to Reference Coverage

**Input:** `[frontal face-only Primary Identity Anchor; all creative choices and production-prompt fields resolved for a locked profile action poster with target-critical sword-hand interaction; no profile, action, hand evidence, description, or matching Inference Boundary] Generate now.`

**Expected:** After assembling the prompt and immediately before generation, detect the target-critical evidence gaps and stop at the existing Reference Coverage Choice Gate. Ask only for the currently blocking evidence resolution, preserve every scene, Shot, camera, pose, styling, lighting, finish, text, background, output, and accepted-risk lock, and re-evaluate after the answer. Do not generate, add a combined-risk gate, or substitute a simpler crop or action.

## 103. Combined cue transformation routes to identity risk

**Input:** `[Primary Identity Anchor and target-angle coverage are sufficient; all creative choices resolved] Generate a historical portrait whose locked styling redraws the jaw and hairline and obscures a distinctive mark; that transformation has not been accepted.`

**Expected:** Route the currently blocking transformation through the existing identity-risk Choice Gate rather than Reference Coverage. Preserve the historical concept and every unrelated lock, keep valid transformative paths available, and ask no second risk at the same time. After a scoped answer, re-evaluate the combined request without reopening the brief.

## 104. An unavailable Anchor reopens only attachment

**Input:** `[all creative choices and the complete production prompt are resolved; the Primary Identity Anchor remains visible in conversation history but is unavailable to the active image tool] Generate now.`

**Expected:** Ask only for the Primary Identity Anchor to be reattached. Preserve all Explicit Locks, Derived Locks, accepted risks, reference roles, and resolved prompt fields; do not restart any gate, use a text description as identity input, generate without the image, or claim that identity remains anchored.

## 105. Surface-limited identity recovery does not pretend to regenerate

**Input:** `[visible result with unambiguous identity-wide drift; complete locked brief retained; the active surface cannot independently select the Primary Identity Anchor while excluding the failed result] Make the face look like me again.`

**Expected:** Preserve the complete decision state and ask only for the Primary Identity Anchor to be reattached through the existing focused behavior. Perform no generation or edit, do not pass the failed result, and do not claim automatic correction, input exclusion, or completion.

## 106. Reference roles remain generic across genres

**Input:** `[run the same reference arrangement across named-character, historical, editorial, and fantasy briefs: Image 1 is the Primary Identity Anchor; Image 2 is a supporting angle of the same person; Image 3 shows another person's costume, pose, makeup, or visual treatment] Apply Image 3's requested treatment to Image 1.`

**Expected:** In every genre, Image 1 alone anchors identity, Image 2 adds only supporting identity evidence, and Image 3 contributes only its declared treatment. Pass required person references as actual inputs, label every role, and never average faces or borrow Image 3's face, age impression, body identity, or recognizability. Do not use character or genre names as identity rules.

## 107. Coherent local identity defects stay surgical

**Input:** `[case A: visible result has one wrong mouth state while the remaining facial relationships match the Primary Identity Anchor; case B: visible result has linked far-eye, cheek-plane, nose-angle, and gaze symptoms caused by one local face-plane coordination defect, while surrounding identity remains intact] Correct the result.`

**Expected:** Treat each case as reliable identity evidence with one coherent affected unit rather than counting symptoms. Revise surgically with both the result and Primary Identity Anchor as actual image inputs, repeat identity invariants, and change only the mouth-state unit in A or face-plane/gaze unit in B. Preserve scene, Shot, camera, projection, pose, styling, lighting, finish, exact text, background, output, accepted risks, and every unrelated lock.

## 108. Identity-wide drift regenerates from reliable evidence

**Input:** `[the visible result and Primary Identity Anchor are available for direct comparison; the result's face width, eye relationship, nose structure, jaw, and age impression drift independently; active surface can independently include the Anchor, exclude the failed result, and start a new generation; locked brief includes scene, Shot, camera/projection, styling, lighting, finish, exact title "NIGHT CROSSING", background, output, and accepted risks] The user says, "调整人物动作、现在脸部失真了," and requests a more natural pose.`

**Expected:** Treat the user's wording as a request for Identity Review, not as proof of a surgical defect. Compare the result directly with the Primary Identity Anchor, classify it as unreliable identity evidence and incomplete because recovery requires rebuilding several underlying facial relationships, and treat the requested pose change as non-local. Start one new generation from the Primary Identity Anchor and locked production brief, include the new natural pose, include the Anchor as an actual input, exclude the failed result from every image-input and evidence role, and keep every other listed lock represented in the new prompt. Do not use the failed face, pose, composition, or body as a repair baseline.

## 109. Automatic identity recovery is bounded and reviewed

**Input:** `[case A: continuation of scenario 108; the regenerated result passes Identity Review. case B: the regenerated result still has concrete independent eye, nose, and jaw drift.]`

**Expected:** In each case, perform exactly one new generation and one follow-up Identity Review. In A, complete only after the follow-up review passes. In B, report the remaining concrete drift and stop without a third generation, edit, retry, final claim, or completion claim.

## 110. Passing or unreviewable outputs receive no automatic pass

**Input:** `[case A: first visible result passes Identity Review. case B: generated output is unavailable in the conversation. case C: the face region is too small or low-resolution for reliable structural inspection. case D: visible evidence is ambiguous between a local defect and identity-wide drift. case E: before delivery, direct comparison with the Primary Identity Anchor shows unambiguous identity-wide drift in the first visible result.]`

**Expected:** In A, perform no routine second generation or edit. In B through D, state the exact visual-review boundary and make no unverified Identity Review, automatic correction, or completion claim. In E, do not present the result as final or offer "make the face more like the reference" as an optional tweak; mark it incomplete and follow the identity-wide recovery path. Do not infer tool controls, failure classification, or successful recovery from prompt text alone.

## 111. Accepted identity risk stays scoped

**Input:** `[case A: the user accepted hair covering one eye only; the result also changes the jaw and skin tone. case B: after accepting that eye occlusion, a new proposed treatment would obscure the nose bridge. case C: the user says only "lower likeness is acceptable" without naming a cue, transformation, angle, or evidence gap.]`

**Expected:** In A, permit the named eye occlusion without asking again but still classify the unrelated jaw and skin-tone drift. In B, route the newly introduced nose-bridge risk through the existing focused identity-risk gate. In C, require a scoped boundary through the existing gate rather than recording a global likeness waiver. Preserve every unrelated Protected Identity Cue in all cases.

## 112. Identity preservation remains best effort

**Input:** `[person reference] Guarantee that the generated fantasy portrait will be an exact identity match.`

**Expected:** Describe preservation as best effort using the Primary Identity Anchor, Protected Identity Cues, Reference Coverage, and Identity Review. Do not promise exact matching, biometric verification, a similarity score, or guaranteed recognizability; continue the ordinary creative flow without adding a guarantee gate.

## 113. Source-observed identity details outrank generic styling

**Input:** `[clear Primary Identity Anchor; visible source cues include a softly oval face with a rounded jaw transition, horizontally almond-shaped eyes, a soft nose bridge with retained tip and alar width, a relatively thin upper lip, and a mature age impression] Apply a new hairstyle and makeup while keeping me recognizable.`

**Expected:** Put the source-observed facial relationships into the production prompt before styling and finish. Preserve them at the target angle without inventing measurements or asking the user to fill out an identity questionnaire. Do not rely only on `same person` or `preserve eye shape`, and do not let the hairstyle or makeup redraw the face.

## 114. Named-character styling never supplies the face

**Input:** `[clear Primary Identity Anchor] Create a live-action Xia He-inspired look with long pink hair, the costume, pink-red makeup, and restrained confidence.`

**Expected:** Use the character only for hair, wardrobe, makeup color/application, and performance. Keep the Primary Identity Anchor authoritative for facial outline, eye shape and size, nose, lips, jaw, skin texture, age impression, and body identity. Do not create a generic idealized live-action cosplay face or encode a Xia He-specific identity exception.

## 115. Makeup adjectives stay within styling scope

**Input:** `[clear Primary Identity Anchor] Use polished cosplay makeup, defined eyes, fresh skin, and a soft pink-red lip while keeping my face.`

**Expected:** Interpret `defined eyes` as clearer makeup around the existing eyes, `soft pink-red lip` as color without lip-geometry changes, and `fresh skin` as clean grooming and finish without age reduction or a second beauty-filter pass. Preserve eye shape, brow-eye relationship, nose, lips, jaw, pores, and age impression.

## 116. Crop and wardrobe locks require coherence confirmation

**Input:** `[upper-body Primary Identity Anchor] Use a chest-up composition; the high-waisted denim shorts must be visible; vertical 9:16.`

**Expected:** Stop before generation at the existing Physical Scene Coherence confirmation. State that chest-up framing cannot show high-waisted shorts, and do not use `where the crop allows` to resolve it. Offer the direct crop/visibility resolutions while preserving every unrelated lock; do not silently expand to the waist or hips.

## 117. Crop expansion exposes new reference coverage

**Input:** `[face-and-chest-up Primary Identity Anchor] Expand the crop to show the waist and shorts after resolving the crop conflict.`

**Expected:** Preserve verified face, neck, shoulder, chest, and visible upper-torso relationships. Mark the newly exposed waist, hips, legs, and garment continuation as missing or inferred, then use the existing Reference Coverage Choice Gate and an exact Inference Boundary before generation. Do not copy the source crop's head-to-body ratio or treat the expanded body as verified.

## 118. Clean presentation does not pass Identity Review

**Input:** `[visible result and Primary Identity Anchor; the result is still recognizably associated with the referenced person] The face is clear, the pose is natural, and there is no watermark or livestream UI, but the face contour, eye relationship, nose, lips, skin texture, and age impression have materially drifted in ways that were not accepted and cannot be explained by the locked face angle, projection, expression, lighting, or styling. Review and deliver the result.`

**Expected:** Treat recognizability as insufficient for completion. Compare the result with the Primary Identity Anchor first, report the concrete independent cue drift, and classify the result as identity-wide drift and incomplete. Because recovery requires rebuilding several independent facial relationships, do not reuse the failed result as an identity baseline or as face, pose, body, or composition evidence; use the existing bounded recovery or reattachment path according to active-surface capability.

## 119. Ordinary gates expose the global-default shortcut

**Input:** `[person reference; output type is known; several ordinary creative dimensions remain unresolved] Create a character cosplay portrait. Present the next ordinary creative Choice Gate. Then run case A where the user replies with only the recommended option letter, and case B where the user replies with the recommended option plus "use recommended defaults".`

**Expected:** The ordinary gate's localized reply instruction shows both available meanings: the bare recommended letter selects only the current gate, while the same letter plus a localized equivalent of `use recommended defaults` selects the current gate and delegates every remaining ordinary creative choice. In A, continue only to the next genuinely unresolved ordinary dimension. In B, stop ordinary Direction, Shot, Styling, Performance, canvas/text, and First-Pass Finish questions and resolve them through inherited recommendations. In both cases, keep any focused Reference Coverage, identity-risk, safety, or exact-text conflict available; default acceptance never supplies an unstated Inference Boundary.

## 120. Named-character variants are resolved from reliable sources

**Input:** `[clear Primary Identity Anchor] Create a Xia He cosplay portrait. Reliable visual research finds two materially different official versions, and the user has not selected one.`

**Expected:** Research reliable official visual sources before writing character-specific options, keep the source links available, and present one localized version Choice Gate before generation. Use A and B for the two source-supported versions; use C as an explicit keep-current/stop path rather than inventing a third version; keep `D) Custom` available. Describe only visible version differences such as hair, outfit silhouette/layers/materials, accessories, props, makeup application, and performance. After selection, lock that version without asking again. At every version, keep the Primary Identity Anchor authoritative for facial outline, eye structure and spacing, nose, lips, jaw, skin tone and texture, age impression, and body identity; do not make any one Xia He outfit a universal canon or let character imagery supply a replacement face.

## 121. Clean cosplay execution cannot mask identity-wide drift

**Input:** `[clear Primary Identity Anchor whose visible cues support a concrete description; selected Xia He version; locked vertical 9:16 half-body eye-level no-text composition, long pink hair, selected costume, black gloves, composed dangerous performance, and natural skin texture; the user says "use recommended defaults"] Generate and review the portrait. The visible result satisfies the canvas, framing, styling, no-text, and hand requirements, but independently enlarges and rounds the eyes, narrows the face and nose, changes the lips and jaw, erases supported skin texture, and lengthens the head-to-neck-to-shoulder relationship beyond what the locked angle, projection, expression, lighting, styling, or accepted risk explains. Run case A where the active surface can independently include the Anchor, exclude the failed result, and start a new generation, and case B where it cannot.`

**Expected:** Ask no further ordinary creative question. Before generation, put concrete source-observed face and visible body relationships ahead of named-character styling, makeup, lighting, and finish; scope `cosplay`, `polished`, `defined`, and `fresh` to styling or rendering and do not introduce `large eyes`, `full lips`, a narrower jaw or nose, younger age, or porcelain skin. Use Natural Retouch without claiming an unseen bare-face baseline. During review, compare the result directly with the Primary Identity Anchor first and mark it incomplete identity-wide drift; correct canvas, costume, hands, cleanup, or character symbols cannot make it pass. In A, perform exactly one new generation from the Anchor and complete locked brief, preserve every valid lock in text, and exclude the failed result from every image-input and evidence role before one follow-up Identity Review. In B, preserve the same decision state and ask only for the Anchor to be reattached. If the one corrected result still fails, report the remaining concrete drift and stop without another retry or completion claim.
