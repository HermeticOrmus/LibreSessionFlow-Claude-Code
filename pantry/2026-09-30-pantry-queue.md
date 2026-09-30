# Pantry queue: LibreSessionFlow-Claude-Code

## How this fills

1. Read the latest competitor map, X mine and people mine.
2. Propose 5 to 8 Goal atoms that answer their themes. The Menu needs at least 3.
3. Each atom needs a Done predicate someone else can check on this repo, a surface, the evidence rows it answers, and a confidence (high, medium or low).
4. Save as `YYYY-MM-DD-pantry-queue.md`; the Menu reads the newest one.
5. Retire an atom only with a bullet under "Explicitly not stocked" of the form `<Title>: shipped, PR #N` or `<Title>: parked, <reason>`.

## Atoms

Sources: [competitor map](2026-09-30-competitor-map.md), [X mine](2026-09-30-x-mine.md), [people mine](2026-09-30-people-mine.md) (no outside voices yet).

| # | Title | Done predicate | Surface | Evidence | Confidence |
|---|-------|----------------|---------|----------|------------|
| 1 | Explain where the plugins sit next to Claude Code's own memory and resume (`builtin-memory-guide`) | A section in `README.md` (or `learning-paths/beginner.md`, linked from the README) compares `/handoff` plus `/pickup` with `claude --continue` and `claude --resume`, and `/absorb` with auto memory (`~/.claude/projects/<project>/memory/`, `MEMORY.md` loading its first 200 lines or 25KB), links https://code.claude.com/docs/en/memory, and says when to use which | repo | Map row "Claude Code built-ins"; matrix rows "Restores the full conversation" and "Automatic capture with no command"; X mine rows PawelHuryn ("Avoid --resume (breaks cache)"), altryne, fabienr34, EXM7777 ("/clear your session as soon as you reach a checkpoint") | high |
| 2 | Ship the Cursor rules the README promises (`cursor-rules`) | Either `.cursor/rules/` holds rule files for the handoff and pickup method (each `.mdc` with a `description`) and the README Compatibility line links them, or that line is rewritten to say what works in Cursor today; after the change, every path the README names under Compatibility exists in the repo | repo | Matrix row "Works in other agents (Cursor, Codex, Gemini CLI, OpenCode)" (Us N; claude-mem, basic-memory, serena Y); Map row cursor-memory-bank | high |
| 3 | Check the repo before writing the handoff (`handoff-verify-first`) | `plugins/handoff/commands/handoff.md` and `plugins/handoff/skills/handoff-patterns/SKILL.md` gain a step before drafting that runs `git status`, `git log` for the session's commits and the handoff's own verify commands, and the template marks each "done" item as checked in this session or recalled; `claude plugin validate plugins/handoff` passes | repo | Map row claude-code-handoff-skill (runs git and the tests before writing, `[V]` and `[?]` tags); matrix row "Verifies repo state before writing the handoff" (Us P) | high |
| 4 | Test the three helper scripts in CI (`helper-tests`) | `tests/` holds pytest tests for `plugins/explore/bin/outline.py` (a Python file and one pattern-parsed language), `plugins/grab/bin/grab.py` (latest command, URL and reply from a fixture transcript under a temporary `CLAUDE_CONFIG_DIR`, with `--dry-run`) and `plugins/maintain/bin/usage.py` (`--config-dir` on a fixture); `python -m pytest tests` passes with no network; `.github/workflows/validate.yml` runs it on every pull request | repo | Matrix row "Tests for the helper scripts, run in CI" (Us N; basic-memory Y) | high |
| 5 | Scan handoffs for credentials before saving (`handoff-secret-scan`) | A helper (for example `plugins/handoff/bin/scan.py`) exits non-zero on a fixture containing `api_key = abc123` or a private-key header line and zero on a clean fixture, using the same patterns as `plugins/share-prompt/skills/prompt-sharing/SKILL.md`; `/handoff` and `/close` call it on the draft and stop to ask when it matches; a test covers both fixtures | repo | Matrix row "Privacy controls for captured content" (Us P; claude-mem Y with `<private>` tags); CONTRIBUTING "Not accepted: Patterns that put credentials in HANDOFF.md" | medium |
| 6 | Show absorb's changes for a yes before writing (`absorb-review-gate`) | `/absorb` without `@dry` prints the planned topic-file and `MEMORY.md` changes and writes them only after the user says yes; `@dry` keeps its current behavior; `plugins/absorb/README.md` documents the gate; `claude plugin validate plugins/absorb` passes | repo | Map row Gemini CLI (Auto Memory "never applies them without your approval"); matrix row "Human review before memory is saved" (Us P) | medium |
| 7 | Measure the explore token savings (`explore-savings`) | A committed script (for example `tests/measure_outline.py`) runs `plugins/explore/bin/outline.py` on a pinned public repository commit, compares the outline's size with the full source size of the files it covers, and prints the ratio; `README.md` and `plugins/explore/README.md` state the measured ratio with the command that reproduces it, or mark "4-8× cheaper" as an estimate | repo | Matrix row "Token-savings claims come with a reproducible method" (Us N; serena P); X mine row Mnilax ("Each skill adds context overhead") | medium |

## Explicitly not stocked (and why)

- The `/grab` name clash with LibreWhatsApp (both packs ship a plugin named `grab`; installed together in one clean config, both are enabled and `claude plugin details grab` resolves to this one): stocked in the LibreWhatsApp queue, since the README there calls its `/grab` the WhatsApp-specific variant.
- Automatic capture through hooks: the matrix shows claude-mem and Claude Code's own auto memory do it, but this pack is invoke-only by design ("nothing runs unless you invoke it"). Revisit only if people ask for it in the people mine.
- Search over past session transcripts: claude-mem and basic-memory cover it with databases; not an atom until the people mine shows demand.
