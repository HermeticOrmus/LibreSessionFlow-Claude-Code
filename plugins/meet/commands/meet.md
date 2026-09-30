---
description: Research a person once and save a contact memory file (web, local projects, your GitHub)
argument-hint: "<full name> [context hint]"
disable-model-invocation: true
---

# /meet

Read `${CLAUDE_PLUGIN_ROOT}/skills/person-intake/SKILL.md` and follow it exactly.

Arguments: $ARGUMENTS

1. Check memory first; an existing contact file ends the run unless a refresh was asked for.
2. Research their public presence and read two or three canonical sources.
3. Search your local projects and your own GitHub account for prior work with them; harvest brand tokens from any match.
4. Write `contact_<lastname>_<firstname>.md` into the memory folder and index it in `MEMORY.md`.
5. Report who they are, prior work found, files written, and sources.
