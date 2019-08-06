# Can't read of my.conf.d

```bash
mysql: Can't read dir of '/usr/local/etc/my.cnf.d' (Errcode: 2 "No such file or directory")
```

## Solved

```bash
mkdir /usr/local/etc/my.cnf.d
``
