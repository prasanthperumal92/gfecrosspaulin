# Brochure review, round 1 (taste critique)

**Job:** let an overseas importer decide, in a few minutes, that Crosspaulin is a real, specifiable product that Grace Ferro can ship to their port, and get them to request a quotation.

**Verdict:** ship after fixes. The structure and copy are good: grades, sizes, terms and contact sit where a buyer looks for them, and the exporter/manufacturer split is honest. But it will not print well. The application photos are web thumbnails blown up 2 to 5 times, and a few credential claims are not backed by any source.

## What matters

**The invention:** page 2's credential chips ("ISO quality assurance", "DUNS 931865379", "REX registered", "FIEO", "APEDA") and "Our buyers are in Europe, the Gulf, Asia, Africa and North America". None of these appear in the listed sources. A DUNS number or a REX claim is the kind of thing a buyer checks. "Test reports are available on request" (p3, p5) has the same problem: no source says reports exist. Source each one, put it behind a [TBC], or cut it. "Grain & *fumigation* covers" (p7) also goes beyond the source.

**The cut:** page 5 repeats page 3 in table form. The "Waterproof 100%", "UV stabilised Yes" and "Colour shown" rows add nothing. Three rows of [TBC] × 4 make the table look unfinished. Merge thickness, tensile and tear into one row ("Thickness / tensile / tear: per manufacturer datasheet [TBC]"). Cutting "Colour shown" also removes a contradiction (see the tell).

**The miss:** a colour story that matches the photos. The cover and page 4 show **yellow** sheets, and the grade cards say "natural" and "black/silver". The colour list (p4, p5) only gives blue, silver, white and green. A buyer will ask whether yellow is orderable. Either add yellow and natural to the sourced list or confirm the photos are custom colours. The page 4 swatches need to match whichever you choose.

**The tell:** page 7. Low-resolution stock photos (tent 190×180 px, canopy 395×164 px, shown 91×58 mm, roughly 50–110 dpi) have a Crosspaulin logo pasted on as a translucent oval. On the pond tile that oval runs into the caption. The SVG labels on page 2 (diagram) and page 8 (flow) render in a fallback Arial instead of Inter. The decorative red "impact" ticks above the diagram encode nothing.

## Score

| Dimension | Score | Note |
|---|---|---|
| Grounded | 2 | Real packing list, real IS 14611 bands, honest exporter role |
| Ranked | 1 | 54-size table gets a full page while MOQ (the buyer's first question) is one [TBC] line; p3's 8 equal-weight cards |
| Sourced | 1 | Mostly sourced and [TBC]-marked; credentials, test reports and fumigation are not |
| Finished | 1 | Copy finished, print assets not (image dpi, empty bottoms on p3/p5/p8) |
| **Total** | **5/8** | Not ready |

## Ranked fix list

1. **Images for print.** Replace `app-tent.jpg`, `app-canopy.jpg`, `app-truck.jpg` and `app-fumigation.jpg` with originals of at least 1100 px wide, or drop to 4 tiles at `.app{height:50mm}` using only the ~530 px images. `cover-hero.jpg` (860 px across 210 mm, about 104 dpi) needs a source of at least 2400 px. Remove the pasted logo ovals. The product is the brand; the caption can say "Crosspaulin on a grain stack".
2. **Credentials (p2).** Keep only the chips that have a source. Mark the rest `<span class="tbc">`, or cut them along with the "Our buyers are in…" sentence and "Test reports available on request".
3. **Colours.** Reconcile the colour list with the photos (yellow, natural). Delete the "Colour shown" row on p5 and update `.swatches`.
4. **p5 table.** Delete the Waterproof, UV and Colour-shown rows. Collapse the three [TBC] rows into one `colspan="4"` row. Use the freed space to pull the IS 14611 reference box up.
5. **SVG fonts.** In the diagram and flow SVGs, set `font-family="Inter, sans-serif"` (or outline the text). Delete the red tick marks above the diagram.
6. **Print legibility.** Footer and legal text at 7–7.5pt in `#9CA3AF`/`#AFC0E4` will fade in print. Use `.foot{font-size:8pt;color:#6B7280}` and `.contact .legal{color:#C7D2EC;font-size:7.5pt}`. Darken `.sizes td.n` to `#6B7280`.
7. **Page balance.** p8 has about 55 mm of dead space between the terms and the contact band. Move "Minimum order" to the top of `.terms` (it is the buyer's first question) and give the flow more room, or raise `.contact{height:90mm}`. p3 has about 45 mm empty at the bottom. Increase `.adv` row gap or add the sourced "5× vs woven" footnote there.
8. **p4 bottom strip.** The third photo repeats the cover. Replace it, or go to two photos.
