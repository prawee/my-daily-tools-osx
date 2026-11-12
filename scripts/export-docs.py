#!/usr/bin/env python3
"""Export this repo's markdown content to another docs framework.

usage: python3 scripts/export-docs.py <docsify|mkdocs|gitbook> [--out DIR] [--name NAME]

Source files are never modified. Output goes to <out>/<target> (default: _export/<target>).
"""
import argparse, json, os, re, shutil, sys

ROOT = os.getcwd()
SKIP = {".git", ".vscode", ".idea", ".claude", "node_modules", "scripts", "_export", "site"}
SKIP_FILES = {".DS_Store", ".gitignore"}


def natkey(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]


def title(path):
    in_code = False
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.startswith("```"):
                    in_code = not in_code
                m = None if in_code else re.match(r"#\s+(.+)", line)
                if m:
                    return m.group(1).strip().replace("[", "(").replace("]", ")")
    except OSError:
        pass
    return os.path.splitext(os.path.basename(path))[0]


def build(d):
    """Tree of ('page', title, relpath) / ('dir', name, relpath, children)."""
    items, entries = [], sorted(os.listdir(d), key=natkey)
    for e in entries:
        p = os.path.join(d, e)
        if os.path.isfile(p) and e.endswith(".md") and not e.startswith("_"):
            rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
            if rel != "README.md":
                items.append(("page", title(p), rel))
    for e in entries:
        p = os.path.join(d, e)
        if os.path.isdir(p) and e not in SKIP and not e.startswith("."):
            kids = build(p)
            if kids:
                items.append(("dir", e, os.path.relpath(p, ROOT).replace(os.sep, "/"), kids))
    return items


def copy_content(dest):
    def ignore(d, names):
        rel = os.path.relpath(d, ROOT)
        return [n for n in names
                if n in SKIP_FILES or n.startswith(".") and n != ".nojekyll"
                or (rel == "." and (n in SKIP or n == "index.html" or n.startswith("_")))
                or n == "__pycache__"]
    shutil.copytree(ROOT, dest, ignore=ignore)


def export_docsify(out, name, tree):
    copy_content(out)
    open(os.path.join(out, ".nojekyll"), "w").close()

    def lines(items, depth):
        for it in items:
            pad = "  " * depth
            if it[0] == "page":
                yield f"{pad}- [{it[1]}](/{it[2]})"
            else:
                yield f"{pad}- **{it[1]}**"
                yield from lines(it[3], depth + 1)
    with open(os.path.join(out, "_sidebar.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(["- [Home](/)", *lines(tree, 0)]) + "\n")
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{name}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/docsify@4.13.1/lib/themes/vue.css">
</head>
<body>
  <div id="app">Loading...</div>
  <script>
    window.$docsify = {{ name: {json.dumps(name)}, loadSidebar: true, subMaxLevel: 2, auto2top: true,
      search: {{ placeholder: 'Search', noData: 'No results', depth: 3 }} }};
  </script>
  <script src="https://cdn.jsdelivr.net/npm/docsify@4.13.1/lib/docsify.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/docsify@4.13.1/lib/plugins/search.min.js"></script>
</body>
</html>
""")
    return "serve with: npx docsify-cli serve " + out


def export_mkdocs(out, name, tree):
    docs = os.path.join(out, "docs")
    copy_content(docs)  # mkdocs requires docs_dir to be separate from mkdocs.yml
    if os.path.exists(os.path.join(docs, "README.md")):
        os.rename(os.path.join(docs, "README.md"), os.path.join(docs, "index.md"))
    else:
        with open(os.path.join(docs, "index.md"), "w", encoding="utf-8") as f:
            f.write(f"# {name}\n")

    def nav(items, depth):
        for it in items:
            pad = "  " * depth
            if it[0] == "page":
                yield f"{pad}- {json.dumps(it[1], ensure_ascii=False)}: {json.dumps(it[2][:])}"
            else:
                yield f"{pad}- {json.dumps(it[1], ensure_ascii=False)}:"
                yield from nav(it[3], depth + 1)
    with open(os.path.join(out, "mkdocs.yml"), "w", encoding="utf-8") as f:
        f.write(f"site_name: {json.dumps(name, ensure_ascii=False)}\n"
                "theme:\n  name: material\n  features: [navigation.sections, search.suggest]\n"
                "nav:\n  - Home: index.md\n" + "\n".join(nav(tree, 1)) + "\n")
    return f"serve with: pip install mkdocs-material && cd {out} && mkdocs serve"


def export_gitbook(out, name, tree):
    copy_content(out)
    if not os.path.exists(os.path.join(out, "README.md")):
        with open(os.path.join(out, "README.md"), "w", encoding="utf-8") as f:
            f.write(f"# {name}\n")

    def walk(items, depth):
        for it in items:
            pad = "  " * depth
            if it[0] == "page":
                yield f"{pad}* [{it[1]}]({it[2]})"
            else:  # GitBook section needs a link: use (or create) the folder README
                readme = os.path.join(out, it[2], "README.md")
                if not os.path.exists(readme):
                    with open(readme, "w", encoding="utf-8") as f:
                        f.write(f"# {it[1]}\n")
                yield f"{pad}* [{it[1]}]({it[2]}/README.md)"
                yield from walk(it[3], depth + 1)
    with open(os.path.join(out, "SUMMARY.md"), "w", encoding="utf-8") as f:
        f.write("# Summary\n\n* [Introduction](README.md)\n" + "\n".join(walk(tree, 0)) + "\n")
    return "import the folder into GitBook (Git Sync) or run: npx honkit serve " + out


TARGETS = {"docsify": export_docsify, "mkdocs": export_mkdocs, "gitbook": export_gitbook}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("target", choices=TARGETS)
    ap.add_argument("--out", default="_export")
    ap.add_argument("--name", default="My Daily Tools")
    a = ap.parse_args()
    out = os.path.join(a.out, a.target)
    if os.path.exists(out):
        sys.exit(f"{out} already exists; remove it or pass --out")
    tree = build(ROOT)
    hint = TARGETS[a.target](out, a.name, tree)

    def count(items):
        return sum(1 if i[0] == "page" else count(i[3]) for i in items)
    print(f"exported {count(tree)} pages -> {out}\n{hint}", file=sys.stderr)
