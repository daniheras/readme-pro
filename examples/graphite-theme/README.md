<div align="center">
  <img src="docs/banner.svg" width="640" alt="graphite - quiet, dark, one red accent">

  **graphite** is a quiet, near-black desktop theme with a single red accent,
  for Hyprland and Waybar (foot on the way).

  <p>
    <img alt="made for Hyprland and Waybar" src="https://img.shields.io/badge/made_for-Hyprland_Waybar-D71921?style=flat-square">
    <a href="LICENSE"><img alt="license MIT" src="https://img.shields.io/badge/license-MIT-3F3F3F?style=flat-square"></a>
    <a href="CONTRIBUTING.md"><img alt="PRs welcome" src="https://img.shields.io/badge/PRs-welcome-8A8A8A?style=flat-square"></a>
  </p>

  <!-- HERO - commented placeholder until the first real capture. Two pipelines:
         1. terminal GIF:  install vhs (needs ttyd + ffmpeg), then  vhs docs/hero.tape  -> docs/img/hero.gif
         2. live desktop:  needs grim, then  scripts/capture.sh hero  -> docs/img/hero.png
         Then replace the palette card below (or this comment) with:
  <img src="docs/img/hero.gif" width="840" alt="graphite running on Hyprland">
  -->

  <img src="docs/palette.svg" width="560" alt="the graphite palette">
</div>

<p align="center">
  <a href="#features">Features</a> &#183; <a href="#install">Install</a> &#183; <a href="#usage">Usage</a> &#183; <a href="#palette">Palette</a> &#183; <a href="#gallery">Gallery</a> &#183; <a href="#faq">FAQ</a> &#183; <a href="#community">Community</a>
</p>

## Features

- **Quiet by design.** Near-black surfaces, 1px borders, soft shadows, 8px
  corners. Nothing shouts, nothing glows.
- **One red accent.** `#D71921` marks focus - the active window border and the
  active workspace - and nothing else. If it's red, it's yours.
- **Hyprland-native.** Active-border gradient from red to graphite at 60deg,
  6px inner and 12px outer gaps, rounded corners.
- **Waybar to match.** Same graphite bar, red active workspace, Nerd Font
  glyphs.
- **One file of truth.** [`theme.json`](theme.json) holds the palette; port it
  to any terminal or compositor.

## Install

You need [Hyprland](https://hypr.land), [Waybar](https://github.com/Alexays/Waybar)
and **Symbols Nerd Font** (the Waybar glyphs).

```sh
git clone https://github.com/<you>/graphite.git
cd graphite
./install.sh    # copies hypr/ and waybar/ into ~/.config, backing up what's there
```

| You want | Do |
|---|---|
| everything | `./install.sh` |
| Hyprland only | `cp -r hypr ~/.config/` |
| Waybar only | `cp -r waybar ~/.config/` |
| foot | not bundled yet - `install.sh` picks up `foot/` the moment it exists |

`install.sh` never overwrites silently: existing `~/.config/hypr`, `waybar`
and `foot` are moved to `<name>.bak.YYYYMMDD-HHMMSS` first.

## Usage

Apply, then reload:

```sh
./install.sh
hyprctl reload          # or relog
pkill waybar; waybar &  # restart the bar
```

Rolling back is one move:

```sh
rm -rf ~/.config/hypr
mv ~/.config/hypr.bak.20260101-120000 ~/.config/hypr
```

## Palette

Single source of truth: [`theme.json`](theme.json).

| Role | Hex | Used for |
|---|---|---|
| background | `#191919` | Waybar background; the base everywhere |
| surface | `#222222` | in `theme.json`, reserved for panels and selections |
| border | `#3F3F3F` | inactive borders, Waybar outline |
| muted | `#8A8A8A` | in `theme.json`, reserved for secondary text |
| foreground | `#EDEDED` | text |
| accent | `#D71921` | active window border, active workspace - focus only |

<!-- Gallery - uncomment as real captures land. Capture: scripts/capture.sh gallery-1
<table>
  <tr>
    <td align="center"><img src="docs/img/gallery-1.png" width="460" alt="full desktop"></td>
    <td align="center"><img src="docs/img/gallery-2.png" width="460" alt="Waybar detail"></td>
  </tr>
</table>
-->

## FAQ

**Where is the foot config?**
Not bundled yet. `theme.json` has the values and `install.sh` already looks
for `foot/`, so dropping a `foot/` config into the repo is enough for the
installer to pick it up. PRs welcome.

**How do I change the accent?**
It lives in three places: `col.active_border` in `hypr/hypr.conf`,
`#workspaces button.active` in `waybar/style.css`, and `colors.accent` in
`theme.json`. Replace `#D71921` / `D71921FF` in all three.

**Does it work on sway or X11?**
The configs target Hyprland and Waybar specifically. The palette in
`theme.json` is portable to anything that takes hex colors.

## Community

- [LICENSE](LICENSE) - MIT.
- [CONTRIBUTING.md](CONTRIBUTING.md) - how to send changes; visual PRs come
  with screenshots.
- [Bug template](.github/ISSUE_TEMPLATE/bug_report.md) - for when something
  looks or behaves wrong.

<div align="center">
  <sub>graphite &#8212; quiet, dark, one red accent.</sub>
</div>
