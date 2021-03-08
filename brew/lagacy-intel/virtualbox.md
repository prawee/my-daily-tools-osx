
# How to install Virtualbox

## Checking

```bash
> brew search virtualbox
==> Casks
virtualbox
virtualbox-extension-pack
homebrew/cask-versions/virtualbox-beta
homebrew/cask-versions/virtualbox-extension-pack-beta
```

## Installation

```bash
> brew cask install virtualbox
Updating Homebrew...
==> Caveats
To install and/or use virtualbox you may need to enable its kernel extension in:
  System Preferences → Security & Privacy → General
For more information refer to vendor documentation or this Apple Technical Note:
  https://developer.apple.com/library/content/technotes/tn2459/_index.html

==> Downloading https://download.virtualbox.org/virtualbox/6.1.4/VirtualBox-6.1.4-1361
######################################################################## 100.0%
==> Verifying SHA-256 checksum for Cask 'virtualbox'.
==> Installing Cask virtualbox
==> Running installer for virtualbox; your password may be necessary.
==> Package installers may write to any location; options such as --appdir are ignored
Password:
installer: Package name is Oracle VM VirtualBox
installer: choices changes file '/var/folders/hj/ff0mk7tn4rb8m2wf3fpdkjyc0000gn/T/choices20200220-62906-mexoh1.xml' applied
installer: Upgrading at base path /
installer: The upgrade was successful.
==> Changing ownership of paths required by virtualbox; your password may be necessary
🍺  virtualbox was successfully installed!
```

## Version

```bash
> vboxmanage --version
6.1.4r136177
```
