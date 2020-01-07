# How to running Sylius on Digitalocean

## Prerequitist

`Create droplet with LEMP`

## More install packgae

```bash
node -v
# -bash: /usr/bin/node: No such file or directory
npm -v
# -bash: /usr/bin/npm: No such file or directory
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
nvm install node -lts
```

```bash
node -v
#v13.5.0
npm -v
#if not to install please upgrade your server first
#6.13.4
npm i -g yarn
yarn --version
#1.21.1
```

## Create Database

```bash
mysql -uroot -p
#password
mysql > create database hhtlao default character set utf8 default collate utf8_general_ci;
mysql > show databases;
#|  hhtlao
```

## Clone your project

```bash
cd /var/www
git clone http://url-of-your-ropo.git ecommerce
cd ecommerce
```

## Configure environment

```bash
cp .env .env.local
```

```bash
APP_DEBUG=0
DATABASE_URL=mysql://root@127.0.0.1/dbname
```

## Installation project

```bash
apt install composer
composer --version
#Composer 1.6.3 2018-01-31 16.28.17
```

### Increase memory

```bash
nano /etc/php/7.2/cli/php.ini
#ctrl+w  => memory
#memory_limit = 2048M
#ctrl + W => timezone
#date.timezone = "Asia/Bangkok"
#ctrl+o => ctrl + X
```

### Enable extension

if you can not using `composer install` please update more php extension first

```bash
php --ini
# Configuration File (php.ini) Path: /etc/php/7.2/cli
# Loaded Configuration File:         /etc/php/7.2/cli/php.ini
# Scan for additional .ini files in: /etc/php/7.2/cli/conf.d
# Additional .ini files parsed:      /etc/php/7.2/cli/conf.d/10-mysqlnd.ini,
# /etc/php/7.2/cli/conf.d/10-opcache.ini,
# /etc/php/7.2/cli/conf.d/10-pdo.ini,
# /etc/php/7.2/cli/conf.d/20-apcu.ini,
# /etc/php/7.2/cli/conf.d/20-apcu_bc.ini,
# /etc/php/7.2/cli/conf.d/20-calendar.ini,
# /etc/php/7.2/cli/conf.d/20-ctype.ini,
# /etc/php/7.2/cli/conf.d/20-curl.ini,
# /etc/php/7.2/cli/conf.d/20-exif.ini,
# /etc/php/7.2/cli/conf.d/20-fileinfo.ini,
# /etc/php/7.2/cli/conf.d/20-ftp.ini,
# /etc/php/7.2/cli/conf.d/20-gettext.ini,
# /etc/php/7.2/cli/conf.d/20-iconv.ini,
# /etc/php/7.2/cli/conf.d/20-json.ini,
# /etc/php/7.2/cli/conf.d/20-mysqli.ini,
# /etc/php/7.2/cli/conf.d/20-pdo_mysql.ini,
# /etc/php/7.2/cli/conf.d/20-phar.ini,
# /etc/php/7.2/cli/conf.d/20-posix.ini,
apt install php-mbstring
apt install php-intl
apt install php-xml
apt install php-gd
apt install php-zip
```

## Continue

```bash
composer install
# ....
# Executing script cache:clear [OK]
# Executing script assets:install public [OK]
yarn install
#Done in 164.37s
yarn build
#Done in 23.21s
```

## Nginx

create script on `/etc/nginx/sites-enabled`

```bash
server {
  listen 80;
  server_name yourdomain or ip-address;
  root /var/www/ecommerce/public;

  index index.html index.htm index.php;

  charset utf-8;

  location / {
    try_files $uri $uri/ /index.php$query_string;
  }

  error_page 404 /index.php;

  location ~ \.php$ {
    fastcgi_pass unix:/var/run/php/php7.2-fpm.sock;
    fastcgi_index index.php;
    fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
    include fastcgi_params;
  }

  location ~ /\.(?!well-known).* {
    deny all;
  }
}
```

## Permission

```bash
chmod -R 777 var/
```

## MySQL

```bash
mysql> create user 'ecom'@'localhost' identified by '--pwd--';
mysql> grant all privileges on dbname.* to 'ecom'@'localhost';
mysql> flush privileges;
mysql> exit;
```

### Update new password

```bash
mysql> update mysql.user set authentication_string = password('new_user_password') where User = 'ecom' and Host = 'localhost';
mysql> plush privileges;
 ```
