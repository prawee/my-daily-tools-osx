---
name: add-doc
description: Create a new markdown guide in this Docsify docs repo, regenerate the sidebar, and publish it to GitHub Pages (commit + push branch docsify). Use when the user asks to add, write, or publish a new doc/guide for a tool.
disable-model-invocation: true
argument-hint: <tool-folder> <topic>
---

Add a new doc to this repo and publish it. Arguments: `$ARGUMENTS` (tool folder, then topic). If either is missing, ask once.

## 1. Create the file
- Folder = tool name, lowercase, e.g. `bun/`, `yeoman/`. Create it if new.
- Filename: follow the numbering style already used in that folder (`ls` it first; e.g. `000-install-cli.md`, `1.install-cli.md`). For a new folder use `000-<topic-slug>.md`. Never overwrite an existing file.
- Content style (match existing guides, e.g. `yeoman/000-install-cli.md`):
  - First line is a single `# Title` (the sidebar uses it as the menu name).
  - Short `##` sections: Requirements, Install, Verify, Usage, Update, Uninstall as relevant.
  - Concise bash code blocks with brief comments; no long prose.
- Only state commands and versions you are confident about; verify with `--help` or official docs if the tool is installed or reachable. Say so if you could not verify.

## 2. Regenerate the sidebar
```bash
python3 scripts/gen-sidebar.py
```
Check `git diff --stat` shows the new doc entry in `_sidebar.md`.

## 3. Preview (optional)
`python3 -m http.server 3000` then open `http://localhost:3000/#/<folder>/<file-without-.md>`.

## 4. Publish
Pages deploys from branch `docsify`. Confirm with `git branch --show-current`; if not on `docsify`, stop and ask.

```bash
git add <new-file> _sidebar.md
git commit -m "Add <topic> guide for <Tool>"
git push
```
Commit message style: imperative, e.g. "Add install guide for Yeoman CLI". Include the Co-Authored-By trailer from the session's attribution instructions.

## 5. Report
Give the live URL: `https://prawee.github.io/my-daily-tools-osx/#/<folder>/<file-without-.md>` and note that the build takes 1-2 minutes.
