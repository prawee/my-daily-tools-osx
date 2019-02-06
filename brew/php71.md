# How to install PHP71 via manaul

### Install PHP71 with Brew
```bash
$ brew search php71
$ brew install php71
# brew reinstall -s php71
```

### Start
```bash
$ brew services start homebrew/php/php71
$ brew services stop homebrew/php/php71
$ brew services restart homebrew/php/php71
```

## Version
```bash
$ php -v
# PHP 7.1.14
```

## Update 20190206
```bash
$ brew uninstall php71 php71-apcu php71-apcu-bc php71-igbinary php71-mcrypt
# Uninstalling /usr/local/Cellar/php71-apcu/5.1.8... (22 files, 163.2KB)
# Uninstalling /usr/local/Cellar/php71-apcu-bc/1.0.3... (3 files, 17.6KB)
# Uninstalling /usr/local/Cellar/php71-igbinary/2.0.5... (7 files, 51.3KB)
# Uninstalling /usr/local/Cellar/php71-mcrypt/7.1.14_20... (7 files, 198.3KB)
$ brew cleanup
$ brew search php
# brew-php-switcher                                        php@7.1
# homebrew/nginx/php-session-nginx-module                  php@7.2
# php                                                      phplint
# php-code-sniffer                                         phpmyadmin
# php-cs-fixer                                             phpunit
$ which php
# /usr/bin/php  <= stock version
$ brew install php@71
# /usr/local/etc/php/7.1/  <=php.ini and php-fpm.ini
# echo 'export PATH="/usr/local/opt/php@7.1/bin:$PATH"' >> ~/.zshrc
# echo 'export PATH="/usr/local/opt/php@7.1/sbin:$PATH"' >> ~/.zshrc
# export LDFLAGS="-L/usr/local/opt/php@7.1/lib"
# export CPPFLAGS="-I/usr/local/opt/php@7.1/include"
$ brew services start php@7.1
$ brew services restart php@7.1
```
```bash
$ echo $PATH
# /usr/local/opt/sphinx-doc/bin:/usr/local/opt/node@10/bin:/usr/local/opt/node@10/bin:/usr/local/sbin:/usr/local/opt/openldap/sbin:/usr/local/opt/openldap/bin:/Users/pod/google-cloud-sdk/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin:/Users/pod/Library/Android/sdk/platform-tools
$ source .zshrc
$ echo $PATH
# /usr/local/opt/php@7.1/sbin:/usr/local/opt/php@7.1/bin:/usr/local/opt/sphinx-doc/bin:/usr/local/opt/node@10/bin:/usr/local/opt/node@10/bin:/usr/local/sbin:/usr/local/opt/openldap/sbin:/usr/local/opt/openldap/bin:/Users/pod/google-cloud-sdk/bin:/usr/local/opt/sphinx-doc/bin:/usr/local/opt/node@10/bin:/usr/local/opt/node@10/bin:/usr/local/sbin:/usr/local/opt/openldap/sbin:/usr/local/opt/openldap/bin:/Users/pod/google-cloud-sdk/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin:/Users/pod/Library/Android/sdk/platform-tools:/Users/pod/Library/Android/sdk/platform-tools
$ which php
# /usr/local/opt/php@7.1/bin/php <= homebrew version
```
## Remove 
```bash
$ brew uninstall php@7.1
# Uninstalling /usr/local/Cellar/php@7.1/7.1.25... (513 files, 63.2MB)
```