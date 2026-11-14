# Unit09 Round52 — far boot and chest ownership

Scope: retain the improved Round51 body and gait. The owner identified only an undersized far foot and an undulating chest-side artifact.

Diagnosis: a proximal fragment under the chest was assigned to the swinging far-arm source material. Its rotation changed the apparent bust underside while the torso itself was static. Move verified chest pixels to the torso and remove those same source pixels before the arm transform; do not freeze the whole arm or change chest proportions. This correction uses W-local x >=42, y <=82 intersected with opaque far-arm material; E uses mirrored coordinates with its own texture.

Far boot: paint a fuller native toe/forefoot/heel around its retained ankle, keeping original sole height and existing transforms. Do not scale the legs or alter IK to compensate for missing foot material. Preserve prior cuff cleanup outside the exact affected foot mask.

Evidence:16 side composites have zero differences outside explicit old/new far-boot masks and chest-fragment source/transformed footprints. Near arm/leg, unbooted leg bases and near boot-contact layers exact. Motion metadata unchanged, including positions and110ms cadence. All58 original files per approved S/N direction unchanged. Four raster support intervals have zero mismatch. Independently decoded ASE32 frame composites match the PNGs. Bob-normalized visible chest core43..52 x68..81 in W-local coordinates now has0 phase-varying pixels on both sides, previously62 W and61 E.

Native before/after playback and stepped poses inspected. Full far foot now reads at contacts/passing poses; its shading remains simpler than near boot and inherited knee/shin contour crawl persists. Numerical bounds do not imply owner artistic approval, retargeting readiness or engine acceptance. No engine/APK work.

Private checkpoint: Unit09_Round52_Far_Foot_And_Chest_Fix.zip retains exact Round51 baseline, source materials, updated layered images, editable32-frame ASE, transparent atlas, reproducible correction/export scripts, hashes, QA and direct moving previews. Public repository receives only this technical lesson; no owner art, phone captures or private conversation.
