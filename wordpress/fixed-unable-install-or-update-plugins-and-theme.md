# Wordpress with FTP or SFTP

## Fixed enabled install themes and plugins

```bash
sudo nano wp-config.php
# defined this before end file
define('FS_METHOD', 'direct');
```

## Reference

<https://www.barrykooij.com/unable-to-install-plugins-on-localhost>
