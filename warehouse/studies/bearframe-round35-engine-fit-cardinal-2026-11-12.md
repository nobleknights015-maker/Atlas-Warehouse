# Bearframe RPG — Round35 cardinal engine-fit export (methods/QA only)
Date: 2026-11-12

The asset team recovered Round33's owner-private cardinal map test and Round32's active feminine motion baseline. New Round35 **private** deliverable: `Bearframe_Round35_Engine_Compatible_Animations.zip` (never commit this ZIP, sprite PNGs or owner environment tiles to this public repository).

## Scope
- Four cardinal exploration views: down, left, right, up; 32×32 native map tiles unchanged.
- Two existing unapproved map-size probes: 48px figure height (frame 32×56) and 64px figure height (frame 40×72).
- Two *asset-only* timing forms, preserving the original sixteen walk frames: `legacy_5` takes indices [0,3,7,11,15] to fit five presentation ticks (250ms total), and `paired_10` uses alternating five-frame step groups [0,2,4,6,7] / [8,10,12,14,15]. No generator re-interpretation or independent pixel redraw was performed.
- All four atlas variants packaged with four-direction sprite-theme fragments, source frame provenance, SHA256 checks, validator, 32px tile-context previews and a separate engine-team presentation-timing proposal.

## Verified vs. unverified
**PASS (offline)**: 136 extracted/selected frame outputs across four profile variants; original RGBA pixels matched exact source exports; consistent frame rectangle sizes/row order; binary alpha; 4 atlases passed read-back verification; 170 package members pass archive CRC and byte hashes.

**NOT YET APPROVED**: aesthetic quality/native cleanup, foot planting in actual installed game, selected 48px vs 64px map scale, physical Android renderer/save/touch test.

## Existing engine limitation (checked current source)
Explicit directional walk animation currently selects global tick modulo walk-frame count. Current host also snaps the logical tile immediately and holds `playerMoving` for five 50ms ticks. The five-frame atlas is backward-compatible without an engine code change, but starts at an arbitrary gait phase and still snaps tiles. The paired ten-frame design requires **engine-owned, optional pattern selection** plus movement-start presentation tick and alternating step parity. The asset team did not change `framework/scene.js`, `enginehost/boot.js`, GitHub gameplay source, or any APK. The engine team must test D-pad hold repeat intervals against the presentation window.

## Continuity
Round29-approved feminine movement baseline and all Round32 withdrawn actions remain unchanged. Legacy eight-way explorations archived, only four-direction cardinal art exported for exploration. Do not promote unverified map-size probes to approved production art. The Founder ultimately decides the 48/64 choice after map/Android inspection.