# Female frame01 v3 — exclusive far-leg joint source ownership

Owner wants the far leg corrected before expanding other animation actions. V2 was a narrow armor-material edit, not a resolved rig.

Detected repeatable construction error:63 pixels per direction shared by far thigh/shin;127 W and135 E shared by far shin/boot. Shared source pixels followed different rotations, producing doubled joint surfaces. Assign shin the knee plate and boot the cuff; all three source masks now pairwise disjoint. Neutral source composite remains pixel-exact. Intentional dark understructure caps are separate from source picture ownership.

Reuse contract: load the explicit far_thigh_exclusive and far_shin_exclusive images in private rig_materials.json with original far_boot. Do not reuse overlapping older files merely because they exist in retained audit materials. Before new actions require zero pairwise source overlap and exact neutral composition. This is a material contract for this character, not a universal retargeter or completion of the other animation set.

Evidence:254 visible pixel changes over16 side frames, confined to old/new far-thigh/shin footprints; much of far leg remains occluded. Every other layer, boots, near leg, torso, cloth and arms exact. S/N composites and movement metadata unchanged. All32 final frames connected; independent ASE cel composition matches32 PNGs. Native before/after playback and stepped contact/passing poses inspected. Neutral/source and scope tests pass.

Visual limit: removing duplicated source joint material gives a modest correction. Dark inner-leg surfaces, boot shape and bent-knee contours may still read poorly; do not claim the entire far leg is artistically accepted or fixed. Keep other-action expansion paused pending visual resolution. No engine/APK or Unit09 changes.

Private packet Female_Frame01_Walk_v3_Exclusive_Joint_Ownership.zip contains current layered art, material contract, correction/export code, original reference, exact baseline layers, editable ASE, direct previews, checksums and original v2 packet including v1 for rollback.709 file hashes and ZIP CRC verified. Public notes contain no owner artwork.
