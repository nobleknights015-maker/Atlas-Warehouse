# LibreSprite native editing study — layered idle prototype, Round 09
Date: 2026-11-11 UTC

## Status
Technical layered-editing, frame export and validation: **PASSED**.
Artistic quality gate: **FAILED** — original generic mechanical training figure remains stiff, broad, and too geometrically simplified to qualify as a polished Bearframe sprite.

## Purpose and privacy
First multi-layer/multi-frame art-school exercise using the LibreSprite 1.3 editor, after the prior successful 2-pixel smoke test. The exercise is **non-canonical original training art** and does not copy the user's Unit 09 or other proprietary sprite sheets. The public repo contains only generic training code, test assertions, and methodology; the original supplied character references are not published here.

## Native editor test
Workflow: https://github.com/nobleknights015-maker/Atlas-Warehouse/actions/runs/42962709703
Output archive: `libresprite-layered-study`, artifact 13829208463 (temporary GitHub artifact).
Source code: `warehouse/tools/editor_armor_lab.py` (Python draws the original design as a true layered .ase file);
`warehouse/tools/editor_armor_polish.js` (LibreSprite itself modifies actual cels and color clusters);
`warehouse/tools/editor_armor_validate.py` (checks the export);
`.github/workflows/libresprite-layered-study.yml` (reproducible runner).

The generated native sprite is 72x112 RGBA, with 4 named layers `internal_structure`, `faceted_armor`, `drapery`, and `signals`; 3 idle frames. The editor successfully reopened, edited, and saved a real editable `.ase`, then exported a PNG sheet, frame metadata, and GIF. The GitHub Actions job completed **success**, including all verification steps. The sprite uses hard alpha, with a 14-color output palette counting transparency.

## Independent validation of returned actual artifact
Downloaded the actual GitHub Actions artifact, unzipped and parsed both source and edited `.ase` documents independently. Verified all four layer names and the frame structure, recomposited per-layer native pixels, then checked that the composites exactly match the editor-exported PNG frames.
Observed 14, 15, and 16 actual source-to-edited pixel changes in frames 0, 1 and 2 respectively. Alpha values and alpha silhouette did not change. No pixel in the foot/ground region y=101..111 changed between the three animation frames; 1x images have stable registration. The frame variation reflects controlled cloth sway and small optical changes, not locomotion.

## Critical review / homework
The dark understructure and bone planes at least separate torso, chest, leg/arm silhouettes, but armor still feels blocky and repetitive; stance is stiff, depth cues are shallow, visor/helmet construction is too simplified, and cloth motion is too minimal. Test figures must never be mistaken for polished production assets. The editor does not replace visual design practice.

**Next art tasks:** study head/torso/hip gesture as large clean shapes at native resolution, hand-correct silhouettes and value ramps, and compare three silhouette options before expanding animation. For future user-approved production trials, prefer private/user-controlled destinations for source character art, not this public repo. Continue other curriculum tracks including Echo glitches, Ghost Grid overgrowth, and Palinode gait.

## References
- LibreSprite 1.3 scripting: https://libresprite.dev/docs/scripting/
- LibreSprite command-line sheet exports: https://libresprite.dev/docs/cli/
- ASE file format: https://github.com/aseprite/aseprite/blob/main/docs/ase-file-specs.md
