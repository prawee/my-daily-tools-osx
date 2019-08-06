# Nginx with PHP7

## Check

```bash
nginx -v
# -bash: /usr/local/bin/nginx: No such file or directory
brew list
```

## Install with brew

```bash
brew install nginx
```

## Start services

```bash
sudo nginx  | brew services start nginx
```

## Make autostart

```bash
sudo cp /usr/local/opt/nginx/*.plist /Library/LaunchDaemons/
sudo chown root:wheel /Library/LaunchDaemons/homebrew.mxcl.nginx.plist
```

## Setup virtuals

```bash
mkdir -p /usr/local/etc/nginx/sites-available
mkdir -p /usr/local/etc/nginx/sites-enabled
mkdir -p /usr/local/etc/nginx/conf.d | sudo mv /usr/local/etc/nginx/servers conf.d
sudo mkdir -p /var/www
sudo chown :staff /var/www
sudo chmod 775 /var/www
```

### Start and Stop

```bash
launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.nginx.plist
launchctl unload -w ~/Library/LaunchAgents/homebrew.mxcl.nginx.plist
```

### Change default nginx.conf

```bash
rm /usr/local/etc/nginx/nginx.conf
curl -L https://gist.github.com/frdmn/7853158/raw/nginx.conf -o /usr/local/etc/nginx/nginx.conf
```

### Make defualt virtual hosts

```bash
curl -L https://gist.github.com/frdmn/7853158/raw/sites-available_default -o /usr/local/etc/nginx/sites-available/default
```

### Control Nginx

```bash
sudo nginx -s reload
sudo nginx -s reopen
```

### Reference

<https://xtracode.me/installing-nginx-php-fpm-mysql-on-mac-os/>
<https://gist.github.com/dtomasi/ab76d14338db82ec24a1fc137caff75b>
<https://gist.github.com/wahyudibo/5c8560ce63c0d57ac3e13855f07578fb>
