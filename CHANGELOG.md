# Changelog

## [1.1.0] - 2026-09-30

### Added

- A public pantry in `pantry/`: a competitor map, an X mine, a people mine, and a pantry queue of Goal atoms, each with a Done-when anyone can check. `pantry/MENU.md` is generated from the queue by the kitchen's `menu.py` and names one atom as up next.
- Two issue forms: `routing-miss` (Claude picked the wrong plugin, skill or agent, or none) and `plugin-proposal` (a new plugin, skill, agent or command), with matching labels.
- A "Ways to contribute" section at the top of `CONTRIBUTING.md` (Menu items, routing misses, plugin proposals, translations, sharing what you built, and the local test loop) and a Contribute section in the README.
- Grok Build support. Grok Build reads the same plugin folders; `.grok-plugin/marketplace.json`, generated from the Claude manifest by `scripts/sync-grok-manifest.py`, makes the repo a Grok marketplace too (`grok plugin marketplace add HermeticOrmus/LibreSessionFlow-Claude-Code`). A `grok` CI job fails when that file drifts, validates every plugin with `grok plugin validate`, and installs all ten into a clean Grok home.
- `./setup.sh --grok` installs through the Grok Build CLI instead of Claude Code, with the same `--only`, `--list`, and `--uninstall` options.
- `LEDGER.md`, the kintsugi ledger: every crack the 1.0.0 release found and sealed, with its evidence, and the cracks still open.

## [1.0.0] - 2026-09-30

The pack becomes installable and every plugin does what its README says. Before this release only `handoff` had working files; the other nine were README-only, and the old `setup.sh` copied folders that Claude Code never loaded.

### Added

- Plugin marketplace `libre-sessionflow` (`.claude-plugin/marketplace.json`) and a `plugin.json` for each of the ten plugins. Install with `/plugin marketplace add HermeticOrmus/LibreSessionFlow-Claude-Code`, then `/plugin install <name>@libre-sessionflow`.
- A working slash command and skill for each of the nine plugins that had none:
  - `pickup`: finds the handoff through an index, re-runs its verify commands and marks each item still done, drifted, or not checkable, loads the key files, and presents one next action; cold mode rebuilds context from git history; conversation mode resumes a chat through LibreWhatsApp; `all` adds your open PRs and issues.
  - `close`: session audit, handoff when work is unfinished, memory update, a session summary kept outside the repo, an offer to commit finished work, and an optional notification.
  - `absorb`: classifies what the session taught, merges it with existing memory, writes topic files and a one-line-per-entry `MEMORY.md` index, and proposes CLAUDE.md lines for instructions.
  - `explore`: search, outline, and unfold, using structural tools when the session has them and the bundled `bin/outline.py` otherwise (exact for Python, pattern-based for thirteen other languages).
  - `grab`: `bin/grab.py` copies the latest command, URL, or reply from the current session transcript to the clipboard on Wayland, X11, macOS, or WSL.
  - `todo`: verbatim capture under today's date, plus `/todo triage`, which proposes a destination for each open item and changes nothing without approval.
  - `share-prompt`: paste-ready prompt delivery through the clipboard, a secret gist, your own command, or LibreWhatsApp `/push`, with a credential check.
  - `meet`: one-pass research of a person (web, your projects, your GitHub account) saved as a contact memory file, with privacy rules.
  - `maintain`: read-only scan of MCP health, plugin token cost, sync conflicts, settings validity, memory size, hooks, and usage (`bin/usage.py`), then fixes one approved change at a time, moving files to a dated trash folder instead of deleting.
- `handoff` indexes every handoff in `~/.claude/sessionflow/handoffs/INDEX.md` for `/pickup`, adds a resume prompt section, copies the resume prompt to the clipboard, backs up another task's HANDOFF.md before replacing it, and offers a location for multi-project sessions.
- `sessionflow.example.json`: optional settings (memory folder, SessionFlow home, notification command or `/push` target, share-prompt recipients, search paths, remote machines for pickup). Every key has a default that works with no setup; environment variables override the file.
- CI workflow that validates the marketplace and every plugin and installs them into a clean config.
- Feedback issue template.

### Changed

- `setup.sh` now registers the marketplace and installs through the Claude Code CLI (`--list`, `--only`, `--scope`, `--uninstall`). `--plugins-dir` is accepted and ignored with a note.
- The handoff skill is now `handoff-patterns` (moved from `skills/handoff.md`), so it no longer shares a name with the `/handoff` command.
- The `handoff-engineer` agent uses the session's model (`model: inherit`) instead of pinning one.
- Each plugin shows one entry in the slash menu: commands are the user entry point and skills are what Claude loads on its own.
- Docs: install steps, troubleshooting, the plugin authoring layout, and plugin READMEs describe what now ships.

### Fixed

- Plugins installed with the old `setup.sh` were never loaded by Claude Code. Remove any `~/.claude/plugins/libre-sessionflow-*` copies and install through the marketplace.
- `claude --clear` in the docs is now `/clear`, which is the actual command.
- Machine-specific examples in the handoff docs and the intermediate learning path are now generic.

## [0.1.0] — 2026-05-23

Initial release. Consolidates the session lifecycle that was scattered across multiple ormus-* repos into a single Libre umbrella.

### Plugins (10 total)

| Plugin | Status |
|---|---|
| **handoff** | depth-complete (the flagship) |
| pickup | shell |
| absorb | shell |
| explore | shell |
| close | shell |
| maintain | shell |
| grab | shell |
| todo | shell |
| share-prompt | shell |
| meet | shell |

### Supersedes

The following ormus-* repos are superseded by this umbrella. They remain live with redirect READMEs pointing here:

- `ormus-handoff` → see `plugins/handoff/`
- `ormus-pickup` → see `plugins/pickup/`
- `ormus-absorb` → see `plugins/absorb/`
- `ormus-explore` → see `plugins/explore/`

### v0.2 priorities

- Deepen `pickup` (it's the most-used plugin and needs the full template)
- Deepen `close` (ritual orchestration; the highest-value combo plugin)
- Deepen `absorb` (cross-session learning is the biggest gap right now)

### v0.3 priorities

- Deepen `maintain`, `explore`, `grab`
- Team-handoff templates
- Multi-machine pickup patterns

### v0.4+

- Chat-tool transport integrations for `share-prompt`
- `meet` deepening
- `todo` triage patterns
