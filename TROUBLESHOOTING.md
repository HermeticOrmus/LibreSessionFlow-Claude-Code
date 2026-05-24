# Troubleshooting

## Plugins not loaded

```bash
ls ~/.claude/plugins/ | grep -c '^libre-sessionflow-'  # should be 10
```

Re-run `./setup.sh`. Restart Claude Code.

## /handoff is too detailed for my session

The agent calibrates to the resume gap. If it asks "what's the gap?" and you say "overnight," it'll write a 40-80 line handoff. If you say "vacation," it'll write 300+. Pick the smallest gap that fits.

## /pickup didn't find HANDOFF.md

It checks: project root, `~/dev/[task]/HANDOFF.md`, the path stored in the last handoff's "saved to" line. If your handoff is elsewhere, pass the path: `/pickup ~/some/other/path/HANDOFF.md`.

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
