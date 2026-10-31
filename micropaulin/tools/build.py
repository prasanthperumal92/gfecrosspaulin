#!/usr/bin/env python3
"""Build step for micropaulin/index.html (idempotent).

- Fills the generated blocks <!--GRADES--> and <!--SIZES--> from the data below.
  Grades and sheet sizes come from the internal price list (M6, docs/micropaulin/); no price is used.
  Weights and oz/yd² are calculated: area (m²) × GSM ÷ 1000; 1 oz/yd² = 33.906 g/m².
- Inlines each <!--SVG:path--> ... <!--/SVG--> block (shared with brochure/tools/build.py).
Run from anywhere: python3 micropaulin/tools/build.py
"""
import pathlib, sys
from decimal import Decimal, ROUND_HALF_UP

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "brochure/tools"))
from build import fill, inline_svgs  # noqa: E402

GSM = [90, 120, 150, 200]
# width × height in feet, in the price list's order
SHEETS = [(6, 6), (9, 6), (9, 9), (12, 9), (12, 12), (15, 9), (15, 12), (15, 15), (18, 12), (18, 15),
          (21, 15), (21, 18), (24, 12), (24, 15), (24, 18), (24, 21), (27, 24), (30, 12), (30, 18),
          (30, 24), (30, 30), (36, 30), (40, 30), (40, 40), (50, 50)]
# colour pictured per grade (M1, M3, M5); None = not confirmed
PICTURED = {90: "Yellow pictured", 200: "Black/silver, lab-tested"}
FT, SQFT = 0.3048, 0.09290304


def kg(m2, gsm):
    # round half up, so 1.25 kg prints as 1.3 (not 1.2)
    return str(Decimal(str(round(m2 * gsm / 1000, 6))).quantize(Decimal("0.1"), ROUND_HALF_UP))


def grades():
    out = ['  <div class="grades">']
    for g in GSM:
        out.append(f'    <div class="grade"><div class="gsm">{g}<small>GSM</small></div>'
                   f'<div class="bar"><span style="width:{g / GSM[-1] * 100:.0f}%"></span></div>'
                   f'<dl><dt>Weight</dt><dd>{g} g/m² · {g / 33.906:.1f} oz/yd²</dd>'
                   f'<dt>Colour</dt><dd>{PICTURED.get(g, "On request")}</dd></dl></div>')
    out.append("  </div>")
    return "\n".join(out)


def sizes():
    out = ['    <table class="sizes">',
           '      <thead><tr class="sup"><th colspan="3"></th><th colspan="4">Nominal weight per sheet in kg, by GSM</th></tr>',
           '      <tr><th>Size (ft)</th><th>Size (m)</th><th>Area</th>' + "".join(f"<th>{g}</th>" for g in GSM) + "</tr></thead>",
           '      <tbody>']
    for a, b in SHEETS:
        m2 = a * b * SQFT
        out.append(f'        <tr><td class="ft">{a}′ × {b}′</td><td class="m">{a * FT:.1f} × {b * FT:.1f} m</td>'
                   f'<td class="m">{m2:.1f} m² <i>({a * b} sq ft)</i></td>'
                   + "".join(f"<td>{kg(m2, g)}</td>" for g in GSM) + "</tr>")
    out += ["      </tbody>", "    </table>"]
    return "\n".join(out)


if __name__ == "__main__":
    path = ROOT / "micropaulin/index.html"
    html = path.read_text()
    for name, content in (("GRADES", grades()), ("SIZES", sizes())):
        html = fill(html, name, content)
    path.write_text(inline_svgs(html, path.parent))
    print(f"micropaulin: {len(GSM)} grades, {len(SHEETS)} sheet sizes written; SVGs inlined")
