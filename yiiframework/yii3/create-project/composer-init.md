# How to create project via git

## Create folder and initial git
```bash
$ cd /var/www
$ mkdir yii3-rbac
$ cd yii3-rbac
$ composer init
#This command will guide you through creating your composer.json config.
Package name (<vendor>/<name>) [pod/yii3-rbac]: prawee/yii3-gae
Description []: Skeleton template project with Yii3
Author [Prawee Wongsa <prawee.w@integra8t.com>, n to skip]: Prawee Wongsa <prawee@hotmail.com>
Minimum Stability []: [enter]
Package Type (e.g. library, project, metapackage, composer-plugin) []: project
License []: MIT
Would you like to define your dependencies (require) interactively [yes]? no
Would you like to define your dev dependencies (require-dev) interactively [yes]? no
# {
#     "name": "prawee/yii3-rbac",
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