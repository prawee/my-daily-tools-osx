---
name: release
description: Create a git tag and GitHub release with release notes for this repo, targeting the merged commit on master. Use when the user asks to cut, tag, or publish a release (e.g. "create tag v2.0.0 and release notes").
disable-model-invocation: true
argument-hint: <version, e.g. v2.0.0>
---

Create a tag + GitHub release. Argument: `$ARGUMENTS` (version, with leading `v`). If missing, look at the latest tag and ask which bump (major/minor/patch) the user wants; never guess a major bump.

## 1. Check state
```bash
git fetch -q --tags origin
gh release list --limit 3                  # latest release/tag and its notes style
git tag --sort=-v:refname | head -3
git log --oneline <last-tag>..origin/master
```
- The tag must not already exist (`git tag -l <version>`); if it does, stop and ask.
- Releases are cut from `origin/master`. If work is still on `develop`/a feature branch, check for an open PR into master (`gh pr list --base master`); if not merged, tell the user and stop. Do not merge PRs without being asked.
- Target = the tip of `origin/master` (`git rev-parse origin/master`), not the local branch.

## 2. Write the notes
Gather what changed since the last tag from merged PRs and commits (`gh pr list --state merged --base develop --base master`, `git log <last-tag>..origin/master`). Structure:
```
## Highlights      (user-visible features, 2-5 bullets, with PR numbers)
## Changed         (removals, behavior changes)
## Notes           (caveats, e.g. what was not verified)
**Full Changelog**: https://github.com/<owner>/<repo>/compare/<last-tag>...<version>
```
- Describe only what the diff shows; state what was not tested.
- Do not write `@username`: GitHub notifies that person. Name contributors in backticks or omit.
- Show the draft to the user only if they asked to review; otherwise proceed.

## 3. Publish
```bash
gh release create <version> --target <origin/master sha> --title "<version>" --latest --notes "<notes>"
```
This creates the tag and release together. Use `--prerelease` instead of `--latest` for pre-releases/RCs. Never move or delete an existing tag, and never use `--force`.

## 4. Verify and report
```bash
git fetch -q --tags
git rev-parse <version>^{commit}      # must equal the target sha
gh release view <version> --json url,isLatest,tagName
```
Report: release URL, tag + commit, and anything in the notes that needs the user's attention. Roll back only if asked: `gh release delete <version> --cleanup-tag`.
