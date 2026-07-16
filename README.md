# CastMe

CastMe is a Codex skill for turning a person reference image into a polished final image while preserving the person's visible identity as much as possible.

It is meant for person-centered outputs such as portraits, professional headshots, social avatars, cinematic posters, editorial images, commercial visuals, and CG or game key art. The skill acts like a visual director: it keeps a complete production checklist, but asks only the choices that matter for this image, explains them through visible examples, and translates them into professional camera, lighting, styling, performance, and delivery direction.

## Install in Codex

This repository is a standalone Codex skill, not a marketplace plugin. With Codex installed, run the bundled skill installer against this GitHub URL:

**macOS / Linux**

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --url https://github.com/cyaoc/cast-me/tree/main/skills/cast-me
```

**Windows PowerShell**

```powershell
python "$HOME\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --url https://github.com/cyaoc/cast-me/tree/main/skills/cast-me
```

The installer places it in `~/.codex/skills/cast-me` and stops if that destination already exists.

### Update

Updating replaces the installed copy, including any local changes made inside it.

**macOS / Linux**

```bash
rm -rf ~/.codex/skills/cast-me
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --url https://github.com/cyaoc/cast-me/tree/main/skills/cast-me
```

**Windows PowerShell**

```powershell
Remove-Item -Recurse -Force "$HOME\.codex\skills\cast-me"
python "$HOME\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --url https://github.com/cyaoc/cast-me/tree/main/skills/cast-me
```

Start a new Codex session after installing or updating, then invoke `$cast-me`.

## How to Use

Attach a person image and invoke the skill:

```text
$cast-me [Image] Create a cinematic poster with the title "MIDNIGHT SIGNAL"
```

You can also describe the output directly:

```text
$cast-me [Image] Make this suitable for a LinkedIn profile photo while keeping the same person
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

This resolves ordinary creative choices. If the reference lacks target-critical body, angle, or performance evidence, the skill may still ask one focused coverage/risk choice unless you explicitly accept inference for that gap.

## How the Guidance Adapts

The eight production dimensions remain an internal checklist, not an eight-question form. Practical images take a shorter route; story-heavy, exact-text, full-body/action, or series work keeps more distinct decisions. There is no target question count: the skill stops when every user-visible tradeoff that could materially change the result is resolved, irrelevant, or explicitly defaulted.

Each question changes one visible part of the result. Creative direction chooses the premise and decisive moment; shot direction chooses the frame and space; styling chooses what the person wears or holds; performance chooses action, expression, gaze, and hands; lighting/color chooses how the moment feels. Preview details are not silently locked.

For example, instead of asking for a specific lens choice, the skill may offer:

- closer portrait - face dominates and the background softens
- waist-up environmental portrait - face stays readable while the setting carries context
- full-body environmental frame - the world carries more story, with higher body-reference risk

Professional capture details are then resolved internally as visible effects. You do not need camera bodies, lens models, ISO, aperture, shutter speed, Kelvin values, or lighting equipment; requested numbers are treated as approximate aesthetic cues, not a guaranteed physical exposure plan.

Strong camera perspectives remain valid choices. When perspective matters, the skill distinguishes:

- physically strong perspective - visible near/far enlargement and foreshortening are intentional
- strong viewpoint with controlled projected proportions - keep spatial impact while restraining head/body exaggeration
- proportion-first perspective - reduce projection drama for familiar body scale

These are generated from the requested theme, not fixed angle or lens presets. A selected camera is not silently downgraded by identity safeguards. The skill separately checks reference coverage, underlying anatomy, projected proportions, pose geometry, and identity readability at the target face angle.

## Useful Request Patterns

```text
$cast-me [Image] Create a natural-light portrait
```

```text
$cast-me [Image] Create a vertical fantasy key art image, keep the original outfit and jewelry
```

```text
$cast-me [Image] Create a 1:1 social avatar, clean background, no text
```

```text
$cast-me [Image] Create a movie poster titled "MIDNIGHT SIGNAL"; keep the person recognizable
```

Typical routes:

- professional avatar: use if missing -> shot/body framing (optionally with an explicit avatar canvas) -> styling if material -> performance -> lighting/color
- directed portrait: creative direction and moment -> shot/perspective -> styling if material -> performance -> lighting/color
- cinematic poster or key art: direction and moment -> shot/perspective -> styling/props -> aspect/text -> performance -> lighting/color, plus one coverage/risk gate only when needed

## What to Specify

A person reference plus the intended image/use and the feeling you want is enough to begin. Include any of these optional details when you already know them:

- output type: portrait, headshot, poster, editorial image, avatar, commercial visual, CG/key art
- aspect ratio or platform: 1:1 avatar, 4:5 social post, 9:16 vertical poster, 16:9 hero image
- wardrobe/accessories: keep, simplify, polish, or replace
- pose and expression
- perspective intent: physically strong exaggeration, strong viewpoint with controlled proportions, or proportion-first
- lighting and color palette
- exact text, or no text
- things to avoid

## Review Changes

Use [the golden conversations](evals/golden-conversations.md) to check adaptive question depth, decision inheritance, risk gates, delivery, and surgical revisions.
