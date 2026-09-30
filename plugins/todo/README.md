# Todo

> Quick-capture a TODO into the current project's TODO.md without breaking the active flow.

## Usage

```
/todo <text>
/todo triage
```

Appends to `./TODO.md` (creating if absent) under today's date, newest date on top. Doesn't pivot Claude's attention; the captured TODO is there for later review, and the session continues where it was.

## Contents

- **Command**: `/todo`
- **Skill**: `todo-capture`

## Triage

`/todo triage` is the pattern library for TODO triage: it proposes, per open item, whether it stays a TODO, becomes a ticket, becomes a memory entry, is already done (with the evidence), or can be dropped. Nothing changes until you approve.
