# Build, Test and Publish a VS Code Extension

Continues from [Create Project with Yeoman](/yeoman/001-create-project.md). Examples use the `mittr-coder` project.

## Build
```bash
cd mittr-coder
pnpm run compile            # type-check + lint + bundle (dev build)
pnpm run package            # same, but minified for production -> dist/extension.js
```

## Test
```bash
pnpm run test               # runs src/test/*.test.ts in a VS Code instance (vscode-test)
```
For manual testing press `F5` in VS Code (see the run section in the previous guide).

## Package as .vsix
`vsce` is the official packaging tool. No global install needed:
```bash
npx @vscode/vsce package --no-dependencies
# -> mittr-coder-0.0.1.vsix
```
`--no-dependencies` is needed because the extension is already bundled by esbuild, and it avoids `vsce` trying to resolve pnpm's `node_modules`.

List what goes into the package:
```bash
npx @vscode/vsce ls --no-dependencies
```

### Before packaging
- **Edit `README.md`.** The generated template text makes `vsce` stop with `ERROR It seems the README.md still contains template text`.
- **Add a `publisher`** to `package.json` (required to publish, see below).
- **Bump `version`** for every release (`0.0.1` -> `0.0.2`).
- **Ignore files you do not ship.** `pnpm-lock.yaml` and `pnpm-workspace.yaml` end up in the package by default, so add them to `.vscodeignore`:
  ```
  pnpm-lock.yaml
  pnpm-workspace.yaml
  ```

## Install the .vsix locally
```bash
code --install-extension mittr-coder-0.0.1.vsix

# remove it again
code --uninstall-extension <publisher>.mittr-coder
```
Or in VS Code: **Extensions** > `...` menu > **Install from VSIX...**

Reload the window, open the Command Palette and run **Hello World** to confirm it works.

## Share without the Marketplace
Send the `.vsix` file to teammates (chat, internal file share, GitHub Release). They install it with the same `code --install-extension` command.

## Publish to the VS Code Marketplace
One-time setup:
1. Create a publisher at https://marketplace.visualstudio.com/manage. The publisher ID goes into `package.json` as `"publisher"`.
2. Create a Personal Access Token in Azure DevOps (https://dev.azure.com) with scope **Marketplace > Manage**, organization set to **All accessible organizations**.

Then:
```bash
npx @vscode/vsce login <publisher>      # paste the token
npx @vscode/vsce publish                # publish the version in package.json
# or bump and publish in one step
npx @vscode/vsce publish patch          # 0.0.1 -> 0.0.2 (also minor, major)
```
It appears at `https://marketplace.visualstudio.com/items?itemName=<publisher>.mittr-coder` after a short verification.

## Publish to Open VSX (VSCodium, Cursor, etc.)
Editors that do not use the Microsoft Marketplace read from https://open-vsx.org.
```bash
npx ovsx publish mittr-coder-0.0.1.vsix -p <open-vsx-token>
```

## Unpublish
```bash
npx @vscode/vsce unpublish <publisher>.mittr-coder
```

## Tested
Verified with `generator-code`, `@vscode/vsce`, pnpm 11 and Node 24: `pnpm run package`, `vsce package --no-dependencies` and `vsce ls` work after the README is edited. The `code --install-extension`, login and publish steps were **not** run.
