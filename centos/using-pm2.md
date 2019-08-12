# How to using PM2

## Checking

```bash
pm2 list
# -bash: pm2: command not found
```

## Installation

```bash
npm i -g pm2
# + pm2@3.5.1
# added 319 packages from 258 contributors in 37.19s
```

## Using

```bash
pm2 list
# [PM2] PM2 Successfully daemonized
# ┌──────┬────┬──────┬────────┬───┬─────┬────────┐
# │ Name │ id │ mode │ status │ ↺ │ cpu │ memory │
# └──────┴────┴──────┴────────┴───┴─────┴────────┘
#  Use `pm2 show <id|name>` to get more details about an app
```

## Reference

<https://www.tecmint.com/install-pm2-to-run-nodejs-apps-on-linux-server>
