#!/usr/bin/env python3
"""usage.py: how often skills, slash commands, subagents, and MCP servers are
used, read from Claude Code session transcripts, plus which of your user-level
skills, commands, and agents never show up.

    usage.py                    scan every transcript
    usage.py --recent 50        scan the 50 most recent transcripts
    usage.py --json             machine-readable output

Reads ${CLAUDE_CONFIG_DIR:-~/.claude}/projects/**/*.jsonl (or --config-dir).
Read-only. Standard library only.
"""
from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter
from pathlib import Path
from typing import Any

COMMAND_TAG = re.compile(r"<command-name>/?([^<\s]+)</command-name>")
BUILTINS = {"clear", "compact", "resume", "login", "logout", "mcp", "model", "effort", "config", "help",
            "exit", "plugin", "plugins", "memory", "init", "status", "cost", "doctor", "agents", "hooks",
            "permissions", "context", "rewind", "export", "add-dir", "ide", "review", "vim", "theme"}


def default_config_dir() -> Path:
    return Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude")


def transcripts(config: Path, recent: int) -> list[Path]:
    files = [p for p in (config / "projects").glob("**/*.jsonl") if p.is_file()]
    files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return files[:recent] if recent else files


def text_of(content: Any) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text")
    return ""


def scan(files: list[Path]) -> dict[str, Counter]:
    counts = {"skills": Counter(), "commands": Counter(), "agents": Counter(), "mcp_servers": Counter()}
    for path in files:
        try:
            handle = open(path, encoding="utf-8", errors="replace")
        except OSError:
            continue
        with handle:
            for line in handle:
                try:
                    evt = json.loads(line)
                except json.JSONDecodeError:
                    continue
                msg = evt.get("message") or {}
                content = msg.get("content")
                if msg.get("role") == "user":
                    for name in COMMAND_TAG.findall(text_of(content)):
                        counts["commands"][name] += 1
                if not isinstance(content, list):
                    continue
                for block in content:
                    if not isinstance(block, dict) or block.get("type") != "tool_use":
                        continue
                    name, inp = block.get("name", ""), block.get("input") or {}
                    if name == "Skill" and inp.get("skill"):
                        counts["skills"][str(inp["skill"]).lstrip("/")] += 1
                    elif name in ("Task", "Agent") and inp.get("subagent_type"):
                        counts["agents"][str(inp["subagent_type"])] += 1
                    elif name.startswith("mcp__"):
                        counts["mcp_servers"][name.split("__")[1]] += 1
    return counts


def inventory(config: Path) -> dict[str, list[str]]:
    skills = sorted(p.parent.name for p in (config / "skills").glob("*/SKILL.md"))
    commands = sorted(p.relative_to(config / "commands").with_suffix("").as_posix().replace("/", ":")
                      for p in (config / "commands").glob("**/*.md")) if (config / "commands").is_dir() else []
    agents = sorted(p.stem for p in (config / "agents").glob("*.md"))
    return {"skills": skills, "commands": commands, "agents": agents}


def used(name: str, counter: Counter) -> bool:
    return any(key == name or key.endswith(":" + name) for key in counter)


def main() -> int:
    ap = argparse.ArgumentParser(description="Usage of skills, commands, agents, and MCP servers.")
    ap.add_argument("--recent", type=int, default=0, help="only the N most recent transcripts (default: all)")
    ap.add_argument("--config-dir", type=Path, default=default_config_dir())
    ap.add_argument("--top", type=int, default=15, help="rows per table (default 15)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    files = transcripts(args.config_dir, args.recent)
    counts = scan(files)
    counts["commands"] = Counter({k: v for k, v in counts["commands"].items() if k not in BUILTINS})
    inv = inventory(args.config_dir)
    unused = {
        "skills": [s for s in inv["skills"] if not used(s, counts["skills"]) and not used(s, counts["commands"])],
        "commands": [c for c in inv["commands"] if not used(c, counts["commands"]) and not used(c, counts["skills"])],
        "agents": [a for a in inv["agents"] if not used(a, counts["agents"])],
    }

    if args.json:
        print(json.dumps({"transcripts": len(files), "counts": {k: dict(v) for k, v in counts.items()},
                          "inventory": inv, "unused": unused}, indent=2))
        return 0

    print(f"# Usage from {len(files)} transcript(s) in {args.config_dir / 'projects'}\n")
    for key, title in (("skills", "Skills"), ("commands", "Slash commands (built-ins excluded)"),
                       ("agents", "Subagents"), ("mcp_servers", "MCP servers (tool calls)")):
        print(f"## {title}\n")
        rows = counts[key].most_common(args.top)
        if not rows:
            print("(none)\n")
            continue
        print("| Name | Uses |\n|---|---|")
        for name, n in rows:
            print(f"| {name} | {n} |")
        print()
    print("## Never used in the scanned transcripts\n")
    for key in ("skills", "commands", "agents"):
        names = unused[key]
        print(f"- {key} ({len(names)} of {len(inv[key])}): {', '.join(names) if names else 'none'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
