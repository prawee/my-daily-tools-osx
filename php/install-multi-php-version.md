# How to installation mulitple version of PHP (M1)

## Current

```bash
php -v
# PHP 8.0.1
```

## More

### PHP 7.1

```bash
arch -arm64 brew install php@7.1
```

```bash
brew link php@7.1
php -v
# PHP 7.1.33
```

### PHP 7.4

```bash
arch -arm64 brew install php@7.4
```

```bash
php -v
# PHP 7.1.33
brew unlink php@7.1
php -v
# PHP 7.4.27
```
