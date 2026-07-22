# How to install `NVM` on Ubuntu

## Checking first
```sh
nvm
Command 'nvm' not found, but there are 14 similar ones.
```

## Install latest version 
Looking version from https://github.com/nvm-sh/nvm

```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.6/install.sh
```

## Source
```sh
source ~/.bashrc | source /home/ubuntu/.bashrcn
```

## List Remote
```sh
nvm list-remote
```
```sh
...
v24.18.0   (Latest LTS: Krypton)
        v25.0.0
        v25.1.0
        v25.2.0
        v25.2.1
        v25.3.0
        v25.4.0
        v25.5.0
        v25.6.0
        v25.6.1
        v25.7.0
        v25.8.0
        v25.8.1
        v25.8.2
        v25.9.0
        v26.0.0
        v26.1.0
        v26.2.0
        v26.3.0
        v26.3.1
        v26.4.0
        v26.5.0
```

## List on your machine
```sh
nvm list
```
```sh
iojs -> N/A (default)
node -> stable (-> N/A) (default)
unstable -> N/A (default)
lts/* -> lts/krypton (-> N/A)
lts/argon -> v4.9.1 (-> N/A)
lts/boron -> v6.17.1 (-> N/A)
lts/carbon -> v8.17.0 (-> N/A)
lts/dubnium -> v10.24.1 (-> N/A)
lts/erbium -> v12.22.12 (-> N/A)
lts/fermium -> v14.21.3 (-> N/A)
lts/gallium -> v16.20.2 (-> N/A)
lts/hydrogen -> v18.20.8 (-> N/A)
lts/iron -> v20.20.2 (-> N/A)
lts/jod -> v22.23.1 (-> N/A)
lts/krypton -> v24.18.0 (-> N/A)
```

## Install some version
### Specific full version
```sh
nvm install v20.20.2 
```
```sh
Downloading and installing node v20.20.2...
Downloading https://nodejs.org/dist/v20.20.2/node-v20.20.2-linux-x64.tar.xz...
################################################################################### 100.0%
Computing checksum with sha256sum
Checksums matched!
Now using node v20.20.2 (npm v10.8.2)
Creating default alias: default -> v20.20.2 *
```

### Specific version
```sh
nvm install 22
```
```sh
Downloading and installing node v22.23.1...
Downloading https://nodejs.org/dist/v22.23.1/node-v22.23.1-linux-x64.tar.xz...
################################################################################### 100.0%
Computing checksum with sha256sum
Checksums matched!
Now using node v22.23.1 (npm v10.9.8)
```

## Version of Node
```sh
node -v
v22.23.1
```

### Switch 
```sh
nvm use 20
node -v
v20.20.2
```
