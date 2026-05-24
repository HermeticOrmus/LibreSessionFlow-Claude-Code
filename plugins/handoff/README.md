# Handoff

> Capture session state at the end. Make tomorrow's session start where today's ended.

## Contents

- **Agent**: `handoff-engineer` — writes HANDOFF.md with the right level of detail for future-you
- **Command**: `/handoff` — orchestrates the capture + saves to project root or `~/dev/<task>/`
- **Skill**: pattern library for what belongs in a handoff vs what's git log territory

## Key capabilities

- **Captures the diff-invisible context**: decisions made, false leads explored, why this approach vs others, things that look weird but aren't
- **Verify commands**: every "done" claim pairs with a command to prove it's still done on resume
- **Open questions**: things unresolved, blocked, needs-decision-before-proceeding
- **Next-step explicit**: not "continue the work" but "edit auth.ts:142 to add the missing null check"
- **Multi-machine aware**: notes which machine the work happened on if it matters
- **Team-aware**: when handing off to another human, includes their context + appreciate-this-first

## When to use

- End of every session > 30 minutes with incomplete work
- Before machine switch (Moon → Sun, etc.)
- Before context-clear or /compact
- Before sleep on a multi-day project
- Before interruption > 4 hours
- When handing off to a teammate

## When NOT to use

- Sessions < 30 minutes with no incomplete work
- One-shot tasks that complete and ship in the same session
- Already wrote a handoff this session; just append rather than re-doing

## Compatibility

Any project, any language. The HANDOFF.md is text and git-tracked; it survives every tool change.
