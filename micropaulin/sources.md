# Sources: Micropaulin brochure

Every number and claim in `micropaulin/index.html`, and where it comes from. Internal file: never publish.

## Register

| ID | Source | Notes |
|---|---|---|
| M1 | `docs/micropaulin/coa-200gsm-black-silver.pdf`: "Certificate of Analysis, 200 GSM Micropaulin (Black Silver)", manufacturer's letterhead, signed by the QA/QC in-charge, dated 31-10-26. Supplied by the owner 2026-10-31 | Scanned, image-only. **Names the manufacturer, its CIN and addresses: never publish the file itself**; send it to buyers only if the owner agrees |
| M2 | `images/micropaulin/logo-banner.jpg` (600 × 180): Micropaulin banner. Logo, "Multilayer laminated tarpaulin", "A product of PANKAJ®", ISO 9001:2015 seal, icons: UV protected, durable, light weight, eco friendly, flexible, multi-layered | Manufacturer marketing (looks like an online-store A+ banner). Source of the logo crop and the stripe motif |
| M3 | `images/micropaulin/listing-*.jpg`, `ad-truck-cover-blue.jpg`: online listing images | Manufacturer marketing. They carry the manufacturer's website and phone number baked in: only crops without them are used |
| M4 | `images/micropaulin/catalogue-cover-spread.jpg`: catalogue cover with an applications wheel | Names the manufacturer; not used as an image. Applications read from it: truck cover, tent for relief, canal liner, terrace gardening (shade net, mulch film, floriculture belong to other product lines) |
| M5 | `images/micropaulin/yellow-90gsm-sheet.jpg`, `yellow-90gsm-stack.jpg`: yellow 90 GSM sheets with eyelets and the printed grade label, white background | Product photos; the sheet is the cover cut-out |
| M6 | `docs/micropaulin/price-list-internal.png`: "Micropaulin — Price Per Piece", supplied by the owner 2026-10-31 | **Internal.** Domestic INR prices per piece including freight. Used only for the grades (90, 120, 150, 200 GSM) and the 25 sheet sizes. No price, rate or ₹ may appear in `micropaulin/` |
| M7 | `images/micropaulin/badge-eco-friendly.jpg`: badge from the online listing, supplied as a URL by the owner 2026-10-31 (220 px) | Used on the cover at the owner's request. An ISI badge was also supplied; the owner dropped it on 2026-10-31 (no BIS licence on file for Micropaulin) |
| C1 | `kb/company.md` (S3, S4) | Exporter contact details, registrations, 16 export markets |
| S5 / G1 | Grace Ferro's own cross-laminated and PVC product pages (see `kb/sources.md`, `purity/sources.md`) | Only the terms common to both are reused: FOB/CIF, the three ports, the payment options |

## Claims by page

| Page | Claim | Source |
|---|---|---|
| 1, 2 | Micropaulin™, "A product of PANKAJ®", multilayer laminated tarpaulin | M2 (logo used as a crop, not redrawn) |
| 1, 3 | Elongation 723% MD / 708% TD ("700%+ both directions") | M1 |
| 1, 3 | Flex 50,000 cycles, pass before and after ageing | M1 |
| 1, 3 | Tear 2,200 gf MD / 2,700 gf TD ("gmf" on the certificate) | M1 |
| 3 | GSM 196 (spec 200 ± 10%), density 0.928 g/cm³, dart impact 380 g, tensile 223 / 204 kg/cm², water-proofness pass, visual satisfactory | M1. MPa = kg/cm² × 0.0980665 (21.9, 20.0) |
| 1 | "Eco friendly product" badge | M7, M2 icon. Owner request 2026-10-31; manufacturer marketing claim, no test or definition behind it |
| 3 | UV-protected, "stated by the manufacturer" | M2 icon, M4 badge. No weathering test supplied |
| 2 | Polyethylene film layers, no woven base | M2 ("multilayer laminated"); density 0.928 g/cm³ (LDPE range) and 700%+ elongation in M1 are typical of film, not woven tape |
| 2 | Silver face and black face on the 200 GSM grade | M1 ("Black Silver"), M3 photo |
| 2 | Made in India by an ISO 9001:2015 certified manufacturer | M1 letterhead, M2 seal |
| 2 | Same PANKAJ® range as Crosspaulin™ | M2 + `kb/manufacturer.md` (S12). Owner to confirm the cross-mention (open question 7) |
| 1, 2, 4, 5 | Grades 90, 120, 150, 200 GSM; 25 sheet sizes 6′ × 6′ to 50′ × 50′; every size in every grade | M6 |
| 4 | Metres, m², oz/yd² and nominal sheet weights | Calculated in `micropaulin/tools/build.py` from M6 |
| 4 | Colour per grade: 90 yellow, 200 black/silver; others "on request" | M5, M1 |
| 2 | Eyelets along the edges; rolls also available | M3 black sheet and M5 (eyelets); M3 yellow rolls photo |
| 5 | Truck covers, relief tents, canal lining | M4 |
| 5 | Site and scaffold covers; covers for goods kept outdoors; stack covers | M3 listing photos (construction, outdoor furniture, rolls with sacks). Captioned "Some images are illustrative" |
| 5 | FOB/CIF; Chennai, Mumbai, Nhava Sheva; LC (usance/UPAS), advance + balance against scanned B/L, D/P | S5 and G1 (both list them) |
| 5 | Contact details | C1 |
| 5 | QR code to https://www.graceferroexports.com/contact | Python `qrcode`; decoded from the rendered PDF with OpenCV on 2026-10-31 |

## Deliberately left out
- "Type HN" from M1: it is the IS 14611 heavy-duty designation, but the tensile result (223 kg/cm² MD) is below the IS 14611 minimum of 250 (`kb/standards.md`). Do not claim IS 14611 or BIS for Micropaulin.
- "100% quality", "100% original", "tear proof", "temperature resistant", "certified quality": marketing claims with no test or definition behind them.
- Manufacturer name, CIN, addresses, website and phone (M1, M3, M4).
- Prices from M6. Roll dimensions, colours for 120 and 150 GSM, MOQ, lead time, packing, HS code. See `kb/micropaulin-open-questions.md`.
