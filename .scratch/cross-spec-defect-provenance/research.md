# Provenance of the three deferred defects

Question: are the three findings that survived five review rounds original logic errors, or drift introduced while implementing the branch?

Baseline for every comparison is `060b5f6`, the review fixed point. The branch is `feat/anime-adaptation`, 19 commits landing three specs and ten issues. Method is git archaeology against the repo's own history and the spec files under `.scratch/`; every claim below cites either the commit that introduced a line or the spec text that asked for it.

Headline: **none of the three is a pre-branch logic error.** One turned out not to be a defect at all — the reviews misread a glossary convention the repository had never written down. One was written into the spec itself, in wording that contradicts itself inside a single document. One is a baseline ambiguity that reviewers resolved by adjudication during implementation.

## A — `stylization intensity` is both a banned term and a load-bearing one

`CONTEXT.md:25` lists `_Avoid_: Style level, chibi mode, stylization intensity` under **Deformation Tier**, while the same phrase carries a first-class production decision and has no glossary entry of its own. Actual usage is 33 occurrences: 17 English (`composition-director.md` 7, `golden-conversations.md` 4, `SKILL.md` 2, `identity-anchor.md` 2, `CONTEXT.md` 2) plus 14 as 风格化强度 in `docs/architecture.md`, which has no English occurrence.

Origin:

- The baseline glossary has no `Deformation Tier` entry at all; `git show 060b5f6:CONTEXT.md` has no match for `stylization`.
- The `_Avoid_` line arrived with `52b0829 feat: resolve deformation tier body evidence`.
- The load-bearing usage arrived *later*, with `e79eca0 feat: control drawn stylization intensity`, and spread to the Golden scenarios in `639b220`.

**Corrected verdict: not a defect.** An earlier draft of this note called it a spec design error, on the grounds that `domain-changes.md:44` bans the phrase while `:47` promotes the concept. That reading does not survive the convention. `:47` says the two are `separate and easy to confuse`, which is the reason `:44` lists the phrase — the entry guards against calling the tier by the neighbouring concept's name. The two lines agree.

The convention decides it. `CONTEXT-FORMAT.md` rules that `_Avoid_` collects the losing words for the concept the entry names — it constrains that entry's naming, not the repository's wording. Read that way there is no violation: the runtime prose uses `stylization intensity` for its own separate decision, which is the correct use.

Repository practice is in fact broader than pure synonyms, and consistently so. `Protected Identity Cue` avoids `Makeup intensity, beauty feature`; `Story Makeup` avoids `Retouch target, accidental blemish, finish effect`; `Character Read` avoids `True temperament, personality diagnosis`. None are synonyms; all are adjacent concepts that must not be collapsed into the entry. `Deformation Tier` avoiding `stylization intensity` is the same move.

Root cause: **`docs/agents/domain.md` never defined what `_Avoid_` means** — the file had no occurrence of the word, so an agent that never read the external `CONTEXT-FORMAT.md` had nothing to constrain the reading, and three successive Standards passes chose the repository-wide one. Remediation `6025c87` made the optics worse without touching the cause, adding `It governs proportion and shape, not the separate ordinary decision about stylization intensity.` at `CONTEXT.md:24`, so the entry now uses the phrase on one line and lists it on the next.

Not reachable at spec review, because there was nothing to catch. It was reachable at the first Standards finding, by asking what `_Avoid_` governs before reporting a violation.

Fix, applied: `docs/agents/domain.md` now states that `_Avoid_` constrains only that entry's naming, that entries hold adjacent concepts as well as synonyms, and that frequent use is not grounds for a canonical term. `CONTEXT.md:25` is left as the spec wrote it. `stylization intensity` gets no entry: `:47`'s reasoning holds — it names a degree, not a concept the vocabulary lacks — and issues 02 through 06 all pin the glossary at `39 canonical terms`.

## B — child-reading proportion versus second-shortest curvature

Four statements in `skills/cast-me/references/identity-anchor.md` interact badly: `:127` offers a sticker gate spanning roughly 4, 3 and 2 heads; `:129` discloses that roughly four-to-five-head proportions read as a child; `:138` requires the second-shortest coherent proportion to describe chest, waist and hip curvature when the source supports it; `:141` forbids combining emphasized adult body characteristics with any child-reading proportion. A sticker gate's second-shortest tier is 3 heads, already below the stated child-reading threshold.

Origin: all four came from one commit. `git log -S` on `four-to-five-head`, `second-shortest coherent proportion`, `emphasized adult body characteristics` and `roughly 4, 3, and 2`, scoped to `skills/`, returns only `52b0829` for each. Re-running each over `6025c87..HEAD` returns nothing.

One remediation commit did touch the neighbouring clause, and it loosened rather than tightened: `ec7f666` changed `move to the closest non-child-reading tier` to `move to a non-child-reading tier`. The word `any` in `:141` has been there since `52b0829`.

The spec requires all four, and it noticed the tension without resolving it:

- anime PRD: middle proportions of roughly four to five heads `read as a child rather than as mild stylization`, and the main expressive division sits between the two and three head-tall readings.
- anime PRD on the second-shortest proportion: curvature is available as an explicit choice `with the disclosed consequence that drawing it reads more mature and therefore partly offsets the tier's younger reading`.
- anime PRD on the exclusion: `Do not combine emphasized adult body characteristics with a proportion that reads as a child... This is a hard exclusion, not a recommendation.`
- `issues/02-resolve-deformation-tier-and-body-evidence.md:19` and `:21` restate both halves, and `:32` requires Golden 141 to pair them in one scenario.

Verdict: **spec design error, but a narrower one than it first looks.** The two rules are reconcilable, and the spec supplies the discriminator without ever stating it as a rule.

Two passes of this note got the verdict wrong in opposite directions. The first called them reconcilable on trigger alone. The second called them irreconcilable, reasoning that curvature `reads more mature and therefore partly offsets the tier's younger reading` places both on one axis. That conflates age reading with adult body emphasis. The exclusion at PRD `:147` is grounded in `sexualized depiction of apparent minors`; its subject is sexualization, not maturity of read. Neutral description of a figure the source already shows is not that.

The spec knew about the collision and decided it. PRD `:232` weighs the two source passages against each other and rules that the capability exists at the second-shortest proportion at an age-reading cost, and `issues/02:32` requires Golden 141 to hold the curvature consequence and the exclusion in one scenario, bounded by `neutral body language without measurements or erotic emphasis`. The discriminator is assemblable from `:147`'s rationale plus `:32`'s bound — but it is written as a rule in neither place, so a reader hitting `:141`'s `any child-reading proportion` has nothing telling them which side neutral carrying falls on. The defect is a missing sentence, not a missing decision.

Reachable at spec review by reading the 4–5 head threshold against the 2–3 head sticker division. No cross-spec comparison needed.

Fix, applied: `identity-anchor.md:141` now states that carrying the figure the source already shows, described neutrally, is not emphasized adult body characteristics, so the disclosed more-mature read does not by itself trigger the exclusion. Golden 141 asserts the same boundary between its cases B and D. PRD `:144` stands as written.

## C — batch requests permit many automatic corrections

With the bound at one automatic correction per visible result under review, a twelve-sticker set is one request with twelve results and therefore up to twelve automatic regenerations.

The baseline was ambiguous, not wrong. `git show 060b5f6:skills/cast-me/references/identity-anchor.md` line 234: `Perform one automatic correction, and never more than one, using the appropriate path above only when the result is visible and inspectable...`. No scope qualifier, because a request produced one image and the two readings were indistinguishable.

Multi-image requests arrive with the anime spec — `issues/05-produce-consistent-sets-and-multi-angle-batches.md:16` requires every item generated independently from the same fixed root — but every mention of automatic correction in that spec is single-application in scope. It never sets a recovery budget for a multi-image request. The edit-chain PRD pushes the case away at `:128`: `Batch generation and multi-panel sheets, which are specified separately.`

Reviewers, not the specs, made the scope concrete: `ec7f666` first wrote `For each visible result under review... A prior correction of a different result in the same request does not consume this bound`; `86a6577` reverted it to request-wide; `69dbbbb` restored per-result, which is the current `identity-anchor.md:299`; `dd48c64` then amended PRD user story 8 from `I do not want more than one automatic correction` to `...on the same result`.

Verdict: **baseline ambiguity plus reviewer adjudication.** The multiplicity is a direct consequence of a scope the specs left open and the review rounds closed, and no Golden asserts the batch case.

**Evidence gap that must be stated.** `.scratch/edit-chain-depth/PRD.md` was not in git before `69dbbbb`; `git log --follow` on it returns only `69dbbbb` and `dd48c64`, and `git ls-tree 060b5f6 .scratch/edit-chain-depth/` is empty. Git therefore cannot show whether `:128` and the per-result justification in Further Notes existed in the working tree before remediation. What is established: in the tracked history the PRD first appears already carrying the per-result justification, and story 8's qualifier was added afterwards. The spec was amended to match the implementation; the full timeline is unrecoverable from git.

`.scratch/anime-stylized-identity/research.md` holds both halves of the problem without joining them. Its §23 says the one-correction bound `应保留，不应放宽` — should be preserved, not relaxed. Its §4 records field reports of roughly five or six usable images out of eight, with two or three needing individual redos. Together those imply a batch will need several redos, but no one turned that into a budget.

Only visible once both specs are read together: edit-chain draws the boundary, anime makes the case reachable.

Fix, applied: no numeric ceiling. Per-result stands, because a request-wide cap of one means the first failing item of a twelve-sticker set consumes the budget and the other eleven ship defective. What was missing is the systemic case, and the two-stage ADR already implies its remedy: when several items of one set fail on the same defect, every regeneration from that sheet inherits it, so correcting each item individually is futile. `identity-anchor.md:301` now attributes a shared defect to the Character Sheet or locked brief and reports the cause once, Golden Shared Checks and Golden 138 case F assert it, and `docs/architecture.md` carries the branch in the F8 flow.

The per-result bound stays with the edit-chain contract, which already specifies it at `:125` and `:133`. Anime issue 05 claims only the shared-defect case that contract left unclaimed when it deferred batch generation. The shared-defect branch was a human product decision in the grilling session, then recorded in issue 05 and implemented in the same change — not an implementation that later rewrote its spec to authorize itself. An earlier draft of this note claimed issue 05 owned the whole multi-image recovery budget; that overreached the edit-chain bound and was narrowed.

## What this says about the review process

Zero pre-branch logic errors. One spec design error, one adjudicated ambiguity, one false positive.

Implementation review worked. Five remediation commits all fixed real problems, and the fifth pass returned zero hard violations. But it could not have caught B, because that is not an implementation mistake — it is a faithful transcription of contradictory requirements.

The leaks are in three distinct shapes:

1. **Self-contradiction inside one document.** The PRD's 4–5 head threshold against its 2–3 head sticker division, papered over with `offset`. Catchable by reading one file carefully at spec review, and it passed.
2. **An unclaimed handoff between specs.** edit-chain marks batch Out of Scope on the grounds that it is `specified separately`, and the spec that was supposed to pick it up never did. Nobody reviewed the handoff itself.
3. **A convention the repository relies on but never states.** Standards review reported the same non-violation three times because `docs/agents/domain.md` left `_Avoid_` undefined. An unwritten convention does not merely fail to catch defects; it manufactures them, and each false positive cost a remediation round.

C also exposes implementation review's failure mode: faced with a question the specs left open, it adjudicated in place, flip-flopped once, and then edited the PRD so the spec ratified the implementation. That may have produced the right answer, but it means the Spec axis was reviewing a document the implementation had rewritten.

Cheap countermeasures for the next spec set:

- Before implementation, diff sibling issues' acceptance criteria against each other for terms that appear in both with opposite instructions.
- Check every cross-spec Out of Scope line that defers to another spec, and confirm that spec actually claims it.
- Applied: `docs/agents/domain.md` now defines `_Avoid_` semantics, so the glossary stops generating false findings.
- When implementation hits a question the spec never decided, raise it as a spec change before writing prose, rather than deciding and back-filling.
