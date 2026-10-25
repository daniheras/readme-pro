# readme-pro

OpenCode skills that build READMEs matched to each project's philosophy — from
brutally minimal to full showcase. One skill family, three intensity levels,
one automatic router.

Not every project needs a hero GIF; a JSON parser with a banner row looks
silly, and a terminal theme without a demo GIF is missing the point. Instead
of one maximal template, readme-pro assesses the project and picks the
intensity that fits: what to include, what to leave out, and how loud to be.

## The four skills

| ID | Loads when | Produces |
|---|---|---|
| `readme-pro` | Any README task, by default | Assesses the project, picks a level, routes to the matching recipe |
| `readme-pro-low` | User wants simple/clean/sober; plain libraries, CLIs, internal tools | Documentation-first README: no badges, no images, no marketing |
| `readme-pro-medium` | User wants a professional/standard README; public-facing apps and tools | Front-door README: pitch, informative badges, screenshot if there's UI, install, usage, configuration |
| `readme-pro-high` | Look and feel *is* the product: UIs, TUIs, themes, dotfiles — or "wow" requests | Showcase README: banner, badge row, hero demo GIF, TOC, gallery, community extras |

The three philosophies they encode:

- **LOW (Yegor school)** — the README is read, not looked at. Every line must inform.
- **MEDIUM (makeareadme / thoughtbot school)** — the README is the front door. What & why in one screen, working install in two.
- **HIGH (doomemacs / sniffnet school)** — the README is part of the product experience. Identity first: derive palette, imagery, and tone from the project itself.

All levels share one rule: **never fabricate**. No badge for CI that doesn't
exist, no license badge without a LICENSE file, no mocked screenshots. A
README that lies gets caught on the first clone.

## Install

**In a project** — copy the skill folders you want:

```sh
cp -r readme-pro/.opencode/skills/readme-pro* your-repo/.opencode/skills/
```

**Globally** — same, into `~/.config/opencode/skills/`.

**As a source** — point your `opencode.jsonc` at this repo:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "skills": ["~/Work/readme-pro/.opencode/skills"]
}
```

## Usage

In any OpenCode session:

- *"write a README for this project"* → `readme-pro` assesses and routes.
- *"make it minimal, no badges"* → load `readme-pro-low` directly.
- *"I want the front page to slap"* → `readme-pro-high`.

The router states the chosen level and the reason in one line, and the
recipe's checklist runs before the README is delivered.

## Evals

Test cases live in `evals/evals.json` with small real fixtures under
`evals/fixtures/` (a CLI tool, a Hyprland theme, an app with a bad README to
rebuild). They cover routing correctness, structure, and the no-fabrication
rule. Run outputs land in `evals/workspace/` (gitignored).

## Sources

The skills distill a curated study list: [Make a README](https://www.makeareadme.com/),
[The Art of README](https://github.com/hacktivistto/The-Art-of-README),
[thoughtbot's guide](https://thoughtbot.com/blog/how-to-write-a-great-readme),
[README-Driven Development](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html),
[Elegant READMEs](https://www.yegor256.com/2019/04/23/elegant-readme.html),
[ARCHITECTURE.md](https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html),
[awesome-readme](https://github.com/matiassingers/awesome-readme), plus
[vhs](https://github.com/charmbracelet/vhs) and
[shields.io](https://shields.io/) for the showcase tooling. Full annotated
list: `.opencode/skills/readme-pro-high/references/examples.md`.

## License

[MIT](LICENSE)
