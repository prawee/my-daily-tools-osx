# How to fixed out of memory

## Error

when you run `strapi develop` that getting this data `FATAL ERROR: Ineffective mark-compacts near heap limit Allocation failed - JavaScript heap out of memory`

## Fixed

```bash
NODE_OPTIONS=--max-old_space_size=8192 strapi build
```
