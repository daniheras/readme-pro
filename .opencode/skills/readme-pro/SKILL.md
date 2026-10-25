---
name: README Pro
description: Assess any project and create or upgrade its README at the right intensity - minimal, standard, or showcase. Use for EVERY README task by default - when the user mentions README, readme.md, docs polish, or repo front page, wants to add badges, banners, demo GIFs, or screenshots, is about to open-source a project, or complains their repo looks plain - even if they never say the word README. After assessing, loads readme-pro-low, readme-pro-medium, or readme-pro-high.
---

# README Pro — route to the right README

A README should match the project's philosophy, not a maximal template. A JSON
parser does not need a hero GIF; a terminal theme without one is missing the
point. This skill assesses the project, picks an intensity level, and executes
the matching recipe.

## Workflow

1. **Assess the project** before writing anything:
   - **What is it?** Library, CLI, app, TUI, theme/dotfiles, framework, config
     collection, docs site.
   - **First 10 seconds:** what must a visitor learn immediately, and what is
     the action that follows (install? star? contribute?).
   - **Visual identity:** does the project have a UI, or is aesthetics part of
     the product (themes, TUIs, desktop rices)? Does it already have a logo,
     palette, or brand accent?
   - **Repo scan:** existing README, LICENSE, CI config (badge eligibility),
     `screenshots/` or `docs/` assets, package metadata, git remote.
   - **Tone:** is the project playful (community tool, rice, theme) or sober
     (enterprise library, infrastructure)?
2. **Pick a level** with the signal table below. Tell the user the level and
   the one-line reason; let them override.
3. **Load the recipe** for that level: call the `skill` tool with
   `readme-pro-low`, `readme-pro-medium`, or `readme-pro-high` and follow it.
   If that skill is not installed, use the fallback cheat sheet below.
4. **Creating vs improving:** if a README already exists, audit it against the
   recipe first — what stays, what is missing, what contradicts the level —
   show the gap list, then rewrite.
5. **Never fabricate.** No badge for CI that does not exist, no license badge
   without a LICENSE file, no screenshots of features that cannot run.
   Propose, don't invent. A README that lies gets caught on the first clone.

## Level signals

| Signal | Points to |
|---|---|
| Plain library, CLI, or internal tool; readers arrive to read, not to admire | LOW |
| General app, library, or tool; professional context; has CI or releases | MEDIUM |
| UI, TUI, theme, dotfiles, rice — look and feel *is* the product | HIGH |
| Visual identity already present in the repo (themes, colors, images) | HIGH |
| Existing README is already styled and the user wants it upgraded | HIGH |
| User asks for "something simple/clean" | LOW or MEDIUM |
| User asks for "wow / chulo / showcase" | HIGH |

Tie-breaker: ask one question describing the two candidate levels in a line
each, and let the user pick.

## Fallback cheat sheet (only if the level skills are unavailable)

- **LOW — documentation-first (Yegor school).** Title + one-paragraph
  what/why, exact install commands, one real usage example, configuration only
  if non-obvious, license line. No badges, no images, no TOC, no emoji, no
  adjectives.
- **MEDIUM — front door (makeareadme / thoughtbot school).** Pitch of three
  sentences or fewer, at most four informative badges (CI, release, license,
  platform), one screenshot if there is UI, features, requirements, install,
  usage with real examples, configuration table, docs link, contributing,
  license. TOC only when long.
- **HIGH — showcase (doomemacs / sniffnet school).** Identity first: derive
  the palette from the project itself. Banner, consistent badge row, hero demo
  (GIF via vhs for terminal projects), TOC, install table, gallery, community
  extras (LICENSE, CONTRIBUTING, issue templates), footer.

## Universal rules (every level)

- Order by reader intent: what & why → install → usage → details.
- The README is a spec: writing it early clarifies the project
  (README-driven development).
- Every section must earn its place; delete ceremony sections.
- Deep internals belong in ARCHITECTURE.md or docs/, linked from the README.
- Real examples only: commands the reader can run, output that is real.
- Match the project's tone; sober by default, personality where the project
  has one.
