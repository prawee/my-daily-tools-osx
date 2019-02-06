# How to install PHP72

```bash
$ brew search php@7.2
# /usr/local/etc/php/7.2/
$ echo $PATH
# /usr/local/opt/php@7.1/sbin:/usr/local/opt/php@7.1/bin:/usr/local/opt/sphinx-doc/bin:/usr/local/opt/node@10/bin:/usr/local/opt/node@10/bin:/usr/local/sbin:/usr/local/opt/openldap/sbin:/usr/local/opt/openldap/bin:/Users/pod/google-cloud-sdk/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin:/Users/pod/Library/Android/sdk/platform-tools
$ brew install php@7.2
$ echo 'export PATH="/usr/local/opt/php@7.2/bin:$PATH"' >> ~/.zshrc
$ echo 'export PATH="/usr/local/opt/php@7.2/sbin:$PATH"' >> ~/.zshrc
$ source .zshrc
$ echo $PATH
# /usr/local/opt/php@7.2/sbin:/usr/local/opt/php@7.2/bin:/usr/local/opt/php@7.1/sbin:/usr/local/opt/php@7.1/bin:/usr/local/opt/sphinx-doc/bin:/usr/local/opt/node@10/bin:/usr/local/opt/node@10/bin:/usr/local/sbin:/usr/local/opt/openldap/sbin:/usr/local/opt/openldap/bin:/Users/pod/google-cloud-sdk/bin:/usr/local/opt/php@7.1/sbin:/usr/local/opt/php@7.1/bin:/usr/local/opt/sphinx-doc/bin:/usr/local/opt/node@10/bin:/usr/local/opt/node@10/bin:/usr/local/sbin:/usr/local/opt/openldap/sbin:/usr/local/opt/openldap/bin:/Users/pod/google-cloud-sdk/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin:/Users/pod/Library/Android/sdk/platform-tools:/Users/pod/Library/Android/sdk/platform-tools
$ which php
# /usr/local/opt/php@7.2/bin/php
$ php -v
# PHP 7.2.14 (cli) (built: Jan 12 2019 05:21:04) ( NTS )
# Copyright (c) 1997-2018 The PHP Group
# Zend Engine v3.2.0, Copyright (c) 1998-2018 Zend Technologies
#     with Zend OPcache v7.2.14, Copyright (c) 1999-2018, by Zend Technologies
```