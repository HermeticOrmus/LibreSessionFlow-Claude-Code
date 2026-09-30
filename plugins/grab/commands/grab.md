---
description: Copy the latest command, URL, or reply from this session to the clipboard
argument-hint: "[session|link|message] [--count N] [--skip N] [--hr] [--dry-run]"
allowed-tools: Bash(python3 ${CLAUDE_PLUGIN_ROOT}/bin/grab.py:*)
---

# /grab

Run:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/bin/grab.py $ARGUMENTS --session-id "${CLAUDE_SESSION_ID}"
```

Report the script's confirmation line and preview. If it exits non-zero, show its message and say the clipboard was not changed. Do not run or paste what was grabbed.

Details and all options: `${CLAUDE_PLUGIN_ROOT}/skills/clipboard-grab/SKILL.md`.
