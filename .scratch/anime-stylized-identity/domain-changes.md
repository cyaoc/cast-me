Status: ready-for-agent

# Domain Changes for Anime and Chibi Character Generation

These are the glossary and decision-record changes that `PRD.md` in this directory depends on. As with the medium-aware identity contract, they are staged here rather than applied directly, because `docs/architecture.md` treats a contradiction between canonical terms and runtime behavior as drift. They land with the implementation.

These changes assume the medium-aware identity contract has already landed, since `Deformation Tier` is defined in terms of the `Medium Contract` that specification introduces.

## ADR

The ADR test is met. The two-stage flow is hard to reverse once every application depends on the sheet. It is surprising without context, because a reader will find an extra generation happening before the one the user asked for. And it is a real trade-off against the obvious alternative, which is what the skill does today.

New file `docs/adr/0008-anchor-drawn-characters-to-a-locked-character-sheet.md`:

```md
# Anchor drawn characters to a locked Character Sheet

Drawn characters are produced in two stages. One Character Sheet locks the drawn design, and every later image of that character is generated from the sheet together with the Primary Identity Anchor, both supplied as actual image inputs. Applications branch from the sheet and never take another application as an input.

CastMe does not generate each drawn image directly from the person reference with a repeated list of features to preserve. That is the current behavior, and it cannot hold a character across images, because consistency of a recurring character across separate generations is a documented model limitation rather than a prompting shortfall. Generating each image from the previous one would hold the character but would push every additional image further along the editing chain, eroding the small marks that carry recognition once deformation flattens body differences. The two-stage flow spends one extra generation once and keeps every delivered image two steps from the user's photograph however many images are produced.

The second step is what the drawn medium pays for that. A photographic result is generated from the person's photograph alone, so a proportionate local repair costs one round trip and the recovery rules permit one. An application carries the sheet as a generated image input, so it already holds a round trip before anything is repaired, and editing it would be the drawn equivalent of editing an edit. Failing applications are therefore regenerated from the sheet and the anchor rather than surgically edited, and the automatic correction never edits one on its own initiative. The same reasoning is stricter on the sheet itself, which the freshly-generated test would otherwise admit: it is the one artifact everything downstream is built from, so a repair made to it is inherited by every image in the set instead of being confined to the one image that failed. The sheet is regenerated too. A user who asks for a local fix anyway still gets one; only the skill's own initiative is constrained.
```

## Glossary

### New term: Character Sheet

Insert after `Primary Identity Anchor`, whose role it must not be confused with:

```md
**Character Sheet**:
The locked drawn design of a person — proportions, face construction, hair, eye rendering, wardrobe, palette, and line and shading treatment — produced once and supplied as an image input to every later image of that character. It governs how the person is drawn and never serves as identity evidence.
_Avoid_: Character anchor, identity anchor, style reference
```

### New term: Deformation Tier

Insert after `Medium Contract`, which it resolves:

```md
**Deformation Tier**:
The selected degree of drawn deformation, presented as three fixed semantic labels whose concrete proportions vary with the intended use. It resolves the request's Medium Contract and therefore decides which identity channels remain open, which carry recognition in their place, and which are disclosed as closed.
_Avoid_: Style level, chibi mode, stylization intensity
```

Deformation Tier and stylization intensity are separate and easy to confuse. The tier is about proportion and shape; stylization intensity is about how far the rendering moves from photographic. A conservative tier can be rendered at high intensity, and a strong tier can be rendered at low intensity. Stylization intensity stays an ordinary production dimension described in the PRD rather than a canonical term, because it names a degree rather than a concept the vocabulary would otherwise lack.

## Baseline counts

`docs/architecture.md` records asset sizes that these changes invalidate. Update them when the changes land, counting from the state after the medium-aware identity contract has landed:

- `CONTEXT.md` gains two terms, reaching 39 counting the two added by the medium-aware identity contract; recount the word total.
- `docs/adr/` reaches 8 ADRs, including the one added by the medium-aware identity contract.
- `golden-conversations.md` currently records 121 scenarios; recount after both specifications' scenarios are added.
