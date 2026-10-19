#!/usr/bin/env bash
# Render brochure/index.html to output/crosspaulin-export-brochure.pdf and page PNGs.
set -euo pipefail
python3 "$(dirname "$0")/build.py"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
CHROME="${CHROME:-$(ls -d "$HOME"/.cache/ms-playwright/chromium-*/chrome-linux64/chrome 2>/dev/null | tail -1)}"
mkdir -p "$ROOT/output" "$ROOT/brochure/review/pages"
"$CHROME" --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=5000 --print-to-pdf="$ROOT/output/crosspaulin-export-brochure.pdf" \
  "file://$ROOT/brochure/index.html" 2>/dev/null
pdfinfo "$ROOT/output/crosspaulin-export-brochure.pdf" | grep -E 'Pages|Page size|File size'
rm -f "$ROOT"/brochure/review/pages/page-*.png
pdftoppm -r 60 -png "$ROOT/output/crosspaulin-export-brochure.pdf" "$ROOT/brochure/review/pages/page"
