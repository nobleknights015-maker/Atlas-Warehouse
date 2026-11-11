# Bearframe Pixel-Art Study Round 18 — Starter four-view sprite adaptation

**Status:** source-derived preparation exercise PASSED TECHNICAL CHECKS; independent character drawing quality NOT PASSED; NOT a production-ready engine asset. Study date: Nov 11, 2026.

## Why this test
Earlier independent drawing attempts of Unit 09 were geometric and much rougher than Vera's professionally styled starter reference sheets. The user asked to show progress; this round tests whether existing reference art can be faithfully prepared for game-scale editing, separately from genuine independent pixel-art mastery.

## Privacy and provenance
Founder-provided Starter A 32-bit-style four-view turnaround was used locally, NOT posted to this PUBLIC repo. The derived images and editable ASE were given privately to the Founder in the ongoing chat ZIP. **The resulting character is Vera's pre-existing visual design; no original character drawing is claimed.**

## Reproducible methods
- Isolated front, left, right, back from 1774×887 RGBA source with manually verified column windows (instead of 450px quarters that would crop the front right arm).
- Downscaled to preserve 238px figure height; each sprite cell is 128×256 and feet end at y=248, heads start at y=11.
- Shared 74-color opaque RGB palette, learned from source appearance, reserved color clusters for high-saturation violet emissives and red/copper details; no dithering.
- Quantized raster uses hard 0/255 alpha and empty RGB=0 beneath transparent pixels. Removed tiny isolated alpha components.
- Packed a 512×256 four-direction transparent atlas and separate frame PNGs.
- Built an editable 32-bit ASE file with 4 orientation frames, 3 layer groups: body/armor, violet emissives, exposed cables. **Four directions, NOT a walk cycle.**
- Independently parsed the ASE file; decompressed each RGBA cel; verified 4×3 frame-layer structure, transparency, and exact composite-pixel identity with all standalone sprites.
- Also checked a smaller 96×192 rendition for visibility and used source-versus-cleaned closeups for visual critique.

## Measured results and caveats
- 4 views, all 128×256, at a common y=248 foot baseline and y=11 top.
- Shared 74 opaque colors + transparent pixel state.
- ASE independent roundtrip and PNG/alpha/color/geometric checks: PASS.
- This session did **not** directly open the resulting proprietary ASE in LibreSprite (no safe public-runner path for the user source); prior GitHub tests have validated the same ASE writer/real editor pipeline with generic art.
- No game-engine runtime, controller, animation or collision test. Pixel-art character quality remains an ARTISTIC REVIEW item, not technically inferred from PNG tests.
- Visually more sophisticated than independent practice only because **Vera's original character is reused**. This is production-method learning, not proof of model or drawing-skill advancement.
- 74 colors still carry noise; further hand refinement and scale selection should precede game integration. The four reference views are not automatically perfectly anatomically matched in every pixel.

## Next study
Draw a genuinely independent, original helmet/shoulder and static front figure at chosen target scale, comparing angular armor construction and value grouping against private user references at native pixels. Fix a design that fails silhouette quality before adding wear, glow or animation. Continue prior separate work on Palinode six-leg gait, Ghost Grid overgrowth and Echo Frame glitches.

**No artwork, confidential information, personal files or private character reference images published to this repository.**
