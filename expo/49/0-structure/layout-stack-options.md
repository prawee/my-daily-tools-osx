# How to update layout with Stack (option)

```bash
nano app/_layout.js
```

## Using Stack with option

```bash
import React from "react";
import { Stack } from "expo-router";

const Layout = () => {
    return (
        <Stack>
            <Stack.Screen
                name="index"
                options={{
                    title: 'login',
                }}
            />
        </Stack.Screen>
    );
}

export default Layout;
```