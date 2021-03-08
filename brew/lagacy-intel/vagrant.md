# Install Vagrant with brew

## Check brew first

```bash
> brew doctor
> brew update
> brew upgrade
> vagrant --version
Vagrant 2.0.0
```

## Installation

Vagrant

```bash
> brew cask install vagrant
brew cask reinstall vagrant
> brew cask reinstall vagrant
==> Downloading https://releases.hashicorp.com/vagrant/2.2.7/vagrant_2.2.7_x86_64.dmg
######################################################################## 100.0%
==> Verifying SHA-256 checksum for Cask 'vagrant'.
==> Uninstalling Cask vagrant
==> Running uninstall script uninstall.tool
Password:
The following files and directories will be removed:
    /opt/vagrant
    /usr/local/bin/vagrant

Do you wish to uninstall Vagrant (Yes/No)?
The uninstallation process requires administrative privileges
because some of the installed files cannot be removed by a
normal user. You may now be prompted for a password...


Successfully uninstalled Vagrant.
Done.
Press any key to exit.
==> Uninstalling packages:
com.vagrant.vagrant
==> Purging files for version 2.0.0 of Cask vagrant
==> Installing Cask vagrant
==> Running installer for vagrant; your password may be necessary.
==> Package installers may write to any location; options such as --appdir are ignored.
installer: Package name is Vagrant
installer: Installing at base path /
installer: The install was successful.
🍺  vagrant was successfully installed!
```

Vagrant Manager

```bash
> brew cask install vagrant-manager
brew cask reinstall vagrant-manager
> brew cask reinstall vagrant-manager
==> Downloading https://github.com/lanayotech/vagrant-manager/releases/download/2.7.1/vagrant-manager-2.7.1.dmg
==> Downloading from https://github-production-release-asset-2e65be.s3.amazonaws.com/18744882/9d66a480-17c4-11ea-8f71-
######################################################################## 100.0%
==> Verifying SHA-256 checksum for Cask 'vagrant-manager'.
==> Uninstalling Cask vagrant-manager
==> Backing App 'Vagrant Manager.app' up to '/usr/local/Caskroom/vagrant-manager/2.5.4/Vagrant Manager.app'.
==> Removing App '/Applications/Vagrant Manager.app'.
==> Purging files for version 2.5.4 of Cask vagrant-manager
==> Installing Cask vagrant-manager
==> Moving App 'Vagrant Manager.app' to '/Applications/Vagrant Manager.app'.
🍺  vagrant-manager was successfully installed!
```

## Version

```bash
> vagrant --version
Vagrant 2.2.7
```
