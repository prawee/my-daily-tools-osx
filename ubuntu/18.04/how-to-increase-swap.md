# How to increase swap file

## Solved

install node then `killed`

## Fixed

```bash
# stop swapfile
sudo swapoff -a
# checking current size
ls -lh /swapfile
-rw------- 1 root root 512M Sep  4  2016 /swapfile
# upsize
sudo fallocate -l 4G /swapfile
# result
ls -lh /swapfile
-rw------- 1 root root 4.0G Jul 23 03:54 /swapfile
```

## Another

```bash
sudo fallocate -l 1G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
sudo swapon --show
sudo cp /etc/fstab /etc/fstab.bak
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
sudo sysctl vm.swappiness=10
echo 'vm.swappiness=10' | sudo tee -a /etc/sysctl.conf
sudo sysctl vm.vfs_cache_pressure=50
echo 'vm.vfs_cache_pressure=50' | sudo tee -a /etc/sysctl.conf
```

## Reference

<https://www.digitalocean.com/community/questions/npm-gets-killed-no-matter-what>
