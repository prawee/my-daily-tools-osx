# How to using PORT

## Find the IDs of processes using a port
```bash
$ sudo lsof -t -i :8081
#2750
```

## Kill the process
```bash
$ kill 2750
# kill $(lsof -t -i :8081)
```