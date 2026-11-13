# Bearframe RPG art study — actual original-source Unit09 articulation proof
Date: 2026-11-12
Status: OFFLINE EXPERIMENT ONLY — art quality and Android integration NOT APPROVED.

## Correction to previous work
The Founder rejected the Round36 result because it merely reorganized/recolored the previous *test-rig* animation to resemble the intended static character, rather than moving the intended character's actual pixels. Comparing a source static 96×160 Unit09 frame with Round32 old walk renders confirmed the old walk art had an artificially narrow/squeezed body, despite a detailed original.

## Current local/private deliverable
`Unit09_Actual_Reference_Animation_Proof.zip` was created from the *original four transparent 96×160 cardinal source views* (N/S/E/W) recovered from the private Round32 source_refs. These correspond visually to the Founder-supplied 8-direction **static study**, which is not itself a walk cycle. Original static source frames were kept byte-for-byte. Movable forearm and upper/lower leg regions were manually masked from those pixels and articulated with nearest-neighbor raster transforms; head, hair, visor, armor/torso remain original. Output: 4 cardinal directions, 8 samples each + exact static idle; only 4 unique integer-raster poses in each 8-sample cycle, no claim of 8 unique poses, and a 768×640 transparent 4×8 atlas. ZIP includes source refs, manual mask/transform script, JSON QA, manifest, and previews. No AI image generation.

## Acceptance: NOT PASSED
Although the original identity and full proportions survive this time, the walk is only an initial rigging proof. Real footfall/contact, knee and ankle section transitions, depth overlap and under-armor repairs remain crude; 96×160 source view is not an approved in-world character size on a 32×32 tile map. Do NOT call production-ready or claim physical Android testing. Next proper effort is native-pixel *hand cleanup* of key poses from this original-source rig, matching the established natural motion and then scaling/editing for the 32px map engine without using the squeezed test-rig art.

Private user art stays OUT of this public Warehouse document.
