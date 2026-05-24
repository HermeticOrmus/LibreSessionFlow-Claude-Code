# Quick start

Twenty minutes to your first handoff + pickup cycle.

## 1. Install

```bash
git clone https://github.com/HermeticOrmus/LibreSessionFlow-Claude-Code.git ~/projects/LibreSessionFlow-Claude-Code
cd ~/projects/LibreSessionFlow-Claude-Code
./setup.sh
```

Restart Claude Code so it picks up the plugins.

## 2. Do real work for ~30 minutes

Open Claude Code in any project. Work on something concrete — fix a bug, refactor a function, design a feature. Generate state.

## 3. Run /handoff before ending

```
/handoff
```

The agent will:

- Ask the resume gap (later today? tomorrow? next week?)
- Draft a HANDOFF.md with the right detail level
- Show the draft for review
- Save to `./HANDOFF.md` (or wherever you specify)

Read the draft. Add anything missing. Save.

## 4. End the session

Either `claude --clear` (clears context), exit the terminal, switch machines, sleep — whatever interruption you have.

## 5. Resume — run /pickup

```
/pickup
```

The agent will:

- Read HANDOFF.md
- Run the verify commands to confirm "done" is still done
- Surface the "Next step" + key context not in the diff
- Wait for your confirmation before proceeding

Spend 1-2 minutes reading. Confirm. Continue working.

## 6. After several cycles — run /absorb

Once a week or after a substantial chunk of work:

```
/absorb
```

Promotes things you've learned from across multiple sessions into persistent project memory at `~/.claude/projects/`. The HANDOFF was for THIS task; absorb is for cross-task learning that should outlive this task.

## 7. Periodically — run /maintain

Monthly hygiene:

```
/maintain
```

Audits MCP health, sync conflicts, skill usage, settings drift. Catches problems before they bite.

## What's gained after a month

After a month of disciplined handoff + pickup:

- Multi-day work resumes cleanly
- New machines + sessions inherit context
- No more "wait, why did I..." reconstructions
- Cumulative memory in `~/.claude/projects/` informs every future session
- The session lifecycle becomes invisible — you don't think about it, you just use it

## Troubleshooting

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md).
