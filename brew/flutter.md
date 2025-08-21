# How to install `Flutter` CLI

## Checking
```sh
flutter
# zsh: command not found: flutter
```

## Searching
```sh
brew info flutter | arch -arm64 brew info flutter

==> flutter: 3.35.1 (auto_updates)
https://flutter.dev/
Installed
/opt/homebrew/Caskroom/flutter/3.0.4 (4.9GB)
From: https://github.com/Homebrew/homebrew-cask/blob/HEAD/Casks/f/flutter.rb
==> Name
Flutter SDK
==> Description
UI toolkit for building applications for mobile, web and desktop
==> Artifacts
flutter -> /opt/homebrew/share/flutter (App Suite)
flutter/bin/dart (Binary)
flutter/bin/flutter (Binary)
==> Analytics
install: 12,201 (30 days), 33,039 (90 days), 95,659 (365 days)
```

## Installation
```sh
arch -arm64 brew install flutter
```

## Configure
```sh
flutter config --no-analytics
```

## Version
```sh
flutter --version
```

## Upgrade
```sh
flutter upgrade
```
