# Create Project with Yeoman

## Requirements
See [Install Yeoman CLI](/yeoman/000-install-cli.md) for the requirements, installing `yo`, and installing a generator.

## Create a project
Create an empty folder first. Most generators scaffold into the current directory.

```bash
mkdir my-project && cd my-project
```

There are two ways to run a generator. Both produce the same result.

### Option 1: with global install
Requires `yo` and the generator installed (see [Install Yeoman CLI](/yeoman/000-install-cli.md)).

```bash
# run by generator name (without the "generator-" prefix)
yo code
```

Or pick from the installed generators interactively:
```bash
yo
```

### Option 2: without global install (npx)
Downloads `yo` and the generator to a temporary cache and runs them, nothing is installed globally.

```bash
npx --package yo --package generator-code yo code
```

Answer the prompts (project name, language, package manager, git init, etc.). The generator then writes the files and installs dependencies.

```bash
✔ What type of extension do you want to create? New Extension (TypeScript)
✔ What's the name of your extension? Mittr Coder
✔ What's the identifier of your extension? mittr-coder
✔ What's the description of your extension? Mittr Assistant for Developer
✔ Initialize a git repository? Yes
✔ Which bundler to use? esbuild
✔ Which package manager to use? pnpm
```

With pnpm 10+, the install stops with `ERR_PNPM_IGNORED_BUILDS: Ignored build scripts: esbuild` because pnpm blocks dependency build scripts by default. Approve them, then build:
```bash
cd mittr-coder
pnpm approve-builds         # interactive, or: pnpm approve-builds --all
pnpm run compile            # type-check + lint + bundle with esbuild
```

Skip the prompts by passing the answers as options:
```bash
yo code -t ts -n "Mittr Coder" --extensionId mittr-coder \
  --extensionDescription "Mittr Assistant for Developer" \
  --gitInit --bundler esbuild --pkgManager pnpm --skipOpen
```

## Run the extension in VS Code
Open the generated project in VS Code:
```bash
# already inside the project folder (after `cd mittr-coder`)
code .

# still in the parent folder
code mittr-coder
```

1. Press `F5` (or **Run and Debug** > **Run Extension**). VS Code builds with the `watch` task, then opens a new **Extension Development Host** window with the extension loaded.
2. In that new window, open the Command Palette (`Cmd+Shift+P`) and run **Hello World**. A notification message appears.
3. After editing the code, reload the host window with `Cmd+R` (or **Developer: Reload Window**) to see the change.
4. Set breakpoints in `src/extension.ts` to debug.

The launch config is generated in `.vscode/launch.json`. The command name comes from `contributes.commands` in `package.json`.

## Sub-generators
Some generators provide extra commands to add pieces to an existing project:
```bash
yo <name>:<subgenerator>

# example
yo webapp:component
```

## Useful options
```bash
yo code --help            # list generator options and arguments
yo code --skip-install    # scaffold only, do not install dependencies
yo code --quick           # skip optional prompts and use defaults
yo code -t ts             # set extension type (ts, js, colortheme, ...)
```

## Next steps
```bash
cd my-project
git status                # review generated files
npm install               # if you used --skip-install
```

## Troubleshoot
```bash
yo doctor
```
