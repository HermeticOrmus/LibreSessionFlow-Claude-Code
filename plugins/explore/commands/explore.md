---
description: Map a codebase's structure for a topic, then read only the symbols that matter
argument-hint: "<topic or symbol> [path]"
---

# /explore

Read `${CLAUDE_PLUGIN_ROOT}/skills/structural-explore/SKILL.md` and follow it.

Arguments: $ARGUMENTS (a topic or symbol name, then an optional path; default path is the project root)

1. Search: structural search tools if the session has them, else `python3 ${CLAUDE_PLUGIN_ROOT}/bin/outline.py <path> --search "<topic>"`.
2. Outline the two or three most relevant files if the search did not already show enough structure.
3. Unfold only the symbols the question needs.
4. Answer with file paths and line numbers, and say which symbols you did not read.
