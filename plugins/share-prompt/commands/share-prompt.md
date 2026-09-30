---
description: Send a paste-ready prompt to a coworker or yourself (clipboard, gist, your own command, or /push)
argument-hint: "@<handle> <prompt body>"
disable-model-invocation: true
---

# /share-prompt

Read `${CLAUDE_PLUGIN_ROOT}/skills/prompt-sharing/SKILL.md` and follow it exactly.

Arguments: $ARGUMENTS

1. Split the first `@handle` from the prompt body; stop with the syntax if either is missing.
2. Resolve the handle from the `share_prompt` settings; unknown handles get a question, never a guess.
3. Refuse bodies that contain credentials unless the user confirms.
4. Wrap the body in a code fence under "Prompt to paste into your Claude Code session:".
5. Deliver through the resolved transport (clipboard by default) and report in one line.
