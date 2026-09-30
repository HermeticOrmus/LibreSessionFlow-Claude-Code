# Pickup, cold mode (no HANDOFF.md)

> Used when the project folder exists but holds no handoff. Reconstruct context from git history and filesystem signals.

## Step C1: find sibling projects

The search term may match several related folders (`shop-api`, `shop-web`, `shop-admin`). Treat them as one ecosystem. For each match, get one line of recent activity:

```bash
# git repo
git -C <dir> log -1 --format="%h %ad %s" --date=relative 2>/dev/null
# not a git repo: newest source file
find <dir> -maxdepth 3 -type f \( -name "*.ts" -o -name "*.js" -o -name "*.py" -o -name "*.go" -o -name "*.rs" -o -name "*.md" \) -not -path "*/node_modules/*" -printf "%T@ %p\n" 2>/dev/null | sort -rn | head -1
```

(`find -printf` is GNU find; on macOS use `stat -f "%m %N"` on the results instead.)

Sort them by most recent activity. The **primary** project is the best name match (exact match first, then most recent); the others are **siblings**.

## Step C2: scan the primary project

Git repo:

```bash
git -C <p> log --oneline --format="%h %ad %s" --date=relative -15   # recent commits
git -C <p> branch --show-current                                    # branch
git -C <p> branch -vv                                               # tracking
git -C <p> status --short                                           # working tree
git -C <p> diff --stat; git -C <p> diff --cached --stat             # uncommitted and staged
git -C <p> log --oneline @{upstream}..HEAD 2>/dev/null || echo "no upstream"   # unpushed
```

Always, git or not: list the fifteen most recently modified files, skipping `node_modules`, `.git`, `dist`, `build`, and similar output folders.

Read the project `CLAUDE.md` and `README.md` if present, for stack and conventions.

## Analysis

1. **Last work cluster**: group the recent commits by theme (commit prefixes such as `feat`, `fix`, `refactor`, `docs` help).
2. **Active area**: which folders and files moved most recently.
3. **Dirty state**: uncommitted, untracked, or recently modified files. The strongest signal of where work was interrupted.
4. **Cross-repo activity**: a sibling changed more recently than the primary often means the work actually moved there.
5. **Predicted last task**: one or two sentences across all the evidence.

## Present

```markdown
## Picked up: <project> (cold, no handoff)

**Path**: <absolute path>
**Branch**: <branch> | **Last commit**: <hash> <subject>
**Git status**: <clean | N changed | N untracked>
**Remote**: <ahead N | in sync | behind N | no upstream>

### Ecosystem activity
| Project | Last activity | Signal |
|---|---|---|

### Last work (inferred)
<one to two sentences>

### Work clusters
- **<theme>** (<n> commits): <summary>

### Active files
<three to five files>

### Dirty state
<uncommitted changes, or "clean">

### Ready
Context inferred from git history; no handoff was found. What do you want to work on?
```

Do not enter plan mode: there is no specific task yet. Orient, then ask. Suggest running `/handoff` at the end of this session so the next pickup has one.
