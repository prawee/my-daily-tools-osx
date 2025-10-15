# Convert original `JS` to `TS`

## With Blank template case

### (1) Root Files
- index.js -> index.ts
- App.js -> App.tsx

```sh
yarn start
# error
```

then fix it with this command
```
yarn add --dev typescript@~5.9.2 @types/react@~19.1.10  | yarn add --dev typescript@~5.9.2 @types/react@~19.1.10 -W
```

then install and run again
```sh
yarn | yarn install
yarn start | npx expo start
```
