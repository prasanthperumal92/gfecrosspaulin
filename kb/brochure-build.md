---
id: KB-11
title: Brochure build and tooling
tags: [brochure, build, pdf, gemini, tools, review, taste]
updated: 2026-10-19
---
# Brochure build and tooling

**Output:** `output/crosspaulin-export-brochure.pdf` (A4, 8 pages).
**Source:** `brochure/index.html` + `brochure/styles.css`.

| Page | Content |
|---|---|
| 1 | Cover |
| 2 | Exporter, manufacturer, cross-lamination diagram |
| 3 | 5× claim, 8 advantages, benefits |
| 4 | 4 grade cards, more weights, colours |
| 5 | Specification table, IS 14611 reference |
| 6 | 54 sizes (ft/m) |
| 7 | Applications |
| 8 | Export terms, enquiry checklist, contact and QR |

## Commands
```bash
brochure/tools/render.sh          # runs build.py, prints PDF, writes page PNGs to brochure/review/pages/
python3 brochure/tools/build.py   # sizes table from docs/packinglist.html + inlines SVGs
python3 brochure/tools/gen_image.py "<prompt>" out.png --ref images/<photo> [--aspect 4:3] [--model gemini-3-pro-image]
```
- The PDF is rendered with Playwright's cached Chromium (`~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome`). Override it with `CHROME=`.
- SVGs with text must be inlined (`<!--SVG:path--><!--/SVG-->` markers) so the web fonts apply.
- Edit sizes in `docs/packinglist.html`, not in the generated table.

## Gemini image generation
Key: `GEMINI_KEY` in `.env.local` (never print it). Available models are gemini-3-pro-image, gemini-3.1-flash-image, gemini-3.1-flash-lite-image and gemini-2.5-flash-image.
Status on 2026-10-19: every model returns 429 "free_tier limit: 0", so billing must be enabled. The queued prompts are in `brochure/assets/generated/prompts.md`.

## Design review
The taste skill (github.com/hmbown/taste, commit c9ec83b) is installed at project scope in `.claude/skills/taste/`. It contains instructions only.
Reports are in `brochure/review/review-1.md` and `review-2.md`, with page snapshots in `review/round1/` and `review/round2/`.
