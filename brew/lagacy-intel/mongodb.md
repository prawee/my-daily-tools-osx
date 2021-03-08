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

## Fixed

### Create new folder

```bash
cd
mkdir data && cd
mkdir data
# data/db
```

### Update configure

```bash
nano /usr/local/etc/mongod.conf
```

```bash
storage:
  #dbPath: /usr/local/var/mongodb
  dbPath: /Users/prawee/data/db
```

```bash
mongod --config /usr/local/etc/mongod.conf
```

### Restart services

```bash
brew services restart mongodb-community
```

## Usage

```bash
mongo
# MongoDB shell version v4.2.1
# connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
# Implicit session: session { "id" : UUID("2997444c-a72b-4b90-a4db-fd37360fcffa") }
# MongoDB server version: 4.2.1
> show dbs;
# admin   0.000GB
# config  0.000GB
# local   0.000GB
```
