#!/usr/bin/env python3
"""Strip Mintlify's own platform branding from a `mintlify export` static build.

Mintlify's "Powered by Mintlify" badge (and a screen-reader-only label saying
the same) aren't removable via any documented config — that's an Enterprise-
plan feature. Since we're self-hosting the static export, this patches the
badge out visually via injected CSS rather than deleting the DOM node: the
badge is rendered by Mintlify's own compiled React bundle, and Next.js
hydration would silently re-insert a deleted node to match its render tree.
Hiding it with CSS survives hydration untouched since hydration never
touches stylesheets.

Usage: rebrand-export.py <exported-site-dir>
"""
import sys
from pathlib import Path

HIDE_CSS = """<style>
a[href*="mintlify.com?utm_campaign=poweredBy"]{display:none!important}
</style>"""

def patch(html_path: Path) -> bool:
    text = html_path.read_text(encoding="utf-8")
    changed = False

    if "</head>" in text and HIDE_CSS not in text:
        text = text.replace("</head>", HIDE_CSS + "</head>", 1)
        changed = True

    old_meta = '<meta name="generator" content="Mintlify"/>'
    new_meta = '<meta name="generator" content="Vocantly Docs"/>'
    if old_meta in text:
        text = text.replace(old_meta, new_meta)
        changed = True

    if changed:
        html_path.write_text(text, encoding="utf-8")
    return changed


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    root = Path(sys.argv[1])
    if not root.is_dir():
        print(f"error: {root} is not a directory")
        sys.exit(1)

    html_files = sorted(root.rglob("*.html"))
    patched = sum(patch(f) for f in html_files)
    print(f"patched {patched}/{len(html_files)} html files in {root}")


if __name__ == "__main__":
    main()
