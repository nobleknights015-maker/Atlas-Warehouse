# Bearframe starter character study — four designs and Unit 09 anatomy correction
**Status: training/reference QA only; NO production approval.** Nov 2026.

## Purpose and copyright/privacy
Founder's four new 32-bit-style starter character reference sheets are for selectable player-character options. Original user-supplied image files and any direct extracts are NOT uploaded to this public repository. This log describes reproducible findings only and does not assert game integration.

## Actual tools/inputs
Examined four RGBA PNG sheets supplied in chat. Each image is 1774x887 and shows front, left profile, right profile and back. Computed threshold-alpha bounding boxes per view, per-view heights, number of distinct RGBA pixels and alpha variation using Python/Pillow and NumPy. Produced local-only diagnostic comparisons with 96-pixel-tall silhouettes and scaled examples. Also manually edited original practice drawing's hips/legs using integer-pixel Pillow polygons and linework.

## Measured data
- Starter A sheet: 311,687 unique RGBA values, view height range 9 px.
- Starter B sheet: 295,485 unique RGBA values, view height range 6 px.
- Starter C sheet: 304,305 unique RGBA values, view height range 2 px.
- Starter D sheet: 343,486 unique RGBA values, view height range 11 px.
- All four sheets: at least 99.9% of visible pixels have alpha between 1 and 254, so their soft blended transparency is not already a hard-alpha native-pixel sprite grid. Vast color count is also evidence against claiming an indexed 16/32-bit limited-palette production sprite. '32-bit-style' is an aesthetic reference, not a guaranteed pixel size/bit depth or engine import specification.
- Four directions have reassuringly consistent full-body heights within each sheet, useful for designing shared anchor conventions. This does not prove exact matching feet or limb lengths.
- At 96px preview size the characters remain broadly humanoid, but many armor textures and differences between A and C disappear; heads, outer silhouette, cloak/ponytail and visor color become important identity features.

## Independent pixel edit
Earlier Unit 09 standing drawing is 128x216 native RGBA with 0/255 alpha and had visibly compressed legs. Rebuilt hips/thighs/knees/shins/boots manually using integer-coordinate raster shapes, extending the native canvas to 128x262; preserved the existing hand-authored torso and arms. Its technical alpha test passes. This is an independent refinement of earlier practice art, NOT copied pixels from a supplied reference and NOT new character production art.

## Critical design evaluation
Proportions are visibly less stumpy than before, but the original sketch remains crude, with rigid boot shapes, overly flat plate construction and weak value hierarchy compared with the source. Overall design-quality gate still FAILED. Native-alpha checks are technical only. Scaling the original generated sheets down with LANCZOS or nearest-neighbor does NOT make them original hand-authored pixel sprites.

## Next priority
1. Lock the game's actual character scale and camera before final sprite layout.
2. Pick one canonical benchmark starter, sketch three full-body thumbnail silhouettes at target game resolution (not 1774x887). Test head/body/leg proportions, shoulder readability, boot baseline and individuality from other starters.
3. Draw a static front pose in native pixels from a blank canvas, build distinct material value groups and non-flat armor facets. Evaluate at actual game scale.
4. Only after static artistic review passes build four-direction consistency and walk cycle, then battle motions and controlled deterioration/glitches.
5. Keep broader professional studies (Palinode six-leg gait, character design, pixel clusters, ancient wear, Echo glitch behavior) in rotation.

## Reference reading
- Saint11 tutorial archive: https://saint11.art/
- Pixel Joint pixel art fundamentals: https://pixeljoint.com/forum/forum_posts.asp?TID=11299
- Neverknights silhouette/readability: https://neverknights.de/en/tutorials/silhouette-readability/
- MDN crisp pixel display: https://developer.mozilla.org/en-US/docs/Games/Techniques/Crisp_pixel_art_look

**Do not publish user-provided sheets or extracted designs in Atlas Warehouse.** This is project-safe methodology and QA data only.
