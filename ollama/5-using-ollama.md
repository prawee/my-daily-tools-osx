# How to using another CLI of Ollama

## CLI
```bash
ollama
# Usage:
#   ollama [flags]
#   ollama [command]

# Available Commands:
#   serve       Start ollama
#   create      Create a model from a Modelfile
#   show        Show information for a model
#   run         Run a model
#   stop        Stop a running model
#   pull        Pull a model from a registry
#   push        Push a model to a registry
#   list        List models
#   ps          List running models
#   cp          Copy a model
#   rm          Remove a model
#   help        Help about any command

# Flags:
#   -h, --help      help for ollama
#   -v, --version   Show version information

# Use "ollama [command] --help" for more information about a command.
```

## Start ollama
```bash
ollama serve
# Error: listen tcp 127.0.0.1:11434: bind: address already in use
```

## List running models
```bash
ollama ps             
# NAME    ID    SIZE    PROCESSOR    UNTIL
```

## List models
```bash
ollama list
# NAME                  ID              SIZE      MODIFIED      
# deepseek-r1:latest    0a8c26691023    4.7 GB    3 minutes ago
```

## Show information
```bash
ollama show deepseek-r1

# Model
#     architecture        qwen2     
#     parameters          7.6B      
#     context length      131072    
#     embedding length    3584      
#     quantization        Q4_K_M    

#   Parameters
#     stop    "<｜begin▁of▁sentence｜>"    
#     stop    "<｜end▁of▁sentence｜>"      
#     stop    "<｜User｜>"                 
#     stop    "<｜Assistant｜>"            

#   License
#     MIT License                    
#     Copyright (c) 2023 DeepSeek
```

## Start models
```bash
ollama run deepseek-r1
>>> Send a message (/? for help)
```
