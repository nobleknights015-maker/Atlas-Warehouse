# Unit09 Round50: restore Round48 body; feet and belly edits only

Owner clarified the last version was not a total rejection: retain the earlier body from the version with bad feet and repair only the feet and belly protrusion. Round48 is the selected baseline for this pass; it is not a new claim of final art approval. Round49's broader arm/ankle/IK changes must not be carried forward.

## Exact baseline and bounded patch
- Reconstructed all16 W/E Round48 PNGs byte-for-byte in baseline48 before editing.
- Instrumented the unchanged baseline builder to also save unbooted leg layers before the existing boot composite. This instrumentation does not change the baseline PNGs.
- Restored Round48's original far_arm and near_arm layers byte-identically, with original swing, poses, joint coordinates, thigh/shin material, lengths and timing.
- Delete only the verified stranded forearm strip from the torso image (68 W source pixels,69 E). Do not redistribute it into animated arm material or alter arm swing.
- Replace only boot material at the ORIGINAL Round48 ankle positions. Use corrected standing boot art and the small inside forefoot from the previous foot-only material preparation; no new IK solve or leg repositioning.
- Per-frame allowed-change mask is the union of old/new boot pixels and the belly-strip deletion. Every final composite has zero changed pixels outside that mask.
- Original body pixels outside the belly strip are exact; original underlying legs and arm layers are exact. Body silhouette may change only where the requested protrusion is removed.
- Approved S/N original files and their existing100ms timing remain unchanged; W/E110ms timing and motion JSON remain unchanged.

## Checks and review
All16 side exposures pass bounded pixel-difference checks. Four entire-raster boot support intervals match in world space. All58 S and58 N file locks pass.32 layered ASE composites independently reproduce PNGs.
Reviewed baseline versus targeted correction playback in native ffplay and opposing contact stills. Corrected boots have clearer toe/heel/sole shapes and the fixed torso remnant is removed. Any broader style or gait limitation inherited from Round48 is deliberately retained. Do not use this narrowly passing comparison as a claim that all art is final or game-ready.

## Reproduce
Install baseline48/requirements.txt. Run in order and stop on failure:
python3 baseline48/build_baseline.py
python3 build_targeted_fix.py
python3 export_editable.py

Current outputs: Unit09_Cardinal_Walk_Round50.aseprite and matching RGBA PNG atlas; per-frame editable layers in walk; unchanged approved S/N files; original baseline and motion in baseline48.
Review GIFs: side_walk_candidate.gif and baseline_vs_targeted_fix.gif.
QA.json records changed pixel counts, all-zero outside-mask counts and preserved-layer checks. allowed_edits_XX.png records each permitted edit region.

## Continuation rule
Keep this body baseline fixed. Future feedback should change the indicated cels or parts only, with an explicit allowed-change region and a direct original/result comparison. Do not change arm swing, pelvis, body proportions or leg pose just to fix a foot. Keep old checkpoints and their research separately. Public warehouse stores only methods and technical notes; owner art remains private in the versioned packet.
