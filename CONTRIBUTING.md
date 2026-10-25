# Contributing to readme-pro

PRs welcome — especially when they come with an eval case that justifies
them.

## How

1. Fork + branch (`feat/my-thing`).
2. If you touch a recipe (`SKILL.md`), explain the *why* in the PR: rules
   that don't know why they exist don't survive.
3. If you add an edge case, add the eval too (`evals/evals.json`, fixture
   included) — grading is the only honest way to show the skill improved
   rather than just changed.
4. Fixtures are small but real: their code must actually work.
5. Skills are edited in `.opencode/skills/` — that's the single source of
   truth. If you touch a `SKILL.md`, run `scripts/sync-claude-plugin.sh`
   before committing so the Claude Code plugin stays in sync.
6. Tone: skill content is sober English; this repo itself swears a little.
   Respect both registers.

## Don't fabricate

Applies to the skills and to PRs: no badges without backing, no screenshots
that aren't real, no eval numbers you can't show.
