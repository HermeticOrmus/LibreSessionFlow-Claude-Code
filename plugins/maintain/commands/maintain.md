---
description: Audit the Claude Code setup (MCP health, plugins, sync conflicts, settings, memory size, usage, hooks) and fix only what you approve
argument-hint: "[mcp | plugins | conflicts | settings | memory | usage | hooks | report]"
disable-model-invocation: true
---

# /maintain

Read `${CLAUDE_PLUGIN_ROOT}/skills/environment-maintenance/SKILL.md` and follow it.

Focus, if given: $ARGUMENTS (with no focus, run the quick scan and ask where to start)

1. Run the read-only quick scan: `claude mcp list`, `claude plugin list`, conflict copies, settings validity, CLAUDE.md and MEMORY.md size, and `python3 ${CLAUDE_PLUGIN_ROOT}/bin/usage.py --recent 50`.
2. Show one status row per area and ask which to work on.
3. Propose fixes; apply each only after a yes. Move files into the dated trash folder instead of deleting.
4. Summarize what was found, fixed, and left.
