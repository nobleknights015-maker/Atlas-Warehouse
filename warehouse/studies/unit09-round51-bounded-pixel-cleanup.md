# Unit09 Round51 bounded pixel-cluster cleanup

## Scope
Owner requested sprite cleanup after retaining the Round50 body. Applied a conservative native-raster color pass to16 W/E exposures. No new rig, animation method, pose fitting, limb scaling or image generation. S/N remains the unchanged approved baseline.

## Edits
Hand-authored small ankle-cuff color clusters with a coherent dark border, warm armor face, highlight and joint crease. Each cuff is clipped to existing opaque pixels; no silhouette is added, erased or moved.
Recolored41 isolated bright knee highlight flecks to existing warm midtones, without replacing kneecap shapes. Preserved classified purple-light and red-cable pixels. Did not globally quantize, blur or denoise the character.
2703 visible pixel colors change across16 side exposures. Body, arms, base leg layers and isolated boot-contact source layers stay byte-identical. Original layers remain in baseline for direct comparison.

## Verification
- Full composite alpha/silhouette matches Round50 exactly for every side exposure.
- Every color change is inside an explicit small ankle/knee cleanup region; zero outside-region differences.
- Body, far/near arms, unbooted leg bases and contact-boot layers are byte-locked.
- Lower four-row visible boot sole bands match the baseline exactly, preserving contact edges.
- Motion JSON and110ms side timing unchanged; all58 S and58 N file hashes pass.
-32 independently decoded layered ASE composites reproduce their PNG counterparts.
- Inspected enlarged before/after cuff details, sprite sheets and native ffplay comparison. Cuffs are quieter and more coherent; inherited rigid motion and broader inferred far-limb drawing remain open. This is a cleanup candidate, not owner approval or final game-ready certification.

## Reproduce
Install requirements.txt, then run:
python3 clean_pixels.py
python3 export_editable.py

Inputs are baseline/W and baseline/E plus original approved S/N. No external art download required. Output: Unit09_Cardinal_Walk_Round51.aseprite and RGBA atlas, separate frames/layers in walk, per-frame cleanup-region masks and QA.json.
side_walk_candidate.gif is the cleaned motion. cleanup_comparison.gif compares old/new. cuff_before_after.png shows enlarged local details.
Current pass intentionally leaves the retained body intact. Future cleanup should use similarly bounded changes and direct comparisons; do not reinterpret cleanup as permission to rebuild proportions or animation.
Owner artwork is private in the versioned packet. Only this technical handoff is deposited publicly.
