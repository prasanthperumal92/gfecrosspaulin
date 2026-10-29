# Crosspaulin Website and Export Brochure

A product website and an 8-page A4 export brochure for **Crosspaulin™**, a cross-laminated multilayer tarpaulin (a product of PANKAJ®). The publisher is **Grace Ferro Exports Pvt Ltd**, the product's distributor and exporter.
Both are static HTML/CSS. The brochure is printed to PDF with headless Chrome.

**Website:** `index.html` (home page) and `brochure/` (the brochure page, with a PDF download). Open `index.html` in a browser to preview.
**PDF:** `output/crosspaulin-export-brochure.pdf`

## Layout

| Path | What it is |
|---|---|
| `index.html`, `site.css` | Website home page. Shares fonts, images and SVGs with the brochure via `brochure/assets/` |
| `brochure/index.html`, `brochure/styles.css` | Brochure source and the website's brochure page, one `<section class="page">` per A4 page. The site bar at the top is screen-only |
| `brochure/assets/` | Images, logos, fonts and generated SVGs used by the brochure |
| `brochure/tools/` | `build.py` (sizes table + SVG inlining, for both pages), `render.sh` (PDF + page PNGs), `package-site.sh` (assembles the public website in `_site/`), `gen_image.py` (Gemini images) |
| `brochure/sources.md` | Where every number and claim in the brochure comes from |
| `brochure/review/` | Design review reports and page snapshots |
| `kb/` | Knowledge base: specs, standards, terms, brand, open questions. Start at `kb/INDEX.md` |
| `docs/` | Source documents: manufacturer information sheet, ISO certificate, old brochure, packing list |
| `images/` | Original owner-supplied photos |
| `output/` | The rendered PDF |

## Generating the PDF (instructions for an agent)

### 1. Prerequisites
- `python3`
- `pdfinfo` and `pdftoppm` (poppler-utils: `sudo apt install poppler-utils`)
- Chromium. `render.sh` uses Playwright's cached build at `~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome`. If that is missing, run `npx playwright install chromium`, or set `CHROME=/path/to/chrome`.

### 2. Make the content changes
- Edit text and layout in `brochure/index.html` and `brochure/styles.css`.
- Edit cut sizes and pack quantities in `docs/packinglist.html`. Do not edit the table between `<!--SIZES:start-->` and `<!--SIZES:end-->`; it is regenerated.
- Do not edit inlined SVG between `<!--SVG:path-->` and `<!--/SVG-->`. Edit the SVG file under `brochure/assets/` instead.
- When a fact changes, update the matching `kb/` page and `brochure/sources.md` too. Then run `python3 kb/build_index.py`.

### 3. Render
```bash
brochure/tools/render.sh
```
This runs `build.py` and prints the PDF to `output/crosspaulin-export-brochure.pdf`. It also writes 60 dpi page PNGs to `brochure/review/pages/`.

### 4. Verify (do not skip)
1. The `pdfinfo` output printed by `render.sh` shows **8 pages**, **A4 (≈595 × 842 pt)**, and a file size under **10 MB**.
2. Render each page large enough to read, then look at every page:
   ```bash
   pdftoppm -r 80 -png output/crosspaulin-export-brochure.pdf /tmp/page
   ```
   Check that no text is clipped or hidden under the contact band on page 8, and that no table runs into a page footer. Also check that no page spills onto an extra page.
3. Check that the brochure contains no `[TBC]` marker unless one is intended: `grep -n TBC brochure/index.html`.
4. Check for leaks. This must return nothing: `grep -niE "malson|CM/L|IN122639|₹|/kg" brochure/index.html index.html`.

### 5. Report
Report the PDF path, the page count and file size, and what changed. Do not publish, upload or send the PDF anywhere unless the owner asks.

## Content rules
- **Never invent** specs, certifications, MOQ, prices or lead times. Every value must be traceable in `brochure/sources.md`. Mark unknown values `[TBC]`.
- **Manufacturer disclosure:** in the brochure, say "Crosspaulin™ by PANKAJ®", "BIS-licensed under IS 14611:2024" and "ISO 9001:2015 certified plant". Do not name the manufacturer's legal entity or print the licence or certificate numbers (see `kb/manufacturer.md`).
- **Internal terms** in `kb/export-terms.md` (manufacturer prices, the 30-day factory lead time, payment terms) never appear in buyer-facing material.
- Keep ™ on Crosspaulin and ® on PANKAJ. Never redraw or recolour logos. Grace Ferro is the exporter, not the manufacturer.
- Use international English, with metric units first and imperial in brackets.
- `images/` and `docs/` are originals: never modify them. Copy what you need into `brochure/assets/`.
- Open questions for the owner are in `kb/open-questions.md`.

## Publishing the website

The website copy matches the brochure. When you change a fact, change it in both `index.html` and `brochure/index.html`. The sizes table and inlined SVGs are filled in both by `build.py`.

```bash
brochure/tools/render.sh          # rebuild the PDF first, so the download is current
brochure/tools/package-site.sh    # writes _site/ and fails if internal details leak
```

Deploy **only `_site/`** to a static host. Never serve the repository root: `kb/`, `docs/` and `brochure/sources.md` contain manufacturer details and internal prices.
