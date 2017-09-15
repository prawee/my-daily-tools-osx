## Nginx with modules

### Unlink before
```bash
$ brew unlink nginx
```

### Install with brew
```bash
$ brew tap homebrew/nginx
$ brew install nginx-full --with-upload-module
```
### Run nginx without root
```bash
$ sudo chown root:wheel /usr/local/opt/nginx-full/bin/nginx
$ sudo chmod u+s /usr/local/opt/nginx-full/bin/nginx
```
### Using nginx without root
```bash
$ nginx -s reload
$ nginx -s reopen
$ nginx -s stop
$ nginx -s quit
$ nginx
```

### List of available configuration options
```bash
$ brew options nginx-full
$ brew info nginx-full
```

### Reference
https://github.com/Homebrew/homebrew-nginx