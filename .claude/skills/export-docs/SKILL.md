---
name: export-docs
description: Export this repo's existing markdown content into another docs framework (Docsify, MkDocs, or GitBook) without modifying the source. Use when the user wants to convert, migrate, or generate a site/config for docsify, mkdocs, or gitbook from the current content.
argument-hint: <docsify|mkdocs|gitbook> [site name]
---

Export the current content to the target framework. Arguments: `$ARGUMENTS`. If the target is missing or not one of `docsify`, `mkdocs`, `gitbook`, ask which one.

## Run
```bash
python3 scripts/export-docs.py <target> [--name "Site Name"] [--out DIR]
```
- Output goes to `_export/<target>/` (git-ignored). Source `.md` files are never changed.
- The script refuses to overwrite an existing output dir; if the user wants a refresh, `rm -rf _export/<target>` first (it is generated output, safe to remove).
- Titles come from each file's first `# heading`; folders become sections; natural sort order (`1.`, `2.`, `10.`).

## What each target produces
| Target | Output | Notes |
|---|---|---|
| docsify | content + `index.html` + `_sidebar.md` + `.nojekyll` | Same setup as this repo's live site |
| mkdocs | `docs/` (content, `README.md` → `index.md`) + `mkdocs.yml` (Material theme, full `nav`) | mkdocs needs docs_dir separate from the config, hence the `docs/` subfolder |
| gitbook | content + `README.md` + `SUMMARY.md` | Folders without a README get a stub so each section has a link target |

## Verify
- Check the script's page count matches `find . -name '*.md'` (excluding `README.md` at root, `_*` files, and skipped dirs like `scripts`).
- If the tool is installed, do a real build/serve (`mkdocs build -f _export/mkdocs/mkdocs.yml`, `npx honkit build _export/gitbook`, `npx docsify-cli serve _export/docsify`). If not, say it was not built, not that it passed.

## Report
Tell the user the output path, page count, and the one-line command to preview it. Do not commit or publish the output unless asked.

## Limits
- Links between pages are not rewritten. Relative links work in all three; absolute `/path` links work in Docsify only.
- MkDocs warns about Markdown files containing raw HTML or unusual syntax; GitBook-specific blocks (hints, tabs) are not generated.
- To publish the live Docsify site in this repo instead, use `/add-doc`.
