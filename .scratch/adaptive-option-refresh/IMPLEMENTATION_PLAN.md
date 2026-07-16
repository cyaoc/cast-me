# Scoped Option Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make every existing creative choice gate refreshable within its own scope without disturbing identity, explicit locks, or unrelated choices.

**Architecture:** Keep the coordinator as the routing authority, add one progressively loaded reference for the shared refresh contract, and leave each owner responsible only for its visible freshness signature. Golden Conversations remain the single behavioral seam.

**Tech Stack:** Markdown Skill contract, Markdown behavior evaluations, existing skill-package validator.

## Global Constraints

- Preserve the existing Style Refresh and its 3/6 Direction Signature rule.
- Use three concrete A/B/C choices plus permanent `D) Custom` for visible refreshable gates.
- Keep all histories conversation-local; add no runtime code, dependency, persistence, or service.
- Ask a compact scope question only when no explicit, active, or recent refresh target exists.
- Do not modify unrelated dirty files.

---

### Task 1: Add the failing behavior contract

**Files:**
- Modify: `evals/golden-conversations.md`

**Interfaces:**
- Consumes: The PRD's routing, history, lock, exhaustion, and boundary rules.
- Produces: User-visible scenarios used for red/green review of the Skill contract.

- [ ] **Step 1: Add shared checks and golden scenarios**

Add checks for scoped routing, per-area Shown Option history, two-part Fresh Option difference, permanent Custom, and fixed focused gates. Add scenarios for explicit target precedence, active/recent scope, ambiguous fallback, pending focused gates, partial lock preservation, three repeated batches for each refreshable owner, Custom, delegation, exhaustion, and Perspective Intent.

- [ ] **Step 2: Verify the new scenarios fail against the current Skill**

Run:

```bash
rg -n 'Route any request for another batch|Scoped Option Refresh|Shown Option|Fresh Option' skills/cast-me/SKILL.md skills/cast-me/references
```

Expected red evidence: the coordinator still routes any another-batch request to Style Refresh, and no generic scoped contract exists.

---

### Task 2: Implement the smallest shared refresh contract

**Files:**
- Create: `skills/cast-me/references/scoped-option-refresh.md`
- Modify: `skills/cast-me/SKILL.md`
- Modify: `skills/cast-me/references/composition-director.md`
- Modify: `skills/cast-me/references/styling-performance.md`
- Modify: `CONTEXT.md`

**Interfaces:**
- Consumes: Existing decision state, owner boundaries, Style Refresh, standard decision format, and focused risk gates.
- Produces: One routing/history/exhaustion contract plus owner-local visible signatures.

- [ ] **Step 1: Add the shared contract**

The new reference must define this routing order:

```text
explicit creative target
otherwise unresolved visible gate
otherwise most recent refreshable gate
otherwise explicit Style Refresh wording
otherwise one compact scope question
```

It must keep per-area Shown Option history, record presented A/B/C plus adopted Custom and delegated choices, require two visible signature differences outside Creative Direction, preserve unrelated values and Explicit Locks, reopen only target-area Derived Locks, and stop honestly at Refresh Exhaustion.

- [ ] **Step 2: Replace the broad coordinator trigger**

Update the coordinator to load the shared reference before presenting or replacing any refreshable creative gate, track the most recent refreshable gate after selection or generation, and use generic lock provenance. Keep focused gates unresolved when the user temporarily refreshes a named creative area.

- [ ] **Step 3: Add owner-local signatures**

Add these visible signatures without creating catalogs:

```text
Decisive Moment: event/action; tension; story evidence; first impression
Shot: scale/cutoff; viewpoint/distance/projection; placement; spatial/background relationship
First-Pass Finish: feeling; lighting/contrast; color relationship; face/material treatment; texture
Layout: structure; subject/text placement; safe areas/readability; variants
Styling: silhouette/layers; materials; accessories; grooming; props
Performance: action/body direction; expression/mouth; gaze; hands/prop interaction; energy
```

Mark existing Shot and professional-headshot Styling menus as example shapes rather than reusable fixed menus. Keep Perspective Intent as a stable classification whose concrete expression refreshes through Shot.

- [ ] **Step 4: Run the affected golden review**

Read the new scenarios against the coordinator and owner references. Expected: every scenario's routing, visible difference, lock inheritance, and boundary has an explicit supporting rule; no scenario relies on exact prose.

---

### Task 3: Validate, review, and commit

**Files:**
- Verify: all scoped production and behavior files
- Publish: `.scratch/adaptive-option-refresh/PRD.md`
- Publish: `.scratch/adaptive-option-refresh/IMPLEMENTATION_PLAN.md`

**Interfaces:**
- Consumes: Completed Skill contract and golden scenarios.
- Produces: A validated, reviewed commit on the current branch.

- [ ] **Step 1: Validate the Skill package**

Run the existing validator. If PyYAML is unavailable, create a throwaway `uv` environment under `/private/tmp` and install it there; do not modify project or global Python state.

- [ ] **Step 2: Run the full golden audit and whitespace check**

Require zero golden failures and run:

```bash
git diff --check
```

- [ ] **Step 3: Commit the scoped work**

Stage only the adaptive option refresh PRD/plan, glossary, Skill contract, owner references, and golden conversations. Commit with:

```bash
git commit -m "feat: add scoped option refresh"
```

- [ ] **Step 4: Run two-axis code review**

Review the committed diff against the pre-implementation fixed point for repository standards and PRD compliance. Fix findings surgically, revalidate, and commit only if needed.
