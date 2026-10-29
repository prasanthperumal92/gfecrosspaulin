#!/usr/bin/env bash
# Assemble the public website in _site/: home page, brochure page and PDF only.
# kb/, docs/, review files and sources.md hold internal details and must never be published.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="$ROOT/_site"
python3 "$ROOT/brochure/tools/build.py"
rm -rf "$OUT"
mkdir -p "$OUT/brochure" "$OUT/output"
cp "$ROOT/index.html" "$ROOT/site.css" "$OUT/"
cp "$ROOT/brochure/index.html" "$ROOT/brochure/styles.css" "$OUT/brochure/"
cp -r "$ROOT/brochure/assets" "$OUT/brochure/"
rm -f "$OUT/brochure/assets/generated/prompts.md"
cp "$ROOT/output/crosspaulin-export-brochure.pdf" "$OUT/output/"
if grep -rniE "malson|CM/L|IN122639|₹|/kg" "$OUT" --include='*.html' --include='*.css' --include='*.svg'; then
  echo "Internal or manufacturer-only details found in _site/" >&2; exit 1
fi
echo "Website assembled in $OUT ($(du -sh "$OUT" | cut -f1))"
