# Round28: fall/recovery leg correction checkpoint

Recover **Bearframe_Round28_Knockdown_Recovery_Leg_Fix.zip** from the user's saved files. This patch replaces only Round27 knockdown/recovery. Recover Bearframe_Round27_Core_Animations_Eight_Directions.zip for the other actions. Do not restart the character or overwrite the accepted walk.

Show test animations directly in chat. The user should not need to download and extract an archive to review them.

## Working files

Read README.md, QA.json and manifest.json. Rendered masters are under fall_v2/knockdown and fall_v2/recover, including per-direction PNGs, named layers, motion data, atlases and native ASE sources. Inline review files are previews/knockdown_fixed.gif, previews/recover_fixed.gif and previews/fall_and_rise.gif. Both actions also have all-eight-direction GIFs and lossless WebP.

Knockdown has8 frames per direction (64 total); recovery has12 (96 total). Both have20 layers and8 direction tags. Canvas256×224, foot pivot(128,184), world grid32×32. Recovery's atlas has12 columns, not8. Exact durations are in the manifest.

## Root cause and repair

The old free3D knee pole combined with different hip/ankle lateral positions drove knees sideways when the hip descended through ankle height. Constant bone lengths did not detect this trajectory error. Old peak lateral offsets were approximately7 and13 guide units.

The corrected leg solver stays in each physical sagittal plane with one fixed signed bend. Lateral offsets are zero and the bend cannot switch when hip/ankle height crosses. Targets are authored to be reachable rather than silently clipped.

Recovery has its own12-key sequence rather than reversing the fall. One leg supports while the unweighted front boot tucks through authored thigh angles; that boot plants during frames5–8 as the hips rise. The other foot steps in, then the first settles into the original idle pose.

Do not infer improved smoothness from lateral offset alone: the active recovery leg's largest per-key displacement is slightly larger than before, while the other leg's largest jump is much smaller. Judge the moving tuck/plant transition.

## Verification and remaining work

The saved checks cover all160 frames: alpha, margins, connected bodies/cuffs/wrists, fixed guide lengths, sagittal planes, fixed bend sign, knee height, actual opaque boot support pixels over40 stationary support intervals, and exact idle/fall/recovery boundaries in all8 views. Both ASEs were independently decoded for160 exact composites and16 tags. E/SE connected playback was reviewed locally and frame-stepped. The original complete Round27 checkpoint was compared against its prior hashes and remains byte-identical.

This is still a source-raster articulation review build. Front/back prone head/torso foreshortening remains weak and source-part seams remain. No final Founder approval, native ASE editor, engine or Android acceptance is claimed. No engine or APK changes.

Reproduction: build_fall.py defines the keys/solver; materials.py and source_refs hold prepared materials; export_fall.py renders/exports; previews_checks.py creates previews and validates contacts/boundaries using the included reference_idle images. Run the latter two scripts from the extracted folder. The rejected8-frame recovery and review sheets are retained for comparison.
