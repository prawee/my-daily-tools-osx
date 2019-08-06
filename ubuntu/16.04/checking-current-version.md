# How to checking current version

## Checking version

```bash
cat /etc/os-release
# NAME="Ubuntu"
# VERSION="16.04.6 LTS (Xenial Xerus)"
# ID=ubuntu
# ID_LIKE=debian
# PRETTY_NAME="Ubuntu 16.04.6 LTS"
# VERSION_ID="16.04"
# HOME_URL="http://www.ubuntu.com/"
# SUPPORT_URL="http://help.ubuntu.com/"
# BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
# VERSION_CODENAME=xenial
# UBUNTU_CODENAME=xenial
lsb_release -a
# No LSB modules are available.
# Distributor ID:Ubuntu
# Description:Ubuntu 16.04.6 LTS
# Release:16.04
# Codename:xenial
hostnamectl
  #  Static hostname: mongodb
  #        Icon name: computer-vm
  #          Chassis: vm
  #       Machine ID: fdde6ec2231ff9e1ace717e4534ff7c5
  #          Boot ID: 32c6710ae096470d87036f09c941aaa3
  #   Virtualization: kvm
  # Operating System: Ubuntu 16.04.6 LTS
  #           Kernel: Linux 4.4.0-157-generic
  #     Architecture: x86-64
uname -r
# 4.4.0-157-generic
```
