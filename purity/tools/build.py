#!/usr/bin/env python3
"""Build step for purity/index.html (idempotent).

- Fills the generated blocks <!--GRADES-->, <!--ROLL--> and <!--SHEETS--> from the data below.
  Grades, roll size and sheet sizes come from the internal price list (P1, docs/purity/).
  Weights and oz/yd² are calculated: area (m²) × GSM ÷ 1000; 1 oz/yd² = 33.906 g/m².
- Inlines each <!--SVG:path--> ... <!--/SVG--> block (shared with brochure/tools/build.py).
Run from anywhere: python3 purity/tools/build.py
"""
import pathlib, sys
from decimal import Decimal, ROUND_HALF_UP

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "brochure/tools"))
from build import fill, inline_svgs  # noqa: E402

GSM = [400, 430, 550, 650, 760]
ROLL_W, ROLL_L = 1.5, 50                                     # metres
SHEETS = [(15, 12), (18, 15), (24, 18), (30, 18)]            # feet
FT, SQFT = 0.3048, 0.09290304


def kg(m2, gsm):
    # round half up, so 32.25 kg prints as 32.3 (not 32.2)
    return str(Decimal(str(round(m2 * gsm / 1000, 6))).quantize(Decimal("0.1"), ROUND_HALF_UP))


def grades():
    out = ['  <div class="grades">']
    for g in GSM:
        out.append(f'    <div class="grade"><div class="gsm">{g}<small>GSM</small></div>'
                   f'<div class="bar"><span style="width:{g / GSM[-1] * 100:.0f}%"></span></div>'
                   f'<dl><dt>Weight</dt><dd>{g} g/m²<br>{g / 33.906:.1f} oz/yd²</dd>'
                   f'<dt>Per roll</dt><dd>{kg(ROLL_W * ROLL_L, g)} kg</dd></dl></div>')
    out.append("  </div>")
    return "\n".join(out)


def roll():
    area = ROLL_W * ROLL_L
    out = ['    <table class="sizes roll">',
           '      <thead><tr><th>Grade</th>' + "".join(f"<th>{g}</th>" for g in GSM) + "</tr></thead>",
           '      <tbody>',
           '        <tr><td class="ft">Roll weight</td>' + "".join(f"<td>{kg(area, g)} kg</td>" for g in GSM) + "</tr>",
           '      </tbody>', '    </table>']
    return "\n".join(out)


def sheets():
    out = ['    <table class="sizes">',
           '      <thead><tr class="sup"><th colspan="3"></th><th colspan="5">Nominal weight per sheet in kg, by GSM</th></tr>',
           '      <tr><th>Size (ft)</th><th>Size (m)</th><th>Area</th>' + "".join(f"<th>{g}</th>" for g in GSM) + "</tr></thead>",
           '      <tbody>']
    for a, b in SHEETS:
        m2 = a * b * SQFT
        out.append(f'        <tr><td class="ft">{a}′ × {b}′</td><td class="m">{a * FT:.2f} × {b * FT:.2f} m</td>'
                   f'<td class="m">{m2:.1f} m² ({a * b} sq ft)</td>'
                   + "".join(f"<td>{kg(m2, g)}</td>" for g in GSM) + "</tr>")
    out += ["      </tbody>", "    </table>"]
    return "\n".join(out)


if __name__ == "__main__":
    path = ROOT / "purity/index.html"
    html = path.read_text()
    for name, content in (("GRADES", grades()), ("ROLL", roll()), ("SHEETS", sheets())):
        html = fill(html, name, content)
    path.write_text(inline_svgs(html, path.parent))
    print(f"purity: {len(GSM)} grades, {len(SHEETS)} sheet sizes written; SVGs inlined")
