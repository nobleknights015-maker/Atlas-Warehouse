# LibreSprite 1.3 — working pixel-editor integration

**Status: INTEGRATION VERIFIED on GitHub Actions; not a completed Bearframe art-quality test.**
Date: 2026-11-11 UTC

## Why
Earlier Auren pixel exercises were mostly Pillow drawing primitives. Valid PNGs, animation loops and procedural polygons did not satisfy Founder's character-design quality requirements. A native pixel editor is an important improvement in tooling, but does not create artistic skill automatically.

## Chosen tool and verified environment
LibreSprite 1.3 (official Linux x86_64 AppImage release), invoked in headless/batch mode on a temporary Ubuntu GitHub Actions runner. Its JavaScript scripting API directly mutates image pixels in an opened sprite/cel; export is performed by LibreSprite itself. A separate Python/Pillow validation step checks the output.

Successful workflow run: https://github.com/nobleknights015-maker/Atlas-Warehouse/actions/runs/42961553641
GitHub workflow: .github/workflows/libresprite-smoke.yml
Input generator and pixel checker: warehouse/tools/libresprite_smoke.py
Real native editor pixel-edit script: warehouse/tools/libresprite_smoke.js

Evidence from run logs:
- `./squashfs-root/AppRun --version` printed `LibreSprite 1.3`.
- LibreSprite loaded and ran our `.js` in batch mode, reporting that it edited two pixels in layer 0 cel 0.
- Python verified a known source RGBA (48,53,69,255) at (16,16) became (171,91,240,255), and the adjacent pixel became (134,72,210,255), while (0,0) remains transparent and dimensions stay 32x32.
- Entire workflow succeeded and produced the `libresprite-editor-smoke` artifact, including input/output PNG and JSON report.

## Important limitations
1. This proves the editor can run and modify pixels; it DOES NOT show good character art, useful animation or game compatibility.
2. The temporary GitHub runner downloads LibreSprite for each workflow; it is not installed persistently in ChatGPT's sandbox or on the Founder's Android phone.
3. This public repository has only a generated, noncanonical 32x32 test image and small scripts. Never upload source user sprites, private files or secrets.
4. The workflow triggers only on relevant pushes and manual dispatch. It is not already a background rendering farm; the ChatGPT hourly study task does NOT inherently run this GitHub Action.
5. Keep run time/CI usage modest; do not continuously download large AppImages every hour merely to claim progress.

## Safe next technical milestones
- Provide a reproducible LibreSprite exercise that starts from a genuinely hand-designed, layered, originally authored small sprite (not raster extraction), then exports RGBA and sheet metadata.
- Test multiple frames, registered pivots, transparency and identical pose bounds.
- Develop a deliberate artist-review checklist versus canonical visual references at native resolution; fail weak designs regardless of editor used.
- Integrate actual source sprites only in approved private/workspace paths or through secure user-directed uploads; do not place characters in the public warehouse.
- Keep documentation and verified lessons in Atlas Warehouse; avoid noisy duplicate receipts.

## Source
Official: https://github.com/LibreSprite/LibreSprite/releases/tag/v1.3
Reference: https://libresprite.dev/docs/scripting/
