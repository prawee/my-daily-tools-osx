# Unable to load script from assets index.android.bundle

## Manual Fixed
1. Go to project directory and create assets folder.
```bash
$ cd /var/www/rnStart
$ mkdir android/app/src/main/assets
```
2. Run this command from create assets.
```bash
$ react-native bundle --platform android --dev false 
    --entry-file index.js 
    --bundle-output android/app/src/main/assets/index.android.bundle 
    --assets-dest android/app/src/main/res 
```
3. Run this command again.
```bash
$ react-native run-android
```

## Automate Fixed
```bash
$ cd /var/www/rnStart
$ nano package.json
# Move into scripts
...
"scripts": {
    ....
    "android-fixed": "react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res && react-native run-android" 
}
...
```

## Reference
https://stackoverflow.com/questions/44446523/unable-to-load-script-from-assets-index-android-bundle-on-windows