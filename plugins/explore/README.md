# Explore

> Token-optimized AST-based code search. Map a codebase structure without burning context on full-file reads.

## What this does

When you need to understand a codebase you don't know, the naive approach (read every file) burns context quickly. Structural parsing gives understanding at a fraction of the token cost: functions, classes, methods, and types with their line ranges, without the bodies.

4-8× cheaper than `grep + read` for "find me X" lookups.

## Contents

- **Command**: `/explore <topic or symbol> [path]`
- **Skill**: `structural-explore`, the search, outline, unfold method
- **Script**: `bin/outline.py`, standard library Python, no install

## How it works

1. **Search** a tree for symbols matching a topic
2. **Outline** one file: every symbol with its line range, no bodies
3. **Unfold** one symbol: just its source, with line numbers

The skill uses structural search tools when the session has them (tree-sitter based MCP tools, or the LSP tool when a language server is configured). Otherwise it runs the bundled script:

```bash
python3 plugins/explore/bin/outline.py src --search "shutdown"
python3 plugins/explore/bin/outline.py src/server.py
python3 plugins/explore/bin/outline.py src/server.py --unfold Server.stop
```

Python is parsed with the `ast` module (exact ranges). JavaScript, TypeScript, Go, Rust, Java, Kotlin, C#, C, C++, Ruby, PHP, Swift, and shell use line patterns with brace or `end` matching, which is reliable for a map and occasionally off for unusual formatting.
