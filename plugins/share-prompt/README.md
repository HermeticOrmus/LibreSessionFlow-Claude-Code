# Share Prompt

> Send a prompt to a coworker in real-time, wrapped for paste-and-go into their own Claude Code session.

## Use case

Live handoffs that aren't worth promoting to a SKILL.md or a wiki entry. Just a one-off prompt that solves the specific thing the coworker is stuck on.

## Contents

- **Command**: `/share-prompt @<handle> <prompt body>`
- **Skill**: `prompt-sharing`

## Transports

| Transport | Setup | What happens |
|---|---|---|
| `clipboard` | none (default) | The code-fenced prompt goes to your clipboard; paste it into any chat |
| `gist` | `gh` logged in | A secret GitHub gist; the link goes to your clipboard |
| `command` | a shell command in settings | Your command reads the message on stdin (a Slack or Discord webhook, a mail CLI) |
| `push` | the LibreWhatsApp pack | Handed to `/push`, which previews and waits for your confirmation |

Recipients are named in `share_prompt.recipients` in `~/.claude/sessionflow.json` (see [`sessionflow.example.json`](../../sessionflow.example.json)). Unknown handles get a question, never a guess. Bodies that contain credentials are refused.
