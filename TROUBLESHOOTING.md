# Troubleshooting

## Plugins not loaded

```bash
claude plugin list | grep -c '@libre-sessionflow'   # one line per installed plugin, 10 for the full pack
```

Re-run `./setup.sh` (or `/plugin install <name>@libre-sessionflow` inside Claude Code). Restart Claude Code.

Installed with an older `setup.sh` that copied folders into `~/.claude/plugins/libre-sessionflow-*`? Claude Code never loaded those copies. Remove them and install through the marketplace as above.

## /handoff is too detailed for my session

The agent calibrates to the resume gap. If it asks "what's the gap?" and you say "overnight," it'll write a 40-80 line handoff. If you say "vacation," it'll write 300+. Pick the smallest gap that fits.

## /pickup didn't find HANDOFF.md

It checks, in order: the handoff index that `/handoff` writes (`~/.claude/sessionflow/handoffs/INDEX.md`, or under `SESSIONFLOW_HOME`), `./HANDOFF.md`, the git root, then recent `HANDOFF.md` files under the search paths (`~/projects` by default). Handoffs written by hand are not in the index. If your handoff is elsewhere, pass the path: `/pickup ~/some/other/path/HANDOFF.md`.

## I keep writing redundant info between HANDOFF and PR description

They serve different audiences:

- **HANDOFF**: future-you (or teammate); diff-invisible context
- **PR description**: customer-facing summary; what the change does

If both are essentially the same, the PR description is probably the right place for that audience, and the HANDOFF is over-detailing.

## I forgot to run /handoff at session end

Solutions:

1. Add a Claude Code hook that prompts for `/handoff` on session end (see settings.json hooks)
2. Set up `/close` to be the only acceptable exit ritual (forces the handoff)
3. Live with occasional missed handoffs; the discipline pays back even at partial adherence

## /grab says no clipboard tool was found

It looks for `wl-copy`, `xclip`, `xsel`, `pbcopy`, and `clip.exe`. Install one, or set `GRAB_CLIPBOARD_CMD` to your own command. Over ssh without a display there is no clipboard to reach; `--dry-run` prints the text instead.

## /close did not notify me

Nothing is sent until you configure it. Set `notify.command` (or `SESSIONFLOW_NOTIFY_CMD`) to a command that reads the message on stdin, or `notify.push_target` if you use LibreWhatsApp. See `sessionflow.example.json`.
