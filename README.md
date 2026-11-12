# Project
This repository is my log for working every day.

## Resource
https://100dayscss.com

## Docs site
Published with [Docsify](https://docsify.js.org) on GitHub Pages: https://prawee.github.io/my-daily-tools-osx/

### Preview locally
```bash
npx docsify-cli serve .
# or
python3 -m http.server 3000
```

### Add new content
1. Create a markdown file in the tool's folder, e.g. `bun/4-new-topic.md`. Start with a single `# Title` line (used as the menu name).
2. Regenerate the sidebar:
   ```bash
   python3 scripts/gen-sidebar.py
   ```
3. Commit and push. GitHub Pages deploys from branch `docsify` and updates in 1-2 minutes.
   ```bash
   git add . && git commit -m "Add <topic> guide for <Tool>" && git push
   ```

With Claude Code, `/add-doc <folder> <topic>` does all of the above.

### Export to another framework
Convert the existing content to MkDocs, GitBook or Docsify without changing the source files:
```bash
python3 scripts/export-docs.py <docsify|mkdocs|gitbook> [--name "Site Name"] [--out DIR]
```
Output goes to `_export/<target>/` (git-ignored). Preview:
```bash
# mkdocs
pip install mkdocs-material && cd _export/mkdocs && mkdocs serve
# gitbook
npx honkit serve _export/gitbook
# docsify
npx docsify-cli serve _export/docsify
```
With Claude Code: `/export-docs <target>`.

### Deploy to GitHub Pages
`/deploy-docs docsify` pushes the current branch (Pages source). `/deploy-docs mkdocs|gitbook` builds the exported site and publishes it to `gh-pages`, asking for confirmation first because it replaces the live site.

### Claude Code skills
Project skills live in `.claude/skills/`. They run only when typed (`/name`), never automatically.

| Skill | Usage | What it does |
|---|---|---|
| `add-doc` | `/add-doc <folder> <topic>` | Writes a new guide in the folder, regenerates `_sidebar.md`, then commits and pushes to `docsify` (live in 1-2 min) |
| `export-docs` | `/export-docs <docsify\|mkdocs\|gitbook>` | Converts existing content to `_export/<target>/`. Never edits sources, never commits |
| `deploy-docs` | `/deploy-docs <docsify\|mkdocs\|gitbook>` | Publishes to GitHub Pages: `docsify` pushes the current branch; `mkdocs`/`gitbook` build the export and publish to `gh-pages` (asks first). Then checks build status and HTTP 200 |

Examples:
```
/add-doc bun how-to-install-plugin      # write + publish a new guide
/export-docs mkdocs                     # generate an MkDocs site to preview
/deploy-docs docsify                    # push the current Docsify site
/deploy-docs mkdocs                     # build MkDocs and switch Pages to gh-pages
```

Requirements: `python3`, `git`, and `gh` (GitHub CLI, logged in). `mkdocs build` needs `mkdocs-material`; GitBook builds need `npx honkit`.

Rollback if a deploy switched the site to the wrong source:
```bash
gh api -X PUT repos/prawee/my-daily-tools-osx/pages -f "source[branch]=docsify" -f "source[path]=/"
```
