# Close

> End-of-session ritual. The full wrap-up: write handoff, update memory, notify next-self, exit cleanly.

## Contents

- **Command**: `/close`
- **Skill**: `session-close`

## What it orchestrates

- `/handoff` to write HANDOFF.md (a short built-in handoff when the handoff plugin is not installed)
- `/absorb` to update persistent memory with session learnings (a short built-in version when absorb is not installed)
- A session summary written to `~/.claude/sessionflow/sessions/<project>/`, outside the repo
- Notification to next-self through a channel you configure (optional)
- Optional: commit + push if the session had a clear shipping outcome, only after you say yes
- Final session summary printed before exit

## Notifications (optional)

With no setup, `/close` prints the summary and sends nothing. To send it somewhere, set one of these in `~/.claude/sessionflow.json` (see [`sessionflow.example.json`](../../sessionflow.example.json)):

- `notify.command` (or `SESSIONFLOW_NOTIFY_CMD`): any shell command that reads the message on stdin, for example an ntfy topic, a Slack or Discord webhook through `curl`, or `cat >> ~/session-log.md`
- `notify.push_target`: a LibreWhatsApp `/push` target such as `wa me`; push previews the message and waits for your confirmation
