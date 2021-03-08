# Install PHP 7.3 with Brew

## Installation

```bash
php -v
# PHP 7.1.23 (cli) (built: Feb 22 2019 22:19:32) ( NTS )
# Copyright (c) 1997-2018 The PHP Group
# Zend Engine v3.1.0, Copyright (c) 1998-2018 Zend Technologies
brew list
# without php
brew install php | brew install php@7.3
# ....
# exit terminal
php -v
# PHP 7.3.6 (cli) (built: May 31 2019 23:38:25) ( NTS )
# Copyright (c) 1997-2018 The PHP Group
# Zend Engine v3.3.6, Copyright (c) 1998-2018 Zend Technologies
#     with Zend OPcache v7.3.6, Copyright (c) 1999-2018, by Zend Technologies
```

## Link

```bash
brew link php@7.3 --force
# ...
# exit terminal
php -v
# PHP 7.3.21 (cli) (built: Aug  7 2020 18:56:36) ( NTS )
# Copyright (c) 1997-2018 The PHP Group
# Zend Engine v3.3.21, Copyright (c) 1998-2018 Zend Technologies
#    with Zend OPcache v7.3.21, Copyright (c) 1999-2018, by Zend Technologies
```

## Reference

<https://stitcher.io/blog/php-73-upgrade-mac>
<https://stackoverflow.com/questions/58290566/install-ext-zip-for-mac>
