# Create project with Yii3

## Create Project
```bash
$ cd /var/www
$ composer create-project --prefer-dist --stability=dev yiisoft/yii-project-template yii3-rbac
```

## Install package and dependencies
```bash
$ cd yii3-rbac
$ composer install | composer update
```

## Permission setup
```bash
$ chmod -R 777 ./public/assets
$ chmod -R 777 ./runtime
```

## Running
### Traditional
```bash
$ php -S localhost:8080 -t public
# localhost:8080
```
### Current
```bash
$ vendor/bin/yii serve -p 8081
# localhost:8081
```