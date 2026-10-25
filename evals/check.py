#!/usr/bin/env python3
"""Programmatic grader for readme-pro evals.

Checks the objective expectations from evals/evals.json against a run's
README (and project dir). Qualitative expectations (tone, routing rationale,
audit-first behavior) are graded by a human or grader agent and merged into
the final grading.json afterwards.

Usage:
    python3 evals/check.py <eval_id> <project_dir> [--json]

  <eval_id>      1 | 2 | 3 (matches evals/evals.json)
  <project_dir>  the run's project copy (contains README.md)
  --json         emit the results as a JSON array instead of a report
"""

import json
import re
import sys
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


def badge_count(text: str) -> int:
    return len(re.findall(r"img\.shields\.io", text))


def ci_badge(text: str) -> bool:
    return bool(
        re.search(r"img\.shields\.io/[^\s\)\]]*(?:actions/workflow|badge/ci|badge/workflow)", text, re.I)
        or re.search(r"badge/[^\s\)\]]*ci[^\s\)\]]*", text, re.I)
        or re.search(r"actions/workflows/[^\s\)\]]*badge\.svg", text, re.I)
    )


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
             (not re.search(r"^#+\s*license\b", readme, re.I | re.M))
             or bool(UNCERTAINTY.search(section(readme, "License")))),
        ]

    elif eid == 2:
        tape_in_repo = list(project.rglob("*.tape"))
        c += [
            ("Theme palette drives design (#191919 / #D71921 present)",
             "191919" in readme.lower() and "d71921" in readme.lower()),
            ("Showcase structure: banner/hero + TOC + install + community",
             all([
                 re.search(r"hero|banner", readme, re.I),
                 TOC_HEADING.search(readme),
                 re.search(r"^#+\s*install\b", readme, re.I | re.M),
                 re.search(r"community|contributing|license", readme, re.I),
             ])),
            ("Hero is a .tape plan or marked placeholder (no fake remote screenshots)",
             bool(tape_in_repo) or "tape" in readme.lower()
             or not remote_asset_urls(readme)),
            ("No CI or release badges",
             not re.search(r"img\.shields\.io/[^\s\)\]]*(?:actions|v/tag|releases)", readme, re.I)),
            ("Install matches install.sh (backup + ~/.config)",
             re.search(r"\.config|install\.sh", readme) is not None),
            ("Proposes LICENSE and CONTRIBUTING",
             "LICENSE" in readme and "CONTRIBUTING" in readme),
        ]

    elif eid == 3:
        c += [
            ("Badge row <= 4 and truthful CI badge present",
             badge_count(readme) <= 4 and ci_badge(readme)),
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
        ]

    return c


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

    results = [{"text": t, "passed": bool(p), "evidence": "programmatic check"} for t, p in checks_for(eid, readme, project)]

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
