# Round 19 — Unit 09 actual source-based animation practice

Date: 2026-11-11. **STATUS: local animation prototypes created and tested; NOT engine-ready.**

Founder supplied actual Unit 09 image sheets: 43157.png (three distinct four-direction body poses, 1448×1086 RGBA) and 43158.png (larger action/cutscene visual reference). These are privately supplied and MUST NOT be placed in this public repository.

## Completed practice
- Cropped 12 real source poses: 3 front, 3 left, 3 right, 3 back. Reframed without stretching to 96×160 RGBA cells with stable 7px bottom margin.
- Constructed four standalone **six-frame** prototype movement loops using sequence [pose0,pose1,pose0,pose2,pose0,pose1]. These use reference-derived poses, not independently repainted walking frames. The violet emissive areas are modulated per frame through an isolated HSV mask.
- Produced four directional GIFs and one 4×6 RGBA PNG atlas, hard-alpha frames.
- Produced a ten-frame front-facing chest-core / visor system failure and recovery sequence with fixed body silhouette and localized frame-specific purple intensity / scan disruption. First attempt **FAILED visual review**: solid magenta bar obscured natural gradient. Revised v2 to use sparse light interruption, retained visor gradient and small independent dark-chest core pulse.
- Revised core sequence returns to a start pixel-identical frame at beat 9 and preserves unchanged opaque silhouette in every frame.
- Validated frame dimensions, binary alpha (0/255), directional frame counts, and actual GIF decode counts. Final GIFs: 6 frames each for movement; 10 for system fault.
- Produced 48px map tile comparative sizes. At native 96×160 cell the unit appears about 3.3 tiles tall; alternate rendered sizes 72×120, 55×92, and 45×75 require actual in-engine readability tests.

## Limitations / blockers
- Walk loops are source-derived and composed of three unique body poses repeated in 6 frames. This is **not** an independently hand-authored complete foot-contact cycle. Body-frame registration and optical glow layer QA pass technically, but visual animation quality remains provisional.
- Reference antialiasing soft edges were hard alpha thresholded; original pixel clusters require human/visual cleanup at final chosen scale.
- Local cutscene glitch preview is a proof of concept, NOT an in-engine cutscene action or mobile-validated runtime.
- The actual runtime character scale, controller animation mapping, cutscene trigger and save/load integration are untested.
- Character silhouette and damage appearance should remain approved; no new permanent paint damage added.
- Keep ALL source imagery, derived frames, GIFs and ZIP private; only this textual method and findings belong in public Atlas Warehouse.

## Next visual practice
Use the large action/cutscene sheet for action pose timing; correct one actual six-frame walk by adjusting foot arcs and contact weighting at the selected target size, then create a clean named cutscene malfunction clip with explicitly triggerable onset/pulse/recovery segments. Audit each frame at 1x/zoom, and finally run in-engine/mobile.
