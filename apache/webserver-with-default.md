# How to install PHP Extension with default webserver

## Clear phpX

```bash
brew remove --force --ignore-dependencies httpd
brew remove --force --ignore-dependencies php70-xdebug php71-xdebug
brew remove --force --ignore-dependencies php70-imagick php71-imagick
brew remove --ignore-dependencies --force php70 php71 php72
```

## Check Apache is working

```bash
sudo apachectl status
sudo apachectl stop
sudo apachectl start
sudo apachectl restart
```

## Install Extension with brew

```bash
#intl
brew install php71-intl
#ImageMagick
brew install php71-imagick
#Memcache
brew install php71-igbinary php71-memcached
#GD
brew install php71-mcrypt
```

## Configure php.ini

```bash
cd /etc
sudo nano php.ini
extension=/usr/local/Cellar/php71-intl/7.1.14_25/intl.so
extension=/usr/local/Cellar/php71-imagick/3.4.3_6/imagick.so
extension=/usr/local/Cellar/php71-igbinary/2.0.5/igbinary.so
extension=/usr/local/Cellar/php71-memcached/3.0.3_3/memcached.so
extension=/usr/local/Cellar/php71-mcrypt/7.1.14_20/mcrypt.so
expose_php=off
# ctrl+O 
# ctrl+x
sudo apachectl restart
```

## Reference

<https://medium.com/@romaninsh/install-php-7-2-on-macos-high-sierra-with-homebrew-bdc4d1b04ea6>
