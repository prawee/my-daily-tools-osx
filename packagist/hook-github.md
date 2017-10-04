## GitHub Service Hook

### Getting API token
Go to https://packagist.org/profile and click "Your API token" button then copy token.

### Via Manual
prepare API_TOKEN from packagist and copy link from github
```bash
$ curl -XPOST -H'content-type:application/json' 'https://packagist.org/api/update-package?username=prawee&apiToken=API_TOKEN' -d'{"repository":{"url":"PACKAGIST_PACKAGE_URL"}}'
# {"status":"success"}
```