# Contributing

Small, quiet PRs are welcome. A few ground rules keep graphite itself:

- **Visual changes come with a screenshot.** Capture with `scripts/capture.sh`
  (needs `grim`); frame with `scripts/frame-image.sh` (needs ImageMagick 7).
- **`theme.json` is the single source of the palette.** Config files may use
  its values — not introduce new ones. If a color is missing for your use
  case, add it to `theme.json` first.
- **The red accent (`#D71921`) marks focus, and nothing else.** Active window
  border, active workspace. Don't spend it anywhere new.
- **Test on a throwaway setup.** `./install.sh` backs up your existing
  `~/.config` entries with a timestamp, but a VM or a second user is safer.

## Reporting a bug

Open an issue with the [bug template](.github/ISSUE_TEMPLATE/bug_report.md):
Hyprland/Waybar versions, what you expected, what happened, and a screenshot
if it's visual.
