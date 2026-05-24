# Contributing

PRs welcome for plugin depth, additional templates, multi-machine + team-handoff patterns, integrations with chat tools.

## Welcome

- Bug fixes
- Plugin deepening (see CHANGELOG maturity matrix)
- Handoff templates for specific scenarios (incident response, code review handoff, vacation handoff, etc.)
- Pickup integrations (auto-run verify commands, surface "Next step" prominently)
- Team-handoff patterns
- Chat-tool integrations (WhatsApp, Slack, Discord, Telegram, Email)

## Not accepted

- Patterns that put credentials in HANDOFF.md
- Patterns that conflate HANDOFF (per-session) with project memory (durable) — keep them separate
- AI-generated content that hasn't been used on a real session

## Branch + PR

`feat/`, `fix/`, `deepen/<plugin>`, `template/<name>`. Commit format: `type(scope): description`. MIT, no CLA.

## Plugin authoring

Each plugin: `plugins/<name>/README.md` + `agents/<name>.md` + `commands/<name>.md` + `skills/<name>.md`. See `plugins/handoff/` for the depth-complete reference.
