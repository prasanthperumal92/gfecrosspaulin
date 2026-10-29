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

# sitemap.xml and robots.txt for search engines; lastmod comes from each page's last commit
SITE_URL="${SITE_URL:-https://gfecrosspaulin.vercel.app/}"
lastmod() { git -C "$ROOT" log -1 --format=%cs -- "$@" 2>/dev/null || date -u +%F; }
{
  echo '<?xml version="1.0" encoding="UTF-8"?>'
  echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
  printf '  <url><loc>%s</loc><lastmod>%s</lastmod></url>\n' "$SITE_URL" "$(lastmod index.html site.css)"
  printf '  <url><loc>%sbrochure/</loc><lastmod>%s</lastmod></url>\n' "$SITE_URL" "$(lastmod brochure/index.html brochure/styles.css)"
  printf '  <url><loc>%soutput/crosspaulin-export-brochure.pdf</loc><lastmod>%s</lastmod></url>\n' "$SITE_URL" "$(lastmod brochure)"
  echo '</urlset>'
} > "$OUT/sitemap.xml"
printf 'User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n' "$SITE_URL" > "$OUT/robots.txt"
if grep -rniE "malson|CM/L|IN122639|₹|/kg" "$OUT" --include='*.html' --include='*.css' --include='*.svg'; then
  echo "Internal or manufacturer-only details found in _site/" >&2; exit 1
fi
echo "Website assembled in $OUT ($(du -sh "$OUT" | cut -f1))"
