# Sources: Purity PVC tarpaulin brochure

Every number and claim in `purity/index.html`, and where it comes from. Internal file: never publish.

## Register

| ID | Source | Notes |
|---|---|---|
| P1 | `docs/purity/price-list-internal.png`: "Purity PVC Tarpaulin — Roll & Sheet" price list, supplied by the owner 2026-10-29 | **Internal.** INR prices including freight and 18% GST. Used only for grades, roll size, sheet sizes and "double-side coated" |
| P2 | `docs/purity/applications-reference.png`: "Applications of PVC Tarpaulin Sheets", supplied by the owner | Appears to come from a third-party website. List of uses only; wording rewritten; its four photos are not used |
| P3 | `docs/purity/features-reference.png`: "PVC Coated Tarpaulin Features", supplied by the owner | Appears to come from a third-party website. Features rewritten; absolute claims softened; "Fire Hydrant" read as "fire retardant" |
| P4 | `images/purity/pvc-rolled-blue.jpg`, `pvc-tent-blue.jpg`, `pvc-eyelet-corner.png`, supplied by the owner | About 640 px wide (eyelet: 354 px). The owner confirmed on 2026-10-29 that they show Purity material and may be used |
| G1 | https://www.graceferroexports.com/products/tarpaulin/pvc (SKU GFE-FRM-PVC), fetched 2026-10-29 | Grace Ferro's own PVC tarpaulin page: temperature rating, ports, payment, Incoterms, samples, certificates, 24-hour quote reply |
| C1 | `kb/company.md` (S3, S4) | Exporter contact details, registrations, 16 export markets |

## Claims by page

| Page | Claim | Source |
|---|---|---|
| 1, 2, 4 | Grades 400, 430, 550, 650, 760 GSM | P1 |
| 1, 2, 4, 5 | Roll 1.5 m × 50 m; sheets 15×12, 18×15, 24×18, 30×18 ft | P1 |
| 2, 4 | PVC-coated on both sides | P1 ("double-side coated") |
| 2 | Base fabric + PVC coating construction | General definition of PVC-coated tarpaulin; the fabric type is unknown and not stated |
| 2 | Exporter text, registrations, 16 countries | C1 |
| 3, 4 | −30 °C to +70 °C, "generally rated" (not a headline fact: it was removed from the page 2 numbers in review 4) | G1 (it is a generic rating for Grace Ferro's PVC line, not a Purity test result) |
| 3 | Waterproof, UV-stabilised, strong, temperature, easy to clean, FR on request | P3, rewritten |
| 3 | Transport, construction, agriculture, events, sports | P2 (transport also in G1) |
| 3 | Tents and shelters; tent caption "Purity PVC tarpaulin" | P4 tent photo (owner-confirmed) |
| 4, 5 | oz/yd², m², sq ft, roll and sheet weights | Calculated in `purity/tools/build.py` from P1 |
| 2, 5 | Purity sheet with hemmed edge and metal eyelets ("Shown:") | P4 eyelet photo (owner-confirmed) |
| 6 | FOB/CIF; Chennai, Mumbai, Nhava Sheva; payment terms; samples; documents; 24-hour reply | G1 |
| 6 | Contact details | C1 |
| 6 | QR code → G1 URL | Generated with Python `qrcode`; decoded with OpenCV on 2026-10-29 |

## Deliberately left out (no source yet)
Brand owner, manufacturer and trademark mark, thickness, base fabric, tensile, tear, adhesion, colours, FR standard, certifications (BIS, ISO), MOQ, lead time, packing, container loading, HS code, grade-by-use recommendations. See `kb/purity-open-questions.md`.
