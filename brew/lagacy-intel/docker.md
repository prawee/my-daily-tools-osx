# Install Docker

## Check

```bash
$ docker
#zsh: command not found: docker
```

## Installation

```bash
brew install docker
docker -v
# Docker version 18.09.3, build 774a1f4
```

## Error

```bash
sudo docker ps
# Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

### Fixed

```bash
brew cask install docker
open /Applications/Docker.app
#allow access permission
docker ps
# CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

## Technical

```bash
brew list
#+docker
```

## Install docker-compose

```bash
brew search docker-compose
brew install docker-compose
#+docker-compose, dgbm, libyaml, openssl@1.1, python@3.8, readline, sqlite, xz
```

## Install docker-machine

```bash
brew search docker-machine
brew install docker-machine
#+docker-machine
```

## Start your first machine

- Open your virtuabox
- Open your terminal

```bash
docker-machine create --driver virtualbox default
```

## Reference

<https://www.robinwieruch.de/docker-macos>