# How to using Swagger with Adonisjs

## Installation
```bash
$ cd /var/www/adonis-api
$ adonis install adonis-swagger
# config/swagger.js
# public/docs
```

## Configure
```bash
$ nano start/app.js
```

```bash
...
const providers = [
    ...
    'adonis-swagger/providers/SwaggerProvider'
    ...
]
...
```

## Usage
Set @swagger tag on your controller
```bash
# app/Controllers/Http/Api/v2/UserController.js
...
class UserController {
    ...
    /**
    * @swagger
    * /api/v2/user:
    *   get:
    *       tags:
    *           - User
    *       summary: Simple API
    *       parameters:
    *           - name: name
    *             description: Name of the user
    *             in: query
    *             required: false
    *             type: string
    *       response:
    *           200:
    *             description: Getting profile
    *             example:
    *               message: Hi
    */
    async profile() {
        ...
    }
    ...
}
...
```