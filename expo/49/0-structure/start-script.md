# Create shell script

```bash
nano start.sh
```

```bash
bunx create-expo . -t expo-template-blank

bunx expo install expo-router react-native-safe-area-context react-native-screens expo-linking expo-constants  
bunx expo install react-native-web@~0.19.6 react-dom@18.2.0
bunx expo install @react-navigation/drawer react-native-gesture-handler react-native-reanimated
```