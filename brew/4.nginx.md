## Nginx

### Check version
```bash
$ nginx -v
# nginx version: nginx/1.12.1
```

### Install with brew
```bash
$ brew doctor
$ brew update
$ brew upgrade
$ brew install nginx
$ brew services start nginx
```

### Default path
```bash
/usr/local/Cellar/nginx/1.12.1/html
```

### Update default configurations
```bash
$ nano /usr/local/etc/nginx/nginx.conf

# nginx.conf
user pod staff;
...
server {
    listen 80;
    ...
    location / {
        ...
        root /var/www;
        ...
    }
    ...
}
...

$ sudo nginx
$ sudo nginx -s reload
```

### How to using services
```bash
$ sudo nginx -s reload
$ sudo nginx -s reopen
```

### Reference
https://www.sylvaindurand.org/setting-up-a-nginx-web-server-on-macos/
