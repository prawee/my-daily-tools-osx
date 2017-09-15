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

### List of available configuration options
```bash
$ brew options nginx-full
$ brew info nginx-full
```

### Reference
https://github.com/Homebrew/homebrew-nginx