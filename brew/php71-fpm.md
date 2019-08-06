# Install PHP-FPM with brew

## Register php repository

```bash
brew tap homebrew/php
```

## Search and install

```bash
brew search php
brew install php71 --without-apache --with-fpm --with-mysql
brew install php71-mcrypt
```

## php.ini

/usr/local/etc/php/7.1/php.ini

## .bash_profile

```bash
sudo nano .bash_profile
PATH="/usr/local/bin:$PATH"  #before /usr/sbin
```

## Launch php-fpm on startup

```bash
mkdir -p ~/Library/LaunchAgents
cp /usr/local/opt/php71/homebrew.mxcl.php71.plist ~/Library/LaunchAgents/
launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.php71.plist
```

### Control PHP71-FPM

```bash
/usr/local/opt/php71/sbin/php71-fpm  | php71-fpm
# php71-fpm start
# php71-fpm stop
# php71-fpm restart
```

### Control PHP71

```bash
sudo brew services start php71
# Successfully started `php71` (label: homebrew.mxcl.php71)
sudo brew services stop php71
# Successfully stopped `php71` (label: homebrew.mxcl.php71)
sudo brew services reload php71
# Successfully started `php71` (label: homebrew.mxcl.php71)
```

### Running processes

```bash
lsof -Pni4 | grep LISTEN | grep php
```

## Reference

<https://xtracode.me/installing-nginx-php-fpm-mysql-on-mac-os/>
