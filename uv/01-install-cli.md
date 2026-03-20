# How to install `UV` CLI

## Finding
```sh
uv
```
```sh
zsh: command not found: uv
```

## Installation
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```
```sh
downloading uv 0.10.12 aarch64-apple-darwin
no checksums to verify
installing to /Users/prawee.won/.local/bin
  uv
  uvx
everything's installed!

To add $HOME/.local/bin to your PATH, either restart your shell or run:

    source $HOME/.local/bin/env (sh, bash, zsh)
    source $HOME/.local/bin/env.fish (fish)
```

## Configure
```sh
sudo nano ~/.zshrc
```
```sh
# UV
source $HOME/.local/bin/env
#source $HOME/.local/bin/env.fish
```
```sh
source ~/.zshrc
```
