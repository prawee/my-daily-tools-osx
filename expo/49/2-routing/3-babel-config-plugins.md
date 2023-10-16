# How to setup plugins for router

```bash
nano babel.config.js
```

```bash
module.exports = function (api) {
    ...
    return {
        ...
        plugins: ['expo-router/babel', 'react-native-reanimated/plugin'],
    }
}
```