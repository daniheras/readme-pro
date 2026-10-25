#!/usr/bin/env python3
"""Scan a directory tree for TODO/FIXME/HACK comments and report them."""

import argparse
import re
import sys
from pathlib import Path

PATTERN = re.compile(r"\b(TODO|FIXME|HACK)\b[:\s]?(.*)")
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules", ".mypy_cache"}
SKIP_SUFFIXES = {".pyc", ".lock", ".min.js", ".svg"}


def scan(root: Path):
    hits = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix in SKIP_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            m = PATTERN.search(line)
            if m:
                hits.append((path, lineno, m.group(1), m.group(2).strip()))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description="Find TODO/FIXME/HACK comments in a tree.")
    parser.add_argument("root", nargs="?", default=".", help="directory to scan (default: .)")
    parser.add_argument("--fail-on-hit", action="store_true", help="exit 1 if any hits are found")
    args = parser.parse_args()

    root = Path(args.root)
    hits = scan(root)
    for path, lineno, tag, note in hits:
        try:
            rel = path.relative_to(root)
        except ValueError:
            rel = path
        print(f"{rel}:{lineno}: {tag}: {note}")
    print(f"\n{len(hits)} hit(s) in {args.root}")
    return 1 if args.fail_on_hit and hits else 0


if __name__ == "__main__":
    sys.exit(main())
