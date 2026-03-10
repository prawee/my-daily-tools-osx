# How to `Upgrade` Ubuntu server

Update to latest

```sh
sudo apt update
```

```sh
sudo apt upgrade -y
```

Running kernel seems to be up-to-date.

Restarting services
```sh
sudo systemctl restart packagekit.service udisks2.service
```

Service restarts being deferred
```sh
sudo systemctl restart networkd-dispatcher.service
sudo systemctl restart unattended-upgrades.service
```

```sh
sudo reboot
```

The system will reboot now!
