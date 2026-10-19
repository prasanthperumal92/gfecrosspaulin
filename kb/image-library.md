---
id: KB-10
title: Image library
tags: [images, photos, assets, gsm, applications]
updated: 2026-10-19
---
# Image library

## Originals (`images/`, owner-supplied, S10; never modify)
| File | Size | Shows |
|---|---|---|
| `natural_90gsm.jpeg` | 899×1599 | 90 GSM natural/transparent close-up, "GSM 90" print |
| `green_120gsm.jpeg` | 899×1599 | 120 GSM green, ISI-style mark, blue edge |
| `150gsm_blue_crosspaulin.jpeg` | 899×1599 | 150 GSM blue close-up |
| `blacksilver_200gsm.jpeg` | 899×1599 | 200 GSM black/silver close-up |
| `crosspaulin_cross_braid.jpeg` | 899×1599 | Macro of the cross-laminated texture (green, blue hem) |
| `cross-laminated-multilayer-tarpaulin-1000x1000.webp` | 1000×730 | Yellow and blue packs on grass, logo top-right |
| `cross-laminated-sheets-main.webp` | 600×600 | Same scene, square |
| `tarpaulin.webp` | 600×600 | Folded yellow 90 GSM pack on white |
| `cross-laminated-multilayer-tarpaulin-1000x1000_blue.webp` | 1000×996 | Blue 90 GSM sheet with eyelets |
| `cross-laminated-multilayer-tarpaulin-500x500.jpg` | 500×499 | Yellow 150 GSM sheet with eyelets |
| `usages.png` | 250×782 | 3 tiles: fumigation covering, truck cover, tent shade (low resolution) |
| `649546268_…_n.jpg` | 512×640 | Social ad: yellow canopy over a pool |
| `docs/crosspaulin-cross-laminated-sheets-brochure.pdf` | 1 page, Letter | Old brochure (image-only); its 4 application photos were cropped at 300 dpi |

## Derived assets (`brochure/assets/`)
Grades `grade-90/120/150/200.jpg`; `texture-macro.jpg`; `cover-hero.jpg` (packs crop without the logo); `sheet-blue-90.jpg`; `sheet-yellow-150.jpg`; `pack-yellow-90.jpg`; applications `app-grain`, `app-truck2`, `app-hay`, `app-pond` (from the old PDF), `app-canopy` (from the ad), and `app-fumigation`, `app-truck`, `app-tent` (from `usages.png`).

## Resolution warning
For print at 300 dpi, the only photos big enough are the 899×1599 close-ups. The cover (860 px) and application tiles (190–540 px) are below print quality, so request originals or generate replacements ([brochure-build.md](brochure-build.md)).

## Generated
SVGs in `brochure/assets/generated/` (diagram, icons, export flow, QR codes). The Gemini prompt queue is in `brochure/assets/generated/prompts.md`.
