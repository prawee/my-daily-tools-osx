# Word Count

## Syntax of wc command
```bash
$ wc [opitons] filenames
```

## Opitons
```bash
$ wc -l # prints the number of lines in a file.
$ wc -w # prints the number of words in a file.
$ wc -c # displays the count of bytes in a file.
$ wc -m # prints the count of characters from a file.
```

## Testing
### wc.text
```bash
test demo
```
### Usage
Basic of wc command
```bash
$ wc wc.text
# 1 2 10 wc.text
```
Count number of lines
```bash
$ wc -l wc.text
# 1 wc.text
```
Display number of words
```bash
$ wc -w wc.text
# 2 wc.text
```

Count number of bytes and characters
```bash
$ wc -c wc.text
# 10 wc.text
```

display length of longest line
```bash
$ wc -m wc.text
# 10 wc.text
```