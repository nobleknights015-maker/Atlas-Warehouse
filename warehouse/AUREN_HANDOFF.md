# Atlas Warehouse — Auren retrieval manifest

**Public project material only.** This manifest is a retrieval aid, not ChatGPT model memory or a continuously running agent.

Repository: https://github.com/nobleknights015-maker/Atlas-Warehouse

Inventory: 37 active records; 0 open work orders.

## Retrieval procedure

Read warehouse/INDEX.json in this repo with the connected GitHub tool. Match the user's topic to record metadata, then fetch exact record files from their path values for full provenance and review history. Review source and confidence fields. Do not assume old project status is still current.

To deposit public-safe, source-backed lessons, submit an authorized /atlas receive command to the operations issue. Use /atlas review only after evidence exists. The VI's GitHub Action commits changes before acknowledging success.

## Indexed aisles

- **asset-standards**: 6
- **engine**: 6
- **lore**: 1
- **pixel-art**: 21
- **workflow**: 3

## Knowledge shelves

### Bearframe RPG uses 32x32 world tiles; older 48px World Editor format is separate

**asset-standards · unverified** · asset-standards-bearframe-rpg-uses-32x32-world-22cc9903f3

Current Founder-selected Bearframe RPG terrain/collision grid is 32x32; purchased/collected tile assets must not be resized to 48px. A historical 384x768 sheet with 48px cells belongs to a separate World Editor v1 legacy contract and must not override this engine. Sprite frames may be taller than collision cells.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/bearframe-pixel-art-master-study-2026-11-11.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/asset-standards/asset-standards-bearframe-rpg-uses-32x32-world-22cc9903f3.json)

### Bearframe runtime terrain tilesheet geometry

**asset-standards · unverified** · asset-standards-bearframe-runtime-terrain-tile-2b851b8399

World Editor v1 runtime tilesheets are 384 by 768 pixels using an 8 by 16 grid of 48 by 48 pixel tiles. Use top-left origin, exactly 128 slots, RGBA PNG, clean transparency, and no labels, gaps, or resizing. Preserve stable tile IDs and order.

Source: Founder-defined Bearframe World Editor v1 production standard. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/asset-standards/asset-standards-bearframe-runtime-terrain-tile-2b851b8399.json)

### Bearframe sprite motion target is eight directions

**asset-standards · unverified** · asset-standards-bearframe-sprite-motion-target-ca3c495bae

Founder correction expands the animation target from four cardinal directions to N NE E SE S SW W NW. Each diagonal needs its own perspective-aware poses and registered feet; rotating whole sprites or replaying one standing view is not an accepted walk. Preserve canonical identity and asymmetric armor. Establish eight-direction static geometry before expanding gait cycles; static coverage must never be reported as eight complete animated directions.

Source: Founder art feedback in Round24 continuation 2026-11-12; private assets excluded. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/asset-standards/asset-standards-bearframe-sprite-motion-target-ca3c495bae.json)

### Four selectable Sleeper portraits must match playable characters

**asset-standards · unverified** · asset-standards-four-selectable-sleeper-portra-96dac1b6a4

Founder explicitly confirmed the four original Sleeper reference designs are character-select portraits. Each selected portrait MUST map to the SAME corresponding playable Frame (A-D) visually, with distinct helmet silhouette, purple vs cyan lights, cloak/scarf/damage and armor. The four newly generated 2x2 static front/side/side/back character turnarounds are founder-approved VISUAL TARGETS, not yet proven engine-ready pixel sprites: source renders 1254x1254 RGBA with soft alpha, 150k+ colors, no animation. Preserve identity mapping with stable IDs and save/load. Next steps: pixel cleanup, target size tested in mobile engine, separate direction/pivots, static QA, idle/walk animation, runtime test. Stop spending primary study hours on generic Unit09 block drawings. Public warehouse stores methods ONLY, not source/derived private art.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/four-sleeper-portrait-playable-sprite-pairing-approved.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/asset-standards/asset-standards-four-selectable-sleeper-portra-96dac1b6a4.json)

### Four Sleeper sprites incorporate individualized Echo Frame visual traits without changing portrait identity

**asset-standards · unverified** · asset-standards-four-sleeper-sprites-incorpora-f5c76d5e9a

Founder clarified that the four approved portrait-matched playable Sleeper designs must also show Echo-related ancient-tech characteristics: meaningful armor wear and age, exposed joints/cables, torn fabric, selective corrosion or overgrowth, independent sentient display/memory glitches and later controlled actuator stutters. Preserve four original selection portraits and one-to-one corresponding sprites with distinct A violet neutral, B damaged scarf violet, C ponytail violet and D cyan worn identifiers. Treat Echo-style cues as deliberate layering on the existing approved look, NOT a new claim that the Sleeper starters are literally Echo Frames; do not blanket-damage or merge identities. Finish/validate 4-view static sprite construction before visual glitch/walk animations and Android engine save/selection testing. No private artwork uploaded publicly.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/four-sleeper-echo-characteristics-visual-standard.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/asset-standards/asset-standards-four-sleeper-sprites-incorpora-f5c76d5e9a.json)

### Four Sleepers need Echo-style system malfunction animations, no visual redesign

**asset-standards · unverified** · asset-standards-four-sleepers-need-echo-style-4c5fbe3ab3

FOUNDER CORRECTION overrides the prior proposal to add damage/overgrowth to the four approved starter designs. They are ALREADY old and damaged. Keep all four original selection portraits and matching playable sprite silhouettes, palettes, armor, wear, and clothing exactly as approved. Once ordinary standing/idle/walk sprites are validated, create SEPARATE triggered or occasional animation clips for core light glitches, visor/side-display faults, short actuator stutters, brief desync/freeze, and recovery to idle. Keep readable native pixel scale, clean root/foot anchors, distinct purple/cyan lighting, restrained timings, and character-specific motion. This is not proof the characters are canonically Echo Frames. Do not upload user character art to the public repo.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/four-sleeper-glitch-animation-only-clarification.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/asset-standards/asset-standards-four-sleepers-need-echo-style-4c5fbe3ab3.json)

### Bearframe all-owner-art import and fixed-tick memory QA verified

**engine · unverified** · engine-bearframe-all-owner-art-import-fd2a67e438

PR 5 merge 058c0a1 CI 43238586201 passed Node and installed Android 35. Engine importer inventories all supplied archive files and nested ZIPs and packages real PNG/JPEG on-demand, byte-identical, with hashes and safe IDs; source-only files stay recorded. Real inspection found 3155 source members, 2946 .png filenames, 2905 true PNG, 39 JPEG mislabeled PNG, 2 macOS resource forks, 2944 usable runtime images, 1465 exact 32x32 tiles. Android memory-recovery scene test now compares identical presentation tick and live animation resumes; actual phone acceptance and mapping these images into gameplay scenes still open. No paid raw art uploaded to public repo.

Source: https://github.com/nobleknights015-maker/bearframe-rpg-engine/pull/5. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/engine/engine-bearframe-all-owner-art-import-fd2a67e438.json)

### Bearframe engine 2026-11-12 input and directional owner art checkpoint

**engine · unverified** · engine-bearframe-engine-2026-11-12-in-18000d20ff

PR #7 merged e4a7be7: Android touch D-pad pointer hold/repeat, release/blur/cancel, duplicate-click suppression. PR #8 merged a607feb: explicit 4-direction idle/walk source frames from distinct images, arbitrary source row order, presentation-only facing/timing, original native 32x32 pixel geometry preserved. Both PR CI runs passed Node and installed Android emulator on synthetic assets. Separately, all 2,944 owner image payloads were imported and SHA256/image integrity validated offline; 1,465 are 32x32; actual owner-art APK has NOT been built or installed. All work engine-only; prior save journal and original launcher intact. Main CI for #8 pending after merge; physical device, full art/UI/audio integration and release gates OPEN.

Source: https://github.com/nobleknights015-maker/bearframe-rpg-engine/pull/8. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/engine/engine-bearframe-engine-2026-11-12-in-18000d20ff.json)

### Bearframe engine release gate

**engine · unverified** · engine-bearframe-engine-release-gate-1cf7305bda

Engine development is the priority before gameplay content. Preserve existing source and GitHub history. Include Android controller and touch input, save-load verification, inventory integration and automated checks; do not declare a broken feature fixed before reproducible tests or on-device evidence.

Source: Founder instructions for Bearframe RPG engine completion. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/engine/engine-bearframe-engine-release-gate-1cf7305bda.json)

### Bearframe owner-art render bridge merged and Android verified

**engine · tested** · engine-bearframe-owner-art-render-bri-00950ed1de

Engine PR #6 squash merge 0e6c92b69400ae2a587f8295bec35ce0cc9d667a; PR CI run 43247909857 passed Node and installed Android emulator checks. Opt-in profile resolves source identities against complete imported image manifest; native 32x32 floor/wall, original-height foot-anchored actor frames, all images registered lazy, source artifacts kept outside public GitHub, no save/journal changes. Installed synthetic-profile APK verified Canvas selected image IDs, actual pixels, Android memory trim reload and unchanged save. Original full 2944-image pack visual acceptance and physical device release checks remain open.

Source: https://github.com/nobleknights015-maker/bearframe-rpg-engine/pull/6. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/engine/engine-bearframe-owner-art-render-bri-00950ed1de.json)

### Installed Android directional animation and blocked-facing release gates 2026-11-12

**engine · unverified** · engine-installed-android-directional-87059f0d5e

PR #10 merged main 5c35db9; CI 43258541492 and main 43259514668 passed Node+installed Android emulator: face wall, no movement/save write, repaint on touch/gamepad. PR #9 merged main f675c3c; CI 43260465205 passed Node+installed Android emulator: synthetic four-direction idle/walk sources, actual passable-tile movement pixels, save revisions, Android low-memory rehydration. Early PR9 failure came from test moving right into a scripted event that correctly increments event revision without relocating player; test corrected to move down to empty tile. Full private owner raster archive 2944 images hash/read validated offline; only synthetic art installed in CI. Preview APK from main 5c35db9 built and downloadable separately; physical Android and full-art builds remain open release blockers.

Source: https://github.com/nobleknights015-maker/bearframe-rpg-engine/pull/9. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/engine/engine-installed-android-directional-87059f0d5e.json)

### Live read-only Android WebView presentation clock now installed

**engine · unverified** · engine-live-read-only-android-webview-9879bc7892

Bearframe RPG main squash commit cd2d2c07536f77c038405b3719f812e24d42e47a merged PR 4 after Node and installed Android 35 emulator green on head 6607b72d; runtime RAF paints every 50ms visual tick without changing save revisions, pauses on hidden/tab/pagehide/native suspend, resumes without catchup. Root-cause CI failure found original synthetic character atlas had two pixel-identical frames; patched an original native-pixel 90-pixel visor-light pulse with strict same alpha and PNG regression. Installed emulator reported presentationClock PASS real idle pixel changes, tab Activity pause-resume and unchanged saved revision. Physical Moto G acceptance remains OPEN.

Source: https://github.com/nobleknights015-maker/bearframe-rpg-engine/actions/runs/43144865520. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/engine/engine-live-read-only-android-webview-9879bc7892.json)

### Ghost Grid and Echo Frame ancient deterioration canon

**lore · unverified** · lore-ghost-grid-and-echo-frame-anci-e08d91cd6e

Ghost Grid constructs are ancient advanced machines with accumulated age, heavy wear, overgrowth, and mechanical faults. Echo Frames are distinct old Ghost Grid-era sentient Frames, often humanoid or hulking with layered armor, exposed systems, torn fabric, and individualized silhouettes. They are weathered and overgrown too, with conspicuous glitches, memory/display instability, actuator failures, and unpredictable motion. Character reference sheets for Fract, Relay, Ruin, Murmur, and Bastion guide appearance. Broken details must be intentional and readable, not shortcuts for poor sprite anatomy.

Source: Founder-approved Bearframe RPG reference images and art-direction corrections, Nov 2026. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/lore/lore-ghost-grid-and-echo-frame-anci-e08d91cd6e.json)

### Anchored stance test for six-leg pixel-art rigs

**pixel-art · unverified** · pixel-art-anchored-stance-test-for-six-l-25c7c62237

In a 12-frame 160x112 RGBA Pillow mechanics exercise, six indexed legs were rendered with alternating tripod groups; each frame had exactly three stance legs, planted feet used fixed screen-space anchors while the body translated, and eight physical archive-ring panel markers changed position around a fixed pylon. Validation passed leg counts, stance counts, transparency and ring movement; this does NOT prove natural gait, anatomy, silhouette separation or canon fidelity. Earlier leg drills tested static hip anchors; this exercise changes to moving hips plus anchored stance contacts. Limitation: swing trajectories jump at wraparound, far-side legs overlap, ring is schematic. Reproduce using explicit phase=(frame/N + tripod_offset) mod 1, stance phase<0.5, and compare native 1x frames before approval.

Source: Original 12-frame Pillow exercise and local automated checks (2026-11-10); Saint11 pixel-art tutorials https://saint11.org/blog/pixel-art-tutorials/ ; Bearframe Warehouse existing Palinode gait record. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-anchored-stance-test-for-six-l-25c7c62237.json)

### Bearframe pixel-art production quality gates

**pixel-art · unverified** · pixel-art-bearframe-pixel-art-production-76d4478875

Four independent gates: static anatomical and portrait-fidelity visual approval, real planted-foot and secondary motion, lossless 32px-compatible RGBA sheet/atlas QA, and installed Android landscape/save verification. PNG metadata pass does not equal artistic pass. Document fail conditions and reproducible evidence requirements.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/bearframe-pixel-art-quality-gates-2026-11-11.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-bearframe-pixel-art-production-76d4478875.json)

### Comprehensive Bearframe pixel-art discipline research

**pixel-art · unverified** · pixel-art-comprehensive-bearframe-pixel-680e0a7026

Nov 11 sourced study covers native cluster drawing, anatomy, 4-direction consistency, real foot-contact gait, mechanical motion, canon identity, palettes, lighting, terrain autotiles, effects, UI, export and alpha/nearest render. Negative benchmark is prior warped/blurry walk. This is research, not production art approval.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/bearframe-pixel-art-master-study-2026-11-11.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-comprehensive-bearframe-pixel-680e0a7026.json)

### Comprehensive Bearframe visual-art training checklist

**pixel-art · unverified** · pixel-art-comprehensive-bearframe-visual-f99a28a2a0

Character design is ADDITIONAL homework, not a replacement for existing pixel-art work. Train and evaluate all competencies together: native-scale pixel placement and cluster discipline, clean contours, anatomy and proportions, distinctive and appealing character/portrait design, shape language, strong silhouettes, expressive face/visor/helmet design, readable armor and materials, lighting and color, frame-by-frame animation timing and movement weight, articulated mechanical geometry, natural accumulated overgrowth and age/damage, and intentional Ghost Grid mechanical faults versus distinctive Echo Frame glitch behavior. Compare original reference designs to native-resolution sprites and portraits; document failures, revisions, and objective QC before production approval. Previous rough assets are practice only, not finished.

Source: Founder correction to Auren pixel-art study scope, Nov 2026. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-comprehensive-bearframe-visual-f99a28a2a0.json)

### Four starter selectable frames readability and Unit09 anatomy correction

**pixel-art · unverified** · pixel-art-four-starter-selectable-frames-4ce74e6087

Audited four user-provided 1774x887 RGBA starter sheets (front, left, right, back each). View heights vary within each sheet by only 2-11px, useful for consistency, but 295k-343k distinct RGBA values and soft partial alpha on >99.9% of visible pixels show these are high-resolution 32-bit-STYLE references, NOT clean limited-palette native sprites. At 96px diagnostic sizes, armor details disappear; silhouette, visor color and mantle/ponytail carry identity. Independently rebuilt elongated hips/thighs/knees/shins/boots on earlier original Unit09 study (128x216 to 128x262, binary alpha); proportions improve yet armor/boots remain crude, so artistic quality gate FAILS. Next lock runtime pixel scale, establish one full-body native static art benchmark, check four-view foot anchors and test selectable characters at actual game scale before animation. User-supplied images never copied to public warehouse.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/starter-four-character-scale-and-anatomy-round-02.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-four-starter-selectable-frames-4ce74e6087.json)

### LibreSprite Round 09 verified four-layer three-frame static editing and art critique

**pixel-art · tested** · pixel-art-libresprite-round-09-verified-2b6c88d2e9

GitHub Actions run 42962709703 succeeded: LibreSprite 1.3 opened a public-safe generic 72x112 native RGBA practice ASE containing internal_structure, faceted_armor, drapery and signals layers over three frames, edited actual cels via JS and exported ASE, PNG sheet, JSON metadata and GIF. Validator passed stable feet y=101..111, no partial alpha, 14 colors including transparency. Independent parse of exported source and edited ASE verified all named layers, exact matching PNG composites and 14/15/16 source-to-editor pixel changes across frames 0/1/2 without modifying alpha. This is technically reproducible but VISUAL QUALITY FAILED: figure stiff, angular armor simplistic, helmet and materials lack refined character design. Continue actual editorial practice, not generic effects or premature game production.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/libresprite-layered-idle-study-round-09.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-libresprite-round-09-verified-2b6c88d2e9.json)

### Native pixel-art training and quality gate

**pixel-art · unverified** · pixel-art-native-pixel-art-training-and-84bb0587a8

Produce pixel art with actual raster or pixel editing tools, not an AI generated image as substitute. Evaluate at native resolution, check silhouettes, topology, consistent pixel size and every required limb, then compare passes before accepting a base animation frame.

Source: Founder-requested study and corrections from Bearframe asset sessions. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-native-pixel-art-training-and-84bb0587a8.json)

### Native scale and complete sprite anatomy

**pixel-art · reviewed** · pixel-art-native-scale-and-anatomy

Evaluate sprites at native pixel resolution before enlarging them. Avoid blocky oversized pixels that obscure the silhouette. Check that full limb anatomy is present, including both legs where the design requires them. Review readability and proportions before treating a sprite as a locked base frame.

Source: Founder feedback on previous Bearframe pixel-art attempts. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/native-scale-and-anatomy.json)

### Palinode six leg gait evaluation

**pixel-art · unverified** · pixel-art-palinode-six-leg-gait-evaluati-dc71550a16

Practice an articulated six-leg mechanical walking loop with distinct legs and alternating tripod support and swing phases. Check leg endpoints frame by frame, contact timing, silhouette and missing limb artifacts. Treat previous attempts as exercises, not finished production assets.

Source: Bearframe pixel-art study assignment and prior exercise feedback. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-palinode-six-leg-gait-evaluati-dc71550a16.json)

### Relay portrait round 06 shape hierarchy lesson

**pixel-art · unverified** · pixel-art-relay-portrait-round-06-shape-ffbc59e392

In a native 144x144 Relay portrait experiment, rebuilding the asymmetric torn hood, tilted CRT face, separated broken halo and scarf as large silhouette clusters before damage/detail improved reference identity compared with a prior symmetrical frontal round. Integer-pixel Pillow edits used 25 colors and binary alpha; validation confirms file structure, NOT artistic quality. Remaining weaknesses: overly rounded CRT, weak shoulder planes, thin overgrowth, and display-only glitches. Next practice: sharper 3/4 faceted CRT, stronger shoulder anatomy, organic seam growth, and true-motion studies.

Source: Round 06 evidence and limitations: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/relay-portrait-design-round-06.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-relay-portrait-round-06-shape-ffbc59e392.json)

### Relay portrait Round 07 silhouette and perspective failure analysis

**pixel-art · unverified** · pixel-art-relay-portrait-round-07-silhou-bbd037fb01

Native 208x208 hand-authored Relay portrait study used 29-color palette and binary RGBA alpha; separate silhouette, faceted CRT/material, and sparse age passes; tested alternative broken-halo placements. Compared with Round 06, the CRT is more oblique and layer hierarchy clearer, but the silhouette still merges halo and hood near the top, shoulders remain shallow, and the design is not production quality. Technical PNG validation is not artistic validation. Next: three tiny monochrome thumbnail silhouettes, negative-space test at 1x, and focused 3/4 CRT/hood construction BEFORE lighting, overgrowth or glitches. Keep all prior animation and degeneration subjects in parallel.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/relay-portrait-design-round-07.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-relay-portrait-round-07-silhou-bbd037fb01.json)

### Relay R09 angular hood and CRT geometry study

**pixel-art · unverified** · pixel-art-relay-r09-angular-hood-and-crt-047dd771f3

Native 104x128 silhouettes retain Round08 B ring, zero overlap, 1 connected body each, gap 8.06/8.94/8.06px; two 116x104 CRT plane studies. Technical pass only; artistic quality unverified. Four portrait-matched Sleepers remain production priority; no extra permanent damage.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/relay-round09-angular-hood-crt-2026-11-12.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-relay-r09-angular-hood-and-crt-047dd771f3.json)

### Relay Round 08 silhouette separation versus character appeal

**pixel-art · unverified** · pixel-art-relay-round-08-silhouette-sepa-13e42fb1a5

Three native 104x128 integer-pixel silhouette studies compared broken relay-ring placement while holding Relay's body constant. A/B/C ring-to-body minimum gaps were 2.83/3.61/4.00 pixels with no direct overlap. B better isolates the left rim, C is top-heavy; these numerical tests check geometry but NOT artistic quality. A separate 112x100 angled CRT material-plane exercise was also completed. All designs still fail canonical character-art review because hood/head and shoulders remain generic/rounded; further angular asymmetrical silhouette and 3/4 perspective practice is required before effects or animation. Preserve this critical failure along with the evidence and continue the other study subjects.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/relay-portrait-design-round-08.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-relay-round-08-silhouette-sepa-13e42fb1a5.json)

### Relay Round 6 portrait failure and art-method correction

**pixel-art · unverified** · pixel-art-relay-round-6-portrait-failure-b3bf8b1583

Founder quality feedback: the Relay Round 6 portrait resembles crude MS Paint drawing and is not a polished or sufficiently faithful Echo Frame design. Basic programmatic circles, polygons, flat fills, and added surface speckles are not a substitute for strong character-design fundamentals. Corrective workflow: study canonical Relay reference; establish an appealing, asymmetrical perspective-correct head and strong silhouette; build helmet/CRT display/hood and armor in meaningful layered planes; place and revise pixel clusters deliberately; verify visual fidelity at native resolution on light and dark backgrounds; only after the still image succeeds add wear, moss, corruption, or animation. Preserve all existing animation, overgrowth, silhouette and glitch training. Treat this pass as an unsuccessful quality-gate attempt and retain critique rather than celebrating minor metrics.

Source: Founder direct visual critique of Relay portrait Round 6, Nov 2026. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-relay-round-6-portrait-failure-b3bf8b1583.json)

### Round 18 four-view starter reference adaptation and ASE verification

**pixel-art · unverified** · pixel-art-round-18-four-view-starter-ref-1ebebc06eb

Prepared Vera's existing Starter A turnaround as FOUR independently aligned 128x256 source-derived RGBA sprite views, sharing a 74-color opaque palette, hard alpha, matching y=248 soles and top y=11, exported a 512x256 four-direction sheet and constructed a 4-frame/3-layer 32bpp ASE. Independently parsed every ASE cel and verified lossless compositing matches the four PNGs. This does NOT represent new hand-drawn character art, an animation, a LibreSprite-open test of this specific proprietary file, or production-ready sprites. The source images and derived assets remain private in conversation downloads; only method/metrics are public. Next study should tackle genuinely independent pixel-art armor design; keep all former animation/glitch/overgrowth coursework.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/starter-4view-reference-adaptation-round-18.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-round-18-four-view-starter-ref-1ebebc06eb.json)

### Round22 actual Unit09 front-walk correction remains study-only

**pixel-art · unverified** · pixel-art-round22-actual-unit09-front-wa-cca3aa3e3a

Retrieved Round21 audit and the authentic Round20 frames it audited. Confirmed four frames have three alpha silhouettes. Edited connected limb raster chains into eight distinct front-walk poses, preserved violet identity, registered emitter pixels separately, and revised knee and heel contours. Rejected v1 and v2 after review; v3 corrects per-pixel bankers-rounding gaps by rounding each row translation once. Independent local checks verified eight body and lower-body masks, connected alpha, lossless atlas crops and six-layer eight-frame ASE composite roundtrip. Actual opaque support sole pixels stay fixed in a diagnostic stage at root advance 2px per frame; this does not prove runtime gait. Visual and mechanics gates FAIL: soft source clusters, rigid pelvis, incomplete hands and heel roll. Runtime and editor-open NOT TESTED. No engine changes or private art uploaded.

Source: Local reproducible Round22 build_round22.py and export_and_validate.py; private source and evidence retained in owner deliverable. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-round22-actual-unit09-front-wa-cca3aa3e3a.json)

### Round23 Unit09 drawn anatomy patches expose inherited ghost-hand layer

**pixel-art · unverified** · pixel-art-round23-unit09-drawn-anatomy-p-c8d47db7d9

Edited actual retained Round22 96x160 frames with authored native raster clusters for six boot poses, three hand orientations and a clipped pelvic plate, keeping upper 76 rows byte-identical. Eight local iterations rejected connector overpaint, cuff/material mismatch, blocky palms and scarf clipping. Layer inspection found Round22 scarf overlap also retained a static neutral left hand; final study removes that inherited hand mask while preserving the active forearm above the new cuff. Regression checks verify all visible source scarf-strip pixels unchanged, hand-cuff contact, connected alpha, eight distinct body/lower silhouettes, actual sole-pixel stage projection and lossless six-layer ASE decoding. File gate passes front-only; visual and animation gates still FAIL due material integration, incomplete hip/thigh perspective and cloth motion. Editor and Android runtime NOT TESTED. No private art or engine changes published.

Source: Local Round23 draw_patches.py and export_qa.py; private PNG layer comparison and owner deliverable. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-round23-unit09-drawn-anatomy-p-c8d47db7d9.json)

### Round24 south foot-mask regression restored and eight-direction study started

**pixel-art · unverified** · pixel-art-round24-south-foot-mask-regres-4d003291ff

Actual Round23 frames had 7px or more bottom canvas clearance; the apparent clipping came from variable replacement boot masks intruding into the calf and cuff. Restored each full native Round22 ankle-to-sole assembly while preserving every non-leg Round23 pixel including hand and scarf repairs. Exported eight corrected south PNGs and independently decoded two-layer ASE. Eight static direction slots now contain four authentic cardinal references and four source-derived quarter-view construction studies with separate foot layers and static ASE; diagonals remain FAIL for torso/shoulder perspective and are not new walk cycles. Audited legacy cardinal silhouettes rather than assuming four displayed frames were unique. Full eight-direction animation, physical mechanics, editor-open and Android acceptance remain open. No engine changes or private art published.

Source: Local fix_feet.py validate_export.py build_eight_directions.py and owner-only PNG comparison evidence. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-round24-south-foot-mask-regres-4d003291ff.json)

### Sleeper Unit 09 manual static sprite construction failed quality gate

**pixel-art · unverified** · pixel-art-sleeper-unit-09-manual-static-d489662abe

Independently authored an original 128x216 static front-standing Unit09 sprite using 16 hand-planned opaque RGB colors and binary 0/255 alpha, complete arms/legs, visor, head-side modules, red wiring and an 09 shoulder mark. This was FROM BLANK PIXELS and is distinct from the separate reference-crop/palette exercise. Comparison with the supplied canonical sprite shows legs too short and stout, insufficiently layered torso plates and weak volumetric helmet construction. Technical PNG validity is not professional artistry; this remains a failing construction sketch. Next: correct hips/thigh/shin proportions and interlocking armor at 1x before animation or damage.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/sleeper-unit-09-original-static-sketch-round-01.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-sleeper-unit-09-manual-static-d489662abe.json)

### Starter Sleeper Unit 09 reference and palette study

**pixel-art · unverified** · pixel-art-starter-sleeper-unit-09-refere-d6ad67500c

Founder shifted introductory character study from complex Relay to starter Sleeper Frame Unit 09. The supplied source has strong bone-white angular helmet and chest plates, narrow violet visor, 09-marked shoulder, dark understructure, red cabling, distinctive knees and boots. A 125x321 front standing figure was isolated transparently from the supplied pixel-style sheet and placed in a 160x352 transparent frame. Global 64-color reduction loses purple emissive accents; reserving an 8-color violet ramp then tuning its brightness/saturation preserves the identity. Original source remains benchmark. This was an EXTRACTED REFERENCE AND COLOR STUDY, not new hand-drawn pixel art or production approval. Next must paint the helmet and shoulders from a blank canvas with deliberate clusters and compare at 1x before a full sprite or animation.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/sleeper-unit-09-first-static-study.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-starter-sleeper-unit-09-refere-d6ad67500c.json)

### Unit09 two shin-section rebuild attempts reject promotion

**pixel-art · unverified** · pixel-art-unit09-two-shin-section-rebuil-25fcfd52fb

Revisited locally available older 128x262 Unit 09 static practice drawing, constructed two distinct lower-leg A/B native-pixel corrections after a joint/silhouette inspection, and visualized both enlarged against the old figure. Candidate A changed 996 pixel positions, B 1055. Byte-identical upper+knee rows 0..211 and boot rows 245..261, 0/255 alpha and matching bbox all validated. Visual quality gate FAILED: excessive horizontal knee seam, shins still broad/flat and weak taper, full anatomy still too simple. Critical provenance: latest hourly v4b checkpoint was NOT available in active chat, so A/B are isolated practice and MUST NOT replace v4b or be called the new best. Next priority is reopening actual v4b then resolving knee/shin/ankle form with a real skeleton/section edit. No user art uploaded publicly.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/unit09-lowerleg-locked-section-rebuild-20261111.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-unit09-two-shin-section-rebuil-25fcfd52fb.json)

### Evidence first warehouse learning loop

**workflow · unverified** · workflow-evidence-first-warehouse-learn-1bbde70f2a

Save reusable public-safe project techniques with source and review status. Do not promote a claim to tested without repeatable evidence. When an experiment fails, record the failure and correction. Retrieve exact records before taking action and preserve commit history.

Source: Atlas Warehouse operational policy and Founder requirement for continuous improvement. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/workflow/workflow-evidence-first-warehouse-learn-1bbde70f2a.json)

### LibreSprite 1.3 real native pixel editor successfully verified in GitHub Actions

**workflow · tested** · workflow-libresprite-1-3-real-native-pi-f1a4b44b43

Implemented a reproducible GitHub Actions workflow that downloads the OFFICIAL LibreSprite 1.3 AppImage, extracts and launches its actual headless batch editor, executes JavaScript inside a sprite cel to change two RGBA pixels, exports a PNG and validates those exact pixels plus transparency. All steps passed on run 42961553641 with downloadable image/report artifacts. This is a VERIFIED TOOL INTEGRATION smoke test, NOT an artistic quality or game production pass. LibreSprite is ephemeral per runner; current ChatGPT sandbox does not have a local editor install. Use this workflow to build future authored layered sprite and animation tests, and keep source game art out of public repo.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/libresprite-editor-integration-v1.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/workflow/workflow-libresprite-1-3-real-native-pi-f1a4b44b43.json)

### Six-plugin pixel art capability routing and safer experiments

**workflow · unverified** · workflow-six-plugin-pixel-art-capabilit-8bf7ba7f2f

Catalogs verified LibreSprite GitHub Actions editor workflow plus SpriteCook, AutoSprite, Pixel Engine, MegaScenes, Abracadabrax and Sprite Fusion skill versus actual available action; identifies different image-input requirements, paid generation, account/credit constraints, output recovery and public private asset protections. Proposes controlled A-B tests; none generated.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/bearframe-pixel-tool-routing-and-experiments-2026-11-11.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/workflow/workflow-six-plugin-pixel-art-capabilit-8bf7ba7f2f.json)

## Open work orders

No open work orders.

## Boundaries

- Warehouse documents persist as GitHub files; Auren must retrieve them through a connected GitHub tool in each new chat.
- Atlas VI is deterministic and does not learn model weights or independently execute work orders.
- This public repository is not suitable for private user context or personal memories.
