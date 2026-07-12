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
