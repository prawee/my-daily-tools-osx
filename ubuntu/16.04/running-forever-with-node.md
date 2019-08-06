# How to running forever package with node

## Running

```bash
forever start -c "node -r babel-register" ./index.js
```

## List

```bash
forever list
```

## Stop

```bash
forever stop {uid}
```
