# How to create migrations 

### How to using migration command
configuration db first.
```bash
$ cd /var/www/yii2-gae-api
# command of yii
$ vendor/bin/yii 
# using migration must be --appconfig
$ vendor/bin/yii migrate --appconfig=config.php
```

### Create migrations
```bash
# exp. vendor/bin/yii migrate/create --appconfig=config.php <file-name> --fields="<fields>"
```