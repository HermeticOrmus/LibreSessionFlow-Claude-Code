# Contributing

PRs welcome for plugin depth, additional templates, multi-machine + team-handoff patterns, integrations with chat tools.

## Ways to contribute

### Take a Menu item

[`pantry/MENU.md`](pantry/MENU.md) lists the next pieces of work, each with a Done-when anyone can check, and names one as up next. The research behind it lives in [`pantry/`](pantry/). Open items are also filed as issues with the [`menu` label](https://github.com/HermeticOrmus/LibreSessionFlow-Claude-Code/issues?q=is%3Aopen+label%3Amenu), and smaller ones show up under [good first issues](https://github.com/HermeticOrmus/LibreSessionFlow-Claude-Code/contribute). To claim one, comment on the issue that you are taking it, then open a pull request that says `Closes #N`.

### Report or fix a routing miss

Every skill, command and agent has a `description` that tells Claude when to use it. When you asked in plain words ("write a handoff", "what was I doing?", "copy that command") and Claude picked the wrong plugin, or none, open a [routing miss](https://github.com/HermeticOrmus/LibreSessionFlow-Claude-Code/issues/new?template=routing-miss.yml) with the prompt you used. The fix is usually a sharper `description` in `plugins/<name>/skills/<skill-name>/SKILL.md`, which makes it a good first pull request.

### Propose or build a plugin

Open a [plugin proposal](https://github.com/HermeticOrmus/LibreSessionFlow-Claude-Code/issues/new?template=plugin-proposal.yml) first, so the job it does and its Done-when are agreed before you build. A plugin here has this layout (details in [Plugin authoring](#plugin-authoring) below):

```text
plugins/<name>/.claude-plugin/plugin.json   name, version, description, author, homepage, repository, license, keywords
plugins/<name>/commands/<name>.md           the slash command; frontmatter: description (+ argument-hint)
plugins/<name>/skills/<skill-name>/SKILL.md the method; frontmatter: name, description (when to use it), user-invocable: false
plugins/<name>/agents/<agent-name>.md       optional; frontmatter: name, description, model: inherit
.claude-plugin/marketplace.json             add an entry for the plugin with the same description as its plugin.json
```

Give the skill a different name from the command, and check the name against the sibling Libre packs: LibreWhatsApp also ships a plugin named `grab`.

### Translate

The docs are English only. Translations of `QUICK_START.md` and the `learning-paths/` guides are welcome as `<file>.<lang>.md` next to the English file. Keep every command and code block identical to the English one.

### Share what you built

Wrote a handoff template for a scenario the pack does not cover, or wired `/close` to your own notifier? Post it in [Discussions](https://github.com/HermeticOrmus/LibreSessionFlow-Claude-Code/discussions) under Show and tell, or send it as a [feedback issue](https://github.com/HermeticOrmus/LibreSessionFlow-Claude-Code/issues/new?template=feedback.yml).

### Test your change locally

Load one plugin from your clone for a single session, without installing it (`--plugin-dir plugins` loads all ten):

```bash
claude --plugin-dir plugins/<name>
```

Validate the marketplace and the plugin you changed:

```bash
claude plugin validate .
claude plugin validate plugins/<name>
```

Install it into a clean, throwaway config, the way a new user would, and check that its command and skill are listed:

```bash
export CLAUDE_CONFIG_DIR=$(mktemp -d)
claude plugin marketplace add ./
claude plugin install <name>@libre-sessionflow
claude plugin details <name>@libre-sessionflow
```

CI runs the same checks on every pull request (the marketplace, every plugin, and a clean-config install of all ten). A second `grok` job checks that `.grok-plugin/marketplace.json` matches the Claude manifest, validates every plugin with `grok plugin validate`, and installs all ten into a clean Grok Build home; after you change `.claude-plugin/marketplace.json`, run `python3 scripts/sync-grok-manifest.py` and commit the file it writes. If this is your first contribution, the CI run waits until a maintainer approves it.

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

Commands are the user entry point and read their skill by path; skills carry the method and are what Claude picks up on its own (`user-invocable: false`, so each plugin shows one entry in the slash menu). Give the skill a different name from the command: two components with the same name collide. Leave commands model-invocable, so another skill can say "run /handoff" and Claude can follow it. Add the plugin to `.claude-plugin/marketplace.json` with the same description as its `plugin.json`, then run `claude plugin validate .` and `claude plugin validate plugins/<name>`.

Settings that depend on a person's own setup (where memory lives, where notifications go) belong in `sessionflow.example.json` with a default that works with no setup, never hard-coded. See `plugins/handoff/` for the reference plugin.
