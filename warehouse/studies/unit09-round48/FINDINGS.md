# Round48 findings and recovery handoff

## Result and status
A new four-cardinal walking CANDIDATE exists: 8 preserved front frames, 8 preserved back frames, and 8 newly articulated frames for each side. Both side legs alternate through contacts and passing positions. This replaces Round47's frozen-stride pelvis oscillation for active testing. It is not owner-approved or production-ready.

The owner rejected Round47's motion as standing in place with pelvic thrust. Its numeric deformation tests remain valid only as technical integration measurements. Do not revive that flex loop or label it walking.

## What was recovered
Read the live warehouse index, exact Revision37 approval and Revision45 pose records, Round44 source ledger, and actual local build sources. The strongest retained pieces are approved S/front and N/back, reference identity, intact full-body contact art, explicit frame timing, editable exports and source locks. Earlier side masks/pose replacements are not approved simply because they exist in the warehouse.

## Applied research
The crucial distinction is between a motion schedule, an anatomical rig, and rendered material. A good IK solver only supplies joint angles. Correct walks also need separate support phases, source material with correct ownership, designed hidden surfaces, draw depth, registered feet and raster review.

Used Ryan Juckett's published analytic two-link implementation as an explicitly marked Python adaptation with its original license. Exercised both bend branches in all target quadrants and verified that unreachable targets are reported. Used Pillow's documented inverse affine mapping for rigid source material. No arbitrary thigh/shin width scaling, body-aspect fitting, image generation, new mesh solver, paid plugin or engine replacement.

## Actual asset edits
- Traced explicit source ownership for near/far thigh, shin, boot and arm on the intact Revision45 reference contact art.
- Camera-near and camera-far visible material ownership is exclusive. Near/far identity stays fixed across the cycle even when the other foot leads.
- Found stranded arm-edge source pixels and assigned them to moving arms rather than leaving fragments on the torso.
- Preserved the matched torso/pelvis rather than splicing an unrelated standing pelvis onto a new lower body.
- Painted the occluded inner far-thigh surface as native polygon/cluster artwork underneath retained visible source material. The single contact source did not contain that whole face. It is new inferred art and needs owner review.
- Authored a far-boot ankle shaft and fixed material registration. Boot orientation and actual sole depth now determine the ankle BEFORE IK. No independent per-frame vertical boot nudge after solving the shin.
- Added explicit mechanical joint caps below retained armor. These are visible understructure artwork, not a claim that a black guide line is sufficient finished anatomy.
- Side upper-body horizontal displacement is exactly zero. Restrained existing one-pixel vertical bob remains. Both arms counter-swing.
- Used a full 8-phase schedule derived from the earlier functional walk structure: contact A, down A, passing A, up A, contact B, down B, passing B, up B. Opposing limb phase differs by four.
- S/N approved original files and layer data remain byte-identical. Preview/combined export pads them by integer (8,10) onto112x176; original96x160 files are included unchanged. S/N clip timing remains100ms; sides110ms. Synchronized comparison GIF uses110ms for display only.

## Measured checks
- 58 S and58 N approved file hashes match.
- 8 distinct W frames and8 distinct E frames; ankle ordering reverses between contact keys.
- Exactly one support leg declared in every side exposure.
- Four actual RASTER BOOT support intervals match pixel-for-pixel after world translation. The near and far boots are separate textures. This tests the entire isolated boot silhouette, not a single invisible anchor.
- Boot material covers the actual solved ankle during the checked support intervals.
- Original thigh and shin lengths are retained by rigid rotations; unreachable plans assert rather than silently drag sockets.
- All side composites have binary alpha and fit inside the export canvas.
- 32 layered ASE composites independently decode to their corresponding PNGs. Four direction tags and an RGBA atlas exported.
- Offline scale probe uses an actual owner station32x32 tile unchanged. Its48x75 sprite reduction is a SIZE PROBE, not a final native-resolution redraw or engine/APK test.

## Critical visual assessment
Reviewed side playback, opposing poses and final four-direction playback in native ffplay; inspected enlarged source ownership, sheet and decoded map-probe frame. The feet now pass and exchange leading roles. The former stationary pelvis thrust is absent. Source leg volume is more coherent because visible material has explicit ownership and missing inner thigh geometry was authored.

Remaining: knee and ankle contour changes still shimmer under nearest sampling; rigid arm swing and shoulder overlap are stiff; contact heel/toe roll is simplified; the inferred far thigh needs closer reference matching; side silhouettes and final map-size pixel cleanup await owner judgment. A connected silhouette or a passing file check is not proof those issues are solved. Do not call the new side art nearly perfect or merely assume only minor polish remains.

## Reproduce and continue
Private packet contains all inputs required by current scripts, source locks, original approved S/N, per-frame side layers, authored masks, motion data, QA, native sheet, layered ASE and inline previews.

Install requirements.txt in an isolated environment. Run sequentially and stop on failure:
python3 build_walk.py
python3 validate_and_preview.py
python3 export_editable.py

DejaVuSans font is expected at the standard Linux path used by the preview scripts. Current active build uses inputs/W_contact.png and E_contact.png; actual E artwork is not generated by mirroring W. Mask geometry is mapped by camera direction.

rejected/build_before_ankle_alignment.py is an internal superseded experiment, not an active entrypoint. It shifted the rendered boot after IK; do not use it.

Keep Revision45 and Round47 as historical checkpoints. Save Round48 separately until owner review. Next corrections should target specific cels/contours and preserve the functional gait; do not restart the animation architecture or revisit rejected full-sheet aspect fits.

## Reuse boundaries
For another character, reuse the semantic phase schedule and solver contract. Fit actual limb axes, reference proportions, source ownership, hidden surfaces and boot registration anew. Asymmetrical armor and foot roll may require replacement cels. No automatic arbitrary-character retargeting has been demonstrated. Finish the feminine art baseline before deriving masculine motion as requested.

## Source record
SOURCES.md lists22 selected primary sources/listings with access limitations, distinguishing code executed from documentation read and leads not run. prior_homework retains Round44's source-backed findings. No claim to have searched every site on the internet. Public warehouse stores only research, source code and methods; private owner artwork and station tile remain in the owner packet.
