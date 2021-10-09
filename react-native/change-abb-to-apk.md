# How to build .abb to .apk

How to build .abb to .apk

## With CLI

```bash
bundletool
# zsh: command not found: bundletool
```

```bash
arch -arm64 brew install bundletool
```

```bash
bundletool version
# 1.8.1
```

## Build

```bash
#root directory of project
cd android/app
bundletool build-apks --bundle=build/outputs/bundle/release/app.aab --output=build/outputs/bundle/release/vinvestor.apks --ks=my-release-key.keystore --ks-key-alias=my-key-alias

Enter keystore password:
```

change name of file to .zip and go to `standalones` folder


