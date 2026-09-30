# Maintain

> Environment hygiene for the Claude Code setup. Periodic MCP health checks, sync-conflict detection, tool-usage analysis.

## What this covers

- MCP server health (auth state, tool whitelist, reachability)
- Sync conflicts in ~/.claude/ (Syncthing `.sync-conflict-*`, Dropbox "conflicted copy", `.orig` and `.rej` files)
- Skill / agent / command audit (which are unused, which are bloated)
- Plugin always-on token cost, from `claude plugin details`
- Settings.json drift detection (invalid JSON, heavy or risky hooks)
- Auto-memory cap fitting (companion to claude-md-overhaul-skills)

## Contents

- **Command**: `/maintain [mcp | plugins | conflicts | settings | memory | usage | hooks | report]`
- **Skill**: `environment-maintenance`
- **Script**: `bin/usage.py`, counts skill, slash command, subagent, and MCP server use across session transcripts and lists the user-level skills, commands, and agents that never show up

## Safety

Read-only until you approve each change. Files are moved into `~/.claude/sessionflow/trash/<date>/` (relative paths kept), never deleted. Secret-looking values are masked when configs are shown. Reports go to `~/.claude/sessionflow/reports/`.
