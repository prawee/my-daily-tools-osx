#!/usr/bin/env python3
"""Generate docsify _sidebar.md from the folder structure. Run from repo root."""
import os, re, sys

ROOT = os.getcwd()
SKIP = {".git", ".vscode", ".idea", "node_modules", "scripts"}

def natkey(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]

def title(path):
    try:
        with open(path, encoding="utf-8") as f:
            in_code = False
            for line in f:
                if line.startswith("```"):
                    in_code = not in_code
                if not in_code:
                    m = re.match(r"#\s+(.+)", line)
                    if m:
                        return m.group(1).strip().replace("[", "(").replace("]", ")")
    except OSError:
        pass
    return os.path.splitext(os.path.basename(path))[0]

def walk(d, depth, out):
    entries = sorted(os.listdir(d), key=natkey)
    for e in entries:
        p = os.path.join(d, e)
        if os.path.isfile(p) and e.endswith(".md") and not e.startswith("_"):
            if depth == 0 and e == "README.md":
                continue
            rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
            out.append(f"{'  ' * depth}- [{title(p)}](/{rel})")
    for e in entries:
        p = os.path.join(d, e)
        if os.path.isdir(p) and e not in SKIP and not e.startswith("."):
            sub = []
            walk(p, depth + 1, sub)
            if sub:
                out.append(f"{'  ' * depth}- **{e}**")
                out.extend(sub)

lines = ["- [Home](/)"]
walk(ROOT, 0, lines)
with open(os.path.join(ROOT, "_sidebar.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print(f"wrote _sidebar.md ({len(lines)} lines)", file=sys.stderr)
