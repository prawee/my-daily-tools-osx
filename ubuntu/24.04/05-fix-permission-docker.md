# Fix with any problem about permission

## Add APG keys
```sh
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

## Verify ubuntu version
```sh
lsb_release -cs
```
```sh
No LSB modules are available.
noble
```

## Set up stable repository
```sh
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu noble stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

## Update package
```sh
sudo apt update
```

## Install Docker and component again
```sh
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## Verify docker install
```sh
sudo systemctl status docker
```
or
```sh
sudo reboot
```

## Make group
```sh
getent group docker
```

```sh
sudo groupadd docker
```

```sh
sudo usermod -aG docker $USER
```
```sh
newgrp docker
```
