# Fixed MySQL database is broken

## Checking status

```bash
brew services list
#mariadb           stopped
```

## Remove old

```bash
cd /usr/local/var/mysql/mysql
rm -rf *
```

## Initial

```bash
mysql_install_db
```

## Start services

```bash
brew services start mariadb
```
