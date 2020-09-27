# How to install XAMPP on OSX

## Search

```bash
brew search xampp
# ==> Casks
# xampp        xampp-vm
```

## Installation

```bash
brew cask install xampp
```

```bash
Updating Homebrew...
==> Auto-updated Homebrew!
Updated 1 tap (homebrew/cask).
==> Deleted Casks
jing

==> Downloading https://downloadsapachefriends.global.ssl.fastly.net/xampp-files/7.4.1/xampp-osx-7.4.1-0-installer.dmg
######################################################################## 100.0%
==> Verifying SHA-256 checksum for Cask 'xampp'.
==> Installing Cask xampp
==> Running installer script 'XAMPP.app/Contents/MacOS/osx-x86_64'
Password:

🍺  xampp was successfully installed!
```

## Start apache

```bash
sudo /Applications/XAMPP/xamppfiles/bin/apachectl start
```