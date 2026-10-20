# Issue Labels

## Triage states

| Canonical role | GitHub label | Meaning |
| --- | --- | --- |
| `needs-triage` | `needs-triage` | Maintainer needs to evaluate this issue |
| `needs-info` | `needs-info` | Waiting on reporter for more information |
| `ready-for-agent` | `ready-for-agent` | Fully specified and ready for an agent |
| `ready-for-human` | `ready-for-human` | Requires human implementation |
| `wontfix` | `wontfix` | Will not be actioned |

## Triage categories

| Canonical role | GitHub label | Meaning |
| --- | --- | --- |
| `bug` | `bug` | Something is broken |
| `enhancement` | `enhancement` | New feature or improvement |

Each issue processed by triage carries exactly one category and one state. Specs and tickets produced by `to-spec` or `to-tickets` use `ready-for-agent` without an additional triage pass.

## Wayfinder types

| GitHub label | Meaning |
| --- | --- |
| `wayfinder:map` | Shared map of decisions for an effort |
| `wayfinder:research` | Research question that a decision depends on |
| `wayfinder:prototype` | Question requiring a concrete prototype |
| `wayfinder:grilling` | Decision requiring a conversation with the user |
| `wayfinder:task` | Work needed before a decision can be made |

Wayfinder child issues carry one type label and belong to a map. Open/closed state records resolution; assignment records a claim. These types do not replace triage states. See `issue-tracker.md` for relationships and blocking.

## Historical research

`research` is a repo-specific label for imported research, specs, and implementation records. These issues close once their source content is archived and verified. Archived `Status:` lines do not assign live triage states, and closing an archive does not certify its original implementation or acceptance.

Use `wayfinder:research` only for research decision tickets within a Wayfinder map.
