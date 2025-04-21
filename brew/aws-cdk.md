# How to install `AWS CDK` with brew

## Checking
```bash
> cdk
zsh: command not found: cdk
```
## Searching
```bash
> brew search aws-cdk | arch -arm64 brew search aws-cdk
==> Formulae
aws-cdk                                     aws-sdk-cpp
```

## Installation
```bash
> arch -arm64 brew install aws-cdk
....
🍺  /opt/homebrew/Cellar/aws-cdk/2.1010.0: 305 files, 23.7MB
==> Running `brew cleanup aws-cdk`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
```

## Version
```bash
> cdk --version
2.1010.0 (build 6b421db)
```
