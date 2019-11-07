# How to upgrade NodeJS

## Checking

```bash
node -v
# v8.16.0
```

## Upgrade

```bash
cd
curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh
nano nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt-get install -y nodejs
```

## Checking again

```bash
node -v
# v10.16.0
```

## Upgrade to v.12.x

```bash
cd
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
apt install nodejs
```

## Checking version

```bash
node -v
#v12.13.0
```
