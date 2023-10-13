# How to create first route or bootstrap

## Create folder

```bash
mkdir app
```

## Create bootstrap file

```bash
nano app/index.js
```

```bash
import { View, Text } from "react-native";

const Home = () => {
    return (
        <View>
            <Text>Home</Text>
        </View>
    )
}

export default Home;
```

## Create layout

```bash
nano app/_layout.js
```

```bash
import { Stack } from "expo-router";

const Layout = () => {
    return <Stack />;
}

export default Layout;
```

## Running

```bash
npx expo
```

## Fix (if not display)

```bash
yarn add expo-font
```