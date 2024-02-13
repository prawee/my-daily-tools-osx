# How to install nodejs on Ubuntu 22.04

## Checking
```bash
node --version
# Command 'node' not found, but can be installed with:
# apt install nodejs
```

## Upgrade
```bash
sudo dpkg --configure -a
sudo apt update
sudo apt list --upgradable
sudo apt upgrade -y
sudo apt autoremove -y
```

## Start
```bash
sudo apt install nodejs
```
...waiting is done

```bash
node -v
# v12.22.9
```

## Update
```bash
cd ~
curl -sL https://deb.nodesource.com/setup_18.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt remove nodejs
sudo apt install nodejs -y
```

## Update if previous is not ok
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
source ~/.bashrc
```

### List
```bash
nvm list-remote
```

### Install or pick some version
```bash
nvm install v18.19.0
```

### Checking
```bash
node -v
# v18.19.0
```

## Reference
<https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-22-04>
