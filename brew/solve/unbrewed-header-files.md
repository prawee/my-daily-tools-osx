# Fixed

```bash 
#Warning: Unbrewed header files were found in /usr/local/include.
```

## Node

```bash
sudo rm /usr/local/include/node/* && sudo rm -rf /usr/local/include/node/* && sudo rm -rf /usr/local/lib/dtrace
sudo chown -R whoami /usr/local && brew post-install node
```

## Reference

<https://github.com/Homebrew/legacy-homebrew/issues/34141>
