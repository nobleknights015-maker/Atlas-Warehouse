# Bearframe selectable Sleepers — Echo characteristics integration standard

**Status:** Founder art-direction clarification, 2026-11-11. Production visuals are not yet engine-ready. Public-safe technical guidance only.

## Locked character-select pairing
The four original Founder-supplied Sleeper sheets are the selectable character PORTRAITS. The four newly approved standing four-view pixel-JRPG turnarounds are VISUAL TARGETS for the matching in-world playable sprites. Keep stable A/B/C/D portrait -> direction sprites -> animations -> persisted selected ID. A does not become B and no one gets a generic shared character sprite.

## New requirement — Echo Frame visual DNA
The Founder requires incorporating Echo Frame characteristics alongside the already approved Sleeper designs, in line with existing Echo/Ghost Grid canon:
- Ancient technology: weathered armor, scuffs, minor chipped plates, exposed underframe, damaged components and hand-me-down asymmetry.
- Organic passage of time: selective corrosion, mineral buildup or small overgrowth/moss only where it supports story and readability, not blanket green texture.
- Salvage/fragmentation: torn scarf, frayed drapery, repaired plates, hanging cables and missing outer plating; preserve each character's existing distinct costume/armor layout.
- **Sentient fault cues:** irregular visor/chest/head-side display segments, ghost-like brief memory-light artifacts, intermittent glyph/optical disruption. This is a planned effect vocabulary, not a claim these frames are literally Echo Frames.
- Motor defects for later animation: subtle calibrated pauses, asymmetrical gait recovery, occasional actuator hitch, damaged limb response. Never introduce a permanent crooked stance that breaks coherent anatomy unless canon demands it.
- Aged technology does **not** erase the four distinct youthful/individual character identities or their portrait correspondence.

## Starter-specific production examples (not fixed new lore)
A: intact identifying segmented helm with violet display, restrained age/armor hairline damage and brief optical interruption.
B: already torn violet scarf, pronounced wear, exposed inner mechanics, irregular pulse.
C: recognizable ponytail/helmet silhouette, localized fractures and purple display/optic distortion, not interchangeable with A or B.
D: distinctive cyan visor/chest/head displays, asymmetric worn garment, selective cable corrosion and cyan ghost signals.

These variations adapt to each user's actual visual reference when available. Preserve portrait details and visually test their effect at real mobile render scale.

## Passes and acceptance
1. Keep original portraits stable on selection UI. Do not alter the portraits merely to add dirt without Founder request; apply Echo motifs to compatible sections of playable character art.
2. Static sprites first: four directions for each character with convincing anatomy, fitted sectional armor, material read, rag/aging motifs, hard-alpha and readable silhouette.
3. Verify arm/leg/boot registration and consistent orientation across directions; hard-pixel edit sources should be clean and layer-editable.
4. Only after static quality approval create movement/idle effects, with **separate overlay layers** for intermittent corrupted displays and nonpersistent actuator glitches. Glitches must not disrupt collision box/ground anchor or consistent identity.
5. Test actual Android landscape gameplay and character-select save/load for all four IDs; frame atlas previews are not runtime tests.
6. Compare each playable sprite against its *own* matching original portrait at 1× and normal game scale; every armor/visor/cloth/lighting distinction must remain readable.
7. Do not assume the four Sleepers are *classified* as Echo Frames. Echo-derived aesthetics and faults can be carried without retconning faction/ontology.

## Source context
- Founder-approved four-character pairing: `warehouse/studies/four-sleeper-portrait-playable-sprite-pairing-approved.md`
- Echo canon record: `warehouse/records/lore/lore-ghost-grid-and-echo-frame-anci-e08d91cd6e.json`
- Source reference artwork and derived asset images remain private to conversation and are NOT stored in the public Atlas Warehouse.
