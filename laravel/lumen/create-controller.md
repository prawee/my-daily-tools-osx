## Create Controller

### Install package
```bash
$ cd <your-project>
$ composer require wn/lumen-generators
```
### 

### Create Controller
```bash
$ cd <your-project>
$ php artisan wn:controller Activity
# ActivitiesController generated ! => app/Http/Controllers/ActivitiesController.php
# activity routes generated! => routes/web.php
```

### Updated
```bash
# web/routes.php
# change variable via generated from $app to $router
```