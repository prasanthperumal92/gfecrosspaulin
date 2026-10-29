# Design review 3: brand separation and blockers (2026-10-29)

**Job:** the Purity brochure must not read as a Crosspaulin variant, and it must print without errors.

## Round 1: side-by-side with Crosspaulin
**Verdict: rework.** The two brochures read as one brand: blue bands, an amber accent within a few degrees of Crosspaulin's orange, identical Montserrat headings and kicker rhythm, the same contact band and the same rounded cards.
**Fix:** a new system, recorded in `kb/purity-brand.md`. Graphite + safety yellow, Barlow Condensed upper-case display type, square corners and rules, a running header with section numbers, a new cover layout, and photo cut-outs on grey panels.

## Round 2: blockers in the new system
1. Page 5 overflow: the Finishing panel ran into the footer. Fixed with a shorter heading, smaller roll figure and tighter panels.
2. Upper-casing changed units ("1.5 M", "(KG)"). Fixed: units sit in `.u` spans, and table headers are no longer upper-cased.
3. Wraps: "−30 to +70 °C" (page 2) and "Minimum order and lead time" (page 6). Fixed: "−30/+70 °C" and "MOQ & lead time".
4. A fallback font (LiberationSans-Bold) was embedded because neither subset has ← →. Fixed: the scale arrows are now a drawn line. `pdffonts` shows only Barlow Condensed and Inter.

## Round 3
**Verdict: ship (working draft).** 6 pages, A4, 0.79 MB (bigger because of the PNG cut-outs). The QR code decodes to the PVC product page. The leak and Crosspaulin-term greps return nothing.
Open, and not design: the Purity logo (real palette), higher-resolution photos, and the datasheet values.
