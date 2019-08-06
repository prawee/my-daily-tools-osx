# The following signatures were invalid: KEYEXPIRED 1507497109

## Problem

```bash
apt update
# ...
# The following signatures were invalid: KEYEXPIRED 1507497109
# ...
```

## Fixed

```bash
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
apt update
# 88 packages can be upgraded.
```
