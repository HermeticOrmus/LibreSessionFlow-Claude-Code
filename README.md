<p align="center">
  <img src="https://ormus.solutions/mascot/pixellab_liquid_to_ouroboros.gif" alt="LibreSessionFlow Claude Code" width="128" style="image-rendering: pixelated;" />
</p>

<h1 align="center">LibreSessionFlow Claude Code</h1>

<p align="center">
  <em>Session lifecycle for Claude Code — 10 plugins making multi-session work resumable, context survive context-clear, new sessions start where the last one ended</em>
</p>

<p align="center">
  <a href="https://github.com/HermeticOrmus/LibreSessionFlow-Claude-Code/stargazers"><img src="https://img.shields.io/github/stars/HermeticOrmus/LibreSessionFlow-Claude-Code?style=flat-square&color=aa8142" alt="Stars" /></a>
  <a href="https://github.com/HermeticOrmus/LibreSessionFlow-Claude-Code/blob/main/LICENSE"><img src="https://img.shields.io/github/license/HermeticOrmus/LibreSessionFlow-Claude-Code?style=flat-square&color=aa8142" alt="License" /></a>
  <img src="https://img.shields.io/badge/Session_Lifecycle-aa8142?style=flat-square" alt="Session Lifecycle" />
  <img src="https://img.shields.io/badge/Claude_Code-aa8142?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code" />
</p>

---

> **Skills, agents, commands, and workflows for session lifecycle in Claude Code.**

Sessions end. Context clears. You switch machines. You sleep. The next session starts fresh, and unless you've captured state somewhere, the model has no memory of yesterday's decisions, false leads, half-finished work.

LibreSessionFlow packages the discipline of session continuity into 10 plugins. **Make multi-session work resumable. Make context survive context-clear. Make new sessions start where the last one ended.**

---

## The session lifecycle

```
START → /pickup → work → /handoff → END
   ↑                                  ↓
   └──── HANDOFF.md persists state ───┘
```

Five-stage cycle, instrumented:

| Stage | Plugin | Purpose |
|---|---|---|
| **Entry** | `/pickup` | Read HANDOFF.md, restore context, verify "done" is still done |
| **Work** | `/explore`, `/grab`, `/todo`, `/share-prompt`, `/meet` | Tools used during the session |
| **Mid-session** | `/maintain` | Environment hygiene, MCP health |
| **Exit** | `/handoff`, `/close` | Capture state, write the handoff, end the ritual |
| **Post-session** | `/absorb` | Distill what was learned into persistent memory |

---

## The 10 plugins

### Cycle entry + exit (the core)

| Plugin | Command | What it does |
|---|---|---|
| **handoff** ⭐ | `/handoff` | Write HANDOFF.md at session end. Captures what's done, what's not, key context not visible in the diff, verify commands. The discipline behind making work resumable. |
| **pickup** | `/pickup` | Read HANDOFF.md at session start. Verify "done" is still done. Restore context before doing anything else. The companion ritual to handoff. |
| **close** | `/close` | End-of-session ritual: update memory, write summary, notify next-self via WhatsApp/Slack/email, exit cleanly. |

### Mid-session tools

| Plugin | Command | What it does |
|---|---|---|
| **explore** | `/explore` | Token-optimized AST-based code search. Map a codebase structure without burning context on full-file reads. 4-8× cheaper than naive grep+read. |
| **grab** | `/grab` | Pull the latest shell command, URL, or AI-generated text into the system clipboard. Cuts the copy-from-terminal-to-elsewhere step. |
| **todo** | `/todo` | Quick-capture a TODO into the current project's TODO.md without breaking the active flow. |
| **share-prompt** | `/share-prompt` | Send a prompt to a coworker in real-time, wrapped for paste-and-go into their own Claude Code session. |
| **meet** | `/meet` | Ingest a new collaborator, client, or unknown name into persistent context. Web research + GitHub recon + memory file write. |

### Post-session integration

| Plugin | Command | What it does |
|---|---|---|
| **absorb** | `/absorb` | Distill what the session taught into persistent memory. Promotes ephemeral session learning to durable cross-session knowledge. |
| **maintain** | `/maintain` | Environment hygiene: MCP health checks, sync-conflict detection, tool-usage analysis, periodic skill audit. |

⭐ = the flagship plugin. Since 1.0.0 every plugin ships a working slash command and skill (10 commands, 10 skills, 1 agent, 3 helper scripts); before that, nine of them were README-only.

---

## Quick start

### Install from Claude Code

```
/plugin marketplace add HermeticOrmus/LibreSessionFlow-Claude-Code
/plugin install handoff@libre-sessionflow
/plugin install pickup@libre-sessionflow
```

Install any of the ten the same way (`absorb`, `close`, `explore`, `grab`, `handoff`, `maintain`, `meet`, `pickup`, `share-prompt`, `todo`). From a terminal, the equivalent is:

```bash
claude plugin marketplace add HermeticOrmus/LibreSessionFlow-Claude-Code
claude plugin install handoff@libre-sessionflow
```

Or clone the repo and let `setup.sh` register the marketplace and install every plugin (`./setup.sh --list` shows them, `./setup.sh --only handoff,pickup` installs a subset, `./setup.sh --uninstall` removes them). This pack has no hooks plugin: nothing runs unless you invoke it.

### Install in Grok Build

Grok Build reads the same plugin folders. Add the marketplace, then install any of the ten by name:

```bash
grok plugin marketplace add HermeticOrmus/LibreSessionFlow-Claude-Code
grok plugin install handoff@LibreSessionFlow-Claude-Code --trust
grok plugin install pickup@LibreSessionFlow-Claude-Code --trust
```

Grok asks you to trust a plugin before it installs it; `--trust` is that answer. To install one plugin straight from its folder, without the marketplace:

```bash
grok plugin install HermeticOrmus/LibreSessionFlow-Claude-Code#plugins/handoff --trust
```

From a clone, `./setup.sh --grok` installs all ten into Grok Build, with the same `--only`, `--list`, and `--uninstall` options. Two limits are known and tracked in [LEDGER.md](LEDGER.md): nine of the ten commands read their skill through `${CLAUDE_PLUGIN_ROOT}`, which Grok Build documents for hooks only, so those commands have not been verified in a live Grok session yet; and `grab` and `maintain` read Claude Code's own transcripts and settings, so under Grok Build they see Claude Code's sessions, not Grok's.

### From a clone

```bash
git clone https://github.com/HermeticOrmus/LibreSessionFlow-Claude-Code.git ~/projects/LibreSessionFlow-Claude-Code
cd ~/projects/LibreSessionFlow-Claude-Code
./setup.sh
```

Restart Claude Code. Then at the end of your next session:

```
/handoff
```

That writes HANDOFF.md. Open a new session tomorrow:

```
/pickup
```

It reads HANDOFF.md and restores context. See [QUICK_START.md](QUICK_START.md) for the full first-week walkthrough.

### Settings (optional)

Everything works with no setup. To change where memory, handoff indexes, and session summaries go, where `/close` sends its summary, or who `/share-prompt` can reach, copy [`sessionflow.example.json`](sessionflow.example.json) to `~/.claude/sessionflow.json` and keep only the keys you need. Environment variables (`SESSIONFLOW_HOME`, `SESSIONFLOW_MEMORY_DIR`, `SESSIONFLOW_NOTIFY_CMD`, `SESSIONFLOW_CONFIG`) override the file. The file stays on your machine.

---

## Learning paths

- **[Beginner](learning-paths/beginner.md)** — your first handoff + pickup cycle
- **[Intermediate](learning-paths/intermediate.md)** — multi-machine, multi-day sessions; absorb learning patterns
- **[Advanced](learning-paths/advanced.md)** — team handoffs, async collaboration, multi-project session juggling

---

## Why this exists

I started instrumenting my Claude Code sessions because I kept hitting the same wall: a great session ends, I open a new one a day later, the new model has no idea what we did or why. I'd waste 20 minutes re-establishing context, sometimes re-discovering things I'd already learned.

The fix wasn't a tool. It was a discipline:

- At session end, write what's done, what's not, what's tricky.
- At session start, read that, verify, then continue.
- Periodically, promote session learnings to persistent memory.

This repo packages that discipline as Claude Code skills + the auxiliary tools (clipboard grabbing, AST exploration, meet-a-new-person) that make the discipline feel natural rather than overhead.

It supersedes a small family of single-purpose ormus-* repos that had this functionality scattered across multiple zero-star projects.

---

## Companion: session-handoff-skills (mini-repo)

The discipline as a single CLAUDE.md drop-in: [`session-handoff-skills`](https://github.com/HermeticOrmus/session-handoff-skills). Use that if you want the rules without the full plugin bundle. Use LibreSessionFlow if you want the working tools.

---

## Compatibility

- **Claude Code**: 2.1 or later (plugin marketplaces; tested on 2.1.285)
- **Cursor**: skill subset works via `.cursor/rules/`
- **OS**: Linux + macOS (Windows via WSL2 should work but untested)

---

## Feedback

Starred this? Tell us what worked and what is missing: [open a feedback issue](https://github.com/HermeticOrmus/LibreSessionFlow-Claude-Code/issues/new?template=feedback.yml). Every piece of feedback gets an answer, and changes that come from it are credited in the release notes.

## Contribute

- Cracks we found and sealed: [LEDGER.md](LEDGER.md). The open rows are work anyone can pick up.
- Pick up the next piece of work from the [Menu](pantry/MENU.md): each item has a Done-when anyone can check, and the research behind it is in [`pantry/`](pantry/).
- New here? Start with the [good first issues](https://github.com/HermeticOrmus/LibreSessionFlow-Claude-Code/contribute).
- Claude picked the wrong plugin? File a [routing miss](https://github.com/HermeticOrmus/LibreSessionFlow-Claude-Code/issues/new?template=routing-miss.yml). Want a new plugin? Open a [plugin proposal](https://github.com/HermeticOrmus/LibreSessionFlow-Claude-Code/issues/new?template=plugin-proposal.yml). Anything else goes in a [feedback issue](https://github.com/HermeticOrmus/LibreSessionFlow-Claude-Code/issues/new?template=feedback.yml).
- Show what you built in [Discussions](https://github.com/HermeticOrmus/LibreSessionFlow-Claude-Code/discussions). The full guide is in [CONTRIBUTING.md](CONTRIBUTING.md#ways-to-contribute).

## Contributing

PRs welcome — especially: more handoff templates for specific scenarios, examples of pickup flows for multi-machine work, integration with team chat tools beyond what's covered.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT © 2026 [Diego Bodart](https://github.com/HermeticOrmus) — see [LICENSE](LICENSE). Built under the [Gold Hat principle](GOLD_HAT.md).

---

## Part of the Libre Open-Source Stack for Claude Code

This repository is part of a growing family of open-source toolkits for Claude Code.

### Libre suite — comprehensive plugin bundles

- [LibreUIUX-Claude-Code](https://github.com/HermeticOrmus/LibreUIUX-Claude-Code) — UI/UX development (152 agents, 70 plugins, 76 commands, 74 skills)
- [LibreArch-Claude-Code](https://github.com/HermeticOrmus/LibreArch-Claude-Code) — Software architecture and system design
- [LibreCopy-Claude-Code](https://github.com/HermeticOrmus/LibreCopy-Claude-Code) — Technical writing and documentation engineering
- [LibreDevOps-Claude-Code](https://github.com/HermeticOrmus/LibreDevOps-Claude-Code) — DevOps engineering and infrastructure automation
- [LibreEmbed-Claude-Code](https://github.com/HermeticOrmus/LibreEmbed-Claude-Code) — Embedded systems, firmware, and IoT development
- [LibreFinTech-Claude-Code](https://github.com/HermeticOrmus/LibreFinTech-Claude-Code) — Financial technology development
- [LibreGEO-Claude-Code](https://github.com/HermeticOrmus/LibreGEO-Claude-Code) — AI-search optimization (ChatGPT, Perplexity, Gemini, Google AI Overviews)
- [LibreGameDev-Claude-Code](https://github.com/HermeticOrmus/LibreGameDev-Claude-Code) — Game development across Godot, Unity, Unreal
- [LibreMLOps-Claude-Code](https://github.com/HermeticOrmus/LibreMLOps-Claude-Code) — ML engineering and AI operations
- [LibreMobileDev-Claude-Code](https://github.com/HermeticOrmus/LibreMobileDev-Claude-Code) — Mobile app development (Flutter, React Native, native iOS, native Android)
- [LibreSecOps-Claude-Code](https://github.com/HermeticOrmus/LibreSecOps-Claude-Code) — Security operations

### Skills mini-repos — single CLAUDE.md drop-ins

- [vibe-engineer-skills](https://github.com/HermeticOrmus/vibe-engineer-skills) — Direct AI codegen well: hypothesis before help, scoped prompts, validate before accepting
- [markdown-discipline-skills](https://github.com/HermeticOrmus/markdown-discipline-skills) — Strip AI-slop from markdown (no em dashes, no marketing fluff)
- [shell-safety-skills](https://github.com/HermeticOrmus/shell-safety-skills) — `set -euo pipefail` discipline plus 15 failure-mode examples
- [commit-standard-skills](https://github.com/HermeticOrmus/commit-standard-skills) — Ormus Commit Standard v1.0 plus commit-msg hook and commitlint
- [unwoke-skills](https://github.com/HermeticOrmus/unwoke-skills) — Strip AI theater (ten sins to eliminate, symmetric engagement)
- [python-conventions-skills](https://github.com/HermeticOrmus/python-conventions-skills) — Modern Python 3.11+ (types, pathlib, async, ruff, mypy, uv)
- [typescript-conventions-skills](https://github.com/HermeticOrmus/typescript-conventions-skills) — TypeScript strict mode, discriminated unions, Result types
- [hermetic-laws-skills](https://github.com/HermeticOrmus/hermetic-laws-skills) — Seven Hermetic Principles applied to engineering
- [riper-workflow-skills](https://github.com/HermeticOrmus/riper-workflow-skills) — Research / Innovate / Plan / Execute / Review systematic dev
- [six-day-cycle-skills](https://github.com/HermeticOrmus/six-day-cycle-skills) — Sustainable shipping cadence with mandatory rest
- [token-optimization-skills](https://github.com/HermeticOrmus/token-optimization-skills) — Claude Code token and context optimization
- [osint-skills](https://github.com/HermeticOrmus/osint-skills) — OSINT research methodology (multi-wave investigative spiral)
- [calcinate-skills](https://github.com/HermeticOrmus/calcinate-skills) — Stage 1 of the Magnum Opus (burn project bloat)
- [claude-md-overhaul-skills](https://github.com/HermeticOrmus/claude-md-overhaul-skills) — Audit CLAUDE.md and MEMORY.md against caps
- [session-handoff-skills](https://github.com/HermeticOrmus/session-handoff-skills) — Session handoff and pickup discipline
- [naming-skills](https://github.com/HermeticOrmus/naming-skills) — Product naming methodology (mine the brand's vocabulary)
- [magnum-opus-skills](https://github.com/HermeticOrmus/magnum-opus-skills) — Seven-stage alchemy applied to project transformation
- [mem-search-skills](https://github.com/HermeticOrmus/mem-search-skills) — Search claude-mem cross-session memory: search, filter, fetch
- [hypothesis-debugging-skills](https://github.com/HermeticOrmus/hypothesis-debugging-skills) — Hypothesis-driven debugging: reproduce, isolate, test, fix
- [vibe-proof-skills](https://github.com/HermeticOrmus/vibe-proof-skills) — Security hardening for vibe-coded full-stack apps
- [tdd-skills](https://github.com/HermeticOrmus/tdd-skills) — Test-driven development (Red-Green-Refactor) for JS/TS and Python
- [mars-skills](https://github.com/HermeticOrmus/mars-skills) — Production-readiness audit: the five mortal sins of vibe-coded MVPs
- [git-workflow-skills](https://github.com/HermeticOrmus/git-workflow-skills) — Clean git workflow: branch, atomic commits, reviewable PRs
- [code-review-skills](https://github.com/HermeticOrmus/code-review-skills) — Domain-aware code review: classify the code, then focus
- [code-comprehension-skills](https://github.com/HermeticOrmus/code-comprehension-skills) — Understand an unfamiliar codebase fast
- [dx-audit-skills](https://github.com/HermeticOrmus/dx-audit-skills) — Audit developer experience: docs, onboarding, tooling friction
- [setup-env-skills](https://github.com/HermeticOrmus/setup-env-skills) — Set up a project's development environment
- [automate-skills](https://github.com/HermeticOrmus/automate-skills) — Turn repetitive tasks into reliable automation scripts
- [quick-fix-skills](https://github.com/HermeticOrmus/quick-fix-skills) — Fast troubleshooting for common issues
- [prime-context-skills](https://github.com/HermeticOrmus/prime-context-skills) — Prime project context at the start of a session
- [auto-docs-skills](https://github.com/HermeticOrmus/auto-docs-skills) — Generate and maintain project documentation
- [learning-skills](https://github.com/HermeticOrmus/learning-skills) — Learn any technology: roadmaps, explanations, practice, cheatsheets, comparisons
- [linux-sysadmin-skills](https://github.com/HermeticOrmus/linux-sysadmin-skills) — Linux system administration: security, performance, diagnostics, monitoring, maintenance

### Template source

- [andrej-karpathy-skills](https://github.com/HermeticOrmus/andrej-karpathy-skills) — the canonical single-file CLAUDE.md pattern (fork of jiayuan_jy's original)

Star the family, not just one — that's how the suite stays coherent.
