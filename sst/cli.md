# How to install CLI of `SST`

## Checking
```bash
$ sst
zsh: command not found: sst
```

## Installation
```bash
$ curl -fsSL https://sst.dev/install | bash
```
```bash
Downloading SST version: 3.13.17 ...
######################################################################## 100.0%
Successfully added SST to $PATH in /Users/prawee/.zshrc
```

## Using
```bash
$ sst

sst: deploy anything

  sst init               Initialize a new project
  sst dev [command]      Run in development mode
  sst deploy             Deploy your application
  sst diff               See what changes will be made
  sst add <provider>     Add a new provider
  sst install            Install all the providers
  sst secret             Manage secrets
  sst shell [command]    Run a command with linked resources
  sst remove             Remove your application
  sst unlock             Clear any locks on the app state
  sst version            Print the version of the CLI
  sst upgrade [version]  Upgrade the CLI
  sst telemetry          Manage telemetry settings
  sst refresh            Refresh the local app state
  sst state              Manage state of your app
  sst cert               Generate certificate for the Console
  sst tunnel             Start a tunnel
  sst diagnostic         Generates a diagnostic report

Learn more at https://sst.dev
```

## Version
```bash
$ sst version
sst 3.13.17
```
