# Grab

> Pull the latest shell command, URL, or AI-generated text into the system clipboard. Skip the copy-from-terminal step.

## Usage

```
/grab              # latest Bash tool call from THIS session
/grab link         # latest URL Claude printed
/grab message      # full text of the latest assistant turn
/grab --count 3    # last three, joined
/grab message --skip 2 --hr   # a draft three replies back, without its framing
/grab --dry-run    # print instead of copying
```

Grabbing the latest command from a WhatsApp chat (`/grab wa <alias>`) lives in the [LibreWhatsApp](https://github.com/HermeticOrmus/LibreWhatsApp-Claude-Code) pack's grab plugin, which shares that pack's chat registry.

## Contents

- **Command**: `/grab`
- **Skill**: `clipboard-grab`
- **Script**: `bin/grab.py`, standard library Python; reads this session's transcript under `${CLAUDE_CONFIG_DIR:-~/.claude}/projects/`

## Clipboard

Cross-platform: `wl-copy` (Wayland), `xclip` or `xsel` (X11), `pbcopy` (macOS), `clip.exe` (WSL), or your own command in `GRAB_CLIPBOARD_CMD`. With no clipboard tool (for example over ssh without a display) the script prints the payload and says the copy did not happen.
