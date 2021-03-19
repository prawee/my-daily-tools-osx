# How to running

## PM2

### Digitalocean

```bash
# manual
NODE_ENV=production strapi start
# pm2
sudo pm2 start "npm start" --name=strapi-server/1337
```

### Locally

```bash
strapi develop
```
