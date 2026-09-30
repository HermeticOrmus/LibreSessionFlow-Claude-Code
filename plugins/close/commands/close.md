---
description: Run the end-of-session ritual (handoff, memory, summary, optional notification) and end the session
disable-model-invocation: true
---

# /close

Read `${CLAUDE_PLUGIN_ROOT}/skills/session-close/SKILL.md` and follow every step in order.

Extra instructions from the user, if any: $ARGUMENTS

1. Audit the session: work done, decisions, state, open threads, learnings.
2. Write a handoff if work is unfinished.
3. Save durable learnings to memory.
4. Write the session summary under the SessionFlow home folder.
5. Offer to commit finished work; never commit without a yes.
6. Notify only through what the user configured; with nothing configured, print the summary and send nothing.
7. Offer distillation if a reusable pattern emerged, then end the session.
