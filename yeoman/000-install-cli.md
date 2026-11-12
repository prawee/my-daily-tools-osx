# Install Yeoman CLI

## Requirements
- Node.js `^20.17.0` or `>=22.9.0` (required by `yo@7.0.1`)
- npm

```bash
node --version
npm --version
```

## Install
```bash
# npm
npm install -g yo

# pnpm
pnpm add -g yo

# yarn
yarn global add yo

# bun
bun add -g yo
```

## Verify
```bash
yo --version
```

## Install a generator
Generators are published as `generator-<name>`. There are two ways to use one.

### Option 1: global install
```bash
# example: generator-code (VS Code extension)
npm install -g generator-code

yo code
```

List installed generators / run interactively:
```bash
yo
```

### Option 2: without global install (npx)
Nothing is installed globally, `yo` and the generator are fetched to a temporary cache.
```bash
npx --package yo --package generator-code yo code
```

## Doctor (troubleshoot)
```bash
yo doctor
```

## Update
```bash
npm install -g yo@latest
```

## Uninstall
```bash
npm uninstall -g yo
```
