# Bearframe RPG — Four selectable Sleepers: matching portraits and playable sprites
Date: 2026-11-11
Status: **FOUNDER APPROVED VISUAL DIRECTION**; sprites are NOT validated engine-ready.

## The now-locked requirement
The four **specific** Sleeper designs supplied earlier by the Founder are the player-selection portraits. Selecting portrait A/B/C/D must spawn/play as that **same** recognizable Frame in the world. Do not treat them as generic interchangeable classes or replace them with old polygon Unit09 doodles.

## Four approved image directions
1. Starter A — purple-lit neutral male-style armored Sleeper, distinctive segmented swept helmet, asymmetric cloth and circuitry.
2. Starter B — purple-lit weathered male-style Sleeper with damaged plates and tattered scarf.
3. Starter C — purple-lit feminine Sleeper with high ponytail/helmet silhouette and detailed plating.
4. Starter D — cyan-lit feminine worn Sleeper, tag, asymmetrical tattered cloth and armor.

The Founder enthusiastically approved the appearance of four new 2×2 static standing front/side/side/back turnarounds produced from original user-supplied character imagery. This is the target LOOK for the eventual playable character sprites, not a claim that those high-resolution renderings are clean native-pixel sprite sheets. Keep portrait and corresponding sprite linked by stable ID.

## Rendering QA observed from the generated files
All four initial rendered 2×2 turnaround PNGs are 1254×1254 RGBA. They have intermediate alpha values and in excess of 150,000 distinct RGBA colors each (as verified locally). These are *visual assets/conversion inputs*, not clean limited-palette animation frames. They must be separated into correctly centered, consistent registered directional poses, then pixel edited and engine tested at chosen in-world resolution. These are static standing turns, no actual walk animation yet.

## Production sequence
1. Lock 4 immutable starter IDs and pairing `selection_portrait` -> `standing_turnaround` -> `animated_player_sprite` (do not mix identities).
2. Check actual mobile gameplay camera/map tile dimensions and select size based on visible on-device readability, not vague preference for largest sprite.
3. Separate all four stand directions for each ID, preserve characteristic silhouette/visor/colors/armor asymmetry, register pivots and ground anchors.
4. Convert/edit pixel clusters and transparency at target native scale; compare to the user's original portrait at 1× and zoom.
5. Use actual skeleton/section editing to correct mistakes *without redrawing the entire elegant reference from simplistic polygons*.
6. Approve static quality, then create four-direction idle/walk and other required action animations with frame QC.
7. Implement actual character selection mapping and test that portrait A always controls matching sprite A, B->B, C->C, D->D, including save/load and Android screen.

## Important privacy/provenance
Neither source portraits nor newly generated or derived private art may be uploaded into the public Atlas Warehouse; this file intentionally contains only descriptive production guidance. The source images originate in a private ChatGPT conversation, so future automation environments may not automatically have access; check tool/file availability before proceeding and don't claim to have viewed images not available.

## Mistakes to avoid
- Returning to blocky Unit09 generic mannequins as the final character target.
- Treating AI-generated 2x2 concept art as an engine-ready sprite atlas.
- Calling a four-view turnaround an animation cycle.
- Failing to maintain stable portrait-to-sprite identity across selection, movement and saves.
