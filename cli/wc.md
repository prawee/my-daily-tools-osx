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
```bash
$ wc -l wc.text
# 1 wc.text
$ wc -w wc.text
# 2 wc.text
$ wc -c wc.text
# 10 wc.text
$ wc -m wc.text
# 10 wc.text
```