#!/usr/bin/env bash
# Render a brochure folder to a PDF in output/ and page PNGs in <folder>/review/pages/.
# Usage: render.sh [folder] [pdf name]
#   render.sh                                          -> brochure/, crosspaulin-export-brochure.pdf
#   render.sh purity purity-pvc-tarpaulin-brochure.pdf
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
DIR="${1:-brochure}"
PDF="$ROOT/output/${2:-crosspaulin-export-brochure.pdf}"
python3 "$ROOT/$DIR/tools/build.py"
CHROME="${CHROME:-$(ls -d "$HOME"/.cache/ms-playwright/chromium-*/chrome-linux64/chrome 2>/dev/null | tail -1)}"
mkdir -p "$ROOT/output" "$ROOT/$DIR/review/pages"
"$CHROME" --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=5000 --print-to-pdf="$PDF" \
  "file://$ROOT/$DIR/index.html" 2>/dev/null
pdfinfo "$PDF" | grep -E 'Pages|Page size|File size'
rm -f "$ROOT/$DIR"/review/pages/page-*.png
pdftoppm -r 60 -png "$PDF" "$ROOT/$DIR/review/pages/page"
