# Pickup, conversation mode

> Used when the argument points at a conversation with a person or a group, not a codebase. The goal is different: orient on the thread's history, the open decision, and the relationship, not on git state.

Conversation mode reads chats through the LibreWhatsApp pack (`/pull`). Without it installed, say that conversation pickup needs LibreWhatsApp (or another `/pull` provider), offer a project pickup instead, and stop.

## Step V1: resolve the chat

1. Strip channel keywords (`conversation`, `chat`, `dm`, `wa`, `whatsapp`, `thread`). What remains is the person or group hint.
2. Resolve it the way `/pull` does: an alias in the LibreWhatsApp registry, a literal chat id, or a match in the `/pull` state files (their `target_alias` and `target_name` fields).
3. Several matches: list them and ask which. None: say `No conversation found for <hint>`, suggest `/meet <name>` to register the person or `/pull wa <id>` with a literal id, and stop.

## Step V2: pull recent messages

Run `/pull <channel> <target>`. Default: the last 30 messages, only what is new since the last pull.

## Step V3: gather context, in order of importance

1. **Who**: the contact memory file `contact_<name>.md` in the memory folder (written by `/meet`), plus the registry entry's style notes. Capture role, register (formal or casual, language), prior decisions, deliverables owed.
2. **Why**: other memory files that mention the person or their project. If the person is tied to a project, include that project's current status.
3. **What was in progress**: earlier session notes (the SessionFlow `sessions/` summaries, handoffs) that mention the name. Search them with `grep -ril "<name>"`; read around the matches only, never whole transcripts.

## Step V4: present

```markdown
## Resumed: conversation with <name>

**Channel**: <channel> · `<chat id>`
**Who**: <one line from contact memory>
**New since last pull**: <N> messages over <date range>
**Register**: <language, formal or casual>

### Thread so far
<chronological distillation. Quote decision-bearing or technical messages verbatim; summarize greetings and small talk.>

### Open decision or question
<the one thing that needs the user's attention, with the options and their trade-offs>

### Broader frame
<two to four bullets of context outside this thread that matters>

### Ready
<one to three possible next moves, each with a one-line trade-off. Do not pick for the user.>
```

## Step V5: finish

- `/pull` already updated its last-seen state.
- Do not enter plan mode; a conversation pickup ends in a reply or a decision, not a code plan.
- Do not draft a reply unless asked. If the user wants one, draft it and hand it to `/push`, which previews before anything is sent.

## Anti-patterns

- Paraphrasing decision-bearing messages. The exact wording is load-bearing; quote it.
- Inventing sentiment. If there is no earlier trail, say `(no earlier notes on this conversation)`.
- Pivoting to project work. If the chat is about a project, keep the conversation as the frame and link to the project.
