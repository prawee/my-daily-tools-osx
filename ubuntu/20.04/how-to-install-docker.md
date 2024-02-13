# How to installation Docker

## SSH

```bash
ssh root@your-server-ip -i <your-ssh-path>
```

## Checking

```bash
docker
# Command 'docker' not found
```

## Upgrade

```bash
sudo apt update
sudo apt list --upgradable
sudo apt upgrade -y
```

## Install docker

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
```

```bash
apt-cache policy docker-ce
```

```bash
sudo apt install docker-ce
```

```bash
sudo systemctl status docker
```

```bash
docker --version
# Docker version 20.10.10, build b485636
```

## Reference

<https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04>