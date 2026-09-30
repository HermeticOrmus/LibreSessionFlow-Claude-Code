---
description: Restore session context from a HANDOFF.md, from git history, or from a chat thread
argument-hint: "[path | project | chat] [all]"
disable-model-invocation: true
---

# /pickup

Read `${CLAUDE_PLUGIN_ROOT}/skills/session-pickup/SKILL.md` and follow it. Its cold and conversation modes live next to it in the same folder.

Arguments: $ARGUMENTS

1. Route the argument: handoff index first, then a path, a project name, or a chat.
2. Read the HANDOFF.md and load the files it names.
3. Re-run its verify commands (read-only ones directly, state-changing ones only after asking) and mark each item still done, drifted, or not checkable.
4. Present a short orientation that ends in one next action.
5. Enter plan mode before any implementation work; mark the index row as picked up.
6. No handoff: reconstruct context from git history instead and ask what to work on.
