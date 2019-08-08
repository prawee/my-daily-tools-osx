# Fixed can not create plugin

## Information

Install API and Graphql already

## Error

```bash
error No generator called `plugin` found.
```

## Fixed

```bash
npm link strapi-helper-plugin
```

### Checking package.json

```bash
strapi: "3.0.0-beta.13",
strapi-admin: "3.0.0-beta.13",
strapi-plugin-users-permissions": "3.0.0-beta.13"
```

## Reference

<https://github.com/strapi/strapi/issues/511>
