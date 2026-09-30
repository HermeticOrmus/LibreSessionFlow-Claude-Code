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

Each plugin:

```
plugins/<name>/
  .claude-plugin/plugin.json      name, version, description, author, homepage, repository, license, keywords
  commands/<name>.md              the slash command; frontmatter: description (+ argument-hint)
  skills/<skill-name>/SKILL.md    the method; frontmatter: name, description
  agents/<agent-name>.md          optional; frontmatter: name, description, model: inherit
  bin/                            optional helper scripts, called through ${CLAUDE_PLUGIN_ROOT}
  README.md
```

Commands are the user entry point (`disable-model-invocation: true`) and read their skill by path; skills carry the method and are what Claude picks up on its own (`user-invocable: false`, so each plugin shows one entry in the slash menu). Give the skill a different name from the command. Add the plugin to `.claude-plugin/marketplace.json` with the same description as its `plugin.json`, then run `claude plugin validate .` and `claude plugin validate plugins/<name>`.

Settings that depend on a person's own setup (where memory lives, where notifications go) belong in `sessionflow.example.json` with a default that works with no setup, never hard-coded. See `plugins/handoff/` for the reference plugin.
