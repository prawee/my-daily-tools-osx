# How to install NodeJS with mongodb droplet

## Installation

```bash
apt install nodejs
```

## Checking version

```bash
node -v
#v8.10.0
```

## Upgrade NodeJS

```bash
curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh
bash nodesource_setup.sh
apt-get install -y nodejs
```

## Checking version again

```bash
node -v
#v10.17.0
```
