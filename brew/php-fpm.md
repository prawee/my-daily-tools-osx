## Install PHP-FPM with brew

### Register php repository
```bash
$ brew tap homebrew/php
```

### Search and install
```bash
$ brew search php
$ brew install php71 --without-apache --with-fpm --with-mysql
$ brew install php71-mcrypt
```

### Control
```bash
$ sudo brew services start php71
# Successfully started `php71` (label: homebrew.mxcl.php71)
$ sudo brew services stop php71
# Successfully stopped `php71` (label: homebrew.mxcl.php71)
$ sudo brew services reload php71
# Successfully started `php71` (label: homebrew.mxcl.php71)
```

### Running processes
```bash
$ lsof -Pni4 | grep LISTEN | grep php
```

### Reference
https://xtracode.me/installing-nginx-php-fpm-mysql-on-mac-os/