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

## Table of Contents
- [Angular](#angular)(Updated)
    - [Installation CLI](https://github.com/prawee/osx/blob/master/angular/1.installation-cli.md)
    - [Create Project](https://github.com/prawee/osx/blob/master/angular/2.create-project.md)
    - [Create Component](https://github.com/prawee/osx/blob/master/angular/3.create-component.md)
- [Brew](#brew)(Updated)
    - [Solve](#solve)
        - [Unbrewed](https://github.com/prawee/osx/blob/master/brew/solve/unbrewed-header-files.md)
    - [Composer](https://github.com/prawee/osx/blob/master/brew/composer.md)
    - [Install](https://github.com/prawee/osx/blob/master/brew/install.md)
    - [Memcached](https://github.com/prawee/osx/blob/master/brew/memcached.md)
    - [Nginx (Applied)](https://github.com/prawee/osx/blob/master/brew/nginx-apply.md)
    - [Nginx (Full)](https://github.com/prawee/osx/blob/master/brew/nginx-full.md)
    - [Nginx](https://github.com/prawee/osx/blob/master/brew/nginx.md)
    - [Node](https://github.com/prawee/osx/blob/master/brew/node.md)
    - [PHP-FPM](https://github.com/prawee/osx/blob/master/brew/php-fpm.md)
    - [PHP Extension](https://github.com/prawee/osx/blob/master/brew/php71-extension.md)
    - [Python3](https://github.com/prawee/osx/blob/master/brew/python3.md)
    - [Vagrant](https://github.com/prawee/osx/blob/master/brew/vagrant.md)
    - [Wget](https://github.com/prawee/osx/blob/master/brew/wget.md)
- [Composer](#composer)
    - [Yii2](https://github.com/prawee/osx/blob/master/composer/yii2.md)
- [GCP](#gcp)
    - [1.Install-SDK](https://github.com/prawee/osx/blob/master/gcp/1.install-sdk.md)
    - [2.Authentication](https://github.com/prawee/osx/blob/master/gcp/2.auth.md)
    - [3.Deploy PHP](https://github.com/prawee/osx/blob/master/gcp/3.deploy-php.md)
- [Git](#git)
    - [Create](https://github.com/prawee/osx/blob/master/git/1.how-to-create.md)
    - [Clone0](https://github.com/prawee/osx/blob/master/git/2.how-to-clone.md)
- [Laravel](#laravel)(Updated)
    - [Create Project](https://github.com/prawee/osx/blob/master/laravel/create-project.md)
    - [Install](https://github.com/prawee/osx/blob/master/laravel/install.md)
    - [Add Homestead](https://github.com/prawee/osx/blob/master/laravel/add-homestead.md)
    - [Configure Homestead](https://github.com/prawee/osx/blob/master/laravel/configuring-homestead.md)
    - [Lumen](#lumen)
        - [Installation](https://github.com/prawee/osx/blob/master/laravel/lumen/install.md)
        - [Create Project](https://github.com/prawee/osx/blob/master/laravel/lumen/create-project.md)
        - [Generate Controller](https://github.com/prawee/osx/blob/master/laravel/lumen/create-controller.md)
        - [Generate Model](https://github.com/prawee/osx/blob/master/laravel/lumen/create-model.md)
- [Memcached](#memcached)
    - [Usage](https://github.com/prawee/osx/blob/master/memcached/usage.md)
- [Meteor](#meteor)(New)
    - [Installation](https://github.com/prawee/osx/blob/master/meteor/1.installation.md)
    - [GAE](#gae)
        - [Create Project](https://github.com/prawee/osx/blob/master/meteor/gae/1.create-project.md)
        - [Deploy](https://github.com/prawee/osx/blob/master/meteor/gae/2.deploy.md)
- [NPM](#npm)
    - [Knex](https://github.com/prawee/osx/blob/master/npm/knex.md)
    - [Sails](https://github.com/prawee/osx/blob/master/npm/sails.md)
- [Odoo](#odoo)
    - [V9](#v9)
        - [Installation](https://github.com/prawee/osx/blob/master/odoo/v9/1.installation.md)
    - [V11](#v11)
        - [Installation](https://github.com/prawee/osx/blob/master/odoo/v11/1.installation.md)
- [Packagist](#packagist)(New)
    - [Hook with Github](https://github.com/prawee/osx/blob/master/packagist/hook-github.md)
- [Python](#python)
    - [PIP](#pip)
        - [Virtualenv](https://github.com/prawee/osx/blob/master/python/pip/virtualenv.md)
        - [Autoenv](https://github.com/prawee/osx/blob/master/python/pip/autoenv.md)
- [React](#react)
    - [Create Project](https://github.com/prawee/osx/blob/master/react/1.create-project.md)
    - [Refactoring](https://github.com/prawee/osx/blob/master/react/2.update-src-project.md)
    - [Route](https://github.com/prawee/osx/blob/master/react/3.create-route.md)
    - [Semantic Setup](https://github.com/prawee/osx/blob/master/react/4.using-semantic-ui.md)
- [React Native](#reactnative)
    - [Fixed gitignore](https://github.com/prawee/osx/blob/master/react-native/fixed-gitignore-not-working-with-gradle.md)
    - [Install](https://github.com/prawee/osx/blob/master/react-native/1.install.md)
    - [Create Project](https://github.com/prawee/osx/blob/master/react-native/2.create-application.md)
- [Silex](#silex)(Updated)
    - [Create Project](https://github.com/prawee/osx/blob/master/silex/1.create-project.md)
    - [Create Log](https://github.com/prawee/osx/blob/master/silex/2.create-log.md)
    - [Using Dump](https://github.com/prawee/osx/blob/master/silex/3.using-dump.md)
    - [Create Service](https://github.com/prawee/osx/blob/master/silex/4.create-services.md)
- [Vue](#vue)
    - [Install](https://github.com/prawee/osx/blob/master/vue/1.installation.md)
- [Wordpress](#wordpress)
    - [Fixed update](https://github.com/prawee/osx/blob/master/react-native/fixed-unable-install-or-update-plugins-and-theme.md)
- [Yii](#yii)(New)
    - [GAE](#gae)
        - [Create Skeletion](https://github.com/prawee/osx/blob/master/yii/gae/1.create-skeleton-for-gae.md)
        - [Deploy](https://github.com/prawee/osx/blob/master/yii/gae/2.deploy.md)
        - [Create Models](https://github.com/prawee/osx/blob/master/yii/gae/3.create-models.md)
        - [Create Controller](https://github.com/prawee/osx/blob/master/yii/gae/4.create-controllers.md)
        - [Create Log]()
        - [Migration]()