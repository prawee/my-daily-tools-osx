# Error: Activity class does not exist

```bash
Error type 3
Error: Activity class {com.react_native/com.react_native.MainActivity} does not exist.
```

## Solve

```bash
adb uninstall com.react_native
#Success
react-native run-android
```

## PS

com.xyz  is mean current package
