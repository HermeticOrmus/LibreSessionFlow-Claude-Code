# Menu: LibreSessionFlow-Claude-Code

Queue: 2026-09-30-pantry-queue.md
Counts: open 7, in flight 0, shipped 0, parked 0, dropped 0, needs fixing 0

## Steer

- none

## Up next

**builtin-memory-guide**: Explain where the plugins sit next to Claude Code's own memory and resume (`builtin-memory-guide`) (queue #1, high, repo, since 2026-09-30)

- Done when: A section in `README.md` (or `learning-paths/beginner.md`, linked from the README) compares `/handoff` plus `/pickup` with `claude --continue` and `claude --resume`, and `/absorb` with auto memory (`~/.claude/projects/<project>/memory/`, `MEMORY.md` loading its first 200 lines or 25KB), links https://code.claude.com/docs/en/memory, and says when to use which
- Verify on: repo
- Evidence: Map row "Claude Code built-ins"; matrix rows "Restores the full conversation" and "Automatic capture with no command"; X mine rows PawelHuryn ("Avoid --resume (breaks cache)"), altryne, fabienr34, EXM7777 ("/clear your session as soon as you reach a checkpoint")
- Issue: none yet (promote after merge)
- Order: builtin-memory-guide, cursor-rules, handoff-verify-first, helper-tests, absorb-review-gate, explore-savings, handoff-secret-scan
- Tie: builtin-memory-guide over cursor-rules, handoff-verify-first, helper-tests, by key order (jev off)

## Atoms

| Key | Title | State | Confidence | Class | Since | Queue # | Issue | Because |
|-----|-------|-------|------------|-------|-------|---------|-------|---------|
| absorb-review-gate | Show absorb's changes for a yes before writing (`absorb-review-gate`) | open | medium | repo | 2026-09-30 | 6 | - | - |
| builtin-memory-guide | Explain where the plugins sit next to Claude Code's own memory and resume (`builtin-memory-guide`) | open | high | repo | 2026-09-30 | 1 | - | - |
| cursor-rules | Ship the Cursor rules the README promises (`cursor-rules`) | open | high | repo | 2026-09-30 | 2 | - | - |
| explore-savings | Measure the explore token savings (`explore-savings`) | open | medium | repo | 2026-09-30 | 7 | - | - |
| handoff-secret-scan | Scan handoffs for credentials before saving (`handoff-secret-scan`) | open | medium | repo | 2026-09-30 | 5 | - | - |
| handoff-verify-first | Check the repo before writing the handoff (`handoff-verify-first`) | open | high | repo | 2026-09-30 | 3 | - | - |
| helper-tests | Test the three helper scripts in CI (`helper-tests`) | open | high | repo | 2026-09-30 | 4 | - | - |

## Retired

| Key | Title | State | Since | Issue | Because |
|-----|-------|-------|-------|-------|---------|
| none | | | | | |

## Notes

- none
