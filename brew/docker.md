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
