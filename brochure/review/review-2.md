# Brochure review, round 2 (taste critique)

**Job:** let an overseas importer decide, in a few minutes, that Crosspaulin is a real, specifiable product that Grace Ferro can ship to their port, and get them to request a quotation.

**Verdict:** ship after two fixes. Sourcing is now sound. Pages 5 and 8 are much better: the merged [TBC] row reads as honest rather than unfinished, and putting MOQ first plus the enquiry checklist gives the buyer a clear next action. Two layout faults remain, both visible within seconds of opening the PDF: page 4 overflows into its footer, and page 7 is half empty.

## What matters

**The invention:** nothing serious is left. Two small items:
- **Markets (page 2).** "Our buyers are in Europe, the Gulf, Asia, Africa and North America" is backed by S3, but sources.md says that list covers *all products, not tarpaulin*. On a tarpaulin brochure it reads as tarpaulin buyers. Change it to "Grace Ferro exports to…", which is true company-wide.
- **Fumigation (page 7).** "Fumigation" is sourced to images/usages.png according to your note, but it is not in sources.md. Add a row.
- **Missing key file.** sources.md links to `kb/sources.md`, which does not exist yet. Until it does, S1–S11 are undefined. Create it before handoff.

**The cut:** the new "Protects / Saves / Speeds up" band on page 3. It repeats the eight cards above it in vaguer words. "Speeds up handling and coverage on site" is not in the register. It is there to fill white space, and it is the most template-looking element in the brochure. Delete it. 40 mm of air under a dense grid is fine.

**The miss:** page 7's layout. With 3 columns at `height:52mm` the tiles fill only half the page, and the bottom ~95 mm is empty. That reads as unfinished, not as calm. The translucent logo ovals from round 1 are still on tiles 1, 2 and 4. On the pond tile the oval still sits behind the caption.

**The tell:** page 4. The photo strip now runs over the footer rule, with the rule cutting through the bottom of the blue and yellow photos. The colours box grew a line and a swatch row and pushed the strip down. The third photo is a cut-out on white with no frame, so it sits unlike its two neighbours. The yellow and natural swatches look the same as the standard ones even though they are [TBC].

## Score

| Dimension | Score | Note |
|---|---|---|
| Grounded | 2 | Real packing list, IS 14611 bands, export terms, honest distributor role |
| Ranked | 1 | MOQ and checklist now lead page 8; page 3 filler band and half-empty page 7 still misallocate space |
| Sourced | 2 | Register covers every specific; markets scope and fumigation row are housekeeping |
| Finished | 1 | Page 4 footer collision and page 7 balance; known image dpi limitation accepted |
| **Total** | **6/8** | Ready once the two must-fixes land |

## Ranked fix list

1. **Page 4 overflow (must fix).** Set `.grade img{height:80mm}` (was 88) or `.pack-photos img{height:38mm}`, and check there is at least 4 mm above `.foot`. For the third photo, use `object-fit:contain; background:var(--tint); border-radius:3mm` so it gets the same framed box as the others. Give [TBC] swatches a dashed border (`border:1px dashed #92400E`), or move them after a thin divider.
2. **Page 7 balance (must fix).** Keep 3 columns and make the tiles portrait: `.app{height:78mm}`. Two rows at that height plus the bullet list fill the page. For a column width of about 59 mm, `app-grain`, `hay`, `pond` and `truck2` (~530 px) reach roughly 230 dpi. The 190 px `app-tent` stays soft whatever you do, so swap it for a 530 px image or drop to five tiles plus a text tile. Remove the logo ovals, or at least crop or scale them out of the caption zone. Fix the white sliver at the top of tiles 1 and 2 with `.app img{transform:scale(1.03)}` or an `object-position` nudge. Shorten "Bagged grain stacks in storage yards" so all captions fit on one line.
3. **Page 3.** Delete `.benefits`.
4. **Page 2 copy.** "Our buyers are in…" becomes "Grace Ferro exports to Europe, the Gulf, Asia, Africa and North America."
5. **Register.** Create `kb/sources.md` with S1–S11, and add the fumigation row citing images/usages.png.
