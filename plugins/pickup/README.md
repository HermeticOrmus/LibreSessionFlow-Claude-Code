# Pickup

> Read HANDOFF.md at session start. Restore context. Verify "done" is still done. Then continue.

The reader-half of the handoff contract. Companion to [handoff](../handoff/).

## What's in here

- Command: `/pickup [path | project | chat] [all]`
- Skill: `session-pickup`, with its cold and conversation modes in the same folder

## What it does

- Finds the right handoff through the index `/handoff` keeps, a path, or a project name
- Verify-command runner that distinguishes "still done" from "drifted" (read-only checks run directly; anything that changes state is shown and needs a yes)
- Multi-task pickup (when several HANDOFFs exist, it lists them and asks which)
- Cold pickup: reconstructs context from git history when no handoff exists
- Pickup-from-social-channel (resume a WhatsApp thread, not just a project) when the LibreWhatsApp pack is installed
- `/pickup <project> all` widens the sweep to your open PRs and issues (`gh`) and the chats you map to the project
- Enters plan mode before implementation work

## Settings (optional)

`pickup.search_paths`, `pickup.remotes` (search another machine over ssh by prefix), and `pickup.chats` in `~/.claude/sessionflow.json`; see [`sessionflow.example.json`](../../sessionflow.example.json).

## Still planned

- Worked examples for: overnight resume, vacation resume, team-handoff resume
