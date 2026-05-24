# Explore

> Token-optimized AST-based code search. Map a codebase structure without burning context on full-file reads.

## What this does

When you need to understand a codebase you don't know, the naive approach (read every file) burns context quickly. Tree-sitter AST parsing gives structural understanding at a fraction of the token cost: functions, classes, types, imports — without the bodies.

4-8× cheaper than `grep + read` for "find me X" lookups.

## Coming in v0.3

Full plugin expansion. Currently a shell pointing at the existing `smart-explore` Claude Code skill.
