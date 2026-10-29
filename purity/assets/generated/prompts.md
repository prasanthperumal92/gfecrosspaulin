# Generated image log (Purity)

## Gemini (photorealistic scenes): not generated yet
On 2026-10-29, `gemini-3.1-flash-image` returned `429 … free_tier … quota`. Billing is still needed on the key's project.
The brochure uses the owner's photos in the meantime. Every prompt ends with "photorealistic, no text, no logos, no faces".

| Output file | Use | Prompt | `--ref` |
|---|---|---|---|
| `cover-hero.png` (`--aspect 4:3`) | Cover, replaces `pvc-rolled-blue.jpg` | Flatbed truck on an open highway, its cargo covered by a glossy blue PVC-coated tarpaulin (smooth surface, welded hems, brass eyelets), roped down tight, golden-hour light | `images/purity/pvc-rolled-blue.jpg` |
| `construction.png` | Page 3 | Building materials and a small excavator on a construction site under a glossy blue PVC tarpaulin, overcast monsoon sky | same |
| `hay-cover.png` | Page 3 | Round hay bales stacked in a field, covered by a glossy blue PVC tarpaulin tied down with ropes through brass eyelets | same |
| `event-shelter.png` | Page 3 | Open-sided event shelter roofed with blue PVC tarpaulin over tables, light rain | same |
| `pitch-cover.png` (`--aspect 16:9`) | Page 3 | Cricket pitch in a stadium covered by a large flat blue PVC tarpaulin, rain clouds | same |
| `relief-tent.png` (`--aspect 1:1`) | Page 3, replaces `pvc-tent-blue.jpg` | Row of blue PVC ridge tents with windows in a dry open field | `images/purity/pvc-tent-blue.jpg` |

Reject any image with text, logos, a woven or matt look (that is Crosspaulin, not PVC) or extra eyelet rows.

## SVG (drawn by Claude)
- `cross-section.svg`: PVC coat / base fabric / PVC coat, exploded. Illustrative.
- `roll.svg`: 1.5 m × 50 m roll (P1).
- `icon-*.svg` (6 features) and `app-*.svg` (6 applications): one stroke style, graphite `#16191D` (on yellow tiles for features, grey for applications).
- `qr-product-page.svg`: Python `qrcode` (SvgPathImage, border 1) → https://www.graceferroexports.com/products/tarpaulin/pvc
