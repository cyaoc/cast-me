Status: ready-for-agent

# Exact Text and Physical Scene Coherence

## Problem Statement

CastMe already builds complete production prompts from a detailed internal decision state, but two small gaps can still weaken the generated image.

First, exact in-image text is quoted and assigned a hierarchy and placement, but the final prompt does not consistently require a concrete type style, color, relative size, precise spatial alignment, or an explicit allowed-text set. The model may therefore improvise typography or introduce extra text even when the user's copy is exact.

Second, creative direction, shot, performance, styling, and First-Pass Finish can be resolved in different turns. The workflow already says that art direction should reconcile them into one physical scene, but its final pre-generation check verifies that each dimension is concrete rather than explicitly verifying Physical Scene Coherence. A rainy-night setting and a noon-sun finish can therefore reach the final prompt as individually complete but mutually incompatible instructions.

These gaps should be closed without changing the existing field-oriented Prompt Structure, making the production prompt visible to the user, adding ordinary typography questions, introducing a separate consistency-review stage, or expanding the existing concrete-visual-language rules.

## Solution

Keep the current production-prompt structure and every existing internal completeness dimension. Strengthen only the exact-text contract and the existing pre-generation check.

Whenever exact text is required, the production prompt must include every allowed string verbatim, its role and hierarchy, a brief-compatible type style, color, relative size, and precise region/alignment. Missing treatment details are derived internally from the selected creative direction, layout, First Read, and intended display size. They do not create another user gate unless a missing typography decision would materially change explicit brand or creative intent. When the listed copy is the complete allowed set, the prompt must forbid any other text.

Before generation, verify Physical Scene Coherence across the resolved setting and time/weather, shot and perspective, performance, styling and materials, and lighting and finish. Resolve Suggested and Derived conflicts internally while preserving the closest coherent expression of the selected direction. A later explicit instruction that clearly reopens or replaces an earlier choice updates that earlier choice without another question. Ask one focused confirmation only when two incompatible Explicit Locks must both otherwise remain and the user's wording establishes no override relationship.

Do not add a new visible workflow stage. This is a final-prompt completeness and coherence refinement inside the existing generation path.

## User Stories

1. As a user supplying exact title copy, I want every character passed to the image model verbatim, so that the model is not asked to paraphrase my text.
2. As a user supplying one title, I want the prompt to forbid unrelated text, so that the image does not acquire invented subtitles, labels, logos, or filler copy.
3. As a user supplying several approved strings, I want the prompt to enumerate the complete allowed set, so that all requested copy is permitted and nothing else is introduced.
4. As a user requesting a poster, I want the title's type style to fit the selected direction, so that typography supports rather than contradicts the image.
5. As a user requesting exact text, I want its color specified, so that the model does not improvise a color that loses contrast or breaks the palette.
6. As a user requesting exact text, I want its relative size and hierarchy specified, so that a title, subtitle, CTA, date, price, or label reads with the intended importance.
7. As a user requesting exact text, I want its region and alignment specified precisely, so that the copy occupies the reserved layout area rather than covering the person or First Read.
8. As a user who provides copy but no typography direction, I want CastMe to infer a suitable treatment, so that I am not forced to choose professional design details.
9. As a beginner, I want missing font, color, size, and placement details resolved internally, so that exact text does not add another routine questionnaire.
10. As a user whose brand typography matters, I want CastMe to ask one focused question when the missing treatment could materially change my brand intent, so that it does not invent a brand decision.
11. As a user who explicitly specifies typography, I want those choices preserved as Explicit Locks, so that internal defaults do not replace my instructions.
12. As a user supplying Chinese or other non-Latin copy, I want the existing character-by-character verification retained, so that Latin-only advice such as all caps or letter spelling is not applied mechanically.
13. As a user requesting an exact numeric type size, I want it treated as layout intent rather than an unverified delivery claim, so that the workflow remains truthful about generation controls.
14. As a user reviewing generated exact text, I want the existing targeted correction and no-text fallback behavior preserved, so that stronger prompting is not misrepresented as a rendering guarantee.
15. As a user choosing a setting and finish in different turns, I want them to form one coherent physical scene, so that the final image does not combine incompatible time, weather, and light.
16. As a user choosing a shot and action separately, I want perspective, body geometry, gaze, contact, and motion to agree, so that the requested performance remains physically readable.
17. As a user choosing wardrobe and lighting separately, I want materials to respond coherently to the environment and light, so that clothing and props do not look pasted into the scene.
18. As a user accepting recommended defaults, I want small cross-dimensional conflicts resolved internally, so that coherence checking does not create another routine gate.
19. As a user whose Explicit Lock conflicts with a Suggested or Derived value, I want the Explicit Lock preserved and the non-explicit value reconciled, so that my stated intent remains authoritative.
20. As a user who clearly says that a new instruction replaces an earlier one, I want CastMe to update the earlier choice without asking again, so that an explicit change is not mistaken for ambiguity.
21. As a user who has supplied two incompatible Explicit Locks without saying which one wins, I want one focused confirmation with a recommended coherent resolution, so that CastMe does not silently discard either choice.
22. As a user resolving a Physical Scene Coherence conflict, I want every unrelated lock preserved, so that one correction does not restart the brief.
23. As a user completing a coherence confirmation, I want generation to continue from the existing decision state, so that I am not sent back through earlier questions.
24. As a user generating a simple image with no conflict, I want the coherence check to remain invisible, so that the ordinary flow does not become longer.
25. As a user relying on detailed identity, anatomy, projection, styling, and delivery constraints, I want all existing production-prompt fields retained, so that prompt-format cleanup does not omit important information.
26. As a user who cannot see the internal production prompt, I want effort spent on completeness rather than rewriting the same information into a more polished paragraph, so that formatting work does not add cost without improving my result.
27. As a user requesting a concrete visual direction, I want the current material, lighting, composition, and texture rules retained, so that this change does not add speculative historical or real-world details.
28. As a maintainer, I want exact-text and coherence behavior tested through complete conversations and production readiness, so that tests protect user-visible behavior rather than a particular prompt serialization.

## Implementation Decisions

- Preserve the existing field-oriented Prompt Structure. Do not convert it into one to three paragraphs, a fixed prose format, or a smaller grouped serialization.
- Preserve every existing internal production dimension and omit only dimensions that are already irrelevant under the current rules.
- Do not expose the production prompt merely to justify its internal format. Prompt visibility is not part of this change.
- Keep exact-text ownership in the existing prompt-craft and layout/output responsibilities. No new module or routing stage is needed.
- For every exact string, require its semantic role, hierarchy, type style, color, relative size, and precise spatial region/alignment in the production prompt.
- Prefer a type category or visible typographic character over an invented named font. Preserve an exact font or brand specification only when the user supplies it or an authoritative reference defines it.
- Prefer relative scale and hierarchy over an implied guarantee of physical point size. Preserve a user-supplied numeric size as intent, but do not claim that the generated asset was measured to that value.
- Treat the user's listed exact copy as the allowed-text set. When it is complete, explicitly forbid all other text. When several strings are allowed, enumerate all of them before forbidding additional text.
- Retain exact-string quoting and character-by-character verification. Do not apply all-caps or letter-by-letter spelling rules to scripts where they are not meaningful.
- Derive missing exact-text treatment internally from intended use, selected creative direction, layout, First Read, palette, and intended display size.
- Do not add a typography gate for ordinary exact-text requests. Ask one focused question only when missing treatment would materially change explicit brand or creative intent, or when supplied typography instructions conflict.
- Preserve the existing targeted exact-text revision and clean no-text fallback. Better prompt specificity does not create an exact-rendering guarantee.
- Make Physical Scene Coherence part of the existing pre-generation check rather than a new workflow step, visible checklist, or user-facing summary.
- Check the resolved setting and time/weather, shot and perspective, performance and pose geometry, styling and materials, and lighting and finish as one internally coherent scene.
- Resolve conflicts involving Suggested or Derived values internally. Preserve any compatible parts and choose the closest coherent expression of the selected direction rather than reopening ordinary choices.
- When an Explicit Lock conflicts with a non-explicit value, preserve the Explicit Lock and reconcile the non-explicit value.
- When a later explicit instruction clearly reopens, changes, or replaces an earlier choice, update the earlier decision and continue without a confirmation gate.
- When two Explicit Locks are physically incompatible and neither overrides the other, ask exactly one focused confirmation. State the conflict concretely, recommend one coherent resolution, and offer the direct alternative without restarting the brief.
- After a coherence confirmation, preserve every unrelated Explicit Lock, Derived Lock, accepted risk, reference decision, and output requirement, then continue from the existing generation state.
- Keep existing identity, reference coverage, anatomy, projection, safety, exact-text verification, refresh, and targeted-revision gates authoritative for their own conflicts. Physical Scene Coherence does not replace them.
- Do not add a rule encouraging unverified real-world or historical facts. Existing concrete material, light, camera, location, prop, composition, and texture rules remain sufficient. Existing research behavior continues to apply only when the user explicitly requests currentness, trends, or factual accuracy.
- Use `Physical Scene Coherence` as the canonical domain term. Do not introduce a separate Consistency Review or Cross-Dimensional Check stage.
- No ADR is required because the change is narrow, prompt-level, and easy to reverse; it does not introduce an architectural trade-off.

## Testing Decisions

- Use the existing golden-conversation behavior suite as the single highest-level testing seam. It already covers exact-text posters, decision inheritance, focused conflicts, prompt completeness, identity preservation, and generation readiness.
- Test externally visible questioning, lock handling, and production-prompt completeness. Do not assert exact prose, field order, label names, prompt length, or paragraph count.
- Extend the existing exact-text poster scenario so that an ordinary title-only request generates without a typography question and the production prompt includes the verbatim title, derived type style, color, relative hierarchy, precise placement, and no unapproved text.
- Add or extend a multiple-copy scenario proving that every allowed string is enumerated once and that additional text is forbidden without excluding requested copy.
- Add a brand-critical typography scenario proving that one focused question is asked only when the missing information would materially change explicit brand intent.
- Preserve the existing exact-text character verification, targeted text correction, and clean no-text fallback checks.
- Add a non-explicit coherence scenario in which a rainy-night direction conflicts with a Suggested or Derived noon-light treatment. The skill must reconcile the finish internally and generate without another user gate.
- Add an explicit-override scenario in which the user clearly changes a rainy-night choice to noon. The earlier choice must be updated without a conflict question.
- Add an incompatible-Explicit-Locks scenario in which rainy-night weather and direct noon sunlight must both otherwise remain. The skill must ask one focused confirmation, recommend a coherent resolution, and preserve every unrelated lock.
- Add a post-confirmation check proving that generation resumes from the existing decision state without repeating resolved creative, shot, styling, performance, finish, reference, or output questions.
- Preserve every existing prompt-completeness and output-recipe scenario. No test should require the production prompt to be converted into paragraphs or grouped sections.
- Run the complete golden-conversation audit and require zero failures.
- Run the existing skill-package validator and whitespace validation as structural checks. They do not create another behavioral testing seam.

## Out of Scope

- Rewriting the production prompt as one to three sentences or paragraphs.
- Consolidating, renaming, reordering, or deleting existing production-prompt fields merely to make the prompt look more directorial.
- Making the production prompt visible to the user.
- Adding a prompt-length, token-count, or field-count target.
- Adding an ordinary typography questionnaire or separate text-design stage.
- Adding a separate Physical Scene Coherence review screen, checklist, workflow stage, or generation pass.
- Embedding font files, selecting installed fonts, building a typography engine, measuring point sizes, or guaranteeing typographic fidelity.
- Guaranteeing exact text rendering from prompt wording alone.
- Adding OCR, external text verification services, Image API integration, a custom backend, or a new dependency.
- Adding a rule to invent specific eras, weather facts, materials, products, places, or historical details from model knowledge.
- Reworking the existing concrete visual language, Taste Rules, output recipes, First Read, First-Pass Finish, Final-Asset Quality, or Natural Retouch contracts.
- Changing identity preservation, Reference Coverage, anatomy, projection, pose, continuity, refresh, safety, or targeted-revision behavior beyond the stated coherence conflict routing.
- Creating an ADR.

## Further Notes

- Current OpenAI guidance says complex image requests may use short labeled segments or line breaks and that minimal prompts, paragraphs, JSON-like structures, instruction-style prompts, and tag-based prompts can all work when intent and constraints are clear. This supports retaining CastMe's current field-oriented structure rather than performing a format-only rewrite.
- Current OpenAI guidance recommends putting literal text in quotes and specifying font style, size, color, and placement. It also recommends explicitly excluding extra text when the allowed copy is fixed. CastMe adapts `size` to relative hierarchy unless the user supplies a numeric intent, because prompt wording alone does not verify final typographic measurements.
- Physical Scene Coherence is a CastMe domain rule inferred from its staged decision model, not an OpenAI-mandated prompt format.
- The domain glossary already records Physical Scene Coherence as a state, not a user-visible review stage.
