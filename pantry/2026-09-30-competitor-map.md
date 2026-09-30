# Competitor map: LibreSessionFlow-Claude-Code

## How this fills

1. Name the product and its surfaces (plugins, agents, skills, commands, install paths).
2. WebSearch / WebFetch public competitor docs, READMEs and homepages: other Claude Code plugin packs and marketplaces in this domain, Cursor rules and plugins, Codex or Gemini CLI extensions, and standalone tools people use for the same job.
3. One row per competitor; blank unknowns; cite a URL per row.
4. Fill the capabilities matrix (Y / N / P / ?) with the capabilities that matter in this domain, and a source per claimed cell.
5. Save as `YYYY-MM-DD-competitor-map.md` (keep this template).

## Product

- Name: LibreSessionFlow-Claude-Code, v1.0.0 (read from `main` at `c5822d8` on 2026-09-30)
- Flagship: `handoff` (`/handoff` writes a HANDOFF.md and indexes it) with its reader `pickup` (`/pickup` finds it, re-runs its verify commands, and shows the next action)
- Our surfaces: 10 plugins in the marketplace `libre-sessionflow` (`absorb`, `close`, `explore`, `grab`, `handoff`, `maintain`, `meet`, `pickup`, `share-prompt`, `todo`), each with one slash command and one skill (`user-invocable: false`); one agent (`handoff-engineer`); three helper scripts (`explore/bin/outline.py`, `grab/bin/grab.py`, `maintain/bin/usage.py`); optional settings in `sessionflow.example.json`. No hooks: nothing runs unless invoked. Install: `/plugin marketplace add HermeticOrmus/LibreSessionFlow-Claude-Code`, then `/plugin install <name>@libre-sessionflow`.

Star counts are from the GitHub API (`gh api repos/<owner>/<repo>`) on 2026-09-30.

## Map

| Competitor | What it is | Overlap with us | Watch / differentiator | Source URL |
|------------|------------|-----------------|------------------------|------------|
| Claude Code built-ins (CLAUDE.md, auto memory, `--continue` / `--resume`) | Memory and session features that ship in Claude Code itself | `absorb` (memory), `pickup` (resume), `close` | Auto memory is on by default and writes `~/.claude/projects/<project>/memory/` with a `MEMORY.md` index (first 200 lines or 25KB load each session); `claude --continue` and `claude --resume` restore saved conversations; docs say auto memory is machine-local | https://code.claude.com/docs/en/memory |
| thedotmack/claude-mem (95,015 stars, Apache-2.0) | Claude Code plugin that captures sessions through lifecycle hooks, compresses them, and injects context into new sessions | `absorb`, `pickup`, `close` | Five lifecycle hooks, SQLite with FTS5 plus a Chroma vector store, `mem-search` skill, web viewer, `<private>` tags; installs for other agents too (OpenCode, Antigravity CLI); the `npx` installer asks you to sign in unless you pass `--provider`; README in many languages | https://github.com/thedotmack/claude-mem |
| ostikwhy-blip/claude-code-handoff-skill (26 stars, MIT) | A Claude Code skill that writes a verified HANDOFF.md at the project root | `handoff`, `pickup` | Runs `git status`, `git log`, `git diff` and the tests before writing, tags each claim `[V]` verified or `[?]` recalled, and re-verifies `[V]` claims on resume; installed by copying into `~/.claude/skills` | https://github.com/ostikwhy-blip/claude-code-handoff-skill |
| basicmachines-co/basic-memory (4,068 stars, AGPL-3.0) | MCP server that keeps knowledge as local Markdown files the AI and the user both read, write and search | `absorb`, `meet`, `pickup` | Semantic search, works from any MCP client (Claude, Codex, Cursor, ChatGPT), optional paid cloud sync and a Teams workspace | https://github.com/basicmachines-co/basic-memory |
| oraios/serena (29,914 stars) | MCP toolkit for symbol-level code retrieval and editing, with a memory system | `explore` | Symbol-level tools across languages; README says not to install it through an MCP or plugin marketplace | https://github.com/oraios/serena |
| vanzan01/cursor-memory-bank (3,059 stars, no license file) | Cursor commands and rules (`/van`, `/plan`, `/creative`, `/build`, `/reflect`, `/archive`) over memory bank files | `handoff`, `pickup`, `todo` | Keeps `tasks.md`, `activeContext.md` and `progress.md` as the running state; Cursor only | https://github.com/vanzan01/cursor-memory-bank |
| Cline Memory Bank (docs pattern) | A structured set of Markdown files Cline reads to keep context across sessions | `handoff`, `absorb` | Six core files (`projectbrief.md`, `productContext.md`, `activeContext.md`, `systemPatterns.md`, `techContext.md`, `progress.md`); the user says "update memory bank" | https://docs.cline.bot/prompting/cline-memory-bank |
| Gemini CLI session management and Auto Memory (google-gemini/gemini-cli, 107,194 stars) | Built-in session saving, `gemini --resume`, checkpointing with `/restore`, and an experimental Auto Memory | `pickup`, `absorb` | Sessions save automatically per project; Auto Memory (off by default) mines past sessions and drafts memory patches and `SKILL.md` files into an inbox that the user approves | https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/auto-memory.md |

## Capabilities matrix

Mark Y / N / P (partial) / ? and cite. Rows are the capabilities that matter for this domain.

Columns: Us = LibreSessionFlow v1.0.0 on `main`; CC = Claude Code built-ins; Mem = claude-mem; HS = claude-code-handoff-skill; BM = basic-memory; Ser = serena; CMB = cursor-memory-bank; Cline = Cline Memory Bank; Gem = Gemini CLI.

| Capability | Us | CC | Mem | HS | BM | Ser | CMB | Cline | Gem | Source notes |
|------------|----|----|-----|----|----|-----|-----|-------|-----|--------------|
| Installs as a Claude Code plugin from a marketplace | Y | Y | Y | N | N | N | N | N | N | Us: README Quick start. CC: built in. Mem: README "/plugin marketplace add thedotmack/claude-mem". HS: README Install copies into `~/.claude/skills`. BM: MCP server. Ser: README says not to use a plugin marketplace. CMB: Cursor. Cline, Gem: other agents. |
| Handoff document written at session end | Y | N | P | Y | ? | ? | P | P | N | Us: `plugins/handoff/commands/handoff.md`. Mem: automatic summaries, not a handoff file. HS: README "writes a verified HANDOFF.md". CMB: `activeContext.md`, `progress.md`. Cline: `activeContext.md`, `progress.md`. |
| Verifies repo state before writing the handoff | P | N | ? | Y | ? | ? | ? | ? | N | Us: the template records verify commands and `pickup` runs them later; the handoff command has no step that runs `git status` or the tests before drafting. HS: README "Runs git status, git log, git diff" and "Re-runs your tests" before writing. |
| Resume re-checks done items against the repo | Y | N | ? | Y | ? | ? | ? | ? | N | Us: `pickup` re-runs verify commands and marks each item still done, drifted, or not checkable (CHANGELOG 1.0.0). HS: "re-verifies the [V] claims against the current repo and reports any drift". CC and Gem resume the conversation as it was. |
| Restores the full conversation | N | Y | P | N | N | N | N | N | Y | Us: restores from the handoff by design. CC: `claude --continue`, `claude --resume`. Mem: injects captured context, not the conversation. Gem: `gemini --resume`. |
| Automatic capture with no command (hooks or background) | N | Y | Y | N | ? | ? | N | N | Y | Us: README "This pack has no hooks plugin: nothing runs unless you invoke it". CC: "Auto memory is on by default". Mem: "5 Lifecycle Hooks". Gem: "Your session history is recorded automatically". |
| Durable cross-session memory files | Y | Y | Y | N | Y | Y | Y | Y | Y | Us: `absorb` writes topic files and a `MEMORY.md` index. CC: auto memory and CLAUDE.md. Mem: SQLite database. BM: Markdown files. Ser: README "Memory Management". CMB, Cline: memory bank files. Gem: Auto Memory patches. |
| Human review before memory is saved | P | N | N | ? | ? | ? | ? | ? | Y | Us: `/absorb @dry` shows the plan; without it `absorb` writes directly. CC: auto memory saves on its own, editable afterwards with `/memory`. Mem: automatic capture. Gem: Auto Memory "never applies them without your approval". |
| Search over past sessions (full-text or semantic) | N | P | Y | N | Y | ? | N | N | P | Us: `pickup` searches the handoff index and project folders, not past sessions. CC: the `/resume` picker has a search. Mem: FTS5 and Chroma hybrid search. BM: "Semantic search". Gem: a session browser for resuming. |
| Token-cheap structural code exploration | Y | N | N | N | N | Y | N | N | N | Us: `explore` with `bin/outline.py`. Ser: symbol-level retrieval tools. |
| Cold start from git history when no handoff exists | Y | N | ? | N | N | ? | N | N | N | Us: `pickup` cold mode (`skills/session-pickup/cold-pickup.md`). |
| Finds handoffs across projects and machines | Y | N | P | N | P | ? | N | N | N | Us: handoff index plus `pickup.remotes` over ssh (`skills/session-pickup/SKILL.md`). CC: "Auto memory is machine-local". Mem: optional Cloud Sync. BM: optional cloud sync. Gem: "Sessions are project-specific". |
| Works in other agents (Cursor, Codex, Gemini CLI, OpenCode) | N | N | Y | N | Y | Y | N | N | N | Us: README Compatibility says "Cursor: skill subset works via `.cursor/rules/`", but the repo ships no `.cursor/` folder. Mem: OpenCode and Antigravity CLI installs, plus `.cursor-plugin` and `.codex-plugin` folders in the repo root. BM: "Claude, Codex, Cursor, ChatGPT". Ser: any MCP client. |
| Memory stays in local files, no hosted service needed | Y | Y | P | Y | Y | ? | Y | Y | Y | Us: settings "The file stays on your machine". CC: machine-local. Mem: the `npx` installer asks for a sign-in unless `--provider` is passed. BM: "Local-first", cloud optional. Gem: `~/.gemini/tmp/<project_hash>/chats/`. |
| Privacy controls for captured content | P | ? | Y | ? | ? | ? | ? | ? | ? | Us: `share-prompt` scans for credentials and `close` says "Never put secrets or tokens in the message"; `handoff` has no credential check, although CONTRIBUTING rejects "Patterns that put credentials in HANDOFF.md". Mem: `<private>` tags. |
| Reports the always-on token cost of what is installed | Y | Y | P | N | N | N | N | N | ? | Us: `maintain` "installed plugins and their always-on token cost". CC: `claude plugin details` prints projected token cost. Mem: "token cost visibility" for memory retrieval. |
| Tests for the helper scripts, run in CI | N | ? | P | N | Y | ? | ? | ? | ? | Us: no tests for `outline.py`, `grab.py` or `usage.py`; CI validates manifests and installs only. Mem: a `tests/` folder in the repo root (CI not checked). BM: README "Tests" badge. HS: the repo holds only `LICENSE`, `README.md`, `SKILL.md` and `assets`. |
| Token-savings claims come with a reproducible method | N | ? | ? | ? | ? | P | ? | ? | ? | Us: README says explore is "4-8× cheaper than naive grep+read" with no method or data. Ser: README describes an evaluation prompt that has an agent run about 20 routine tasks. |
