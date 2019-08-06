# How to setup development environment for spring framework

## Tools

1. Postman
2. MariaDB
3. Sequel Pro
4. Java 8 SDK
5. Spring Tool Suite(STS)

## Postman

Download from <https://www.getpostman.com>

## MariaDB

Installation mariadb with brew

## Sequel Pro

Download from <https://sequelpro.com>

## JAVA 8 SDK

```bash
java -version
# java version "1.8.0_131"
# Java(TM) SE Runtime Environment (build 1.8.0_131-b11)
# Java HotSpot(TM) 64-Bit Server VM (build 25.131-b11, mixed mode)
echo $JAVA_HOME
# empty
echo "export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home" >> ~/.zshrc
source ~/.zshrc
echo $JAVA_HOME
# /Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home
```

## Spring Tool Suite(STS) with VSCode

Download from <https://spring.io/tools>
Then <https://marketplace.visualstudio.com/items?itemName=Pivotal.vscode-boot-dev-pack>
