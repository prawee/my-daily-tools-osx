# Requirements are not fulfilled

```html
Some system requirements are not fulfilled. Please check output messages and fix them.
```

## timezone

```bash
php -i | grep timezone
# Default timezone => UTC
# date.timezone => no value => no value
```

```bash
php --ini
# Configuration File (php.ini) Path: /usr/local/etc/php/7.4
# Loaded Configuration File:         /usr/local/etc/php/7.4/php.ini
# Scan for additional .ini files in: /usr/local/etc/php/7.4/conf.d
# Additional .ini files parsed:      /usr/local/etc/php/7.4/conf.d/ext-opcache.ini
```

```bash
nano /usr/local/etc/php/7.4/php.ini
# ctrl + w => date.timezone
```

```bash
date.timezone = "Asia/Bangkok"
```
