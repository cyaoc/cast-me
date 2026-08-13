# Domain Docs

This is a single-context repository.

Before exploring or changing the project:

- Read the root `CONTEXT.md` and use its canonical vocabulary.
- Read relevant ADRs under `docs/adr/` when that directory exists.
- Surface any conflict with an ADR instead of silently overriding it.

If a needed domain term is missing, use the domain-modeling workflow rather than inventing a competing synonym.

## Reading `_Avoid_`

Every `CONTEXT.md` entry ends with an `_Avoid_` line. It constrains only how that entry may be named — do not use these words to mean this term. It is not a repository-wide ban on the words themselves, and a phrase listed under one entry may be the correct, load-bearing wording for its own concept elsewhere.

Entries carry two kinds of wording: worse synonyms for the term, such as `Style level` under `Deformation Tier`, and adjacent concepts that must not be collapsed into it, such as `stylization intensity`, which names a separate production decision. Do not read the second kind as a defect because the phrase appears often in runtime prose.

A phrase listed under `_Avoid_` earns a canonical term of its own only when the vocabulary would otherwise lack the concept, not because it is used frequently.
