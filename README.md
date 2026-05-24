<p align="center">
  <img src="https://ormus.solutions/mascot/chain_braces_to_swan.gif" alt="LibreSessionFlow Claude Code" width="128" style="image-rendering: pixelated;" />
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

⭐ = depth-complete plugin (the rest are shell-improved; depth scheduled v0.3-v0.5)

---

## Quick start

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

- **Claude Code**: 1.x+
- **Cursor**: skill subset works via `.cursor/rules/`
- **OS**: Linux + macOS (Windows via WSL2 should work but untested)

---

## Contributing

PRs welcome — especially: more handoff templates for specific scenarios, examples of pickup flows for multi-machine work, integration with team chat tools beyond what's covered.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT © 2026 [Diego Bodart](https://github.com/HermeticOrmus). Built under the [Gold Hat Manifesto](GOLD_HAT.md).
