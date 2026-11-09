# Create Project with OpenSpec

> Tested with OpenSpec 1.16.1

## 1. Create project directory
```bash
mkdir my-project
cd my-project
git init
```

## 2. Initialize OpenSpec
```bash
openspec init

# non-interactive
openspec init --tools claude
```
Select the AI tools you use (Claude Code, Cursor, Codex, etc.)

## 3. Generated structure
```
openspec/
├── config.yaml      # project config (schema: spec-driven)
├── specs/           # current specs (source of truth)
└── changes/
    └── archive/     # completed changes
.claude/             # for Claude Code
├── commands/opsx/   # slash commands
└── skills/          # openspec-* skills
```
> `project.md` and `AGENTS.md` are no longer generated. Put project context in `openspec/config.yaml` instead.

## 4. Fill in project context
Edit `openspec/config.yaml` (tech stack, conventions, rules per artifact).

## 5. Create the first change
```
/opsx:propose "Add user authentication"
```
Creates `openspec/changes/<change-name>/` with proposal, design, tasks and spec deltas.

## 6. Slash commands (default profile)
| Command | Purpose |
|---|---|
| `/opsx:explore` | explore ideas before proposing |
| `/opsx:propose` | create a change with all artifacts |
| `/opsx:apply` | implement the tasks |
| `/opsx:sync` | sync spec deltas into main specs |
| `/opsx:archive` | archive a completed change |
| `/opsx:update` | update an existing change |

More workflows (new, continue, ff, bulk-archive, verify, onboard):
```bash
openspec config profile
```

## 7. CLI commands
```bash
openspec list                 # list active changes
openspec show <change>        # show change details
openspec validate <change>    # validate spec formatting
```

## Existing project
Run `openspec init` in the project root.
