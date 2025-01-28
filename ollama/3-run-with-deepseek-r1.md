# How to using `DeepSeek R1`

## CLI
```bash
ollama run deepseek-r1
```

### Error
```bash
pulling manifest 
Error: Post "http://127.0.0.1:11434/api/show": read tcp 127.0.0.1:58986->127.0.0.1:11434: read: connection reset by peer
```

### Success
```bash
pulling manifest 
pulling 96c415656d37... 100% ▕████████████████████████████████████████▏ 4.7 GB                         
pulling 369ca498f347... 100% ▕████████████████████████████████████████▏  387 B                         
pulling 6e4c38e1172f... 100% ▕████████████████████████████████████████▏ 1.1 KB                         
pulling f4d24e9138dd... 100% ▕████████████████████████████████████████▏  148 B                         
pulling 40fb844194b2... 100% ▕████████████████████████████████████████▏  487 B                         
verifying sha256 digest 
writing manifest 
success
>>> Send a message (/? for help)
```