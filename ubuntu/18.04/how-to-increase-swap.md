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
