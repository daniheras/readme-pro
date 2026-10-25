# Polish tools (HIGH level)

Tiered tooling for the showcase recipe. Tier 0 needs no installs; the rest
are optional upgrades — detect before use, never block on them. All commands
assume the target repo is the working directory.

**Detect before use:**

```sh
magick -version   # Tier 1: ImageMagick
vhs --version     # Tier 2: vhs (also needs ttyd + ffmpeg)
```

Install hints by OS (optional upgrades only):

| Tool | Linux | macOS | Windows |
|---|---|---|---|
| ImageMagick 7 | `pacman -S imagemagick` / `apt install imagemagick` / `dnf install ImageMagick` | `brew install imagemagick` | `winget install ImageMagick.ImageMagick` (or use WSL) |
| vhs | `pacman -S vhs` (needs `ttyd` + `ffmpeg`) | `brew install vhs` | WSL recommended |

## Tier 0 — hand-authored SVG (no tools at all)

SVG is plain text: write banner and palette strips by hand and commit them.
GitHub renders them from relative paths.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="640" height="160" viewBox="0 0 640 160">
  <rect width="640" height="160" fill="#191919"/>
  <text x="320" y="88" text-anchor="middle" font-family="monospace"
        font-size="40" fill="#EDEDED">&#9656; graphite_</text>
  <rect x="492" y="60" width="22" height="34" fill="#D71921"/>
</svg>
```

Reference it with `<div align="center"><img src="assets/banner.svg" width="640" alt="graphite"></div>`
and add `width=` so mobile scales. Build palette strips the same way: one
`<rect>` per swatch from the project's palette.

## Tier 2 — vhs: terminal GIFs as code

<https://github.com/charmbracelet/vhs>

- A `.tape` file is a script that renders into a GIF: hero demos become
  reproducible, and the tape belongs in the repo.
- Dependencies: `ttyd` + `ffmpeg` (install hints in the table above).
- Outputs GIF / MP4 / WebM / PNG. `vhs record` captures real keystrokes.

Example tape with a themed "window" look:

```tape
Output docs/demo.gif
Set FontSize 20
Set Width 1200
Set Height 600
Set Theme {
  "background": "#191919",
  "foreground": "#F8F8F2",
  "cursor": "#D71921"
}
Set WindowBar Rings
Set BorderRadius 8
Set MarginFill "#191919"
Set Margin 20

Type "hyprctl reload" Enter
Sleep 3s
```

- `Set Theme` accepts a built-in name or a JSON object; provide all 16
  palette colors when matching a theme's identity.
- `Set WindowBar`, `Set BorderRadius`, `Set MarginFill` produce the framed
  "window" look.
- Version the `.tape` in the repo so the hero can be regenerated.

## shields.io — badges

<https://shields.io>

Static badge:

```md
![made for Hyprland](https://img.shields.io/badge/made_for-Hyprland-D71921?style=flat-square&logo=archlinux&logoColor=white)
```

Useful dynamic endpoints:

```md
![version](https://img.shields.io/github/v/tag/USER/REPO?style=flat-square)
![ci](https://img.shields.io/github/actions/workflow/status/USER/REPO/ci.yml?branch=main&style=flat-square)
![license](https://img.shields.io/github/license/USER/REPO?style=flat-square)
```

- Colors take hex without `#` (`D71921`).
- `logo` accepts simple-icons slugs.
- Keep one style across the whole row (`style=flat-square` everywhere).

## github-readme-stats — profile cards

<https://github.com/anuraghazra/github-readme-stats>

```md
![stats](https://github-readme-stats.vercel.app/api?username=USER&show_icons=true&hide_border=true&bg_color=191919&title_color=D71921&text_color=F8F8F2)
```

Colors are customizable — match the project palette. Use sparingly; cards are
for profile READMEs, not every project README.

## Tier 1 — framing screenshots (rounded + border + shadow)

Only when ImageMagick is present; otherwise ship the raw screenshot. The
bundled script normalizes virtual-canvas geometry, rounds the corners, draws
a 2px border along the rounded contour, adds a drop shadow, and pads
symmetrically so the blur isn't clipped:

```sh
scripts/frame-image.sh screenshots/*.png

# tweak per project identity:
RADIUS=16 BORDER="#D71921" MARGIN=32 scripts/frame-image.sh docs/hero.png
```

Requires ImageMagick 7 (`magick`). Adjust radius, border color, and shadow to
match the project's palette.

## GIF budget and optimization

- Target: hero GIF ≤ ~5 MB, gallery GIFs smaller.
- ffmpeg palette method (good quality, small size):

```sh
ffmpeg -i in.mov -vf "fps=15,scale=900:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" out.gif
```

- Alternatives: <https://ezgif.com/> (web) and Gifski
  <https://github.com/sindresorhus/Gifski> (macOS).
- Above the budget: host as MP4/WebM (GitHub accepts uploaded videos in
  READMEs via user-attachments URLs) and keep a static first frame as
  fallback.
