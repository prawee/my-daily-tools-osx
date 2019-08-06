# How to uninstall all Python from macOS

## Uninstall with Brew

```bash
brew list
# python python3 python@2 ...
brew uninstall --force python
# Uninstalling python... (26,371 files, 437.6MB)
brew uninstall --force python@2
# Uninstalling python@2... (9,491 files, 168.3MB)
brew list
# without any python ...
```
