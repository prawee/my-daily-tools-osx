# Can't run a refresh new project  (react-native 0.59.1)

## Problem

<https://github.com/facebook/react-native/issues/24112>

## Solve with short-term

have CMD/Terminal exist 2 windows

- windows 1 with > react-native run-android  
- windows 2 with build android  

Then
On windows 2

```bash
react-native  start --reset-cache
```

On windows 1

```bash
kill $(lsof -t -i:8081)
react-native run-android
```

## Solve with long-term

using react-native 0.58.6 (stable version)
