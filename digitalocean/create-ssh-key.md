# How to generate SSH key

## Generate key

```bash
cd ~/.ssh
ssh-keygen -t rsa -b 4096 -C "konkeanweb@gmail.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/pod/.ssh/id_rsa): {name}
Enter passphrase (empty for no passphrase): {pass}
Enter same passphrase again: {pass again}
Your identification has been saved in test.
Your public key has been saved in test.pub.
The key fingerprint is:
SHA256:7FA9IRKRMJxO98EOCBSrQh4MA2zOtchBOzoYSn6WZW8 konkeanweb@gmail.com
The key's randomart image is:
+---[RSA 4096]----+
|Bo++o++=. .      |
|o=.o=.+.oo .     |
|*B=o.+ +..o      |
|OBo.= .oo  .     |
|Bo +  .ES        |
|..o   .o         |
|        .        |
|                 |
|                 |
+----[SHA256]-----+
```

## View all SSH

```bash
cd ~/.ssh
ls -la
-rw-r--r--   1 pod  staff   353 Jan 27 20:58 known_hosts
#.......
#.......
```
