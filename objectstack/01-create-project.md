# How to create project with `ObjectStack`

## Make folder
```bash
mkdir objectstack
cd objectstack
```

## Create project
```bash
npx @objectstack/cli init mitr-core
```
```bash
◆ Init
────────────────────────────────────────
  Project: mitr-core
  Namespace: mitr_core
  Template: app — Full application with objects, views, and actions
  Directory: /Users/prawee.won/code/objectstack/mitr-core

  Created files:
    + package.json
    + objectstack.config.ts
    + tsconfig.json
    + src/objects/index.ts
    + src/objects/mitr_core_item.ts
    + .gitignore

  → Installing dependencies with npm...
```
```bash
npm warn deprecated prebuild-install@7.1.3: No longer maintained. Please contact the author of the relevant native addon; alternatives are available.

added 308 packages, and audited 309 packages in 48s

68 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
  → Validating scaffold...
  ✓ Scaffold validated (namespace: mitr_core)
  ✓ Project initialized!

  Next steps:
    cd mitr-core
    npx objectstack validate   # Check configuration
    npx objectstack dev        # Start development server
    npx objectstack generate   # Add objects, views, etc.
```

## Usage
```bash
cd mitr-core
```

### Validate
```bash
npx objectstack validate
```
```bash
◆ Validate
────────────────────────────────────────
  → Loading configuration...
  Config: /Users/prawee.won/code/objectstack/mitr-core/objectstack.config.ts
  Load time: 29ms
  → Validating against ObjectStack Protocol...

  ✓ Validation passed (31ms)

  Mitr Core v0.1.0
  Mitr Core application built with ObjectStack

  Data: 1 Objects  3 Fields

  ⚠ No apps or plugins defined — this stack may not do much
```

### Develop
```bash
npx objectstack dev
```
```bash
✓ Server is ready

  ➜  API:       http://localhost:3000/
  ➜  Console:   http://localhost:3000/_console/

  🔑  Dev admin: admin@objectos.ai / admin123
      seeded on empty DB · dev only — do not use in production
```
