# Build android with Expo

## Custom

```bash
eas build
```

```bash
✔ Select platform › Android
✔ Generated eas.json
```

```bash
✔ What would you like your Android application id to be? … com.xx.booking
✔ Using remote Android credentials (Expo server)
```

```bash
✔ Generate a new Android Keystore? … yes
✔ Created keystore
```

```bash
Compressing project files and uploading to EAS Build. Learn more
✔ Uploaded to EAS
```

```bash
Waiting for build to complete. You can press Ctrl+C to exit.
✔ Build finished
```

## APK

```bash
nano eas.json
```

```bash
{
    ...
    "staging": {
      "android": {
        "buildType": "apk"
      }
    }
    ...
}
```

```bash
eas build -p android --profile staging
```