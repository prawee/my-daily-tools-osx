# How to usage

```bash
telnet localhost 11211
```

## Statistics

```bash
stats
```

## Slabs

```bash
stats slabs
```

## Items

```bash
stats items
```

## Clear

```bash
flush_all
```

## Clear via without telnet

```bash
echo 'flush_all' | nc localhost 11211
```
