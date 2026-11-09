# Create Project with OpenSpec

## 1. Create project directory
```bash
mkdir my-project
cd my-project
git init
```

## 2. Initialize OpenSpec
```bash
openspec init
```
- Select the AI tools you use (Claude Code, Cursor, Codex, etc.)
- OpenSpec generates the `openspec/` directory and the tool-specific slash commands

## 3. Generated structure
```
openspec/
├── specs/       # current specs (source of truth)
├── changes/     # proposed changes (one folder per change)
│   └── archive/ # completed changes
└── project.md   # project conventions and context
AGENTS.md        # instructions for AI assistants
```

## 4. Fill in project context
Edit `openspec/project.md` with:
- Purpose of the project
- Tech stack
- Code conventions
- Testing strategy

Or ask your AI assistant:
```
Please read openspec/project.md and help me fill it out with details about my project, tech stack, and conventions
```

## 5. Create the first change
Ask your AI assistant:
```
/openspec:proposal Add user authentication
```
This creates `openspec/changes/add-user-authentication/` containing:
- `proposal.md` — why and what changes
- `tasks.md` — implementation checklist
- `specs/` — spec deltas

## 6. Workflow commands
```bash
openspec list                 # list active changes
openspec show <change>        # show change details
openspec validate <change>    # validate spec formatting
```

```
/openspec:apply <change>      # implement the tasks
/openspec:archive <change>    # archive after deployment
```

```bash
openspec archive <change> --yes   # CLI alternative to archive
```

## Existing project
Run `openspec init` in the project root; existing files are left untouched.
