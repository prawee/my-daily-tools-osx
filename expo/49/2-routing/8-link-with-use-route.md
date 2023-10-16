# Using useRoute for link to another page

## Index to Register

```bash
nano app/index.js
```

```bash
import { useRouter } from "expo-router";
import { ..., Button } from "react-native";
....

const Home = () => {
    const router = useRouter()
    return (
        <View>
            <Button onPress={() => router.push("/register")} title="Open Register" />
            ...
        </View>
    )
}
```