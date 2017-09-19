## Knex.js

## Installing to global
```bash
$ npm install -g knex-cli
```

## How to make migrations
```bash
# go to root directory of your project
$ knex migrate:make <filename>
# ./migrations/filename.js
```

## How to run migrations
```bash
# go to root directory of your project
$ knex migrate:lastest .
# Batch 1 run: 1 migrations
```