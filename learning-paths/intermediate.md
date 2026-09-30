# Intermediate — multi-machine, multi-day, multi-task

## Multi-machine handoff

You work on a laptop during the day, switch to a desktop for evening sessions, sometimes a build server for heavy compute. Each machine has its own state. The handoff needs to bridge them.

Add to HANDOFF.md:

```markdown
## Machine notes
- Branch pushed: yes
- Local-only files needing sync: [list]
- Machine-specific config: [if any]
- Verified working on: laptop
```

The pickup on the other machine starts with: pull latest, run sync, verify branch matches.

## Multi-day handoff

For work that spans 3+ sessions, the project starts accumulating context. Move durable lessons from HANDOFF (per-task) to project memory (~/.claude/projects/<project>/memory/).

Use `/absorb` weekly. It surfaces what's been showing up in HANDOFFs and asks if you want to promote it.

## Multi-task handoff

If you have 4 active tasks, you have 4 HANDOFF.md files. One per task. Stored at `~/dev/<task>/HANDOFF.md`.

`/pickup <task-slug>` picks up the right one through the handoff index. Without an argument, it takes the newest open handoff, and asks when several match.

For work that spans machines, `pickup.remotes` in `~/.claude/sessionflow.json` lets `/pickup <prefix> <project>` search and read a project on another machine over ssh.

## Re-handoff during a session

Long sessions sometimes need a mid-session checkpoint. Run `/handoff` mid-session to capture state-so-far before continuing. This is rare but useful for high-stakes work.

## Next: [Advanced](advanced.md)
