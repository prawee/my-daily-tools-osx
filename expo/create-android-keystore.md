# How to create an android keystore file

## Checking command line

```bash
keytool
# Key and Certificate Management Tool

# Commands:

#  -certreq            Generates a certificate request
#  -changealias        Changes an entry's alias
#  -delete             Deletes an entry
#  -exportcert         Exports certificate
#  -genkeypair         Generates a key pair
#  -genseckey          Generates a secret key
#  -gencert            Generates certificate from a certificate request
#  -importcert         Imports a certificate or a certificate chain
#  -importpass         Imports a password
#  -importkeystore     Imports one or all entries from another keystore
#  -keypasswd          Changes the key password of an entry
#  -list               Lists entries in a keystore
#  -printcert          Prints the content of a certificate
#  -printcertreq       Prints the content of a certificate request
#  -printcrl           Prints the content of a CRL file
#  -storepasswd        Changes the store password of a keystore

# Use "keytool -command_name -help" for usage of command_name
```

## Generate file

```bash
cd ~
mkdir Keystore
cd Keystore
keytool -genkey -v -keystore file.keystore -alias YOUR_ALIAS_NAME -storepass YOUR_ALIAS_PWD -keypass YOUR_ALIAS_PWD -keyalg RSA -validity 36500
What is your first and last name?
  [Unknown]: pos
What is the name of your organizational unit?
  [Unknown]: programmer
What is the name of your organization?
  [Unknown]: gpslao
What is the name of your City or Locality?
  [Unknown]: Vientiane
What is the name of your State or Province?
  [Unknown]:  vientiane
What is the two-letter country code for this unit?
  [Unknown]: LA
Is CN=pos, OU=programmer, O=gpslao, L=vientiane, ST=vientiane, C=LA correct?
  [no]:  yes

# Generating 2,048 bit RSA key pair and self-signed certificate (SHA256withRSA) with a validity of 36,500 days
#         for: CN=pos, OU=programmer, O=gpslao, L=vientiane, ST=vientiane, C=LA
# [Storing gpslao.keystore]

# Warning:
# The JKS keystore uses a proprietary format. It is recommended to migrate to PKCS12 which is an industry standard format using "keytool -importkeystore -srckeystore gpslao.keystore -destkeystore gpslao.keystore -deststoretype pkcs12".
```
