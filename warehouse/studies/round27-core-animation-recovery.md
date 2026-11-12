# Round 27 Unit09 core animations — recovery and reuse

Continue the actual editable checkpoint, not another study restart.

## Retrieve

Find the saved package by exact filename: **Bearframe_Round27_Core_Animations_Eight_Directions.zip**. Extract it and read README.md, QA.json and manifest.json. The output master directory is actions_v4 (including the final neutral-boundary and blade-sweep corrections). Previous Round26 walking files are preserved in walk_checkpoint.

Open previews/Unit09_Core_Animation_Reel.mp4, then per-action eight-direction GIF/WebP previews and native contact sheets. Editable ASE files are under actions_v4/STATE/. Source layers have their physical-part mapping in each direction's motion.json.

## Scope and contract

Eleven animation types in all eight directions: idle, preserved walk, run, attack, guard, hurt, cast, interact, knockdown, recovery, and separate malfunction. There are 704 frame entries across 88 directional clips; holds and exact neutral endpoints are intentional. Do not call these 704 unique hand-painted poses.

New action canvas: 256×224, pivot (128,184), world tiles still32×32. Original walk remains112×192, pivot(56,168); offset(72,16) registers it inside the new canvas without scaling. Atlas row order S SW W NW N NE E SE. Actions have20 editable depth layers,64 exposures and8direction tags per ASE. FX are separate hard-pixel layers.

Scripts build_actions.py, materials.py, export_actions.py and make_previews.py are self-contained with the supplied prepared source_refs. No image-generation service was used. This is source-derived raster articulation and native contour cleanup, not hundreds of independent paintings.

## Reusable lessons

- When a projected bone collapses to zero length, an unconstrained inverse raster map can fill the entire canvas with one sampled pixel. Bound the projected mapping before sampling; keep guide lengths and raster mapping limits distinct.
- Keep fractional root motion through stage-space quantization, then subtract the snapped root. Pre-rounding the root caused a one-pixel run support slide.
- Test actual opaque boot pixels, not just guide metadata. Run support is frames0–1 and4–5; airborne phases are separate. Follow the supplied per-direction integer phase/cycle contract rather than assuming arbitrary equal map speeds.
- Camera-plane crossing can flip an otherwise upright head180degrees. Head orientation and torso foreshortening need explicit treatment.
- Review small detached facets before deleting them. Five late helmet cases were repaired with explicit contour pixels.
- Exact neutral/action boundaries exposed small hand and foot mismatches after mechanics checks passed. Test idle-to-action and return, fall-to-recovery and recovery-to-idle.
- Rebuilding a pose can change depth-slot names. Remove stale generated layer aliases; do not present them as extra intended layers.
- Short blade-tip trails read as hooks. A broader tapered sweep around the hilt reads better.

## Verified limits

The saved validator passed all640 new frames: binary alpha, clear margins, one connected body excluding FX, connected cuffs/wrists, numerical guide lengths, run support pixels, atlas crops and independent decoding of640 ASE composites and80tags. Preview duration totals and transition boundaries were also checked. All64 previous walk PNG bytes and four cardinal source hashes were unchanged. Local ffplay playback and frame stepping sampled walk/hurt/cast presentations.

These are scoped checks, not final artistic approval. Front/back prone poses remain weak because foreshortening hides the body; rear views can read as a crouch. Joint seams, broad guard/cast hands, narrow profile torso, diagonal helmet planes, inconsistent source shoulder details, secondary hanging material and VFX polish remain open. Native ASE editor and actual game/Android acceptance were not performed. No engine or APK was modified.

Preserve this core-motion checkpoint. Continue with critical native-frame and moving-loop review before cosmetic polish or character redesign. Unit09 remains distinct from canonical Sleeper A–D.
