# Using useRoute for link and button to another page

## Index to Register

```bash
nano app/index.js
```

```bash
import { Link, useRouter } from "expo-router";
import { ..., Button } from "react-native";
....

const Home = () => {
    const router = useRouter()
    return (
        <View>
            <Link href={'/register'} asChild>
                <Button title="Open Register" />
            </Link>
            ...
        </View>
    )
}
```