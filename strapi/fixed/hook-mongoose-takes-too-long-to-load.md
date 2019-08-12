# Fixed can not start project

## Error

```bash
(hook:mongoose) takes too long to load
```

## Fixed

Update timeout from 3000 to 10000 at `config/hook.json`
