#!/usr/bin/env bash
# Sync the canonical skills (.opencode/skills/) into the Claude Code plugin
# (plugin/skills/). The .opencode/skills/ folders are the single source of
# truth; run this after editing any SKILL.md, before committing.
set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)

mkdir -p "$root/plugin/skills"
for skill in readme-pro readme-pro-low readme-pro-medium readme-pro-high; do
  rm -rf "$root/plugin/skills/$skill"
  cp -r "$root/.opencode/skills/$skill" "$root/plugin/skills/$skill"
  echo "synced: $skill"
done
