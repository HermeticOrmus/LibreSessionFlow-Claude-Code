---
description: Capture a TODO into the project's TODO.md and keep working, or triage the open items
argument-hint: "<todo text> | triage"
---

# /todo

Read `${CLAUDE_PLUGIN_ROOT}/skills/todo-capture/SKILL.md` and follow it exactly.

Arguments: $ARGUMENTS

- Text given: capture it verbatim into `<project root>/TODO.md` under today's date, confirm in one line, then resume the work that was in progress.
- `triage`: propose a destination for each open item and change nothing until the user approves.
- Nothing given: ask "What's the todo?" in one line and wait.
