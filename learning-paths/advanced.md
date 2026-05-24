# Advanced — team handoffs, async collaboration, session juggling

## Team handoff

When the handoff is to a teammate (not future-you):

```markdown
## For [name]

Why I'm handing off: [vacation / different expertise / specific block]

What I'd appreciate you doing FIRST:
1. [Specific starting point]
2. [Specific second action]

Where to ping me if questions: [WhatsApp / Slack / email]
Time you can reach me: [hours + timezone]

Branch: [name] (pushed: yes/no)
PR: [#number, state]
```

The "What I'd appreciate you doing FIRST" is the highest-leverage line. It saves the recipient 10-20 minutes of trying to understand where to start.

## Async collaboration

For globally distributed teams, every team member writes handoffs at end-of-day. The next time-zone team picks up via the handoffs. Treat HANDOFF.md as a baton, not a journal.

## Session juggling

Operating 4-8 active projects simultaneously is hard. The portfolio of HANDOFFs is your only sane way to switch between them.

Pattern:

- One HANDOFF per project (at project root)
- `/pickup <project-slug>` or `cd <project>` then `/pickup`
- Spend < 5 minutes reading before doing anything else
- If you can't get oriented in 5 minutes, your last HANDOFF was insufficient — fix the next one

## Incident handoff

If an incident is in progress and you have to hand off mid-incident:

```markdown
## Current incident state
[What's broken; severity; pageable people contacted]

## What I've done in the last hour
[Specific timeline]

## Current hypothesis
[Shape of the issue as I understand it]

## What I've ruled out
[Hypotheses tested + how]

## Next experimental step
[The next thing to try to narrow the root cause]

## Stakeholders + comms
[Who needs updates, on what cadence, via what channel]
```

This template is also good for `pickup` during incident response — it ensures the new on-call doesn't waste time re-discovering ground.

## What's still hard

- **Handoff fatigue**: writing a handoff feels like overhead in the moment. The discipline pays back invisibly. Trust the math.
- **Over-detailing**: every line in a handoff is a line someone has to read. Calibrate to the gap.
- **Team handoffs across time zones**: synchronous handoffs (Slack call) supplement async handoffs (HANDOFF.md). Don't choose one; use both.
- **Memory pollution**: if too much per-task detail leaks into project memory, the memory becomes noise. Be ruthless about what promotes from HANDOFF to memory.
