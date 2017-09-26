## Knex.js

## Installing to global
```bash
$ npm install -g knex
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

### How to make seed data
```bash
# go to root directory of your project
$ knex seed:make <filename>
# ./seeds/filename.js
```

### How to run seeds
```bash
# go to root directory of your project
$ knex seed:run
# Ran 2 seed files
```