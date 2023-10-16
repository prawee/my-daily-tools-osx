# How to create layout

```bash
nano app/_layout.js
```

## Original

```bash
import React from "react";
import { View, Text } from "react-native";

const Layout = () => {
    return (
        <View>
            <Text>Layout</Text>
        </View>
    );
}

export default Layout;
```

## Using Stack

```bash
import React from "react";
# import { View, Text } from "react-native";
import { Stack } from "expo-router";

const Layout = () => {
    # return (
    #     <View>
    #         <Text>Layout</Text>
    #     </View>
    # );
    return <Stack />;
}

export default Layout;
```