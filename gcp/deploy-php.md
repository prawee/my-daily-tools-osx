## Google cloud platform

### Running your application (Yii2)
```bash
$ php -S localhost:8000 -t ./frontend/web
```

### Create app.yaml
```bash
runtime: php
env: flex
service: backend

runtime_config: 
  document_root:
```

### Deploy
```bash
# go to project root directory
$ gcloud app deploy ./app.yaml
# Do you want to continue (Y/n)? Y [enter]
# Please check your service before press Y
# Waiting...

```

### Reference
https://cloud.google.com/appengine/docs/flexible/php/quickstart
https://cloud.google.com/sdk/gcloud/reference/app/deploy