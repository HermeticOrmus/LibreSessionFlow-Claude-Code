# Pickup

> Read HANDOFF.md at session start. Restore context. Verify "done" is still done. Then continue.

The reader-half of the handoff contract. Companion to [handoff](../handoff/) (which is depth-complete).

## What's in here

- Agent: `pickup-companion` (shell)
- Command: `/pickup` (shell)
- Skill: pickup pattern library (shell)

## Coming in v0.3 (depth pass)

- Full agent prompt detailing the pickup ritual
- Verify-command runner that distinguishes "still done" from "drifted"
- Multi-task pickup (when several HANDOFFs exist in the same project)
- Pickup-from-social-channel (resume a WhatsApp/Discord/email thread, not just a project)
- Worked examples for: overnight resume, vacation resume, team-handoff resume

For now, this plugin is a shell pointing at the depth-complete [handoff](../handoff/) plugin's pickup section.
