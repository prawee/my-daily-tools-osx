---
name: deploy-docs
description: Deploy this repo's docs to GitHub Pages as Docsify (from the branch itself) or as an exported MkDocs/GitBook static site (to the gh-pages branch). Use when the user asks to deploy, publish, or push the docs site to GitHub Pages.
disable-model-invocation: true
argument-hint: <docsify|mkdocs|gitbook>
---

Deploy the docs to GitHub Pages. Argument: `$ARGUMENTS` (default `docsify`). Anything else: ask.

Get the repo and current Pages config first:
```bash
REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
gh api repos/$REPO/pages --jq '{status,source,html_url}'   # 404 = Pages not enabled yet
```
Tell the user what is currently live (source branch + URL) before changing anything.

## A. docsify (served straight from a branch, no build)
1. `git branch --show-current` must be the Pages source branch (currently `docsify`). If not, stop and ask.
2. `python3 scripts/gen-sidebar.py`; if `_sidebar.md` changed, include it in the commit.
3. `git status --short`: commit only what the user wants published (`git add <files>`), message in repo style ("Add <topic> guide for <Tool>"), with the Co-Authored-By trailer from the session attribution. Then `git push`.
4. If Pages is not enabled or the source differs, ask before switching:
   `gh api -X PUT repos/$REPO/pages -f "source[branch]=<branch>" -f "source[path]=/"` (use POST to create).
5. Verify (below).

## B. mkdocs / gitbook (static build published to `gh-pages`)
1. Export + build (needs the tool installed; if missing, say so and stop, don't fake a build):
   ```bash
   rm -rf _export/<target>
   python3 scripts/export-docs.py <target>
   mkdocs build -f _export/mkdocs/mkdocs.yml -d ../site     # -> _export/site
   # gitbook: npx honkit build _export/gitbook _export/site
   touch _export/site/.nojekyll
   ```
2. **Ask the user to confirm first**: publishing replaces whatever `gh-pages` holds and, if Pages currently serves another branch (e.g. `docsify`), switches the live site to this one. State both facts.
3. Publish via a temporary worktree, leaving the working branch untouched:
   ```bash
   git fetch origin gh-pages 2>/dev/null
   git worktree add /tmp/gh-pages-deploy gh-pages 2>/dev/null || git worktree add --orphan -b gh-pages /tmp/gh-pages-deploy
   rsync -a --delete --exclude .git _export/site/ /tmp/gh-pages-deploy/
   git -C /tmp/gh-pages-deploy add -A
   git -C /tmp/gh-pages-deploy commit -m "Deploy <target> site"   # + Co-Authored-By trailer
   git -C /tmp/gh-pages-deploy push origin gh-pages
   git worktree remove --force /tmp/gh-pages-deploy
   ```
   Never force-push. If the push is rejected, fetch and rebase in the worktree instead.
4. Point Pages at `gh-pages` if it isn't already (PUT as in A.4). Then verify.

## Verify
```bash
gh api -X POST repos/$REPO/pages/builds --jq .status    # trigger a build
sleep 60
gh api repos/$REPO/pages/builds/latest --jq '{status,error}'   # want status "built"
curl -s -o /dev/null -w "%{http_code}\n" <html_url>             # want 200
```
Also curl the page and check it is the expected framework (e.g. `docsify` in the HTML, or `mkdocs` meta). If the build is still `building`, wait and retry; report real status, never assume success.

## Report
Give the live URL, which branch/source it deploys from, the commit pushed, and how to roll back (switch Pages source back, e.g. `gh api -X PUT repos/$REPO/pages -f "source[branch]=docsify" -f "source[path]=/"`).
