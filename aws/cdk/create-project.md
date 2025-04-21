# How to create project with `AWS CDK`

## Prerequisite
- Node v20.19.x or higher
- Bun 1.0.6 or higher
- AWS CDK 2.1010.x or higher

## Initial
### Prepare folder first
```bash
$ cd code/brt
$ mkdir aws && cd aws
$ mkdir auther-msc && cd auther-msc
$ pwd
# /Users/prawee/code/brt/aws/auther-msc
```
### Let's go
```bash
$ cdk init -l typescript
# Welcome to your CDK TypeScript project

This is a blank project for CDK development with TypeScript.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

## Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `npx cdk deploy`  deploy this stack to your default AWS account/region
* `npx cdk diff`    compare deployed stack with current state
* `npx cdk synth`   emits the synthesized CloudFormation template

Initializing a new git repository...
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint: 	git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: 	git branch -m <name>
Executing npm install...
npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm warn deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
✅ All done!
```

## Running
```bash
$ npm run test
$ npm run build
```
