# Install Extension for Yii2

## Intl extension

```bash
brew search php
brew install php71-intl
```

## Brew

```bash
sudo brew services reload nginx
sudo brew services reload php71
```

## Nginx

```bash
sudo nginx -s reload
sudo nginx -s reopen
```

## More

```bash
brew install php71-memcached
sudo brew services reload php71
brew install php71-imagick
sudo brew services reload php71
brew install php71-pdo-pgsql
sudo brew services reload php71
```

## Support Yii2

```bash
# Intl
brew install php71-intl
# Memcache
brew install php71-igbinary php71-memcached
# ImageMagick
brew install php71-imagick
# PDO PostgreSQL
brew install php71-pdo-pgsql
# APC
brew install php71-apcu-bc php71-apcu
# After install install extension
brew services restart php71
```

## Note

```bash
# Extension Path => /usr/local/etc/php/7.1/conf.d/
```
