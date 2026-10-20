Status: ready-for-agent

# Anime and Chibi Character Generation from a Person Reference

## Problem Statement

Users want a drawn version of themselves: an anime avatar, a chibi sticker set, a character sheet they can reuse. CastMe can already name a non-photographic medium and adapt its finish to that medium, but it cannot produce a drawn character that stays the same character across more than one image, and it has no vocabulary for how far to deform.

Four gaps block the request.

There is no anchor stage. Every image is generated independently from the person reference, so the second image is a different character wearing the same description. Cross-generation character consistency is a documented model limitation, and the documented remedy is a reusable character anchor produced once and then supplied as an actual image input to everything that follows.

There is no deformation vocabulary. Deformation is continuous and consequential rather than a style label. Head-to-body ratio encodes apparent age in the drawing conventions this output belongs to, and it determines which identity channels survive at all: as deformation increases, the body differences that distinguish people flatten and recognition shifts onto hairstyle, eye shape, distinctive marks, and characteristic wardrobe. Without a named tier the user cannot state what they want, and the skill cannot resolve which channels remain open.

Body evidence makes that resolution delicate. The current contract treats clearly shown shoulder width, chest volume, torso shape, and body build as preserved by default with no gate at all, requires chest volume to be named directly in the prompt when it is clearly shown, and requires garments to drape over the verified shape rather than flatten or replace it. For some people the figure is the most distinguishing visible thing about them. A deformation tier that quietly discards all of it would remove something the user was never asked about, and the drawing convention does not actually require that: only the shortest proportion genuinely cannot carry a figure, while the next one up can, at the cost of reading more mature.

There is no stylization-intensity control. This is a spectrum that fails at both ends: too little conversion produces a filtered photograph, and too much replaces the person's features with the model's default anime face. Today the intensity is hidden inside whichever style the user happened to name.

There is no style vocabulary beyond a style name. Naming an artist or a school does not reliably control the result, and it reportedly makes rendering artifacts worse, because reference lookup pulls retrieved images into the generation context.

Sets make all of this harder. Sticker packs and multi-angle sheets generated one image at a time drift, and the details that erode first are precisely the small marks that carry recognition once body differences are gone.

This specification depends on the medium-aware identity contract specified in `.scratch/medium-aware-identity-contract/`. Without it every drawn result fails Identity Review, the bounded automatic correction fires, and the correction pulls the drawing back toward photography — which is how a half-converted image gets produced. Implement that specification first.

## Solution

Add a **Character Sheet** stage. Before any application image, produce one drawn design of the person and lock it: proportions, face construction, hair, eye rendering, wardrobe, palette, and line and shading treatment, on a clean background. Every later image is generated from the Character Sheet together with the Primary Identity Anchor, both supplied as actual image inputs with their roles stated, and instructed not to redesign the character.

Applications branch from the Character Sheet; they never derive from each other. That keeps every delivered image two steps from the user's photograph no matter how many images the user asks for, which is what the edit-chain constraint requires.

An application is therefore never a freshly generated result, because the Character Sheet is a generated image among its inputs. A failing application is regenerated from the Character Sheet together with the Primary Identity Anchor rather than surgically edited, and the bounded automatic correction never edits one on its own initiative. The Character Sheet is the drawn request's locked produced artifact: every regeneration carries it, and the sheet itself is regenerated rather than edited when it fails, because a repair made to the sheet would be inherited by every image built from it.

Add a **Deformation Tier** choice. The three semantic labels are fixed — conservative, standard, strong — so that a returning user sees a stable menu, while the concrete proportion each label maps to varies with the intended use. The permanent Custom path remains. The tier resolves the Medium Contract, and therefore decides which identity channels Identity Review will judge, which ones carry recognition instead, and which are disclosed as closed before generation.

Make stylization intensity an explicit parameter rather than an implication of the chosen style, because it fails at both ends and neither end is the style's fault.

Describe style through six visible axes — line, surface coloring, colour logic, eye rendering, texture, and background — using concrete visible anchors, and never name an artist or a school. Keep the optical finish separate from surface coloring rather than treating them as one scale. In the production tradition this output belongs to they are decided by different roles and combine freely, so flat colour with heavy light diffusion and the same flat colour with none are both legitimate destinations rather than two points on one slider.

Offer the recognizable drawn looks as named starting points defined by their visible features. Anime is not one appearance and it is not only chibi: flat cel, semi-gradient, thick-painted, watercolour, lineless, monochrome with screentone, and toon-shaded three-dimensional are distinct destinations with documented distinguishing characteristics, and deformation is a separate question from all of them. A user who says only that they want anime should be shown that choice rather than have it made for them.

Keep the Character Sheet stage deliberately conservative: the original head angle and expression, even lighting, no extreme viewpoint. Variation belongs to the application stage, where the existing rules about redesigning expression, gaze, and face angle continue to apply unchanged.

Produce sets and multi-angle sheets as one planned batch when the active surface supports it, and fall back to sequential generation from the Character Sheet when it does not, without claiming batch consistency that was not used.

## User Stories

1. As a user who wants an anime version of myself, I want one drawn design produced and locked first, so that later images show the same character rather than a new interpretation each time.
2. As a user, I want the Character Sheet generated from my actual photograph, so that the drawn character starts from my real face rather than a description of it.
3. As a user, I want every later image to receive both my photograph and the Character Sheet as real image inputs, so that identity and drawn design are anchored together.
4. As a user, I want each supplied image's role stated explicitly, so that the Character Sheet governs how I am drawn while my photograph governs who I am.
5. As a user, I want later images instructed not to redesign the character, so that the locked design is treated as a constraint rather than a suggestion.
6. As a user requesting several images, I want each one generated from the Character Sheet rather than from the previous image, so that the tenth image is no more degraded than the first.
7. As a user, I want the Character Sheet stage to keep my original head angle and expression, so that the design is aligned to my face with as few variables as possible.
8. As a user, I want the Character Sheet stage to avoid dramatic lighting and extreme viewpoints, so that the locked design is not distorted by a lighting or perspective decision that belongs to a later image.
9. As a user, I want expression, gaze, pose, and camera angle fully available at the application stage, so that a conservative design stage does not make my images static.
10. As a user who only wants a single drawn image, I do not want a mandatory two-stage process, so that a one-off request stays direct.
11. As a user who already has a Character Sheet, I want to reuse it in a later conversation by supplying it, so that the design outlives one session.
12. As a user unsure how stylized I want to look, I want three tiers labeled in plain language, so that I can choose without knowing what a head-to-body ratio is.
13. As a returning user, I want the three tier labels to stay in the same order with the same meanings, so that I can build a reliable expectation.
14. As a user, I want the concrete proportion behind each label to suit the use I named, so that the conservative option for a sticker pack is not the conservative option for a profile picture.
15. As a user with an exact proportion in mind, I want the Custom path, so that the fixed labels do not become the only reachable results.
16. As a user choosing between the two most deformed readings, I want the real differences described — rounder shapes, fewer separated hair masses, features placed lower on the face, and simplified hands — so that the choice is about visible results rather than a number.
17. As a user, I want deformation kept within the range that drawn practice actually supports, so that the skill does not offer a proportion nothing in the medium can render coherently.
18. As an adult user, I want to be told that a middle proportion will read as a child rather than as a mild stylization, so that I do not pick it expecting a subtle effect.
19. As a user who accepts a strongly deformed tier, I want the younger appearance treated as part of that choice rather than as a defect, so that my own decision is not corrected against me.
20. As a user, I want my chosen tier to decide which identity channels are judged, so that review measures what the drawing can actually express.
21. As a user at a strongly deformed tier, I want hairstyle outline, eye shape, distinctive marks, and characteristic wardrobe emphasized, so that I remain recognizable as body differences flatten.
22. As a user with a mole, scar, freckles, or under-eye shadow, I want those emphasized rather than tidied away at deformed tiers, so that the details recognition depends on are strengthened rather than lost.
23. As a user at an equal-proportion tier, I want structural features such as nose bridge and upper-lip thickness still carried, so that a mild tier is not treated like a strong one.
24. As a user whose figure is one of the most distinguishing things about me, I want visible body shape treated as identity evidence rather than as something a drawing style may discard, so that a stylized version of me does not arrive with a generic body.
25. As a user comparing tiers, I want each one to state whether it can carry my visible body shape, so that I choose knowing what the choice costs.
26. As a user choosing the second-shortest proportion, I want chest, waist, and hip curvature available as an explicit option, so that a deformed version can still reflect my figure.
27. As a user taking that option, I want to be told it reads as more mature, so that I understand it partly offsets the tier's younger appearance.
28. As a user whose chosen tier cannot carry my body shape, I want to be told before generation rather than discovering it in the result, so that evidence the skill normally preserves without ever asking is not dropped silently.
29. As a user who wants both strong deformation and my figure, I want a less deformed tier offered as the way to get both, so that I receive a real resolution rather than a refusal.
30. As a user, I do not want adult body emphasis combined with a proportion that reads as a child, so that the tier system cannot be used to assemble that combination.
31. As a user whose body shape is carried, I want it described in neutral concrete terms without measurements or erotic emphasis, so that the drawn version follows the existing rules for body evidence.
32. As a user, I want to be told before generation which identity channels my tier closes, so that I can change tier before spending a generation.
33. As a user, I want the tier's visible consequences described in the production prompt as what the drawing does, not as what it omits, so that the prompt does not state constraints in a form that risks producing them.
34. As a user at a strongly deformed tier, I want my figure to stay identifiable in silhouette at thumbnail size, so that a sticker still reads as me at the size stickers are actually seen.
35. As a user, I want stylization intensity chosen explicitly, so that how converted I look is a decision rather than a side effect of the style I named.
36. As a user, I do not want a result that is my photograph with a filter over it, so that a low intensity still means an actual drawing.
37. As a user, I do not want my features replaced by a generic anime face, so that a high intensity still means me.
38. As a user, I want intensity raised in steps rather than set to maximum at once, so that the failure at the far end is avoidable.
39. As a user, I want my skin, lighting, and shading converted to the drawn medium along with my eyes and hair, so that I do not receive a half-photographic hybrid.
40. As a user, I do not want an instruction to preserve every pore, so that the request does not fight the simplification a drawing requires.
41. As a user, I want style described through line, surface coloring, colour logic, eye rendering, texture, and background, so that I can change one aspect without restating the whole look.
42. As a user who says only that I want anime, I want the recognizable drawn looks offered as named starting points, so that the word does not silently resolve to one default appearance.
43. As a user comparing those looks, I want each described by its visible features rather than by its name alone, so that I can tell them apart before spending a generation.
44. As a user, I want the number of shading layers treated as a concrete coloring choice, so that flat animation shading and richer illustration shading are distinguishable.
45. As a user, I want screentone available as a texture choice, so that the printed-manga look is reachable.
46. As a user, I want the optical finish chosen separately from how surfaces are colored, so that flat cel with soft light diffusion and flat cel with none are both available rather than one being a compromise of the other.
47. As a user asking for an older-looking result, I want it produced through palette and optical finish rather than by changing the painting technique, so that I get a period look instead of a different medium.
48. As a user requesting a set, I want one set of character colours carried across every image, so that my colours do not drift between stickers.
49. As a user, I want background treatment chosen separately from how the character is drawn, so that changing the background does not change my face.
50. As a user, I do not want a named artist or school used to specify my style, so that the result does not depend on whatever images a reference lookup happens to retrieve.
51. As a user, I want style stated as visible features such as line weight, shading-layer count, and eyelash treatment, so that the description controls the result.
52. As a user, I want to be told when my style choices fall in the range where rendering artifacts are strongest, so that I can decide knowingly.
53. As a user, I do not want the looks ranked by how well they are likely to come out, so that a guess is not presented to me as a measurement.
54. As a user supplying a style reference image, I want it used only for how I am drawn, so that another artwork's face never becomes mine.
55. As a user requesting a sticker set, I want the whole set planned and produced together where the surface supports it, so that the set is internally consistent.
56. As a user requesting a multi-angle character sheet, I want the angles produced together, so that the views agree with each other.
57. As a user, I want set production preferred over generating one image at a time because sequential editing erodes the small marks I am recognized by, so that consistency is protected for an identity reason and not only for speed.
58. As a user on a surface without batch production, I want sequential generation from the Character Sheet instead, so that the request still completes.
59. As a user in that situation, I do not want the skill to claim it used batch consistency, so that its description of what it did stays truthful.
60. As a user requesting a set, I want each image checked for the same dimensions, so that an automatic crop does not leave one sticker a different size.
61. As a user wanting transparent stickers, I want to be told before generation that transparency is not produced by this model and to be given the downstream step, so that I am not promised a file the workflow cannot deliver.
62. As a user requesting a chibi sticker set, I want characteristic expressions and mannerisms treated as a recognition signal at that tier, so that the set feels like me and not like a generic mascot.
63. As a user requesting an avatar or an equal-proportion portrait, I do not want mannerisms weighted heavily, so that a guess about how I move does not override my actual structure.
64. As a user, I want any mannerism taken from a single photograph marked as an assumption and never used to fail a review, so that one frozen moment is not treated as a habit.
65. As a user requesting a drawn image with another person, I want to be told this is not supported rather than shown a blended face, so that the limitation is stated instead of demonstrated.
66. As a user, I want the drawn likeness described as best effort with no similarity score, so that the new capability does not come with a promise the skill cannot keep.
67. As a user whose drawn image has a flaw, I want it redrawn from my locked design rather than patched in place, so that repairs do not pile up on top of the design step.
68. As a user, I want a redraw to keep using my locked design, so that fixing one image does not hand me a different character.
69. As a user whose locked design itself has a flaw, I want the design redrawn rather than patched, so that one repair is not inherited by every image I go on to ask for.
70. As a user who wants a small fix made in place anyway, I want that still possible, so that the recommendation does not harden into a restriction.
71. As a maintainer, I want the Character Sheet named distinctly from the Primary Identity Anchor, so that the drawn design is never mistaken for the identity source.
72. As a maintainer, I want this built on the existing Identity Anchor, composition, and refresh seams, so that a new capability does not become a new module.
73. As a maintainer, I want tier values treated as drawing conventions rather than model thresholds, so that a documented convention is not confused with an unverified measurement.
74. As a maintainer, I want the body-evidence gradient expressed as a tier property rather than as a separate body question, so that the existing no-gate preservation default is narrowed in exactly one place.
75. As a maintainer, I want no look offered whose name has no agreed definition in the source material, so that the menu does not invent vocabulary.
76. As a maintainer, I want the Character Sheet's place in the edit-chain contract stated here rather than in the edit-chain specification, so that the medium-independent rule stays medium-independent.
77. As a maintainer, I want scenarios that vary the tier, the use, and the style axes, so that the implementation cannot pass by recognizing one request shape.

## Implementation Decisions

- Depend on the medium-aware identity contract. This specification assumes Protected Identity Cues already resolve per Medium Contract and that Identity Review already judges only open and transferred channels. Do not reimplement any of that here.
- Name the locked drawn design a **Character Sheet**. Do not call it a character anchor: the repository already has Primary Identity Anchor as the authoritative person reference, and two anchors would compete. The Character Sheet governs how the person is drawn and never becomes identity evidence.
- Produce the Character Sheet as an ordinary generation with a clean background, then treat it as a reusable input. It is an artifact, not a new workflow stage with its own gates.
- Supply both the Primary Identity Anchor and the Character Sheet as actual labeled image inputs to every application image, and state how they interact. The existing rule requiring the Primary Identity Anchor for identity-preserving generation is unchanged; the Character Sheet is additional, never a replacement.
- Branch every application from the Character Sheet. Applications must never take another application as an image input, which holds every delivered image at two steps from the user's photograph regardless of how many are produced.
- Name the Character Sheet as the drawn request's locked produced artifact in the edit-chain contract, so that it belongs to the request's fixed root. Every regeneration carries it alongside the Primary Identity Anchor. The identity-wide regeneration path must not drop it: the sheet is not a person reference and never identity evidence, so an inputs rule phrased around person references alone would exclude it and return the request to generating each drawn image straight from the photograph, which is the single-stage behavior this specification exists to replace.
- Classify an application as not freshly generated, since the Character Sheet is a generated image among its inputs. The bounded automatic correction therefore regenerates a failing application from the Character Sheet and the Primary Identity Anchor, excluding the failed result, and never surgically edits it.
- Regenerate the Character Sheet rather than edit it when it fails its own review, even though the freshly-generated test would otherwise admit it. Every application inherits the sheet, so one edit to it is multiplied across the whole set rather than confined to a single image.
- Keep the user-requested edit available on an application. Recommend regeneration from the Character Sheet and the Primary Identity Anchor, and carry the edit out when the user asks for it, passing the application being edited plus the Primary Identity Anchor. Do not add the Character Sheet to those inputs; its design is already present in the image being edited.
- Skip the Character Sheet stage for a single drawn image with no continuity requirement. Introduce it when the user asks for a set, a series, a reusable design, or a second image of the same character. Such an image takes only the Primary Identity Anchor as an image input, so it is freshly generated in the ordinary way and the surgical row stays available to it. Drawn output is not categorically excluded from surgical repair; only images built on a Character Sheet are.
- Accept a user-supplied Character Sheet from an earlier session in its input role, subject to the same reference-role labeling as any other input.
- Keep the Character Sheet stage conservative: original head angle and expression, even lighting, no extreme viewpoint. State explicitly that this applies to the Character Sheet stage only, because the existing contract treats expression, gaze, and face angle as temporary state that later images may redesign freely.
- Add a **Deformation Tier** resolved through the existing Choice Gate mechanics: three fixed semantic labels in a stable order plus the permanent Custom path. Fixed labels with use-dependent values are chosen deliberately over regenerating the option set each time, because menu research finds user-visible adaptation slower and less predictable than a stable layout while user-controlled customization is both preferred and fast.
- Map tiers to head-to-body proportions drawn from established illustration convention: equal proportion for adult anime, roughly six for adolescent readings, four as the practical upper bound of chibi, and the main expressive division between the two and three head-tall readings. These are drawing conventions with industry sources, not measured model thresholds.
- Disclose that middle proportions of roughly four to five heads read as a child rather than as mild stylization. Do not present them as a neutral midpoint.
- Express tier differences as visible drawing parameters rather than as a number alone: shape roundness, degree of simplification, vertical placement of features, hand treatment ranging from articulated fingers to a thumb-and-block simplification, and whether waist, chest, and hip curvature is drawn.
- Let the resolved tier drive the Medium Contract's channel resolution. As deformation increases, hairstyle, eye shape, distinctive marks, and characteristic wardrobe become the transferred channels that carry recognition and are weighted up. Resolve the contract once for the request: the Character Sheet and every application built from it are reviewed against the same record, so a set is never judged under two criteria.
- Resolve Visible Body Evidence as a gradient across tiers rather than as an open or closed switch. Equal proportion carries it unchanged from current behavior. The intermediate tiers carry it in simplified form. At the second-shortest proportion it is available as an explicit choice, because that proportion can render chest, waist, and hip curvature, with the disclosed consequence that drawing it reads more mature and therefore partly offsets the tier's younger reading. Only the shortest proportion cannot carry it.
- Disclose the loss before generation whenever the resolved tier would drop body evidence the source actually shows. This is required rather than optional because the current contract preserves that evidence by default without ever asking, so a tier choice is the only place the user can be told it is going away.
- Offer a less deformed tier as the resolution when a user wants a figure the chosen tier cannot carry. Do not add the figure back on top of a proportion that cannot support it.
- Do not combine emphasized adult body characteristics with a proportion that reads as a child. Head-to-body ratio encodes apparent age, the shortest proportions read as young, and the existing safety ladder already treats sexualized depiction of apparent minors as high risk. This is a hard exclusion, not a recommendation, and it is resolved by moving the tier rather than by moderating the description.
- Keep the existing prompt rules for body evidence unchanged wherever the channel remains open: name the relationships neutrally and concretely, name chest volume directly with its surrounding shoulder and upper-torso relationships when it is clearly shown, and never introduce measurements, cup sizes, or erotic emphasis.
- Keep wardrobe owned by Styling even when it carries recognition. The tier changes its review weight, not its ownership.
- Add stylization intensity as an explicit production dimension with two named failure ends. Direct it to be raised progressively rather than set to maximum, and require the prompt to state positively that skin, lighting, and shading convert to the medium along with eyes and hair.
- Define six style axes: line, surface coloring, colour logic, eye rendering, texture, and background. Place shading-layer count under surface coloring and screentone under texture.
- Add colour logic as a real axis. An earlier draft dropped it as the one axis with no counterpart, which was wrong: it corresponds to a dedicated decision-making role in animation production whose output is a colour specification shared by the whole team, and the academic treatment models a character's palette as a small fixed set of colour slots constrained by consistency within a cast and distinguishability between its members. The axis governs which slots exist, what each holds, and how the whole set shifts with time of day, weather, and mood. Shading-layer count governs how many steps each slot is cut into, which is a different question. Do not fix a slot count; the one published figure comes from a single study.
- Give the colour logic axis one concrete derivation rule: a shadow colour is not the base colour with its brightness lowered. Lower brightness while holding or slightly raising saturation and shifting hue, conventionally toward the cool side, with skin as the documented exception where the shift goes warm to keep blood tone. Avoid pure black as a shadow colour, and give nominally white items a slight tint so that their shadow layer still reads. These are consistent across illustration teaching sources but were not confirmed at production level, so state them as defaults the user can override rather than as rules.
- Treat optical finish as a property that combines with any surface coloring rather than as a position on the coloring axis. Light diffusion, bloom around bright areas, lens flare shape, and bokeh shape belong here. This mirrors the compositing stage, which is a separate role from colour finishing in the production tradition being imitated.
- Offer named looks as starting points, each specified by visible features rather than by its name: flat cel as solid fills with hard shadow boundaries and prominent line art; semi-gradient as the same base with shadows blurred into the base colour; thick-painted as opaque layered colour with ambiguous shadow boundaries and often no main line at all; watercolour as soft boundaries, lightened line, deliberate unevenness and paper texture; lineless as form separated by colour and value with only minimal coloured line at features, which is a different choice from flat; monochrome as screentone standing in for shading; and toon-shaded three-dimensional as two or three discrete colour steps with a drawn contour.
- Give the texture axis concrete screentone parameters, which are the best documented of any axis because they come from the official manual of the tool the convention belongs to: dot frequency, density, dot shape, and screen angle. Express them as visible descriptions rather than as numeric settings, since the generation surface exposes no such controls.
- Give the line axis concrete parameters: the three weight tiers of contour, boundary, and detail; how much weight varies within one drawing, where uniform reads as hard and strongly varied reads as soft; whether strokes taper at their ends; line colour; and whether line exists at all, which is a three-way choice between full line, minimal coloured line, and none.
- Give the eye axis concrete parameters: highlight count and placement, iris gradient direction, whether the iris carries radial texture, whether lashes are black or coloured, and whether a hard boundary separates iris from sclera. Assign highlight strength to the optical finish rather than to coloring, because in production it is a compositing decision.
- Express retro versus modern through palette and optical finish rather than through the painting technique. A period look is a restricted palette plus a specific finish, and the single most identifiable modern marker is the full-frame light diffusion introduced when production moved off film to stop images looking harsh. One concrete period technique is worth naming: taking the line colour from the deeper shadow colour. Apply the palette restriction to the character layer only. The historical limit was a cel-paint constraint and never applied to the painted background, so reducing colour across the whole image reproduces something that never existed.
- Prefer a named look over accepting an unfamiliar style word as-is. An unrecognized style term does not degrade gracefully: generation research documents unrecognized prompts collapsing onto a narrow set of default images that persist even when style modifiers are attached to them.
- Do not offer a look whose name has no agreed definition in the source material, and do not offer a working method as if it were a look. Grisaille produces a thick-painted result and is a route rather than a destination.
- Require style to be expressed through visible anchors. Prohibit artist and school names, which reportedly worsen rendering artifacts because reference lookup introduces retrieved images into the generation context, which the repository already discourages on controllability grounds, and which carry subject bias in training data such that a style name pulls its most common subject matter along with it.
- Note artifact risk when a choice lands in the range where the model's own rendering artifact is strongest, which is dense high-frequency micro-structure. State it as information about a known model artifact, not as a claim about how well a look can be produced.
- Do not rank or grade the named looks by expected quality. The only supporting evidence is category-level, and no per-look comparison exists.
- Treat batch production of sets and multi-angle sheets as a surface capability boundary using the existing pattern. Prefer it when available, fall back to sequential generation from the Character Sheet when not, and never claim batch consistency that was not used.
- Verify dimensions across a delivered set, because an edit tends to crop in order to align output to a supported resolution bucket.
- State the transparency limitation before generation and record the downstream cutout as a delivery requirement. Do not imply the model can produce a transparent background.
- Weight mannerisms by tier and use: meaningful at strongly deformed sticker sets, where static cues are minimal and the audience knows the person, and low elsewhere. Mark any mannerism drawn from a single reference as an assumption, and never let it produce a review failure.
- Keep another person's drawn or photographic style reference limited to rendering treatment. It never supplies face identity, age impression, or body identity.
- Keep multi-person drawn output unsupported and say so. Identity blending is a method-level limitation rather than a prompting problem, and the skill remains single-anchor.
- Add **Character Sheet** and **Deformation Tier** to the domain glossary with an accompanying ADR for the two-stage decision, drafted in `domain-changes.md` alongside this file.

## Testing Decisions

- Use `evals/golden-conversations.md` as the single behavioral seam, as every prior specification in this repository does.
- Assert observable routing, gate structure, image-input roles, prompt obligations, disclosures, and review outcomes. Do not assert exact option wording or a specific proportion table.
- Add a Character Sheet scenario covering a request for a reusable drawn character. Assert that the sheet is produced first from the person reference on a clean background, with original head angle and expression, and that it locks proportions, face construction, hair, eye rendering, wardrobe, palette, and line and shading treatment.
- Add an application scenario asserting that both the Primary Identity Anchor and the Character Sheet are actual labeled image inputs, that their interaction is stated, and that the prompt forbids redesigning the character.
- Add a multi-image scenario asserting that each application branches from the Character Sheet and that no application is ever an image input to another.
- Add a failing-application scenario asserting that the bounded automatic correction regenerates from the Character Sheet and the Primary Identity Anchor rather than surgically editing the application, and that the failed application is excluded from the inputs.
- Assert in that scenario that the regeneration carries the Character Sheet, so that the redrawn image is the same character rather than a new interpretation.
- Add a failing-Character-Sheet scenario asserting that the sheet is regenerated rather than edited, even though nothing else would disqualify it from a surgical repair.
- Add a scenario in which the user explicitly asks for a small fix to one application. Assert that regeneration from the Character Sheet and the Primary Identity Anchor is recommended, that the edit still proceeds when the user asks for it, and that its inputs are the application plus the Primary Identity Anchor without the Character Sheet.
- Add a single-image scenario asserting that no Character Sheet stage is introduced when there is no continuity requirement.
- Add an application scenario with a new expression, gaze, pose, and camera angle, asserting that the conservative Character Sheet rules do not leak into it.
- Add a tier gate scenario asserting three fixed labels in stable order plus the Custom path, with concrete proportions adapted to the stated use.
- Add a second tier gate for a different use, asserting the labels are identical while the concrete values differ.
- Add an adult middle-proportion scenario asserting the child-reading disclosure appears and that the option is not described as mild.
- Add a strongly deformed scenario asserting that hairstyle, eye shape, marks, and characteristic wardrobe become the weighted channels, and that any channel the tier closes is disclosed before generation without appearing in the prompt as a negative statement.
- Add a body-evidence gradient scenario using a source whose figure is clearly visible, covering all four tiers. Assert that equal proportion carries it unchanged, the intermediate tiers carry it simplified, the second-shortest proportion offers it as an explicit choice with the more-mature consequence stated, and the shortest proportion discloses the loss before generation.
- Add a case in which the user wants both the shortest proportion and their figure preserved. Assert that a less deformed tier is offered as the resolution and that the figure is not drawn onto the shortest proportion.
- Add a case combining a child-reading proportion with a request emphasizing adult body characteristics. Assert the combination is refused as a combination and resolved by moving the tier, and that the refusal does not silently rewrite the request into a moderated version of itself.
- Add a case asserting that wherever body evidence is carried, the prompt names it neutrally and concretely, including chest volume with its shoulder and upper-torso relationships when clearly shown, and introduces no measurements, cup sizes, or erotic emphasis.
- Add an equal-proportion scenario asserting structural features are still carried, proving the tier resolves rather than a single drawn default applying everywhere.
- Add a stylization-intensity scenario covering both failure ends: a filtered-photograph result and a generic-anime-face result must both be treated as failures of the parameter rather than of the style.
- Add a style-axis scenario asserting that line, surface coloring with shading-layer count, colour logic, eye rendering, texture with screentone, and background are separately expressible, and that changing background leaves character rendering unchanged.
- Add an unqualified-request scenario in which the user asks only for an anime version. Assert that the named looks are offered as a choice, that each is described by visible features, and that the skill does not resolve to one look on its own.
- Add an orthogonality scenario combining flat cel with a heavy optical finish and the same flat cel with none. Assert both are produced as requested and that neither is described as a compromise or a contradiction.
- Add a period-look scenario asserting that the request is met through palette and optical finish, and that the painting technique named by the user is not silently changed.
- Add a colour-logic scenario across a set, asserting one shared set of character colours is carried into every image and that it is expressed separately from shading-layer count.
- Add a scenario asserting the skill offers no ranking of the named looks by expected quality and makes no claim about which will come out better.
- Add a scenario in which the user names an artist. Assert the skill converts it into visible feature language rather than passing the name through.
- Add a set scenario on a surface that supports batch production, asserting one planned batch, and a paired scenario on a surface that does not, asserting sequential generation from the Character Sheet with no batch-consistency claim.
- Add a set scenario asserting dimension verification across the delivered images.
- Add a transparency scenario asserting the limitation is stated before generation and the cutout is recorded as a downstream delivery requirement.
- Add a mannerism scenario pairing a chibi sticker set, where mannerisms are weighted and marked as assumptions, with an avatar request where they are not weighted; assert that no review failure is ever attributed to a mannerism.
- Add a multi-person drawn request asserting the limitation is stated and no blended result is produced.
- Preserve every scenario introduced by the medium-aware identity contract specification unchanged, and confirm the photographic controls still pass.
- Run the existing structural skill validator afterwards as a packaging and reference-integrity check.

## Out of Scope

- Multi-person drawn output, couple illustrations, and group images.
- Transparent background generation, alpha channels, and automated cutout.
- Any ranking, grading, or difficulty estimate across the named looks. No per-look evidence exists.
- Any look, term, or axis value that appears in only one source or that a source's own author describes as their personal coinage.
- A fixed catalog of background options. The axis is established; no particular set of options is.
- Any success-rate promise for batch production, and any claim about how many images in a batch are typically usable.
- Any numeric threshold for how many design iterations cause drift.
- Any stated maximum number of reference images.
- Video, animation, motion, and sequential-frame output.
- A style browser, style gallery, preset catalog, or persistent character library.
- A new module, agent, or workflow stage. This is built on existing seams.
- Similarity scores, biometric matching, and identity guarantees.
- Changes to photographic behavior of any kind.

## Further Notes

- Batch consistency behavior is described consistently by several independent third-party sources but was not confirmed in official documentation, and it depends on a paid-tier reasoning mode. That is why it is specified as a capability boundary with a fallback rather than as a promised feature. A reported usable-rate for batches comes from a single source and is deliberately absent here.
- Mannerism weighting rests on findings that dynamic identity signatures help recognition only when the viewer already knows the person and static cues are degraded. Both conditions hold for a chibi sticker set seen by friends and hold for little else, which is why the weighting varies rather than applying uniformly. Extracting a genuine mannerism requires several expressions; a single photograph cannot supply one, which is why any inferred mannerism is marked as an assumption.
- Equal-proportion anime demonstrably still carries structural features such as nose bridge and upper-lip thickness. Any implementation that treats all drawn output as strongly deformed has misread both this specification and the one it depends on.
- The source material is not internally consistent about body shape under deformation. One passage states that the two shortest proportions flatten body differences regardless of the original build, while another states that the second-shortest proportion can be drawn with chest, waist, and hip curvature and reads more mature when it is. The gradient resolves the two: the capability exists at that proportion and comes with an age-reading consequence, and only the shortest proportion truly cannot carry it. An earlier draft of this specification stated that body channels close entirely at deformed tiers, which contradicted four separate places in the current contract where visible body evidence is preserved by default, named directly in prompts, and protected from being flattened by clothing.
- The relationship between the Character Sheet and the industry practice of a color-key board is close: both are a reference artifact approved once and then used to keep everything downstream coherent. The difference is only what they anchor.
- The named looks come from an illustration-side vocabulary, while the two-stage split between surface coloring and optical finish comes from the animation production side. The two vocabularies are commonly conflated and the illustration-side sources state outright that the look names have no strict definitions. They are offered as starting points with visible features attached for exactly that reason; an implementation that turns them into mutually exclusive modes would enforce a boundary the source material does not.
- The colour logic axis is supported at two different strengths and this specification uses each accordingly. That the axis exists is well supported: it is a separately credited decision-making role in animation production that split off from art direction as the work specialized, and a peer-reviewed treatment formalizes a character's palette as a small set of colour slots with cast-level consistency and distinguishability constraints. Its concrete content is weaker: the published slot count comes from a single study, and the shadow-derivation rule is consistent across illustration teaching sources but was not confirmed inside production practice. That is why no slot count appears here and the derivation rule is specified as an overridable default.
- Two style questions were deliberately left unspecified for lack of evidence. There is no per-look reachability data, only a category-level finding that drawn-anime styles reproduce better than physical-media styles and that watercolour sits in the harder category. And screentone's behavior under generation is entirely unmeasured; it is flagged only as dense high-frequency micro-structure, which is where the model's own artifact is known to be strongest, not as a look that is known to fail.
- The most detailed eye-parameter breakdown found during research was disclosed by its own author as machine-generated and was discarded. The eye parameters here were assembled from separate sourced pieces instead, which is why the list is shorter than it could have been.
- The rendering artifact affecting the active model was re-checked on 2026-08-12, which was the condition this specification placed on finalizing the artifact-risk guidance. No official fix has been announced, the community issue list still carries it as open, and the latest named-engineer signal, dated 2026-08-06, is that it is still being worked on and still visible in the wild. The guidance above is therefore settled rather than provisional, and it should be revisited only when a fix is announced. Findings and sources are in `tiling-grime-status.md` alongside this file.
- Research backing this specification is in `research.md` alongside this file, which labels every design decision by evidence strength. Decisions marked as inference appear here only in this section or in Out of Scope.
