# How to installation MariaDB

## Check

```bash
mysql -v
# The program 'mysql' can be found in the following packages
```

## Installation

```bash
apt-get install software-properties-common
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://mirrors.bestthaihost.com/mariadb/repo/10.1/ubuntu xenial main'
apt-get update
apt-get install mariadb-server
# Y
# [root password]
# [retype root password]
```

## Configure Secure

```bash
mysql_secure_installation
# Enter current password for root (enter for none): [current password]
# Change the root password? [Y/n] [n]
# Remove anonymous users? [Y/n] [Y]
# Disallow root login remotely? [Y/n] n
# Remove test database and access to it? [Y/n] Y
# Reload privilege tables now? [Y/n] Y
# Thanks for using MariaDB!
```

## Usage

```bash
mysql -uroot -p
# [your password]
# MariaDB [(none)]>
```

## Create db

```bash
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
3 rows in set (0.00 sec)

MariaDB [(none)]> create database adonis_cit;
Query OK, 1 row affected (0.00 sec)

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| adonis_cit         |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.00 sec)
```
