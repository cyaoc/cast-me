# Identity Image Director

Identity Image Director is a Codex skill for turning a person reference image into a polished final image while preserving the person's visible identity as much as possible.

It is meant for person-centered outputs such as portraits, professional headshots, social avatars, cinematic posters, editorial images, commercial visuals, and CG or game key art. The skill acts like a lightweight visual director: it asks only for missing production-critical choices, gives concrete options, and lets you accept recommended defaults when you want to move quickly.

## Install in Codex

From this repository:

```bash
mkdir -p ~/.codex/skills
cp -R skills/identity-image-director ~/.codex/skills/
```

Then start a new Codex session, or reload Codex if your environment supports skill reloads.

## How to Use

Attach a person image and invoke the skill:

```text
$identity-image-director [Image] Create a cinematic poster with the title "MIDNIGHT SIGNAL"
```

You can also describe the output directly:

```text
$identity-image-director [Image] Make this suitable for a LinkedIn profile photo while keeping the same person
```

The skill will ask for missing production-critical choices one at a time. Reply with the option letter, or add overrides in the same message:

```text
B
```

```text
B + use recommended defaults
```

```text
C + 4:5 crop + keep the headwear + soft smile + no text
```

If you want the skill to stop asking questions and choose the rest, say:

```text
use recommended defaults
```

or:

```text
you decide
```

## Useful Request Patterns

```text
$identity-image-director [Image] Create a natural-light portrait
```

```text
$identity-image-director [Image] Create a vertical fantasy key art image, keep the original outfit and jewelry
```

```text
$identity-image-director [Image] Create a 1:1 social avatar, clean background, no text
```

```text
$identity-image-director [Image] Create a movie poster titled "MIDNIGHT SIGNAL"; keep the person recognizable
```

## What to Specify

Include any of these details when you already know them:

- output type: portrait, headshot, poster, editorial image, avatar, commercial visual, CG/key art
- aspect ratio or platform: 1:1 avatar, 4:5 social post, 9:16 vertical poster, 16:9 hero image
- wardrobe/accessories: keep, simplify, polish, or replace
- pose and expression
- lighting and color palette
- exact text, or no text
- things to avoid
