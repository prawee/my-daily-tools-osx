# How to fixed default password is invalid

## Information

- macOs Mojave
- installation mariadb via brew

## Problem

```bash
ERROR 1698 (28000): Access denied for user 'root'@'localhost'
```

## Fixed

```bash
sudo mysqladmin -u root --password='' password root
# enter your password
```
