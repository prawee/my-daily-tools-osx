# If you want to remove or unload httpd 

## Check on 80 port

```bash
sudo lsof -i:80
# http  40135   _www    4u  IPV6 0xbecef8469a6f24f5 ...
# http  40137   _www    4u  IPV6 0xbecef8469a6f24f5 ...
# http  40139   _www    11u IPV6 0xbecef8469a6f24f5 ...
sudo apachectl stop
sudo lsof -i:80
# nothing that's ok  work!
# ps. but restart machine it's comming again
```

## Stop Service

```bash
sudo apachectl -k stop
sudo launchctl unload -w /System/Library/LaunchDaemons/org.apache.httpd.plist
```

## Rerference

<https://superuser.com/questions/986775/how-can-i-remove-apache2-that-i-have-installed-in-mac-os-x>
