Status: ready-for-agent

# Context-Efficient Reference Loading

## Problem Statement

CastMe currently requires a normal generation run to read the identity, composition, and styling/performance reference modules before generation, even when large parts of those modules are irrelevant to the current request. The main skill instructions also repeat reference routing, ownership, generation checks, and review checks that already exist in the owning reference modules.

This weakens the skill's progressive-disclosure design. It increases the amount of text the model must hold during ordinary work, makes core rules compete with conditional details, and raises the maintenance risk that duplicated rules drift apart. The problem is the unconditional loading and repeated guidance, not the number of reference files.

The skill must reduce required context without weakening identity preservation, the standard decision format, Explicit Lock and Derived Lock behavior, beginner-facing guidance, First-Pass Finish, final-asset quality, prompt completeness, or surgical revision behavior.

## Solution

Replace unconditional reference loading with one compact routing contract in the main skill instructions. The routing contract maps task conditions to stable Markdown section headings. The agent should prefer reading only the relevant sections when its file tools support targeted reads and fall back to the complete owning reference file when they do not.

Keep a small mandatory core for normal person-centered generation:

- identity `Priority`, `Reference Transfer`, and `Reference Coverage`
- final-prompt `Identity Prompt Constraints`
- `Final-Asset Quality`
- `First-Pass Finish`
- `Prompt Structure`

Read other sections only when their choice, risk, research branch, output requirement, or revision concern is active. Do not track formal "sections already read" state; rely on the current task context and avoid knowingly rereading material already loaded.

For a narrow revision to a visible result, bypass the normal-generation core. Read the identity `Revision` section and the relevant section owned by the visible problem. Add other core sections only when the requested change actually touches identity, composition, final quality, or finish.

Keep shared behavioral rules in one place. The main skill instructions remain the single source of truth for the standard decision format, decision-state meanings, one-decision-per-turn behavior, and the beginner technical-parameter boundary. Reference modules keep only their domain-specific application of those rules.

Replace the long generation and review checklists in the main instructions with short cross-module completion conditions. Each reference module remains responsible for its own detailed generation and review checks.

Report the before-and-after word counts and rule disposition after implementation. The user will manually test and confirm behavior.

## User Stories

1. As a CastMe user with a complete brief, I want the skill to read only the rules needed for my image, so that generation is not burdened by unrelated guidance.
2. As a CastMe user who needs progressive guidance, I want all relevant clarification rules to remain available, so that context reduction does not skip important choices.
3. As a user providing a person reference, I want identity priority, reference transfer, and reference coverage to remain mandatory, so that progressive loading does not weaken likeness or evidence handling.
4. As a user requesting a normal final image, I want final-asset quality and First-Pass Finish to remain mandatory, so that context reduction does not reduce output quality.
5. As a user receiving a final production prompt, I want identity constraints and the prompt structure applied every time, so that the result remains complete and concrete.
6. As a beginner, I want to choose visible outcomes rather than ISO, aperture, shutter speed, Kelvin values, equipment, or lighting modifiers, so that the interaction remains approachable.
7. As a user answering a clarification, I want the standard recommendation and options format to remain consistent, so that routing changes do not alter the interaction contract.
8. As a user with Explicit Locks, I want every explicit decision preserved across later questions, refreshes, generation, and revision, so that loading fewer references does not reopen my choices.
9. As a user with Derived Locks, I want only the owning refreshed area to reopen them, so that progressive loading preserves Scoped Option Refresh behavior.
10. As a user asking for styling or performance guidance, I want the relevant styling/performance sections loaded, so that clothing, props, pose, expression, gaze, hands, and action remain coherent.
11. As a user whose request does not involve styling or performance decisions, I want those unrelated sections omitted, so that they do not consume context or distract the model.
12. As a user asking for a named character, uniform, historical costume, or other canon-dependent look, I want the visual-research rules loaded when that branch is active, so that the skill does not guess niche visual facts.
13. As a user asking for a Trend Refresh, I want current-direction research rules loaded only for that explicit current or trending request, so that ordinary creative work remains local.
14. As a user requesting a series, I want continuity rules loaded for the series, so that identity, wardrobe, prop state, weather, light direction, geography, and color treatment remain stable.
15. As a user requesting one image, I want series continuity rules omitted, so that a single image does not inherit an unnecessary contract.
16. As a user asking to fix one visible issue, I want a surgical revision path that reads only revision and issue-owning guidance, so that the skill does not restart the full brief.
17. As a user asking to fix a hand, I want identity and unrelated visual locks preserved without reloading every creative module, so that the correction stays narrow.
18. As a user asking for a finish correction, I want the relevant finish and identity rules loaded, so that the visible issue is corrected without changing composition, pose, wardrobe, text, or background.
19. As a user reviewing a visible result, I want identity checked every time and only the participating modules checked in detail, so that review remains relevant rather than exhaustive by default.
20. As a user on a surface that cannot read part of a Markdown file, I want the skill to fall back to the complete owning reference, so that optimization never becomes a correctness dependency.
21. As a maintainer, I want one routing table to decide when reference material is needed, so that loading behavior has one source of truth.
22. As a maintainer, I want reference modules to state their ownership without defining a second loading policy, so that routing instructions do not drift.
23. As a maintainer, I want stable Markdown headings used as routing targets rather than line numbers, so that ordinary edits do not invalidate the routing contract.
24. As a maintainer, I want duplicated routing and cross-module checks removed, so that core rules remain prominent and easier to update.
25. As a maintainer, I want domain-specific parameter guidance preserved where it affects production prompts, so that deduplication does not erase a distinct internal constraint.
26. As a maintainer, I want no read-state machine, parser, heading validator, or new runtime mechanism, so that context optimization does not create a maintenance system.
27. As a maintainer, I want no new reference files in this change, so that the smallest sufficient structural change is attempted first.
28. As a maintainer, I want a before-and-after rule inventory, so that merged duplicates can be distinguished from accidentally lost behavior.
29. As a maintainer, I want before-and-after word counts, so that the context reduction is visible without introducing tokenizer dependencies or false precision.
30. As the user approving the skill, I want to perform the behavioral confirmation manually, so that this change does not add tests or automation I did not request.

## Implementation Decisions

- Keep the existing reference-file structure. Do not add, split, merge, or rename reference modules in this change.
- Replace the unconditional instruction to read all normal-generation reference modules with one compact condition-to-section routing table in the main skill instructions.
- Use stable Markdown heading names as routing targets. Do not use line numbers.
- Define section-level reading as a preferred optimization, not a correctness requirement. When the active environment cannot read a section selectively, read the complete owning reference file.
- Do not add formal state for sections already read. Avoid rereading when the material is already present in the current task context.
- For every normal person-centered generation, require the identity `Priority`, `Reference Transfer`, and `Reference Coverage` sections.
- Before writing a final generation prompt, require `Identity Prompt Constraints`, `Final-Asset Quality`, `First-Pass Finish`, and `Prompt Structure`.
- Read creative-direction, shot, perspective, art-direction, output-recipe, layout, styling, performance, pose, research, continuity, and other conditional sections only when the current request activates them.
- Route non-obvious conditional concerns explicitly:
  - side-facing identity, action, or strong perspective requires `Face Visibility and Performance Integrity`, `Perspective Intent`, `Camera and Capture Plan`, and `Pose Geometry` as relevant to the request
  - wardrobe, accessories, props, pose, action, expression, gaze, hands, or performance requires the corresponding styling/performance sections
  - named characters, uniforms, historical dress, or other canon-dependent styling requires `Role, Costume, and Visual Research`
  - exact text, layout, platform delivery, or a requested series requires `Layout and Output Contract` and its relevant continuity rules
  - replacement or new creative choices requires `Scoped Option Refresh` plus the section that owns the target creative area
- A narrow revision bypasses the normal-generation mandatory core. It requires identity `Revision` plus the section that owns the requested visible correction. Add other sections only when the correction touches their concerns.
- When reviewing a visible result, always read identity `Revision` and review identity first. Then read the participating module sections that contain the relevant final review checks. Review composition, styling, performance, text, quality, finish, or delivery only when those modules participated in the generation or revision.
- Keep the main skill instructions as the single source of truth for:
  - the localized standard decision format
  - `locked: explicit`, `locked: derived`, `suggested`, and `unresolved`
  - one unresolved dimension or tightly coupled decision group per turn
  - the beginner-facing technical-parameter boundary
- Reference modules may state how a shared rule applies to their domain, but must not redefine the shared rule.
- Preserve the composition rule that numeric camera and exposure terms are optional internal aesthetic cues tied to visible consequences. It has a distinct internal production-prompt scope and is not a duplicate of the beginner-facing question boundary.
- Keep one short ownership sentence at the start of each reference module. Remove duplicated self-loading instructions such as "required before" or "use whenever"; the main routing table owns those decisions.
- Remove the repeated reference-routing map later in the main workflow once the compact routing table replaces it.
- Reduce the main generation and review checklists to these cross-module completion conditions:
  - every required focused gate is resolved
  - locked user intent is unchanged
  - the results of every participating module are represented in the production prompt or revision
  - claims about tool controls, output quality, size, text, and visual review are truthful and verified where required
- Keep detailed identity, composition, styling, performance, text, quality, finish, and revision checks in their owning reference modules.
- Do not create a script, parser, read tracker, heading validator, new dependency, configuration system, hook, or runtime service.
- Do not add or change domain glossary terms. This is a skill-loading and documentation-ownership change, not a change to the CastMe domain model.
- Do not create an ADR. The decision is local, reversible, and does not introduce a hard-to-reverse architecture boundary.
- Capture the implementation baseline from the current worktree immediately before editing, not from the last commit, so unrelated uncommitted skill changes are included in the comparison.
- After implementation, report:
  - before-and-after word counts for the main instructions and reference modules
  - before-and-after minimum required reading for normal generation and narrow revision
  - section-level preferred reading and whole-file fallback figures separately when they differ
  - each normative rule marked as retained, merged into its single source, or removed as duplication
- Do not install a tokenizer. Do not use token count as an acceptance requirement. Word count is the primary context-size estimate; byte count may be included as a secondary measure.
- Do not set a hard word-count reduction target. Necessary behavior must not be removed merely to hit a number.

## Testing Decisions

- Behavioral acceptance is manual and belongs to the user. Do not add automated tests, golden scenarios, fixtures, scripts, or test dependencies for this change.
- Use the existing golden-conversation document only as a coverage reference while comparing rules. Do not modify it as part of this specification.
- Before editing, inventory the normative behavior in the affected main instructions and reference sections. After editing, account for every item as retained, merged, or intentionally removed as duplication.
- Treat an unexplained missing normative behavior as a failed implementation review. Repetition may be deleted; behavior may not disappear silently.
- Provide the user with the final rule-change summary and word-count comparison so they can choose representative manual conversations.
- Require both the complete-brief normal-generation path and the narrow-revision path to read fewer words than the captured baseline. No whole-file fallback path may require more words than the corresponding baseline path.
- Suggested manual confirmation areas are normal generation with a complete brief, guided generation with missing choices, a conditional research or continuity branch, and a narrow visible revision. These are suggestions for the user, not automated implementation work.
- Existing skill-format validation may be run only as a structural check. It does not replace the user's behavioral confirmation.

## Out of Scope

- Adding, splitting, merging, or renaming reference files.
- A formal state machine for loaded or unread sections.
- A Markdown parser, section extractor, heading validator, or context-loading runtime.
- Guaranteed section-level loading on every ChatGPT, Codex, or Agent Skills-compatible surface.
- Tokenizer installation, exact token accounting, API billing estimates, or model-specific context benchmarks.
- A hard word-count or percentage-reduction target.
- New automated behavioral tests, golden conversations, fixtures, evaluation scripts, or dependencies.
- Changes to identity preservation, Scoped Option Refresh, Style Refresh, Trend Refresh, First-Pass Finish, Final-Asset Quality, Natural Retouch, First Read, or existing safety behavior.
- New domain terminology or changes to the glossary.
- An ADR.
- Rewriting unrelated prose, examples, formatting, or project documentation.

## Further Notes

- The optimization must remain subordinate to correctness. Section-level reads are preferred when available; complete-file reads are the safe fallback.
- The first implementation should prove whether removing unconditional loading and duplicated guidance is sufficient. Split large references only if later manual use still demonstrates a concrete context or missed-rule problem.
- The user explicitly chose manual behavioral confirmation and asked to avoid further test design.
