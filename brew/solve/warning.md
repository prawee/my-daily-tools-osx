# How to solve warning

## mongodb
```bash
$ brew cleanup
# Warning: Skipping mongodb: most recent version 4.0.3_1 not installed
$ brew uninstall mongodb
$ brew cleanup
```

## homebrew/nginx/upload-nginx-module
```bash
$ brew cleanup
# Warning: Skipping homebrew/nginx/upload-nginx-module: most recent version 2.3.0 not installed
$ brew uninstall upload-nginx-module
# Uninstalling /usr/local/Cellar/upload-nginx-module/2.255.2... (16 files, 174KB)
# upload-nginx-module 2.255.1 is still installed.
# Remove all versions with `brew uninstall --force upload-nginx-module`.
$ brew uninstall --force upload-nginx-module
# Uninstalling upload-nginx-module... (9 files, 144KB)
```