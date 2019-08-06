# How to adding user and priviledge

## Adding User

```bash
# login with root
adduser meteor
# ...
# Enter new UNIX password: {password}
# Retype new UNIX password: {repeat password}
# ...
#    Full Name []: {Prawee Wongsa}
#    Room Number []: {}
#    Work Phone []: {}
#    Home Phone []: {}
#    Other []: {}
#  Is the information correct? [Y/n] Y
```

## Adding root privileges

```bash
usermod -aG sudo meteor
```
