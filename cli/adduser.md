# How to add user to Linux

## Adding account
```bash
$ adduser milk
# Adding user `milk' ...
# Adding new group `milk' (1004) ...
# Adding new user `milk' (1004) with group `milk' ...
# Creating home directory `/home/milk' ...
# Copying files from `/etc/skel' ...
Enter new UNIX password: [enter password]
Retype new UNIX password: [enter password again]
# passwd: password updated successfully
# Changing the user information for milk
# Enter the new value, or press ENTER for the default
# 	Full Name []:
# 	Room Number []:
# 	Work Phone []:
# 	Home Phone []:
# 	Other []:
Is the information correct? [Y/n] Y
```

## Role same root
```bash
$ usermod -aG sudo milk
```