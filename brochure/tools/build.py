#!/usr/bin/env python3
"""Build step for brochure/index.html and the website home page index.html (idempotent).

- Fills the sizes table between <!--SIZES:start--> and <!--SIZES:end-->
  from docs/packinglist.html (two half tables in the brochure, one on the website).
- Inlines each <!--SVG:path--> ... <!--/SVG--> block from the SVG file, so the
  page's web fonts apply to SVG text (fonts don't load inside <img> SVGs).
  The path is relative to the HTML file.
Run from anywhere: python3 brochure/tools/build.py
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
src = (ROOT / "docs/packinglist.html").read_text()
rows = []
for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", src, re.S):
    cells = [re.sub(r"<[^>]+>", "", c).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)]
    if len(cells) == 6:
        rows.append(cells)
assert len(rows) == 54, len(rows)


def metres(size):
    a, b = (int(x) for x in re.findall(r"\d+", size))
    return f"{a * 0.3048:.1f} × {b * 0.3048:.1f} m"


def table(chunk):
    out = ['    <table class="sizes">',
           '      <thead><tr class="sup"><th colspan="3"></th><th colspan="4">Pieces per bundle, by GSM</th></tr>',
           '      <tr><th>#</th><th>Size (ft)</th><th>Size (m)</th><th>90</th><th>120</th><th>150</th><th>200</th></tr></thead>',
           '      <tbody>']
    for no, size, *q in chunk:
        ft = size.replace("'", "′").replace(" x ", " × ")
        out.append(f'        <tr><td class="n">{no}</td><td class="ft">{ft}</td><td class="m">{metres(size)}</td>'
                   + "".join(f"<td>{v}</td>" for v in q) + "</tr>")
    out += ["      </tbody>", "    </table>"]
    return "\n".join(out)


def build(html_path, tables):
    html = html_path.read_text()
    block = "<!--SIZES:start-->\n" + "\n".join(tables) + "\n<!--SIZES:end-->"
    html = re.sub(r"<!--SIZES:start-->.*?<!--SIZES:end-->", lambda _: block, html, flags=re.S)
    html = re.sub(r"<!--SVG:(.*?)-->.*?<!--/SVG-->",
                  lambda m: f"<!--SVG:{m[1]}-->" + (html_path.parent / m[1]).read_text().strip() + "<!--/SVG-->",
                  html, flags=re.S)
    html_path.write_text(html)


build(ROOT / "brochure/index.html", [table(rows[:27]), table(rows[27:])])
build(ROOT / "index.html", [table(rows)])
print("sizes table: 54 rows written; SVGs inlined (brochure and website)")
