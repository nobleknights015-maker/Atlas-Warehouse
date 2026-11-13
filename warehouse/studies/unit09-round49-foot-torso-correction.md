# Unit09 Round49 side-foot and torso correction

Current active candidate: Round49. Retains Round48's alternating gait, native thigh/shin lengths, matched source body and preserved S/N files. Replaces Round48's side boot material and corrects torso/forearm ownership. This remains a review candidate, not approved final art.

## Owner feedback and cause
The side boots looked distorted and a thin object projected from the belly. Layer isolation confirmed a strip of source forearm remained in the torso image while another arm image animated separately. The old boot masks also carried raised-heel/calf material into foot rotation.

## Targeted edits
- Reassign the complete source front-forearm silhouette to far_arm. Torso pixels in that verified protrusion region are now zero in both views.
- Use a fresh grid array for ownership tests. An internal correction attempt reused a scalar loop variable as a grid and failed to clear the remnant; caught by playback and fixed before final export. A dedicated raster regression check now guards this.
- Restrict the far arm's high forward swing so it remains close to the torso; do not delete the limb.
- Replace side boot cutouts with corresponding camera-near/camera-far standing source boots from the earlier actual character art. W near=source boot1, far=boot0; E near=boot0, far=boot1. Actual E artwork remains independently sourced.
- Register each boot at its anatomical ankle with no boot scaling. Author the small occluded inside forefoot beneath far-boot source material using the existing palette.
- Remove the old fixed rear-foot rotation; reduce swing roll. Keep whole-boot raster contact testing and solve ankles from sole depth before leg IK.
- Front/back source PNGs, layers and motion files remain unchanged.

## Verification and critique
All58 front and58 back file locks pass. Four whole-raster support intervals pass.32 layered ASE composites decode exactly. Every side exposure still has alternating support and canvas-safe binary alpha. Added zero-residual-forearm region check on both torso materials.
Reviewed final side playback in native ffplay after correction and inspected isolated source layers. The static belly spike is absent and boots read with flatter soles and clearer toes/heels. Knee/ankle contour flicker, rigid arm articulation and inferred far-limb detail remain open; no claim all side art problems are solved. Owner review remains required.

## Reproduce
Install requirements.txt. Run in order, stopping on errors:
python3 build_walk.py
python3 validate_and_preview.py
python3 export_editable.py

Current editable output is Unit09_Cardinal_Walk_Round49.aseprite with32 frames and four direction tags; matching RGBA atlas and motion JSON included. Side preview: side_walk_candidate.gif. Full four-direction preview: four_direction_walk.gif.
Prior Round48 research and its README are retained under prior_homework; no new research round is claimed. Input boot sources and masks/registration logic are included so edits can be reproduced. Current sources live in inputs and walk material_* files. Old diagnostic masks are historical.
The supplied phone video and its screenshot are not included in the project archive or public warehouse. Only safe technical notes are published.
