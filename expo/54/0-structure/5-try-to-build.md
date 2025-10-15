# Try to testing build

## With `EAS`

### Checking `EAS` on your machine
```sh
eas --version
zsh: command not found: eas
```

### Install `EAS` CLI
```sh
npm install -g eas-cli
...
added 465 packages in 23s
60 packages are looking for funding
```

### `EAS` version
```sh
eas --version
eas-cli/16.23.0 darwin-arm64 node-v20.19.5
```

## Login `EAS`
```sh
eas login
```
```sh
✔ Email or username … xyz@hotmail.com
✔ Password … **************
Logged in
```

## Build Configure
```sh
eas build:configure
```
```sh
✔ Would you like to automatically create an EAS project for @prawee/try-expo? … yes
✔ Created @prawee/try-expo on EAS
✔ Linked local project to EAS project f95a3324-ea98-46cd-9ba0-02be06b2XXXX
✔ Which platforms would you like to configure for EAS Build? › All

✔ Generated eas.json. Learn more

🎉 Your project is ready to build.

- Run eas build when you are ready to create your first build.
- Once the build is completed, run eas submit to upload the app to app stores.
- Learn more about other capabilities of EAS Build
```

### Build `iOS`

```sh
eas build -p ios --profile development
```
```sh
✔ What would you like your iOS bundle identifier to be? … com.prawee.tryexpo
✔ iOS app only uses standard/exempt encryption? Learn more … yes
No remote versions are configured for this project, buildNumber will be initialized based on the value from the local project.
✔ Initialized buildNumber with 1.

Compressing project files and uploading to EAS Build. Learn more
✔ Uploaded to EAS 2s
✔ Computed project fingerprint
```

### Build `Android`
```sh
eas build -p android --profile development
```
```sh
✔ What would you like your Android application id to be? … com.prawee.tryexpo
No remote versions are configured for this project, versionCode will be initialized based on the value from the local project.
✔ Initialized versionCode with 1.
✔ Using remote Android credentials (Expo server)
✔ Generate a new Android Keystore? … yes
Detected that you do not have keytool installed locally.
✔ Generating keystore in the cloud...
✔ Created keystore

Compressing project files and uploading to EAS Build. Learn more
✔ Uploaded to EAS 2s
✔ Computed project fingerprint
```

### Build `Web`
```sh
npx expo export
```
