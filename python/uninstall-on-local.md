# How to uninstall Python on local

## Checking
```bash
$ which python
/usr/local/bin/python
```

## Uninstall
```bash
$ sudo rm -rf ~/Applications/Python
$ sudo rm -rf /usr/local/bin/python
```
## Clear
Using global search and typing "~/Library" then press Enter and follow delete step
```bash
$ sudo rm -rf ~/Library/Cahces/(App Name)
$ sudo rm -rf ~/Library/Preferences/(App Name)
$ sudo rm -rf ~/Library/Application Suport/(App Name)

# bin
$ cd /usr/local/bin
$ rm -rf python*
```