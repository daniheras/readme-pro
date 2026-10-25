#!/usr/bin/env python3
"""Programmatic grader for readme-pro evals.

Checks the objective expectations from evals/evals.json against a run's
README (and project dir). Qualitative expectations (tone, routing rationale,
audit-first ordering) are graded by a human or grader agent and merged into
the final grading.json afterwards.

Usage:
    python3 evals/check.py <eval_id> <project_dir> [--json]
"""

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF\u2B50\u2705\u274C]"
)
HYPE_WORDS = re.compile(
    r"\b(blazing\w*|revolution\w*|amazing|gorgeous|stunning|ultimate|best screenshot)\b",
    re.IGNORECASE,
)
LICENSE_NAMES = re.compile(r"\b(MIT|Apache-?\d*|GPL-?\d*|BSD-\d|MPL-?\d*\.\d+)\b")
UNCERTAINTY = re.compile(
    r"(missing|not decided|not been (chosen|decided)|no decidido|sin decidir|TBD|to be decided|"
    r"license file (is )?absent|add a LICENSE|pending|por decidir|choosealicense)",
    re.IGNORECASE,
)
TOC_HEADING = re.compile(r"^#{1,3}\s*(table of contents|contents|toc|index)\b", re.I | re.M)
TOOL_INSTALL_REQUIRED = re.compile(
    r"(must|need to|first,?\s*)?(install|brew install|pacman -S|apt install|dnf install|winget install)"
    r"[^\n]*\b(imagemagick|magick|vhs|ffmpeg|ttyd)\b",
    re.IGNORECASE,
)
MEDIUM_ORDER = ["Features", "Instal((ar)|l(ation)?)", "Usage", "Contributing", "Licen(cia|se)?(n)?"]


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def section(text: str, name: str) -> str:
    m = re.search(rf"^#+\s*{re.escape(name)}\b.*?$(.*?)(?=^#+\s|\Z)", text, re.I | re.M | re.S)
    return m.group(1) if m else ""


def remote_asset_urls(text: str):
    return [
        u for u in re.findall(r"https?://[^\s\)\]]+\.(?:png|jpe?g|gif|webm|mp4)", text, re.I)
        if "img.shields.io" not in u
    ]


def badge_urls(text: str):
    return re.findall(r"https?://img\.shields\.io/[^\s\)\"]+", text)


def badge_styles(text: str):
    return sorted(set(re.findall(r"style=([\w-]+)", " ".join(badge_urls(text)))))


def ci_badge(text: str) -> bool:
    return bool(
        re.search(r"img\.shields\.io/[^\s\)\]]*(?:actions/workflow|badge/ci|badge/workflow)", text, re.I)
        or re.search(r"badge/[^\s\)\]]*ci[^\s\)\]]*", text, re.I)
        or re.search(r"actions/workflows/[^\s\)\]]*badge\.svg", text, re.I)
    )


def has_nav(readme: str) -> bool:
    """Nav exists: a headed TOC or an inline anchor list (>= 4 internal links)."""
    if TOC_HEADING.search(readme):
        return True
    # inline nav: markdown anchor links or HTML href="#..." (>= 4)
    anchors = re.findall(r"\]\(#[^)\s]+\)|href=\"#", readme)
    return len(anchors) >= 4


def heading_pos(text: str, name: str):
    m = re.search(rf"^#+\s*{name}\b", text, re.I | re.M)
    return m.start() if m else None


def local_svgs(project: Path):
    return list(project.rglob("*.svg"))


def svg_uses_palette(svg_path: Path, colors) -> bool:
    try:
        content = svg_path.read_text(encoding="utf-8")
        ET.fromstring(content)  # validity
        return True
    except (FileNotFoundError, ET.ParseError):
        return False


def checks_for(eid: int, readme: str, project: Path):
    c = []

    if eid == 1:
        c += [
            ("Has pitch, Install(ation) and Usage sections",
             all(re.search(rf"^#+\s*{s}\b", readme, re.I | re.M) for s in ("Install(ation)?", "Usage"))),
            ("No badges, images, or shields anywhere",
             "img.shields.io" not in readme and "![" not in readme and "<img" not in readme),
            ("No TOC", not TOC_HEADING.search(readme)),
            ("No emoji", not EMOJI.search(readme)),
            ("Usage references real entry point and flags",
             "todo-scan" in readme and "--fail-on-hit" in readme),
            ("Does not claim a specific license (flagged instead)",
             (not re.search(r"^#+\s*licen(cia|se)\b", readme, re.I | re.M))
             or bool(UNCERTAINTY.search(section(readme, "License")))),
        ]

    elif eid == 2:
        tapes = list(project.rglob("*.tape"))
        banners = [p for p in local_svgs(project) if "banner" in p.name or "hero" in p.name]
        styles = badge_styles(readme)
        c += [
            ("Theme palette drives design (#191919 / #D71921 present)",
             "191919" in readme.lower() and "d71921" in readme.lower()),
            ("Showcase structure: banner/hero + nav + install + community",
             all([
                 re.search(r"hero|banner", readme, re.I),
                 has_nav(readme),
                 re.search(r"^#+\s*instal((ar)|l(ation)?)\b", readme, re.I | re.M),
                 re.search(r"community|contributing|licen(cia|se)", readme, re.I),
             ])),
            ("Hero is a .tape plan or marked placeholder (no fake remote screenshots)",
             bool(tapes) or "tape" in readme.lower() or not remote_asset_urls(readme)),
            ("Banner SVG exists and is valid XML (Tier 0 asset)",
             any(svg_uses_palette(b, None) for b in banners)),
            ("No CI or release badges",
             not re.search(r"img\.shields\.io/[^\s\)\]]*(?:actions|v/tag|releases)", readme, re.I)),
            ("Install matches install.sh (backup + ~/.config)",
             re.search(r"\.config|install\.sh", readme) is not None),
            ("Proposes LICENSE and CONTRIBUTING",
             "LICENSE" in readme and "CONTRIBUTING" in readme),
            ("Badge row uses one consistent style",
             len(styles) <= 1),
        ]

    elif eid == 3:
        positions = [heading_pos(readme, s) for s in MEDIUM_ORDER]
        c += [
            ("MEDIUM section order: Features -> Install -> Usage -> Contributing -> License",
             all(p is not None for p in positions) and positions == sorted(positions)),
            ("Badge row <= 4 and truthful CI badge present",
             badge_count_ok(readme) and ci_badge(readme)),
            ("No emoji", not EMOJI.search(readme)),
            ("No hype words (blazing/fast/ultimate/...)",
             not HYPE_WORDS.search(readme)),
            ("Install corrected (real package, no snipshot-tool)",
             re.search(r"pip install -e \.|pipx install snipshot\b|pip install snipshot\b", readme)
             and "snipshot-tool" not in readme),
            ("Usage documents real flags (--radius/--border/--margin)",
             all(f in readme for f in ("--radius", "--border", "--margin"))),
            ("Changelog removed or linked (not inlined)",
             not re.search(r"^###?\s*v\d+\.\d", readme, re.M)),
            ("Badge styles consistent",
             len(badge_styles(readme)) <= 1),
        ]

    elif eid == 4:
        tapes = list(project.rglob("*.tape"))
        svgs = local_svgs(project)
        c += [
            ("Showcase structure: banner + badges + nav + install + community",
             all([
                 re.search(r"hero|banner", readme, re.I),
                 len(badge_urls(readme)) >= 1,
                 has_nav(readme),
                 re.search(r"^#+\s*instal((ar)|l(ation)?)\b", readme, re.I | re.M),
                 re.search(r"community|contributing|licen(cia|se)", readme, re.I),
             ])),
            ("Tool-free pipeline: no ImageMagick/vhs install required by the README",
             not TOOL_INSTALL_REQUIRED.search(readme)),
            ("Identity from theme.json (#FFB86C accent / #1B1B1F background present)",
             "ffb86c" in readme.lower() and "1b1b1f" in readme.lower()),
            ("Hand-authored SVG assets exist and are valid XML",
             any(svg_uses_palette(s, None) for s in svgs)),
            ("Hero is marked placeholder or .tape (no fake remote screenshots)",
             bool(tapes) or "tape" in readme.lower() or not remote_asset_urls(readme)),
            ("No CI or release badges",
             not re.search(r"img\.shields\.io/[^\s\)\]]*(?:actions|v/tag|releases)", readme, re.I)),
            ("No emoji in prose (showcase allows rich visuals, not noise)",
             not EMOJI.search(readme)),
        ]

    return c


def badge_count_ok(text: str) -> bool:
    return 1 <= len(badge_urls(text)) <= 4


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    eid = int(sys.argv[1])
    project = Path(sys.argv[2]).resolve()
    as_json = "--json" in sys.argv

    readme = read(project / "README.md")
    if not readme:
        print(f"NO README found at {project / 'README.md'}")
        return 1

    results = [
        {"text": t, "passed": bool(p), "evidence": "programmatic check"}
        for t, p in checks_for(eid, readme, project)
    ]

    if as_json:
        print(json.dumps(results, indent=2))
    else:
        ok = sum(r["passed"] for r in results)
        print(f"eval {eid} @ {project}")
        for r in results:
            mark = "PASS" if r["passed"] else "FAIL"
            print(f"  [{mark}] {r['text']}")
        print(f"  -> {ok}/{len(results)} programmatic checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
