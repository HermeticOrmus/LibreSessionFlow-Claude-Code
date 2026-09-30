# Absorb

> After a session ends, distill what was learned into persistent memory.

HANDOFF.md captures state for the next session of THIS task. Absorb promotes learning to durable cross-session knowledge — things that should outlive this specific task.

## Contents

- **Command**: `/absorb [@project:<name>] [@dry]`
- **Skill**: `absorb-learnings`, the method; Claude also uses it on its own when you say "remember what we learned"

## What it does

- Scans the session for knowledge the code cannot show: intent, direction, domain rules, decisions with their reasons, stakeholder context, working preferences
- Classifies each finding, drops noise and duplicates, and merges with what memory already holds (new observations win, with the reason)
- Writes topic files (`project_<name>.md`, `feedback_<topic>.md`, `reference_<topic>.md`) and keeps `MEMORY.md` a one-line-per-entry index
- Proposes CLAUDE.md lines for findings that are instructions rather than observations
- Refuses to store secrets or ephemeral task state
- `@dry` shows the plan without writing

Heuristics for what belongs in memory vs handoff vs git log vs project docs are part of the skill.

## Where memory goes

1. `SESSIONFLOW_MEMORY_DIR`, or `memory_dir` in `~/.claude/sessionflow.json` (copy [`sessionflow.example.json`](../../sessionflow.example.json))
2. Otherwise the project's Claude Code auto memory folder (`~/.claude/projects/<project>/memory/`), which Claude Code loads at session start
3. Otherwise `<project root>/.claude/memory/`; add `@.claude/memory/MEMORY.md` to the project CLAUDE.md so it loads

No setup is needed for the default.

## Still planned

- Companion to mem-search-skills mini-repo (if shipped)
