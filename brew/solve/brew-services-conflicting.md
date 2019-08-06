# Found command `brew-services` in following places

```bash
Warning: You have external commands with conflicting names.
Found command `brew-services` in following places:
  /usr/local/Homebrew/Library/Taps/homebrew/homebrew-services/cmd/brew-services.rb
  /usr/local/Homebrew/Library/Taps/gapple/homebrew-services/cmd/brew-services.rb
```

## Solved

```bash
brew untap gapple/services
```
