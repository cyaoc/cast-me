Status: ready-for-agent

# Establish Fixed-Root Recovery Across Revisions

## What to build

Implement the fixed-root recovery behavior from [`../PRD.md`](../PRD.md) through the existing Identity Anchor owner and composition guidance. Make regeneration from the request's fixed root the default recovery, while preserving surgical edit as the proportionate exception for one coherent local defect on a freshly generated ordinary result and preserving direct edit when the user explicitly asks for it.

Answer freshness from the current exchange and the operation's actual image inputs rather than from a counter or reconstructed history. Treat a result as freshly generated only when CastMe produced it in the current exchange, can still see it, and no image input to that operation was itself generated. If provenance is unavailable or indeterminate, recommend regeneration.

This ticket must not change the paragraph governing the bounded single automatic correction. Ticket 02 owns that paragraph and its cross-spec sequencing.

## Acceptance criteria

- [ ] Define the request's fixed root as the image inputs every generation for the request starts from and which do not grow across revisions: the Primary Identity Anchor, any required reliable supporting person reference, and any locked produced artifact reused by every image in the request.
- [ ] Restate regeneration inputs as the complete fixed root plus the locked brief, excluding the failed result. Carry every accumulated scene, Shot, camera, pose, Styling, lighting, finish, exact-text, background, output, and accepted-risk lock rather than restarting the creative flow.
- [ ] State freshness as a property of the producing operation's complete image-input set. The Primary Identity Anchor merely appearing among those inputs is not sufficient when another input was generated.
- [ ] Make regeneration the default recovery and surgical edit the exception for one coherent local defect on a freshly generated ordinary result that remains reliable evidence.
- [ ] When a user requests another change to a result that is not freshly generated, recommend regeneration from the fixed root with all accumulated locks, but keep direct edit available when explicitly requested.
- [ ] Preserve the existing explicit-edit inputs: the result being edited plus the Primary Identity Anchor. Do not add a locked produced artifact whose design is already present in that result.
- [ ] Never edit a locked produced artifact that later images reuse. Regenerate that artifact from its fixed root even when it is freshly generated and otherwise has one coherent local defect.
- [ ] If the current exchange no longer establishes how a result was produced, regenerate without claiming knowledge of its history. Add no counter, ledger, scratchpad, hook, service, file, database, or read-state tracker.
- [ ] For a requested series, generate each image from the fixed root and locked brief rather than from the preceding output. Preserve Look Continuity through the written brief.
- [ ] Do not use denoising, cleanup, sharpening, generic quality-improvement instructions, an earlier-image reminder, a visual dirtiness judgment, a quality metric, or a numeric edit threshold as recovery.
- [ ] Never claim that noise, artifacts, dirtiness, or degradation were detected or removed, and never show a count, tally, or remaining-edits figure.
- [ ] Preserve Structural Scale Failure recovery, unavailable-anchor reattachment, passing-first-result behavior, both existing recovery operations, and all existing review conditions.
- [ ] Update `skills/cast-me/references/identity-anchor.md` and `skills/cast-me/references/composition-director.md` only. Do not add a term, glossary change, ADR, module, agent, workflow stage, gate, runtime component, user-visible control, or medium-specific rule.
- [ ] Do not alter the bounded single-automatic-correction paragraph; leave its operation restriction to ticket 02.

## Verification

- [ ] Modify the `Shared checks` likeness-complaint routing entry and Golden 107, `Coherent local identity defects stay surgical`, in `evals/golden-conversations.md`; review both directly against `skills/cast-me/references/identity-anchor.md` so that freshly generated ordinary results remain surgical while regeneration becomes the default.
- [ ] Add Golden 128, `Later revisions restart from the fixed root`, and review it directly against `skills/cast-me/references/identity-anchor.md`; cover an already-edited result, all accumulated prompt locks, a regeneration recommendation, and direct edit remaining available on explicit request.
- [ ] Add Golden 129, `Generated inputs do not qualify a result as fresh`, and review it directly against `skills/cast-me/references/identity-anchor.md`; cover a result produced from the Primary Identity Anchor plus a locked produced artifact, prove Anchor membership alone is insufficient, and preserve the explicit-edit input boundary.
- [ ] Add Golden 130, `Locked produced artifacts are regenerated`, and review it directly against `skills/cast-me/references/identity-anchor.md`; cover a freshly generated reusable artifact failing with an otherwise surgical defect and require regeneration from its fixed root.
- [ ] Add Golden 131, `Unknown provenance defaults to regeneration`, and review it directly against `skills/cast-me/references/identity-anchor.md`; cover unavailable production history without a history claim, counter, ledger, or edit-count promise.
- [ ] Add Golden 132, `Multi-round and series work do not chain generated edits`, and review it directly against `skills/cast-me/references/identity-anchor.md` and `skills/cast-me/references/composition-director.md`; cover at least three requested changes and a related-image series, with each unrequested operation starting from the fixed root and continuity carried by the brief.
- [ ] Add Golden 133, `Cleanup requests restart instead of judging degradation`, and review it directly against `skills/cast-me/references/identity-anchor.md` and `skills/cast-me/references/composition-director.md`; cover a cleanup or sharpening request without a cleanup edit, appearance verdict, removal claim, metric, numeric threshold, or remaining-edits figure.

## Blocked by

- None — can start immediately.
- Independent of `.scratch/medium-aware-identity-contract/issues/`; it may proceed in parallel with that specification because this ticket does not change the bounded single automatic correction.
