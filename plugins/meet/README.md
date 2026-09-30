# Meet

> Ingest a new collaborator, client, or unknown name into Claude's persistent context.

## What it does

- Web research on the person/company
- GitHub recon (your own account's repos and code, plus their public profile if the name maps to a username)
- Local memory search for prior interactions
- Optional brand harvest from prior shipped work for that person
- Writes a persistent contact memory file

## Contents

- **Command**: `/meet <full name> [context hint]`
- **Skill**: `person-intake`

## Settings (optional)

In `~/.claude/sessionflow.json` (see [`sessionflow.example.json`](../../sessionflow.example.json)):

- `meet.github_owner`: the GitHub user or org to search; default is the account `gh` is logged in as
- `meet.search_paths`: local folders to search; default is the current project plus `~/projects`
- `memory_dir`: where the contact file goes; default is the project's auto memory folder

## Privacy

Only what is material to working with the person is saved: no home addresses, age, family details, or personal numbers. Nothing is fabricated; missing facts stay missing.
