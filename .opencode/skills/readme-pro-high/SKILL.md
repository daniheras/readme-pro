---
name: README Pro — High
description: Build a showcase README - banner, badge row, hero demo GIF or framed screenshot, TOC, gallery, community extras. Choose this level whenever look and feel is part of the product (UIs, TUIs, themes, dotfiles, rices) or the user wants a wow-factor front page ("chulo", impressive, eye-catching). Use instead of readme-pro when the level is already known.
---

# Level: HIGH — showcase

Philosophy: the README is part of the product experience (doomemacs,
sniffnet). Identity first: colors, imagery, and tone derive from the project
itself — a theme's own palette, a TUI's look, a brand accent. Decoration that
could belong to any project is wasted decoration; the point is that the front
page *feels like* the project before a single line is read.

## Identity example

**Bad identity:** generic blue shields + a stock lightbulb icon on a theme
whose palette is graphite + #D71921.

**Good identity:** badge row and banner reuse the theme's own colors; the
accent shows up in the platform badge; the hero GIF is recorded with the
theme applied.

## Step 1 — Find the identity

- **Theme / dotfiles:** use the project's own palette (primary accent,
  background) for the banner and badge colors.
- **TUI / app:** screenshot or record the real UI; never mock it.
- **No visual identity yet?** Propose one (accent color + wordmark or
  monogram) and confirm with the user before building assets.

## Tool tiers — the zero-dependency guarantee

The README must be deliverable on any OS with nothing installed. Never block
on a tool; climb tiers only when the tool is actually there:

- **Tier 0 — always available, no installs:** hand-authored SVG assets
  (banner, palette strip — SVG is plain text, write it), shields.io badge
  URLs (a web service), tables, and centered HTML. This alone can carry a
  complete showcase README.
- **Tier 1 — if ImageMagick is present** (`magick -version`): frame real
  screenshots with `scripts/frame-image.sh`. If it is missing, ship the raw
  screenshot — it renders fine, just plainer.
- **Tier 2 — user opt-in only:** vhs terminal GIFs (needs ttyd + ffmpeg).
  Offer it; if the user installs it, record the hero. Otherwise ship the
  `.tape` as the documented pipeline with the hero slot left wired for the
  generated GIF.

## Step 2 — Structure

1. **Banner** — centered; hand-authored SVG wordmark (Tier 0) or rendered
   image; matches the palette.
2. **Badge row** — one consistent style (flat or flat-square); platform badge
   ("made for X"), version, license, CI. Badge tokens may carry the accent
   color. shields.io URLs make this Tier 0.
3. **Hero demo** — the best available in this order: recorded GIF (Tier 2,
   via vhs with a versioned `.tape` — see `references/tools.md`), framed
   screenshot (Tier 1, via `scripts/frame-image.sh`), raw real screenshot or
   Tier 0 visual (always works). The hero sits above the fold; install must
   not drown below it.
4. **Nav / TOC** — linked section list right after the hero.
5. `## Features` — bolded lead-ins, capability-oriented.
6. `## Install` — a table for variants/platforms; keep it scannable.
7. `## Usage` — real examples; for TUIs, keybinding tables.
8. `## Gallery` — two-column table of framed screenshots or GIFs.
9. `## FAQ` — the questions that actually repeat in issues.
10. `## Community` — LICENSE, CONTRIBUTING.md, issue templates; these raise
    the repo's community-standards score.
11. **Footer** — socials, related projects, a "built with" line if
    meaningful.

## Rules

- The prose stays sober even when the visuals are rich; personality allowed,
  noise not.
- Assets are versioned in the repo (`docs/`, `assets/`) and referenced by
  relative path.
- **Screenshots must be real captures.** Rendering HTML mocks and presenting
  them as screenshots is fabrication, however faithful the render. When no
  capture is possible, use the placeholder pattern: a commented hero/gallery
  block ready to uncomment, plus the documented pipeline (`.tape`, capture
  scripts) so anyone can produce the real asset later.
- Hero GIF at roughly 5 MB or less; prefer MP4/WebM above that; optimize
  frames (see `references/tools.md`).
- Badges must be real (existing CI, releases, license).
- Check mobile: banner scales, tables wrap, gallery images have width caps.

## References

- `references/tools.md` — vhs, shields.io, stats cards, GIF sizing.
- `references/examples.md` — curated READMEs and what to steal from each.
- `scripts/frame-image.sh` — frame screenshots (rounded + border + shadow).

## Checklist

- [ ] Identity derived from the project, not generic
- [ ] Banner + badge row + hero above the fold; install reachable in one scroll
- [ ] Hero shows the real product at the best available tier (GIF via vhs,
      framed screenshot, raw screenshot, or hand-authored SVG); no mocked or
      fabricated imagery
- [ ] Assets in-repo with relative paths; GIF size checked
- [ ] TOC links work; heading style consistent
- [ ] Install table covers the real variants
- [ ] Gallery framed and legible
- [ ] LICENSE + CONTRIBUTING present; badges truthful
- [ ] Prose sober; tone matches the project
