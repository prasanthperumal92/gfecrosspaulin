---
id: KB-18
title: Micropaulin: product and test data
tags: [micropaulin, product, specifications, test report, certificate of analysis, sizes, price]
updated: 2026-10-31
---
# Micropaulin™ multilayer laminated tarpaulin

"Micropaulin™, multilayer laminated tarpaulin, a product of PANKAJ®" (M2). Same manufacturer and brand house as Crosspaulin™ ([manufacturer.md](manufacturer.md)); the same disclosure rule applies: never name the manufacturer in buyer material. Grace Ferro is the distributor and exporter. Sources: [`micropaulin/sources.md`](../micropaulin/sources.md).

## Certificate of Analysis, 200 GSM black/silver (M1, dated 2026-10-31)
| Test | Unit | Result |
|---|---|---|
| GSM | 200 ± 10% | 196 |
| Visual | – | Satisfactory |
| Colour | – | Black silver |
| Type | – | HN (not printed; see below) |
| Density | g/cc | 0.928 |
| Dart impact | gmf | 380 |
| Tensile strength MD / TD | kg/cm² | 223 / 204 |
| Elongation MD / TD | % | 723 / 708 |
| Tear strength MD / TD | gmf | 2,200 / 2,700 |
| Water-proofness | – | Pass |
| Flex, before / after ageing | 50,000 cycles | Pass / pass |

Test methods and the ageing conditions are not stated.

## How it differs from Crosspaulin
| | Crosspaulin (KB-04) | Micropaulin 200 GSM (M1) |
|---|---|---|
| Construction | Cross-laminated, oriented layers | Multilayer laminated film |
| Tensile MD / TD | 250 / 200 kg/cm² (declared) | 223 / 204 kg/cm² (tested) |
| Elongation MD / TD | 400 / 300% (declared) | 723 / 708% (tested) |
| Standard | BIS-licensed, IS 14611:2024 | None claimed. MD tensile is below the IS 14611 minimum of 250, so "Type HN" is not used |

The selling point is stretch, tear and flex rather than raw tensile strength.

## Range (M6, price list, 2026-10-31)
- Grades: 90, 120, 150, 200 GSM. Every size is listed in every grade.
- 25 sheet sizes (ft, width × height): 6×6, 9×6, 9×9, 12×9, 12×12, 15×9, 15×12, 15×15, 18×12, 18×15, 21×15, 21×18, 24×12, 24×15, 24×18, 24×21, 27×24, 30×12, 30×18, 30×24, 30×30, 36×30, 40×30, 40×40, 50×50. Data lives in `micropaulin/tools/build.py`.
- Colours: 90 GSM yellow (M5), 200 GSM black/silver (M1, M3); 120 and 150 not shown. Yellow rolls appear in M3; roll dimensions unknown.

**M6 is internal.** It is a domestic INR price-per-piece list including freight (piece price = sq ft × rate per sq ft for the grade). Never publish prices, rates or ₹; read the figures from `docs/micropaulin/price-list-internal.png` when needed.

## Not known [TBC]
Whether sizes are cut or finished, roll width and length, colours for 120 and 150 GSM, thickness, number of layers, UV test data, test methods, MOQ, lead time, packing, HS code. See [micropaulin-open-questions.md](micropaulin-open-questions.md).
