# Design review 2: Purity PVC tarpaulin brochure (2026-10-29)

All four fixes from review 1 are applied and checked on the re-rendered pages.

**Verdict:** ship as a working draft. What remains is owner input, not design:
- **Brand:** the palette is a placeholder until the Purity logo arrives. Swap the `:root` tokens in `styles.css` and the two hex values in `assets/generated/*.svg`.
- **Photos:** the owner confirmed on 2026-10-29 that the three photos show Purity material. All are about 640 px wide. The cover photo prints at about 100 dpi, which is acceptable for screen and office print but not for offset. Get high-resolution photos or generate scenes once Gemini billing is enabled.
- **Specs:** page 4 shows only sourced rows. When the datasheet arrives, add thickness, tensile and tear strength, adhesion and colours, and shorten the "Need test data" box.

Checks: 6 pages, A4 (595 × 842 pt), 0.49 MB. The QR code decodes to https://www.graceferroexports.com/products/tarpaulin/pvc. The leak grep and the Crosspaulin-terms grep both return nothing.
