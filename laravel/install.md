## Install Laravel CLI

### Required
```bash
$ composer --version
# Composer version 1.5.2 2017-09-11 16:59:25
```

### Check exist CLI
```bash
$ laravel
# zsh: command not found: laravel
```

### Installation with composer
```bash
$ composer global require "laravel/installer"
# waiting about 1 minute or depend on your internet
```

### Config PATH
```bash
$ export PATH=${PATH}:~/.composer/vendor/bin
# ~/.bash_profile | ~/.bashrc  | ~/.zprofile
```

### Recheck again
```bash
$ laravel
#  Usage: 
#   command [options] [arguments]
```

### Reference 
https://laravel.com/docs/5.5