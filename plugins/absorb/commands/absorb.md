---
description: Distill what this session taught into persistent memory files
argument-hint: "[@project:<name>] [@dry]"
---

# /absorb

Read `${CLAUDE_PLUGIN_ROOT}/skills/absorb-learnings/SKILL.md` and follow it exactly.

Arguments: $ARGUMENTS

1. Resolve the memory folder (settings, then the project's auto memory folder, then `<project root>/.claude/memory/`).
2. Extract knowledge the code cannot show, classify it, and drop noise and duplicates.
3. Merge against what is already saved; new observations win over old assumptions.
4. Write topic files and the `MEMORY.md` index (or, with `@dry`, only show the plan).
5. Print the ABSORBED report with every file touched.
