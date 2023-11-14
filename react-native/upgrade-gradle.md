# How to upgrade Gradle

## Version

```bash
./android/gradlew --version
```

```bash
------------------------------------------------------------
Gradle 5.5
------------------------------------------------------------

Build time:   2019-06-28 17:36:05 UTC
Revision:     83820928f3ada1a3a1dbd9a6c0d47eb3f199378f

Kotlin:       1.3.31
Groovy:       2.5.4
Ant:          Apache Ant(TM) version 1.9.14 compiled on March 12 2019
JVM:          1.8.0_292 (AdoptOpenJDK 25.292-b10)
OS:           Mac OS X 10.16 x86_64
```

## Upgrade

```bash
./android/gradlew wrapper --gradle-version 6.0
```

```bash
BUILD SUCCESSFUL in 1s
1 actionable task: 1 executed
```