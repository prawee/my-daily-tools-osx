# How to create project via git

## Create folder and initial git
```bash
$ cd /var/www
$ mkdir yii3-web
$ cd yii3-web
$ composer init
#This command will guide you through creating your composer.json config.
Package name (<vendor>/<name>) [pod/yii3-web]: prawee/yii3-web
Description []: Skeleton template project with Yii3
Author [Prawee Wongsa <prawee.w@integra8t.com>, n to skip]: Prawee Wongsa <prawee@hotmail.com>
Minimum Stability []: [enter]
Package Type (e.g. library, project, metapackage, composer-plugin) []: project
License []: MIT
Would you like to define your dependencies (require) interactively [yes]? no
Would you like to define your dev dependencies (require-dev) interactively [yes]? no
# {
#     "name": "prawee/yii3-web",
#     "description": "Skeleton template project with Yii3",
#     "type": "project",
#     "license": "MIT",
#     "authors": [
#         {
#             "name": "Prawee Wongsa",
#             "email": "prawee@hotmail.com"
#         }
#     ],
#     "require": {}
# }
Do you confirm generation [yes]? yes
```

## Installing packages
```bash
$ cd /var/www/yii3-web
$ composer require yiisoft/yii-base-web
# Using version ^3.0@dev for yiisoft/yii-base-web
# ./composer.json has been updated
# Loading composer repositories with package information
# Updating dependencies (including require-dev)
# Package operations: 24 installs, 0 updates, 0 removals
#   - Installing hiqdev/composer-config-plugin (dev-master 9f61a78): Cloning 9f61a78208 from cache
#   - Installing symfony/polyfill-ctype (dev-master 82ebae0): Cloning 82ebae0220 from cache
#   - Installing vlucas/phpdotenv (2.6.x-dev 2a7dcf7): Cloning 2a7dcf7e3e from cache
#   - Installing doctrine/lexer (dev-master 4ab6ea7): Cloning 4ab6ea7c83 from cache
#   - Installing egulias/email-validator (2.1.7): Downloading (100%)         
#   - Installing symfony/polyfill-mbstring (dev-master fe5e94c): Cloning fe5e94c604 from cache
#   - Installing symfony/polyfill-iconv (dev-master f037ea2): Cloning f037ea22ac from cache
#   - Installing symfony/polyfill-php72 (dev-master ab50dcf): Cloning ab50dcf166 from cache
#   - Installing symfony/polyfill-intl-idn (v1.10.0): Downloading (100%)         
#   - Installing swiftmailer/swiftmailer (dev-master c2100aa): Cloning c2100aa5bf from cache
#   - Installing psr/simple-cache (dev-master 408d5ea): Cloning 408d5eafb8 from cache
#   - Installing yiisoft/cache (dev-master f9aa30c): Cloning f9aa30ca51 from cache
#   - Installing psr/container (1.0.0): Downloading (100%)         
#   - Installing yiisoft/di (dev-master fb3de76): Cloning fb3de76755 from cache
#   - Installing psr/log (1.0.2): Downloading (100%)         
#   - Installing yiisoft/log (dev-master 30d24a5): Cloning 30d24a57eb from cache
#   - Installing yiisoft/yii-core (dev-master b94f3a3): Cloning b94f3a3066 from cache
#   - Installing yiisoft/yii-swiftmailer (dev-master f07b6d7): Cloning f07b6d7efc from cache
#   - Installing yiisoft/db (dev-master 36c97b1): Cloning 36c97b18b2 from cache
#   - Installing yiisoft/active-record (dev-master bed8118): Cloning bed8118208 from cache
#   - Installing yiisoft/view (dev-master 58a2fa1): Cloning 58a2fa1318 from cache
#   - Installing psr/http-message (dev-master f6561bf): Cloning f6561bf28d from cache
#   - Installing yiisoft/yii-web (dev-master 2b3d8e9): Cloning 2b3d8e9354 from cache
#   - Installing yiisoft/yii-base-web (dev-master 786adc5): Cloning 786adc53eb from cache
# hiqdev/composer-config-plugin suggests installing symfony/yaml (^2.0 || ^3.0 || ^4.0 for YAML files support)
# swiftmailer/swiftmailer suggests installing true/punycode (Needed to support internationalized email addresses, if ext-intl is not installed)
# yiisoft/yii-core suggests installing ezyang/htmlpurifier (Version '^4.6' is required at 'yii\helpers\HtmlPurifier' and for 'html' data format support (e.g. 'yii\i18n\Formatter:asHtml()'))
# yiisoft/yii-web suggests installing yiisoft/yii2-coding-standards (you can use this package to check for code style issues when contributing to yii)
# Writing lock file
# Generating autoload files
# Assembling config files 
```

## Fixed dependencies
```bash
$ composer require symfony/yaml
# Using version ^4.3@dev for symfony/yaml
# ./composer.json has been updated
# Loading composer repositories with package information
# Updating dependencies (including require-dev)
# Package operations: 1 install, 0 updates, 0 removals
#   - Installing symfony/yaml (dev-master 9744e59): Cloning 9744e5991d from cache
# symfony/yaml suggests installing symfony/console (For validating YAML files using the lint command)
# Writing lock file
# Generating autoload files
# Assembling config files
$ composer require ezyang/htmlpurifier
# Using version dev-master for ezyang/htmlpurifier
# ./composer.json has been updated
# Loading composer repositories with package information
# Updating dependencies (including require-dev)
# Package operations: 1 install, 0 updates, 0 removals
#   - Installing ezyang/htmlpurifier (dev-master a93250f): Cloning a93250f251 from cache
# Writing lock file
# Generating autoload files
# Assembling config files
$ composer require yiisoft/yii2-coding-standards
# Using version dev-master for yiisoft/yii2-coding-standards
# ./composer.json has been updated
# Loading composer repositories with package information
# Updating dependencies (including require-dev)
# Package operations: 2 installs, 0 updates, 0 removals
#   - Installing squizlabs/php_codesniffer (dev-master b289337): Downloading (100%)
#   - Installing yiisoft/yii2-coding-standards (dev-master 63385e6): Cloning 63385e68af from cache
# Writing lock file
# Generating autoload files
# Assembling config files
```

## Create public folder and initial file to first run
```bash
$ mkdir public
$ cd public
$ nano index.php
```
### index.php
```bash
use yii\helpers\Yii;
use yii\di\Container;
use hiqdev\composer\config\Builder;

(function() {
    require_once __DIR__ '/../vendor/autoload.php';
    $container = new Container(require Builder::path('web'));
    Yii::setContainer($container);
    $container->get('app')->run();
})();
```

## Running project
```bash
$ php -S localhost:8080 -t public
```