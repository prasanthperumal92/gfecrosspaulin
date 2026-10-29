# Design review 1: Purity PVC tarpaulin brochure (2026-10-29)

Reviewed with the `taste` skill (critique mode) on the 70 dpi page renders.

**Job:** let an overseas tarpaulin buyer choose a grade and a supply form, then send an enquiry.
**Verdict:** ship after small fixes. Sourcing is clean; the issues are repetition and one missing item.

## What matters
- **The miss: colour.** Every buyer asks about colour, and the brochure says nothing except in the enquiry list. Colours are unknown (open question), so add a spec row "Blue shown; ask for available colours" rather than inventing a range.
- **The cut: repeated facts.** "Within 24 hours" appears twice on page 6 (price row and benefits). Page 5 states 1.5 m and 50 m three times (heading, drawing, fact tiles). Page 2's "2 faces" tile repeats the section heading "Coated on both sides".
- **The tell: filler tile.** "2 faces / PVC-coated, top and bottom" exists because the strip wanted four tiles. Replace it with a sourced fact the buyer uses: the service temperature range.
- **Invention check:** none found. Every number is from P1, calculated in `build.py`, or from the GFE PVC product page (G1). The tent caption describes the photo, not a Purity claim; keep it until the owner confirms the photo (open question 4).

## Fixes
1. Add a colour row to the spec table on page 4.
2. Page 6: price row says "On request."; the 24-hour promise stays in the benefits row.
3. Page 5: drop the "50 m on the roll" label from the roll drawing.
4. Page 2: replace the "2 faces" tile with "−30 to +70 °C".
