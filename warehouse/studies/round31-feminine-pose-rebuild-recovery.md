# Round31 feminine pose rebuild — corrective checkpoint

Recover the latest saved master version, uploaded as Bearframe_Round31_Feminine_Pose_Rebuild.zip, containing Bearframe_Round31/. It replaces the same saved master identity used for Bearframe_Round30_Feminine_Reference_Master.zip; previous versions remain history. Keep art private. Round29 remains the approved feminine baseline.

## Rejection is authoritative

Read reviewed record asset-standards-round30-gesture-and-seated-mot-87d06d1210. Founder rejected the Round30 gestures and floor/seated family; the seated poses looked like crouching splits. Round30 reference coverage and technical passes were not artistic acceptance. Round31 is a corrective review candidate, not accepted art. Masculine variants remain deferred.

## Actual corrections

Crossed wrists extend across the body with deliberate elbow directions; combat-ready hands have distinct height/reach; temple gesture uses a smaller bent-arm target. Look-around removes the old head bob and keeps the helmet center fixed, but still relies on sampled feature projection and needs better native turn keys.

Seated poses first lower into a narrow crouch, then fold the shins across the front while pelvis settles close to the floor. A reachable side/front hand brace supports the low phase. Source-derived profile joint clusters remain provisional. Do not return to simply lowering a wide-legged standing rig.

Knees-to-prone catches with hands before lowering the chest. A hip arc clears knees. Resting prone thighs, shins and boots extend backward and low rather than leaving upright boots. Added prone_to_knees gives the new pose a compatible exit. Rise-from-knees brings a lead foot forward before lifting hips. The new chain is collapse_to_knees → knees_to_prone → prone_hold → prone_to_knees → rise_from_knees. Do not attach the preserved old recover directly to this new prone endpoint; old knockdown/recover remain their own compatible pair.

## Sources and counts

29 states,232 directional clips,3440 frame entries;9 approved Round29 states retain1088 frame entries exactly. Source entrypoints: motion.py, render.py, materials.py, approved_feminine_motion.py, prepare_palms.py, export_all.py, check_expansion.py, finish_contract.py, previews.py, package.py. Actual editable masters are feminine_v1/STATE/*_8directions.aseprite,20 layers each. Physical names/depth order are in motion metadata. Native256×224, pivot(128,184),32×32 world grid; row order S SW W NW N NE E SE. Binary alpha; nearest sampling.

Run prepare_palms.py, export_all.py, check_expansion.py, finish_contract.py, previews.py in order. Python3/Pillow/NumPy/SciPy and system DejaVuSans.ttf. Layer PNG caches are regenerated; if absent, check_expansion.py can read stored ASE cels directly, without older-round folders. Approved frame hashes are included. VIDEO_COMMAND.txt rebuilds optional MP4. package.py checks all member hashes. USER_CRITIQUE.json and ROUND31_CHANGES.json preserve the correction history; rejected/ retains old code.

## Verification and its limits

Checks pass3440 stored ASE composite comparisons,232tags,448 fixed support intervals,64 exact action seams and3440 packed reconstructions from six2048pages. Actual resolved wrist positions are checked against authored brace targets; knee clearance and fixed segment lengths are checked. Seated/prone FK is not standing-boot contact certification. Native ffplay overview/chain playback plus sampled key-pose grids were reviewed. No Android runtime, engine changes, native ASE editor acceptance or Founder art approval is claimed. Front/back prone foreshortening and sampled head turns remain weak. Do not relabel the candidate approved.

## Show tests inline

Embed previews/gesture_rebuild.gif and previews/floor_and_meditation_feminine.gif directly in chat. knees_to_recovery.gif shows the new complete floor chain; meditation_sequence.gif shows seated chain; STATE_all8.gif/WebP cover all directions. No test download/extraction requirement.

## Retained lesson

Check the visible silhouette and support sequence before treating file-level QA as success. Mechanical length preservation can coexist with an obviously wrong pose. A hand target is not contact if the solver clamps it away; verify the resolved wrist. The pelvis, shins and ankle order must describe an actual seated figure. A prone figure also needs resting feet and view-appropriate head/torso foreshortening.
