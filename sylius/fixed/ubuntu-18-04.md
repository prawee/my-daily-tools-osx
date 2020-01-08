# How to checking required

## Ubuntu version

```bash
lsb_release -ds
```

## Create new user

```bash
adduser devchill --gecos "Prawee Wongsa"
#Enter new UNIX password & Retype
usermod -aG sudo devchill
su - devchill
```

## Set up timezone

```bash
sudo dpkg-reconfigure tzdata
#Type password
# Current default time zone: 'Asia/Bangkok'
# Local time is now:      Thu Jan  9 03:00:02 +07 2020.
# Universal Time is now:  Wed Jan  8 20:00:02 UTC 2020.
```

## Update system is up to date

```bash
sudo apt update && sudo apt upgrade -y
```

## Install this package

```bash
sudo apt install -y git curl wget unzip socat
```

## PHP and timezone

```bash
php --version
# PHP 7.2.24-0ubuntu0.18.04.1 (cli) (built: Oct 28 2019 12:07:07) ( NTS )
# Copyright (c) 1997-2018 The PHP Group
# Zend Engine v3.2.0, Copyright (c) 1998-2018 Zend Technologies
#     with Zend OPcache v7.2.24-0ubuntu0.18.04.1, Copyright (c) 1999-2018, by Zend Technologies
```

```bash
sudo nano /etc/php/7.2/fpm/php.ini
# memory_limit = 1024M
# date.timezone = Asia/Bangkok
sudo systemctl restart php7.2-fpm.service
```

## Nginx

```bash
# sudo apt install -y nginx
sudo nginx -v
# nginx version: nginx/1.14.0 (Ubuntu)
```

## Configure

```bash
sudo nano /etc/nginx/sites-enabled/yoursite.conf
```

```bash
server {
  listen 80;
  server_name example.com;
  root /var/www/sylius/public;
  location / {
    try_files $uri /index.php$is_args$args;
  }
  location ~ ^/index\.php(/|$) {
    fastcgi_pass unix:/run/php/php7.2-fpm.sock;
    fastcgi_split_path_info ^(.+\.php)(/.*)$;
    include fastcgi_params;
    fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
    fastcgi_param DOCUMENT_ROOT $realpath_root;
    internal;
  }
  location ~ \.php$ {
    return 404;
  }
  client_max_body_size 6m;
}
```

```bash
sudo nginx -t
sudo systemctl reload nginx.service
```

## Composer

```bash
composer --version
# Composer 1.6.3 2018-01-31 16:28:17
```

## Node.js

```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt install -y nodejs
node --version
# v10.18.0
```

## Yarn

```bash
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update && sudo apt-get install yarn
yarn --version
# 1.21.1
```

## Sylius

```bash
sudo mkdir -p /var/www/sylius
sudo chown -R devchill:devchill /var/www/sylius
cd /var/www/sylius
```

```bash
sudo rm -rf vendor
composer install
sudo rm -rf node_modules
yarn install
yarn build
sudo chown -R www-data:www-data /var/www/sylius
```
