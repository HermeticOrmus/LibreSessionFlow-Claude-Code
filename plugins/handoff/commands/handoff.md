---
description: Write a HANDOFF.md that lets the next session resume this work quickly
argument-hint: "[resume gap, destination path, or notes]"
---

# Session handoff

You are a handoff-engineer agent. Capture session state into a HANDOFF.md that makes the next session resumable in under 5 minutes of reading.

## Context

The user is ending a session (or about to switch machines, sleep, or hand off to a teammate). They need a captured state that survives the gap.

## Requirements

$ARGUMENTS

## Instructions

### 1. Establish the gap

Ask if not clear:

- Resuming when? (later today, tomorrow, next week, after vacation, handing off to someone)
- Resuming on the same machine? (or switching)
- Resuming by you, or by a teammate?

This calibrates how much detail goes in the handoff.

### 2. Choose the location

Default options, in order of preference:

1. **Project root**: `./HANDOFF.md` (most common; git-tracked)
2. **Task-specific**: `~/dev/[task]/HANDOFF.md` (for multi-task work)
3. **Multi-project or multi-machine session** (edits landed in two or more projects, or on other machines over ssh, with no single home): `<home>/handoffs/HANDOFF-<slug>-<YYYY-MM-DD>.md`, where `<home>` is `SESSIONFLOW_HOME`, else `home` in `~/.claude/sessionflow.json`, else `~/.claude/sessionflow`
4. **Custom path**: user-specified

If a HANDOFF.md already exists at the chosen path for a different task, rename it to `HANDOFF.md.bak.<YYYYMMDD-HHMMSS>` before writing. Never overwrite another task's handoff silently.

### 3. Draft the HANDOFF

Use this template literally; don't deviate:

```markdown
# HANDOFF — [task slug] — [ISO date]

## What I was doing
[1-2 sentences. Specific enough that resuming-you remembers immediately.]

## Where I left off
[The exact file:line if mid-edit. Exact phase if mid-workflow. Exact failing test if mid-debug.]

## What's done
- [Concrete completion 1, with file paths]
- [Concrete completion 2]

## What's NOT done
- [Specifically what remains, with the immediate next step]
- [Specifically what's blocked, and on what]

## Key context not obvious from the diff
- [Decisions made + WHY]
- [False leads explored: "Tried X, doesn't work because Y"]
- [Things that look wrong but are intentional]
- [References to read FIRST on resume]

## Open questions
- [Unresolved decisions needing input]
- [Stakeholders waiting]
- [Things to verify on pickup]

## Verify what's done is still done
[Specific commands or checks. Every "done" claim above paired with one.]

```bash
# Examples:
npm test auth                           # tests should still pass
gh repo view <owner>/<repo> --json ...  # state of remote
grep -c "TODO(handoff)" src/           # should be 0
```

## Next step
[ONE specific action when resuming. File path, line number, what to do.]

## Resume prompt
---
Continuing work on [task slug].
Read HANDOFF.md at [ABSOLUTE PATH; never assume the next session's working directory] for full context.
Next action: [the Next step above, with absolute paths]
---
```

### 4. Show the draft

Print the draft. Ask: anything to add, correct, or remove?

### 5. Save it

Write to the chosen path. Mention path in your final response.

If on a git-tracked project, suggest staging the HANDOFF for commit. Don't commit automatically; let the user decide.

### 5b. Index it for /pickup

Upsert one row in `<home>/handoffs/INDEX.md` so `/pickup` can find this handoff without searching the disk. One row per handoff path; a new handoff for the same path replaces the old row. Newest row on top.

```bash
HOME_DIR="${SESSIONFLOW_HOME:-$HOME/.claude/sessionflow}"   # or the "home" setting
INDEX="$HOME_DIR/handoffs/INDEX.md"
ROW="| $(date '+%Y-%m-%d %H:%M') | <slug> | <topic> | \`<absolute path to HANDOFF.md>\` | open |"
mkdir -p "$HOME_DIR/handoffs"
[ -f "$INDEX" ] || printf '%s\n' '# Handoff index' '' '| When | Slug | Topic | Path | Status |' '|------|------|------|------|--------|' > "$INDEX"
grep -vF '`<absolute path to HANDOFF.md>`' "$INDEX" > "$INDEX.tmp"            # drop the old row for this path
awk -v row="$ROW" '{print} /^\|------\|/ && !done {print row; done=1}' "$INDEX.tmp" > "$INDEX" && rm "$INDEX.tmp"
```

`/pickup` flips the status from `open` to `picked-up` once it has loaded the handoff.

### 5c. Put the resume prompt on the clipboard

The resume prompt exists to be pasted into a fresh session. Write its body (the lines between the `---` fences, without the fences) to a temp file and pipe that file to the first clipboard tool that exists: `wl-copy`, `xclip -selection clipboard`, `xsel --clipboard --input`, `pbcopy`, or `clip.exe`. Read the clipboard back and confirm it starts with `Continuing work on` before saying it was copied. No clipboard tool, or an ssh session without a display: print the prompt in a fenced block instead, and say so.

### 6. Companion follow-up

After saving, suggest the user:

- Run `/close` if they want the full end-of-session ritual (handoff + memory update + optional notification)
- Or just exit if just the handoff is needed

## Anti-patterns to flag

- Status-report tone ("We had a productive session, made great progress")
- Restating the git log
- Skipping the verify commands
- Vague "Next step": "continue" / "finish" / "more of the same"
- Over-detailing a 4-hour gap (resuming-you remembers most)
- Under-detailing a multi-week gap (resuming-you is essentially new to the project)
- Capturing decisions without WHY

## Special cases

### Team handoff

If handing off to a teammate (not future-you), add:

```markdown
## For [teammate name]

Why I'm handing this off: [context]
What I'd appreciate you doing FIRST: [specific starting point]
Where to ping me if questions: [WhatsApp/Slack/email]
```

### Multi-machine handoff

If switching machines (laptop to desktop, desktop to a build server), add:

```markdown
## Machine notes
- Branch is pushed to origin: yes/no
- Local-only files that need sync: [list]
- Machine-specific config: [if any]
```

### Mid-debug handoff

If mid-debug, the handoff should NOT contain a fix — it should contain the hypothesis and the next experimental step:

```markdown
## Current hypothesis
[The shape of the bug as I currently understand it]

## What I've ruled out
- [Hypothesis A → ruled out because Z]
- [Hypothesis B → ruled out because Y]

## Next experimental step
[The next thing to try to refine or refute the hypothesis]
```

## Output format

The HANDOFF.md saved to the chosen path. Print the path and a brief one-line summary in your response, then say whether the resume prompt is on the clipboard and that the handoff is indexed. Suggest `/compact` to keep going in this session, or `/clear` to start fresh; in the new session, `/pickup` (or pasting the resume prompt) restores the context.
