# How to installation MongoDB with Brew

## Setup

```bash
brew tab mongodb/brew

```

## Search

```bash
brew search mongodb
# gcollazo-mongodb                                          mongodb-compass-readonly
# mongodb-compass                                           mongodbpreferencepane
# mongodb-compass-community                                 nosqlbooster-for-mongodb
# mongodb-compass-isolated-edition                          homebrew/cask-versions/mongodb-compass-beta
```

## Installation

```bash
brew install mongodb-community
# ==> Installing mongodb-community from mongodb/brew
# ==> Downloading https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-4.2.1.tgz
# ######################################################################## 100.0%
# ==> Caveats
# To have launchd start mongodb/brew/mongodb-community now and restart at login:
#   brew services start mongodb/brew/mongodb-community
# Or, if you don't want/need a background service you can just run:
#   mongod --config /usr/local/etc/mongod.conf
# ==> Summary
# 🍺  /usr/local/Cellar/mongodb-community/4.2.1: 21 files, 273.5MB, built in 29 seconds
```

## Starting mongodb-community server

```bash
brew services start mongodb-community
# ==> Successfully started `mongodb-community` (label: homebrew.mxcl.mongodb-community)
```
