---
id: KB-15
title: Purity brochure: brand and design
tags: [purity, brand, colours, logo, images]
updated: 2026-10-29
---
# Purity brochure design

## Palette (PLACEHOLDER, not from a logo)
No Purity logo has been supplied. The palette is graphite and safety yellow, chosen on 2026-10-29 to look clearly different from Crosspaulin's royal blue and orange. Blue appears only where it shows the product itself (photos, cross-section and roll diagrams).

| Token | Hex | Use |
|---|---|---|
| `--ink` | `#16191D` | Text, rules, icon strokes (also hard-coded in `assets/generated/icon-*.svg`, `app-*.svg`) |
| `--graphite` | `#23282F` | Cover, grade headers, table headers, contact band |
| `--steel` | `#5B6470` | Secondary text |
| `--yellow` | `#FFC20E` | Accent: section markers, feature icon tiles, cover brand name, page numbers. Never use it for text on white |
| `--paper` | `#F1F2F4` | Panels behind photos and cards |

When the logo arrives: sample it, swap the `:root` tokens in `purity/styles.css` (and the icon stroke colour), and record it here.

## How it differs from Crosspaulin
| | Crosspaulin | Purity |
|---|---|---|
| Colour | Royal blue + orange | Graphite + safety yellow |
| Display type | Montserrat, mixed case | Barlow Condensed, upper case (`purity/assets/fonts/`, SIL OFL, from fontsource 5.0.13) |
| Shapes | Rounded cards, diagonal stripes | Square corners, hairline and 0.6 mm rules, yellow square markers |
| Page furniture | Striped top bar, kicker + heading | Running header with a section name and a yellow page number |
| Cover | Full-bleed photo on top, blue band below | Graphite, huge yellow wordmark, product cut-out on a grey panel, GSM spec strip |

Shared on purpose: Inter body text, the A4 grid, and the Grace Ferro contact details.
Inside upper-case headings, wrap units in `<span class="u">` so that "1.5 m" does not print as "1.5 M". Neither font subset has arrow glyphs, so draw arrows instead of typing them.

## Images
- Owner photos (P4) in `images/purity/`. `purity/assets/*.png` are cut-outs (white background removed by flood fill) so they sit on grey panels. The owner confirmed on 2026-10-29 that they show Purity material and may be used. They are still low resolution (about 640 px).
- Gemini: still blocked on 2026-10-29 (429, free-tier quota). Queued prompts: `purity/assets/generated/prompts.md`.
- SVGs drawn by Claude: cross-section, roll, six feature icons, six application icons, QR code.
