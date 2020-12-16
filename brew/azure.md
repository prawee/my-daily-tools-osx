# How to installation Azure CLI

## Brew

### Checking

```bash
az
#bash: az: command not found
```

### Installation

```bash
brew update && brew install azure-cli
```

waiting a minute

### Checking again

```bash
az version
```

```bash
{
  "azure-cli": "2.16.0",
  "azure-cli-core": "2.16.0",
  "azure-cli-telemetry": "1.0.6",
  "extensions": {}
}
```

## Reference

<https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-macos>
