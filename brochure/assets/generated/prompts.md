# Generated image log

## Gemini (photorealistic scenes): not generated yet

As of 2026-10-19, every Gemini image model on `GEMINI_KEY` returns
`429 RESOURCE_EXHAUSTED … free_tier … limit: 0`. The key's Google project has no billing.
The brochure uses real photos for every scene in the meantime.

Once billing is enabled, generate these and swap them into `index.html`:

| Output file | Replaces | Prompt | `--ref` |
|---|---|---|---|
| `cover-hero-ai.png` (`--aspect 4:3`) | `assets/cover-hero.jpg` | Photorealistic commercial photo of neatly folded cross-laminated tarpaulin packs in blue, yellow and green, stacked on a pallet in a bright modern warehouse, soft daylight. No text, no logos, no people. | `images/cross-laminated-multilayer-tarpaulin-1000x1000.webp` |
| `port-cargo.png` | — (new, page 7) | Photorealistic photo: large blue tarpaulin (match the reference colour, eyelets and printed triangle) tightly covering stacked grain sacks at a sunny port yard, shipping containers behind. No text, no logos, no faces. | `images/cross-laminated-multilayer-tarpaulin-1000x1000_blue.webp` |
| `truck-cover.png` | `assets/app-truck2.jpg` | Photorealistic photo: flatbed truck on a highway with cargo covered by the blue reference tarpaulin, roped down. No text, no logos, no faces. | same blue ref |
| `relief-tent.png` (`--aspect 1:1`) | `assets/app-tent.jpg` (low res) | Photorealistic photo: row of simple ridge tents made from the blue reference tarpaulin in a dry open field, overcast light. No text, no logos, no faces. | same blue ref |
| `construction.png` | — (new) | Photorealistic photo: building materials on a construction site covered with the yellow reference tarpaulin. No text, no logos, no faces. | `images/cross-laminated-multilayer-tarpaulin-500x500.jpg` |
| `container-loading.png` | — (new, page 8) | Photorealistic photo: bundled, shrink-wrapped tarpaulin bales being loaded into a 40 ft shipping container by forklift. No text, no logos, no faces. | `images/cross-laminated-sheets-main.webp` |

## SVG (drawn by Claude)

- `cross-section.svg`: exploded view of the layers. Illustrative; the layer count is not specified.
- `icon-*.svg`: 8 advantage icons in one stroke style, using the brand blue and orange.
- `export-flow.svg`: order → production (35–40 days) → packing → FOB/CIF shipment.
- `qr-product-page.svg`, `qr-website.svg`: made with the Python `qrcode` package.
