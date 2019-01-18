#How to keep storage

##NPM
```bash
$ npm cache verify
$ npm cache clean --force
```

##Cache
```bash
$ sudo du -sh /Library/Caches
Password: 
#187M /Library/Caches
$ rm -rf /Library/Caches/*
```