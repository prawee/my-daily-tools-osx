# How to using `Monorepo` with `Bun`

In `package.json` add this

```sh
{
  ...
  "workspaces": [
     "packages/*"
  ],
}
```

On `root directory` add this

```sh
mkdir packages & cd packages
mkdir pkg-a
touch pkg-a/index.tsx
touch pkg-a/package.json
touch pkg-a/tsconfig.json
```

On `packages/pkg-a/index.tsx` add this
```sh
import { Text, View } from 'react-native';

export default () => (
  <View>
    <Text>App!</Text>
  </View>
)
```

On `packages/pkg-a/package.json` add this
```sh
{
    "name": "@aethers/app",
    "version": "1.0.0"
}
```

On `packages/pkg-a/tsconfig.json` add this
```sh
{
  "extends": "expo/tsconfig.base",
  "compilerOptions": {
    "strict": true
  }
}
```
