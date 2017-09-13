## Node

### Check version
```bash
$ nginx -v
# nginx version: nginx/1.12.1
```

### Origin remove
```bash
$ sudo rm -rf /usr/local/{lib/node{,/.npm,_modules},bin,share/man}/{npm*,node*,man1/node*}
```

### Install 
```bash
$ brew install node
$ brew link --overwrite node
```