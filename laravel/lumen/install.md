## Install Lumen for RESTFul

### Make Lumen comment
```bash
$ composer global require "laravel/lumen-installer"
```

### Set path
```bash
$ cd
$ nano ~/.bash_profile | nano ~/.zprofile
```

```code
#lumen
$ export PATH="~/.composer/vendor/bin:$PATH"
```

### Enable/Active command
```bash
$ cd
$ source ~/.bash_profile | source ~/.zprofile
```

### Check
```bash
$ lumen -V
```