---
name: README Pro — Low
description: Write or upgrade a README in the minimal, documentation-first style - no badges, no images, no marketing. Choose this level whenever the user asks for something simple, clean, sober, or "sin florituras", or the target is a plain library, CLI, script collection, or internal tool. Use instead of readme-pro when the level is already known.
---

# Level: LOW — documentation first

Philosophy: the README is *read*, not looked at. Inspired by Yegor's "Elegant
READMEs". Every line must inform; decoration is noise. This is the honest
level for most libraries, CLIs, and internal tools — readers here want to
decide in 60 seconds, and decoration slows that decision down.

## Allowed structure (in this order)

1. `# Project name` + one-paragraph pitch: what it is, why it exists, who it
   is for.
2. `## Install` — exact, copy-pasteable commands; per package manager only if
   it truly differs.
3. `## Usage` — at least one real, runnable example. An example beats three
   paragraphs of prose.
4. `## Configuration` — only if options are non-obvious; list each flag or
   field with its meaning and default.
5. `## Constraints` or `## FAQ` — only if there are real limitations users
   will hit.
6. `## License` — one line with the SPDX identifier.

Stop there. Anything beyond this needs a justification.

## Pitch example

**Bad** (marketing, tells nothing):
> TODO-Scan is the ultimate, blazingly fast developer companion that
> revolutionizes code hygiene!

**Good** (informative, sober):
> todo-scan walks a directory tree and lists every TODO, FIXME, and HACK
> comment with file and line number, so stale notes can't hide until review
> day.

## Forbidden at this level

- Badge rows, shields, images, GIFs.
- Table of contents.
- Emoji and decorative separators.
- Marketing adjectives ("blazingly fast", "powerful", "elegant").
- Empty ceremony sections ("Contributing" with no instructions, "Roadmap"
  with no items).
- Changelogs, contributor walls, donation links.

## Writing rules

- Short declarative sentences; imperative for steps.
- Never "just", "simply", "easily" — they condescend.
- Show, don't tell: one code block beats three paragraphs.
- Bold sparingly (at most once per section).
- No HTML in the body unless strictly required.

## If improving an existing README

Audit against the structure above: what stays, what moves to docs/ or
ARCHITECTURE.md, what gets deleted. Present the plan before rewriting.

## Checklist

- [ ] Pitch answers what + why in four sentences or fewer
- [ ] Install commands are exact and copy-pasteable
- [ ] Usage example runs as-is (no unexplained placeholders)
- [ ] No badges, images, emoji, or TOC
- [ ] No invented features or aspirational sections
- [ ] License section matches the actual LICENSE file (flag it if missing,
      don't claim one)
- [ ] A reader gets the full picture in about 60 seconds
