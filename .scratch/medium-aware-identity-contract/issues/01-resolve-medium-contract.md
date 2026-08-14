Status: ready-for-agent

# Resolve the Medium Contract end to end

## What to build

Implement the core Medium Contract from [`../PRD.md`](../PRD.md) through the existing Identity Anchor owner and the existing Illustration or Other Non-Photographic Output recipe. Resolve one request-wide channel record from the already-locked medium and any explicitly requested deformation, use it consistently before generation and during Identity Review, and keep the photographic path unchanged. Do not add a question, Choice Gate, module, workflow stage, or runtime component.

Land the corresponding Medium Contract ADR and glossary changes from [`../domain-changes.md`](../domain-changes.md) in this ticket. Canonical terms must not describe behavior that the runtime references do not yet implement.

## Acceptance criteria

- [ ] Resolve every Protected Identity Cue to `open`, `transferred`, or `closed` from the locked medium and explicitly requested deformation only. Lighting, framing, occlusion, resolution, and other scene conditions do not participate, and the skill does not infer deformation the user did not request.
- [ ] Resolve and record the channel set once when creative direction locks. Identity Review reads that same record across generation and regeneration; re-resolve only when Style Refresh or Scoped Option Refresh explicitly reopens the medium or requested deformation, and disclose again only when the closed set changes.
- [ ] Keep the structural cue class fixed and medium-independent as specified by the PRD. A cue is open only when the medium renders the person's own quantity, transferred when medium convention governs its shape but it carries recognition, and closed when the medium cannot express it.
- [ ] Keep transferred hair, wardrobe, and styling details owned by Styling and user-changeable even when Identity Review weights them more heavily.
- [ ] Preserve the existing photographic Protected Identity Cue catalog and photographic behavior unchanged.
- [ ] Add the Medium Contract explanation test to oversized-head/body deformation, apparent-age drift, and waxy/plastic/over-smoothed skin handling. Explained locked intent is accepted; unexplained deformation, age change, or surface treatment still fails, including in drawn output.
- [ ] Disclose closed channels before generation in plain visible language only when the resolved contract closes channels protected by the photographic default. The disclosure is a statement, not a gate or question.
- [ ] Never put a closed-channel statement into the production prompt. When a closed channel must be represented, describe positively what the selected medium renders.
- [ ] Judge Identity Review on open and transferred channels only. While any structural channel remains open, recognizability alone remains insufficient. When none remains open, recognition through transferred channels decides completion and thumbnail-size filled-silhouette readability is a hard additional requirement.
- [ ] Keep accepted risk scoped to the channels the resolved contract closes; unrelated open channels remain protected. Keep identity preservation best effort without a score, biometric claim, similarity measure, or guarantee.
- [ ] Update `skills/cast-me/references/identity-anchor.md` for channel resolution, disclosure, prompt constraints, medium preconditions, and review behavior.
- [ ] Update `skills/cast-me/references/composition-director.md` so the non-photographic recipe applies the resolved contract and positive medium language without creating a new recipe, stage, or option system.
- [ ] Add `Medium Contract` to `CONTEXT.md`, modify `Protected Identity Cue` and `Identity Review` exactly as required by `domain-changes.md`, and add `docs/adr/0007-resolve-identity-constraints-against-selected-medium.md` in the same change as the runtime references.
- [ ] Synchronize `docs/architecture.md` with the new runtime behavior, owner/routing description, recounted sizes for every changed asset, 36 canonical terms, 7 ADRs, and Golden 1–126 coverage. `Uneven Stylization` remains for ticket 02.
- [ ] Do not add deformation tiers, numeric proportions, style axes, character sheets, edit-chain rules, another module, or any other downstream-spec behavior.

## Verification

- [ ] Modify the `Shared checks` Identity Review entry in `evals/golden-conversations.md` so it reads the resolved Medium Contract and preserves the any-open-structural-channel boundary.
- [ ] Add Golden 122, `Medium Contract resolves once and discloses only closed channels`, covering one request-wide record, closed-channel disclosure without a gate, no disclosure when nothing closes, refresh-driven re-resolution only when medium or deformation reopens, and the absence of closed-channel statements from the production prompt.
- [ ] Add Golden 123, `Requested drawing deformation is intent, not a blanket exemption`, pairing requested strong deformation and its younger read with unexplained deformation and age drift that must still fail. Include at least one non-anime non-photographic medium.
- [ ] Add Golden 124, `Surface treatment follows the selected medium`, pairing valid flat cel treatment with photorealistic waxy or over-smoothed skin that must still fail.
- [ ] Add Golden 125, `Open structural channels keep cue-level review strict`, covering an equal-proportion drawing and the exactly-one-structural-channel-open boundary. Assert cue-level review, recognizability remaining insufficient, and no silhouette-floor substitution.
- [ ] Add Golden 126, `Transferred channels and thumbnail silhouette govern no-open review`, covering closed structural channels, weighted hairstyle/eye-shape/distinctive-mark/wardrobe recognition, no failure for absent closed cues, and failure when the full-size figure is recognizable but its filled silhouette is unreadable at thumbnail size.
- [ ] Extend `Accepted identity risk stays scoped` with a drawn case proving that accepted closed channels do not waive unrelated open channels.
- [ ] Keep `Medium-adapted CG First-Pass Finish`, `Final quality is shared across media`, `Editorial, commercial, avatar, and illustration adapt impact`, `Identity Review reports visible cue drift only`, `Close crop to full-body proportion recovery`, `Identity preservation remains best effort`, `Clean presentation does not pass Identity Review`, and `Clean cosplay execution cannot mask identity-wide drift` unchanged as controls.
- [ ] Review the new and modified Golden behavior directly against `skills/cast-me/references/identity-anchor.md` and `skills/cast-me/references/composition-director.md`.

## Blocked by

- None — can start immediately. This ticket has no external blocker.
