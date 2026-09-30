#!/usr/bin/env python3
"""grab.py: copy the latest shell command(s), URL(s), or assistant message(s)
from the current Claude Code session transcript to the system clipboard.

Sources:
    session (default)  Bash commands Claude ran in this session
    link | url         URLs Claude wrote in its replies
    message | msg      full text of Claude's replies (drafts, emails, prose)

Usage:
    grab.py                         latest Bash command
    grab.py --count 3               last 3 commands, joined by blank lines
    grab.py link                    latest URL from Claude's replies
    grab.py message --skip 2        the reply three turns back
    grab.py message --hr            only the part between the first and last '---' line
    grab.py --dry-run               print instead of touching the clipboard

The transcript is found by session id (--session-id, else the
CLAUDE_CODE_SESSION_ID environment variable), under
${CLAUDE_CONFIG_DIR:-~/.claude}/projects. Without an id it falls back to the
newest transcript of the current directory's project.

Clipboard: GRAB_CLIPBOARD_CMD if set, else the first of wl-copy, xclip, xsel,
pbcopy, clip.exe found on PATH. Standard library only.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterator

Item = tuple[str, str]  # (timestamp, text)

GRAB_SIGNATURE = re.compile(r"grab\.py|(^|\s)/grab\b")
URL_RE = re.compile(r"https?://[^\s<>\"`\]()*]+")
URL_TRAIL = ".,;:!?"
URL_PLACEHOLDER = re.compile(r"\.\.\.|\{|\}|<|>")
SOURCES = {"session": "session", "link": "link", "url": "link", "message": "message", "msg": "message"}
NOUNS = {"session": "command", "link": "URL", "message": "message"}


def config_dir() -> Path:
    return Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude")


def find_transcript(session_id: str) -> Path:
    projects = config_dir() / "projects"
    if session_id:
        for p in projects.glob(f"*/{session_id}.jsonl"):
            return p
    encoded = re.sub(r"[^A-Za-z0-9]", "-", str(Path.cwd()))
    pool_dir = projects / encoded
    if not pool_dir.is_dir():
        pool_dir = projects
    pool = sorted(pool_dir.glob("*.jsonl") if pool_dir != projects else projects.glob("*/*.jsonl"),
                  key=lambda p: p.stat().st_mtime, reverse=True)
    if not pool:
        sys.exit(f"grab: no session transcript found under {projects}")
    return pool[0]


def events(path: Path) -> Iterator[dict[str, Any]]:
    with open(path, encoding="utf-8") as f:
        for line in f:
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def is_real_user_turn(content: Any) -> bool:
    """A user-role event that is a human message, not a tool result."""
    if isinstance(content, str):
        return True
    if isinstance(content, list):
        return not any(isinstance(b, dict) and b.get("type") == "tool_result" for b in content)
    return False


def source_session(path: Path) -> list[Item]:
    out = []
    for evt in events(path):
        content = (evt.get("message") or {}).get("content")
        if not isinstance(content, list):
            continue
        for block in content:
            if isinstance(block, dict) and block.get("type") == "tool_use" and block.get("name") == "Bash":
                cmd = (block.get("input") or {}).get("command", "")
                if cmd and not GRAB_SIGNATURE.search(cmd):
                    out.append((evt.get("timestamp", ""), cmd))
    return out[::-1]


def source_links(path: Path) -> list[Item]:
    out = []
    for evt in events(path):
        msg = evt.get("message") or {}
        if msg.get("role") != "assistant" or not isinstance(msg.get("content"), list):
            continue
        for block in msg["content"]:
            if isinstance(block, dict) and block.get("type") == "text":
                for url in URL_RE.findall(block.get("text") or ""):
                    if not URL_PLACEHOLDER.search(url):
                        out.append((evt.get("timestamp", ""), url.rstrip(URL_TRAIL)))
    return out[::-1]


def source_messages(path: Path) -> list[Item]:
    """One item per assistant turn: every text block between two human messages."""
    turns, cur, cur_ts = [], [], ""
    for evt in events(path):
        msg = evt.get("message") or {}
        role, content = msg.get("role"), msg.get("content")
        if role == "assistant" and isinstance(content, list):
            for block in content:
                if isinstance(block, dict) and block.get("type") == "text" and block.get("text"):
                    cur.append(block["text"])
                    cur_ts = evt.get("timestamp", "") or cur_ts
        elif role == "user" and is_real_user_turn(content):
            if cur:
                turns.append((cur_ts, "\n\n".join(cur)))
            cur, cur_ts = [], ""
    if cur:
        turns.append((cur_ts, "\n\n".join(cur)))
    return turns[::-1]


def clipboard_cmd() -> list[str] | None:
    override = os.environ.get("GRAB_CLIPBOARD_CMD")
    if override:
        return shlex.split(override)
    candidates = []
    if os.environ.get("WAYLAND_DISPLAY"):
        candidates.append(["wl-copy"])
    candidates += [["xclip", "-selection", "clipboard"], ["xsel", "--clipboard", "--input"],
                   ["pbcopy"], ["clip.exe"], ["wl-copy"]]
    for cmd in candidates:
        if shutil.which(cmd[0]):
            return cmd
    return None


def strip_hr(body: str) -> str:
    lines = body.split("\n")
    hr = [i for i, line in enumerate(lines) if line.strip() == "---"]
    return "\n".join(lines[hr[0] + 1:hr[-1]]).strip() if len(hr) >= 2 else body


def main() -> int:
    ap = argparse.ArgumentParser(description="Copy the latest command, URL, or reply from this Claude Code session.")
    ap.add_argument("source", nargs="?", default="session", help="session (default) | link | message")
    ap.add_argument("--count", type=int, default=1, help="how many items to grab, newest first (default 1)")
    ap.add_argument("--all", action="store_true", help="grab every item in the scan window")
    ap.add_argument("--scan", type=int, default=20, help="how far back to look (default 20 items)")
    ap.add_argument("--skip", type=int, default=0, help="skip the newest N items first")
    ap.add_argument("--hr", action="store_true", help="keep only the text between the first and last '---' line")
    ap.add_argument("--session-id", default="", help="transcript to read (default: $CLAUDE_CODE_SESSION_ID)")
    ap.add_argument("--dry-run", action="store_true", help="print to stdout instead of the clipboard")
    args = ap.parse_args()

    if args.source in ("wa", "ds", "em"):
        sys.exit("grab: chat sources live in the LibreWhatsApp pack's grab plugin "
                 "(https://github.com/HermeticOrmus/LibreWhatsApp-Claude-Code).")
    source = SOURCES.get(args.source)
    if not source:
        sys.exit(f"grab: unknown source '{args.source}'. Use session, link, or message.")

    sid = args.session_id if args.session_id and "$" not in args.session_id else os.environ.get("CLAUDE_CODE_SESSION_ID", "")
    path = find_transcript(sid)
    found = {"session": source_session, "link": source_links, "message": source_messages}[source](path)
    found = found[: args.scan]
    noun = NOUNS[source]
    if not found:
        sys.exit(f"grab: no {noun}s found in this session (scanned {args.scan})")

    found = found[args.skip:]
    pick = found if args.all else found[: max(args.count, 1)]
    if not pick:
        sys.exit(f"grab: nothing left after --skip {args.skip}")
    if args.hr:
        pick = [(ts, strip_hr(body)) for ts, body in pick]
    payload = "\n\n".join(body for _, body in pick)

    if args.dry_run:
        print(payload)
        return 0

    cmd = clipboard_cmd()
    if not cmd:
        print(payload)
        sys.exit("grab: no clipboard tool found (wl-copy, xclip, xsel, pbcopy, clip.exe); "
                 "printed above instead. Set GRAB_CLIPBOARD_CMD to use another.")
    if subprocess.run(cmd, input=payload, text=True).returncode != 0:
        print(payload)
        sys.exit(f"grab: '{' '.join(cmd)}' failed; printed above instead")

    preview = payload if len(payload) <= 400 else payload[:400] + "..."
    print(f"grabbed {len(pick)} {noun}(s) to the clipboard ({len(payload)} chars)")
    print("--- preview ---")
    print(preview)
    return 0


if __name__ == "__main__":
    sys.exit(main())
