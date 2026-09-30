#!/usr/bin/env python3
"""outline.py: structural code map without reading whole files.

    outline.py <file>                       symbols of one file with line ranges
    outline.py <dir> --search <term>        ranked symbols across a tree, plus per-file counts
    outline.py <file> --unfold <symbol>     source of one symbol, with line numbers
    outline.py <dir>                        per-file symbol counts for a tree

Python files are parsed with the standard library `ast` module, so their
symbols and ranges are exact. Other languages (JS/TS, Go, Rust, Java, Kotlin,
C#, C/C++, Ruby, PHP, Swift, shell) use line patterns plus brace or `end`
matching: good for a map, not a compiler. Standard library only.
"""
from __future__ import annotations

import argparse
import ast
import os
import re
import sys
from pathlib import Path
from typing import Iterator

Symbol = dict  # keys: kind, name, start, end, sig

SKIP_DIRS = {".git", "node_modules", "dist", "build", "out", "target", "vendor", ".venv", "venv",
             "__pycache__", ".next", ".nuxt", ".output", "coverage", ".tox", ".mypy_cache"}
MAX_BYTES = 1_000_000

JS = [
    ("function", r"^\s*(?:export\s+)?(?:default\s+)?(?:async\s+)?function\s*\*?\s*(\w+)"),
    ("class", r"^\s*(?:export\s+)?(?:default\s+)?(?:abstract\s+)?class\s+(\w+)"),
    ("function", r"^\s*(?:export\s+)?(?:const|let|var)\s+(\w+)\s*(?::[^=]+)?=\s*(?:async\s+)?(?:\([^)]*\)|\w+)\s*(?::[^=]+)?=>"),
    ("type", r"^\s*(?:export\s+)?(?:declare\s+)?(?:interface|type|enum)\s+(\w+)"),
    ("method", r"^\s+(?:(?:public|private|protected|static|async|readonly|override|get|set)\s+)*(?!if\b|for\b|while\b|switch\b|catch\b|return\b|function\b)(\w+)\s*\([^)]*\)\s*(?::\s*[^{;]+)?\{\s*$"),
]
PATTERNS = {
    "py": [],
    "js": JS,
    "go": [("function", r"^func\s+(?:\([^)]*\)\s*)?(\w+)"),
           ("type", r"^type\s+(\w+)\s+(?:struct|interface)")],
    "rs": [("function", r"^\s*(?:pub(?:\([^)]*\))?\s+)?(?:const\s+)?(?:async\s+)?(?:unsafe\s+)?fn\s+(\w+)"),
           ("type", r"^\s*(?:pub(?:\([^)]*\))?\s+)?(?:struct|enum|trait|union)\s+(\w+)"),
           ("impl", r"^\s*impl(?:<[^>]*>)?\s+(?:[\w:<>]+\s+for\s+)?([\w:]+)")],
    "java": [("class", r"^\s*(?:(?:public|private|protected|abstract|final|static|sealed|open|data|internal)\s+)*(?:class|interface|enum|record|object)\s+(\w+)"),
             ("method", r"^\s+(?:(?:public|private|protected|static|final|abstract|synchronized|override|suspend|async|virtual|internal)\s+)+[\w<>\[\],.?\s]*?\b(\w+)\s*\([^;]*$"),
             ("function", r"^\s*(?:(?:public|private|internal|suspend|inline)\s+)*fun\s+(?:<[^>]*>\s*)?(?:[\w.]+\.)?(\w+)")],
    "c": [("type", r"^\s*(?:typedef\s+)?(?:struct|class|enum|union)\s+(\w+)\s*(?:[:{]|$)"),
          ("function", r"^(?!\s)(?!return\b)(?!.*;\s*$)[\w*&:<>,\s]*?\b(\w+)\s*\([^;]*\)\s*(?:const\s*)?\{?\s*$")],
    "rb": [("method", r"^\s*def\s+(?:self\.)?(\w+[?!=]?)"),
           ("class", r"^\s*(?:class|module)\s+([\w:]+)")],
    "php": [("function", r"^\s*(?:(?:public|private|protected|static|abstract|final)\s+)*function\s+(\w+)"),
            ("class", r"^\s*(?:abstract\s+|final\s+)?(?:class|interface|trait|enum)\s+(\w+)")],
    "swift": [("function", r"^\s*(?:(?:public|private|internal|fileprivate|open|static|override|mutating)\s+)*func\s+(\w+)"),
              ("type", r"^\s*(?:(?:public|private|internal|final|open)\s+)*(?:class|struct|enum|protocol|extension|actor)\s+(\w+)")],
    "sh": [("function", r"^\s*(?:function\s+)?([\w-]+)\s*\(\)\s*\{?"),
           ("function", r"^\s*function\s+([\w-]+)\s*\{?")],
}
EXT = {".py": "py", ".js": "js", ".jsx": "js", ".mjs": "js", ".cjs": "js", ".ts": "js", ".tsx": "js",
       ".mts": "js", ".cts": "js", ".vue": "js", ".svelte": "js", ".go": "go", ".rs": "rs",
       ".java": "java", ".kt": "java", ".kts": "java", ".cs": "java", ".scala": "java",
       ".c": "c", ".h": "c", ".cc": "c", ".cpp": "c", ".cxx": "c", ".hpp": "c", ".hh": "c",
       ".rb": "rb", ".php": "php", ".swift": "swift", ".sh": "sh", ".bash": "sh", ".zsh": "sh"}


def lang_of(path: Path) -> str | None:
    return EXT.get(path.suffix.lower())


def read_lines(path: Path) -> list[str] | None:
    try:
        if path.stat().st_size > MAX_BYTES:
            return None
        return path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return None


def python_symbols(path: Path, lines: list[str]) -> list[Symbol] | None:
    try:
        tree = ast.parse("\n".join(lines), filename=str(path))
    except SyntaxError:
        return None
    out = []

    def visit(node: ast.AST, prefix: str) -> None:
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                start = min([d.lineno for d in child.decorator_list] + [child.lineno])
                kind = "class" if isinstance(child, ast.ClassDef) else ("method" if prefix else "function")
                name = f"{prefix}{child.name}"
                out.append({"kind": kind, "name": name, "start": start,
                            "end": child.end_lineno or child.lineno, "sig": lines[child.lineno - 1].strip()})
                if isinstance(child, ast.ClassDef):
                    visit(child, name + ".")

    visit(tree, "")
    return out


STRIP = re.compile(r"(\"(\\.|[^\"\\])*\"|'(\\.|[^'\\])*'|`[^`]*`|//.*$)")


def brace_end(lines: list[str], i: int) -> int:
    """Last line (0-based) of the block whose signature starts on line i."""
    depth, opened, paren = 0, False, 0
    j, limit = i, min(len(lines), i + 5000)
    while j < limit:
        for ch in STRIP.sub("", lines[j]):
            if ch == "(":
                paren += 1
            elif ch == ")":
                paren -= 1
            elif ch == "{":
                depth, opened = depth + 1, True
            elif ch == "}":
                depth -= 1
                if opened and depth <= 0:
                    return j
        if not opened and paren <= 0:
            k = j + 1
            while k < len(lines) and not lines[k].strip():
                k += 1
            if k < len(lines) and lines[k].lstrip().startswith("{"):
                j = k
                continue
            return j
        j += 1
    return i


def ruby_end(lines: list[str], i: int) -> int:
    indent = len(lines[i]) - len(lines[i].lstrip())
    for j in range(i + 1, len(lines)):
        stripped = lines[j].strip()
        if stripped == "end" and len(lines[j]) - len(lines[j].lstrip()) == indent:
            return j
    return i


def pattern_symbols(lang: str, lines: list[str]) -> list[Symbol]:
    compiled = [(k, re.compile(p)) for k, p in PATTERNS[lang]]
    out, seen = [], set()
    for i, line in enumerate(lines):
        if len(line) > 400:
            continue
        for kind, rx in compiled:
            m = rx.match(line)
            if m and i not in seen:
                seen.add(i)
                end = ruby_end(lines, i) if lang == "rb" else (brace_end(lines, i) if lang != "sh" or "{" in line else i)
                out.append({"kind": kind, "name": m.group(1), "start": i + 1, "end": end + 1, "sig": line.strip()[:160]})
                break
    classes = [s for s in out if s["kind"] in ("class", "impl")]
    for s in out:
        if s["kind"] == "method":
            owner = [c for c in classes if c["start"] < s["start"] <= c["end"]]
            if owner:
                s["name"] = f"{owner[-1]['name']}.{s['name']}"
    return out


def symbols(path: Path) -> list[Symbol] | None:
    lang = lang_of(path)
    if not lang:
        return None
    lines = read_lines(path)
    if lines is None:
        return None
    if lang == "py":
        result = python_symbols(path, lines)
        return result if result is not None else []
    return pattern_symbols(lang, lines)


def walk(root: Path) -> Iterator[Path]:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and not d.startswith("."))
        for name in sorted(filenames):
            p = Path(dirpath) / name
            if lang_of(p):
                yield p


def score(sym: Symbol, path: Path, terms: list[str]) -> int:
    name, sig, where = sym["name"].lower(), sym["sig"].lower(), str(path).lower()
    total = 0
    for t in terms:
        if name == t or name.endswith("." + t):
            total += 10
        elif t in name:
            total += 6
        elif t in sig:
            total += 3
        elif t in where:
            total += 1
        else:
            return 0
    return total


def fmt(sym: Symbol) -> str:
    span = f"{sym['start']}-{sym['end']}" if sym["end"] > sym["start"] else f"{sym['start']}"
    return f"  {sym['kind']:<8} {sym['name']}  (L{span})  {sym['sig']}"


def main() -> int:
    ap = argparse.ArgumentParser(description="Structural code map: outline, search, unfold.")
    ap.add_argument("path", help="file or directory")
    ap.add_argument("--search", help="rank symbols across the tree that match these words")
    ap.add_argument("--unfold", help="print the source of one symbol (name or Class.method)")
    ap.add_argument("--max", type=int, default=20, help="max symbols for --search (default 20)")
    args = ap.parse_args()

    root = Path(args.path)
    if not root.exists():
        sys.exit(f"outline: no such path: {root}")

    if args.unfold:
        if not root.is_file():
            sys.exit("outline: --unfold needs a file")
        syms = symbols(root) or []
        want = args.unfold.lower()
        match = [s for s in syms if s["name"].lower() == want] or \
                [s for s in syms if s["name"].lower().endswith("." + want)]
        if not match:
            names = ", ".join(s["name"] for s in syms[:40])
            sys.exit(f"outline: no symbol '{args.unfold}' in {root}. Symbols: {names}")
        lines = read_lines(root) or []
        for s in match:
            print(f"# {root}:{s['start']}-{s['end']}  {s['kind']} {s['name']}")
            for n in range(s["start"], s["end"] + 1):
                print(f"{n:>6}  {lines[n - 1]}")
        return 0

    if root.is_file():
        syms = symbols(root)
        if syms is None:
            sys.exit(f"outline: unsupported or unreadable file: {root} (read it directly)")
        print(f"{root}  ({len(syms)} symbols)")
        for s in syms:
            print(fmt(s))
        return 0

    files = list(walk(root))
    if args.search:
        terms = [t.lower() for t in args.search.split()]
        hits, per_file = [], {}
        for p in files:
            for s in symbols(p) or []:
                sc = score(s, p, terms)
                if sc:
                    hits.append((sc, p, s))
                    per_file[p] = per_file.get(p, 0) + 1
        hits.sort(key=lambda h: (-h[0], str(h[1]), h[2]["start"]))
        print(f"-- matching symbols for '{args.search}' ({len(hits)} found, showing {min(len(hits), args.max)}) --")
        for sc, p, s in hits[: args.max]:
            span = f"{s['start']}-{s['end']}" if s["end"] > s["start"] else f"{s['start']}"
            print(f"  {s['kind']:<8} {s['name']}  ({p}:{span})")
        print("-- files --")
        for p, n in sorted(per_file.items(), key=lambda kv: -kv[1])[:15]:
            print(f"  {p}  ({n} matching)")
        return 0

    print(f"{root}  ({len(files)} code files)")
    for p in files:
        syms = symbols(p)
        if syms is not None:
            print(f"  {p}  ({len(syms)} symbols)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
