#!/usr/bin/env bash
# Install the graphite theme into ~/.config with a timestamped backup.
set -euo pipefail

DEST="${HOME}/.config"
STAMP=$(date +%Y%m%d-%H%M%S)

for src in hypr waybar foot; do
  if [ ! -d "$src" ]; then
    echo "skipping $src (not present in repo)" >&2
    continue
  fi
  if [ -e "$DEST/$src" ]; then
    echo "backing up $DEST/$src -> $DEST/$src.bak.$STAMP"
    mv "$DEST/$src" "$DEST/$src.bak.$STAMP"
  fi
  mkdir -p "$DEST"
  cp -r "$src" "$DEST/$src"
  echo "installed $src -> $DEST/$src"
done

echo "graphite installed. Reload Hyprland or relog to apply."
