# Bearframe pixel art: Round 26 recovery and reuse

This is an actionable continuation checkpoint for future asset sessions. Recover the actual working files before creating a replacement.

## Recover the asset

Find the saved package by its exact filename in the user's ChatGPT files:
**Bearframe_Round26_Eight_Direction_Walking_64_Frames.zip**

The archive is the authoritative editable asset checkpoint. This public guide stores methods and retrieval instructions, not character artwork. A previous session's scratch path is not a durable recovery location.

Extract the package and read `ROUND26_README.md`, `ROUND26_QA.json`, `SOURCE_PROVENANCE.json`, and `BASELINE_LOCK.json`. Locate `build_walk.py` and `export_validate.py` rather than assuming an extraction root. The final output directory is `walk_v5`; rejected versions are not animation masters.

Open `walk_v5/all_directions_1x.gif` first, then inspect the native audit sheet, individual direction strips, three-loop contact stages and frame 7-to-0 seam sheets. The editable master is `walk_v5/Unit09_8Direction_Walk_64Frames.aseprite`. Named per-part PNG layers and `frame_layer_map.json` preserve physical-part identity despite changing depth slots.

## Working contract

- Eight directions, atlas row order: S, SW, W, NW, N, NE, E, SE.
- Eight actual movement poses per direction; 64 total.
- RGBA frame 112×192; foot pivot (56,168).
- Eight columns and eight rows; atlas 896×1536.
- Each pose 100 ms; loop 800 ms.
- Terrain grid remains 32×32. Transparent sprite clearance does not redefine tiles.
- Four Founder-liked cardinal source PNGs in `source_refs` are protected by hashes.
- Unit09 is a practice character, separate from canonical selectable Sleeper A–D.
- Engine and APK were not modified.

## Reuse the successful method

Keep the original detailed raster materials. Separate registered body parts and use fixed-length articulated guides, counter-swing and projected near/far depth order. Round26 is source-derived raster articulation with local pixel cleanup; it is not 64 independently painted frames.

Use one complete face/helmet surface per view. The authentic oblique source pose supplies useful diagonal helmet material. The rejected Round24 method pasted a profile face onto a nearly frontal body; it produced double-visors and poor directional volume. Round25's simplified replacement lost the source's detailed identity.

Keep shin, cuff and boot continuity. Round23's variable boot masks cut away calf/cuff volume. Complete boot assemblies plus frame clearance fixed that regression.

Project joint targets into stage space before integer quantization; subtract the snapped root afterward. Quantizing limbs independently produced planted-foot drift. Test the last-to-first join too: SE/NW needed a small toe-off guide correction with the leg IK recomputed. A passing interior stance is insufficient.

Use the per-direction motion trajectories in `manifest.json` and `motion.json`. Arbitrary equal map velocities are not guaranteed to match the supplied projected foot planting.

## Validation and remaining work

The saved validator checks distinct poses, binary alpha, connected bodies, boot/cuff and hand/forearm joins, declared opaque boot contact points, guide lengths, support and loop drift, atlas crops and independent decoding of all 64 layered ASE composites.

These checks passed in the saved build. They do not establish final artistic or runtime approval. The user subsequently described the animation as substantially better; final production approval remains open.

Review elbow/knee texture seams, dark narrow profile torso, diagonal helmet/armor planes, inconsistent shoulder details in the source views and secondary cloth motion. Inspect actual pixels and moving loops after edits; do not substitute numerical checks for visual critique.

Recommended next work is core animation coverage before cosmetic polish, while fixing structural errors immediately. Exact action scope still follows the user's next instruction. Preserve this walking checkpoint and its accepted character identity.

## Reproduction

The package contains both Python entry points and source references. Dependencies include Pillow, NumPy and SciPy; ffmpeg was used for the preview video. Inspect script path configuration before running in a new location. Preserve the recovered checkpoint before rebuilding. Update the private working archive and this continuity record after meaningful improvements.
