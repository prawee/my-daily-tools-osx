# How to install `Docker` on Ubuntu

## Update first
```sh
sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
```

## Install dependencies
```sh
sudo apt install curl apt-transport-https ca-certificates software-properties-common -y
```

## Install Docker
```sh
sudo apt install docker.io -y
```

```sh
docker -v
Docker version 29.1.3, build 29.1.3-0ubuntu3~24.04.2
```

## Restart
```sh
sudo systemctl status docker
```
