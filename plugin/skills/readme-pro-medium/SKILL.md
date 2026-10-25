---
name: README Pro — Medium
description: Write or upgrade a README to the standard professional form - pitch, truthful badges, screenshot when there is UI, install, usage, configuration, contributing, license. Choose this level when the user wants a trustworthy professional README for a public-facing app, library, or tool, or asks to fix hype, broken install steps, or add a proper badge row. Use instead of readme-pro when the level is already known.
---

# Level: MEDIUM — the front door

Philosophy: the README is the project's front door (makeareadme, thoughtbot).
A visitor should learn what and why within one screen and reach a working
install within two. Professional and informative, not loud — trust is built
with precision, not volume.

## Structure (in order)

1. `# Name` + pitch: what it does, the key differentiator, who it is for.
   Three sentences or fewer.
2. **Badge row** — at most four badges, and each must *inform*: build/CI
   status, latest release, license, primary platform or runtime. One
   consistent style (flat-square). Drop any badge that cannot be backed by
   reality.
3. **Screenshot** — only if the project has a visible UI. One image, framed
   and legible; stored in the repo (`docs/` or `screenshots/`) and referenced
   by relative path.
4. `## Features` — 3–7 bullets, capability-oriented ("X does Y"), no fluff
   adjectives.
5. `## Requirements` — runtime and OS versions as a short list.
6. `## Install` — numbered steps or short code blocks; per-platform variants
   only when they truly differ.
7. `## Usage` — the minimal working example first, then the most common
   second use.
8. `## Configuration` — a table: option | default | description.
9. `## Documentation` — link out (wiki, docs site, ARCHITECTURE.md) instead
   of inlining depth.
10. `## Contributing` — two or three lines: dev setup, where issues go, PR
    expectations.
11. `## License` — SPDX identifier + link to the file.

Add a TOC only when the README is long (roughly more than 8 sections or 250
rendered lines).

## Pitch example

**Bad:** "Snipshot is a powerful, blazingly fast screenshot tool."
(powerful how? for whom?)

**Good:** "Snipshot frames screenshots with rounded corners, a border, and a
drop shadow, ready for READMEs and docs. One command, pure ImageMagick."

## Rules

- Badges carry information, never decoration; verify each badge target exists.
- Every code block must be runnable as written.
- Tables over paragraphs for options and platform variants.
- Link, don't inline: changelogs, architecture, full docs.
- Consistent heading style (sentence case everywhere).

## If improving an existing README

Audit against the structure: keep working content, flag missing sections,
list what moves out to docs/. Show the gap list, then rewrite.

## Checklist

- [ ] Pitch lands what + differentiator + audience in three sentences or fewer
- [ ] Every badge corresponds to something real (CI config, release, LICENSE)
- [ ] Screenshot framed, legible at 100%, stored in-repo with a relative path
- [ ] Install reaches a working state on the primary platform
- [ ] Usage example runs as-is
- [ ] Configuration documented in a table
- [ ] Contributing and License present
- [ ] No marketing adjectives; tone professional
