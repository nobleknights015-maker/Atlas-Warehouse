# Atlas Warehouse — Auren retrieval manifest

**Public project material only.** This manifest is a retrieval aid, not ChatGPT model memory or a continuously running agent.

Repository: https://github.com/nobleknights015-maker/Atlas-Warehouse

Inventory: 17 active records; 0 open work orders.

## Retrieval procedure

Read warehouse/INDEX.json in this repo with the connected GitHub tool. Match the user's topic to record metadata, then fetch exact record files from their path values for full provenance and review history. Review source and confidence fields. Do not assume old project status is still current.

To deposit public-safe, source-backed lessons, submit an authorized /atlas receive command to the operations issue. Use /atlas review only after evidence exists. The VI's GitHub Action commits changes before acknowledging success.

## Indexed aisles

- **asset-standards**: 1
- **engine**: 1
- **lore**: 1
- **pixel-art**: 12
- **workflow**: 2

## Knowledge shelves

### Bearframe runtime terrain tilesheet geometry

**asset-standards · unverified** · asset-standards-bearframe-runtime-terrain-tile-2b851b8399

World Editor v1 runtime tilesheets are 384 by 768 pixels using an 8 by 16 grid of 48 by 48 pixel tiles. Use top-left origin, exactly 128 slots, RGBA PNG, clean transparency, and no labels, gaps, or resizing. Preserve stable tile IDs and order.

Source: Founder-defined Bearframe World Editor v1 production standard. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/asset-standards/asset-standards-bearframe-runtime-terrain-tile-2b851b8399.json)

### Bearframe engine release gate

**engine · unverified** · engine-bearframe-engine-release-gate-1cf7305bda

Engine development is the priority before gameplay content. Preserve existing source and GitHub history. Include Android controller and touch input, save-load verification, inventory integration and automated checks; do not declare a broken feature fixed before reproducible tests or on-device evidence.

Source: Founder instructions for Bearframe RPG engine completion. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/engine/engine-bearframe-engine-release-gate-1cf7305bda.json)

### Ghost Grid and Echo Frame ancient deterioration canon

**lore · unverified** · lore-ghost-grid-and-echo-frame-anci-e08d91cd6e

Ghost Grid constructs are ancient advanced machines with accumulated age, heavy wear, overgrowth, and mechanical faults. Echo Frames are distinct old Ghost Grid-era sentient Frames, often humanoid or hulking with layered armor, exposed systems, torn fabric, and individualized silhouettes. They are weathered and overgrown too, with conspicuous glitches, memory/display instability, actuator failures, and unpredictable motion. Character reference sheets for Fract, Relay, Ruin, Murmur, and Bastion guide appearance. Broken details must be intentional and readable, not shortcuts for poor sprite anatomy.

Source: Founder-approved Bearframe RPG reference images and art-direction corrections, Nov 2026. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/lore/lore-ghost-grid-and-echo-frame-anci-e08d91cd6e.json)

### Anchored stance test for six-leg pixel-art rigs

**pixel-art · unverified** · pixel-art-anchored-stance-test-for-six-l-25c7c62237

In a 12-frame 160x112 RGBA Pillow mechanics exercise, six indexed legs were rendered with alternating tripod groups; each frame had exactly three stance legs, planted feet used fixed screen-space anchors while the body translated, and eight physical archive-ring panel markers changed position around a fixed pylon. Validation passed leg counts, stance counts, transparency and ring movement; this does NOT prove natural gait, anatomy, silhouette separation or canon fidelity. Earlier leg drills tested static hip anchors; this exercise changes to moving hips plus anchored stance contacts. Limitation: swing trajectories jump at wraparound, far-side legs overlap, ring is schematic. Reproduce using explicit phase=(frame/N + tripod_offset) mod 1, stance phase<0.5, and compare native 1x frames before approval.

Source: Original 12-frame Pillow exercise and local automated checks (2026-11-10); Saint11 pixel-art tutorials https://saint11.org/blog/pixel-art-tutorials/ ; Bearframe Warehouse existing Palinode gait record. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-anchored-stance-test-for-six-l-25c7c62237.json)

### Comprehensive Bearframe visual-art training checklist

**pixel-art · unverified** · pixel-art-comprehensive-bearframe-visual-f99a28a2a0

Character design is ADDITIONAL homework, not a replacement for existing pixel-art work. Train and evaluate all competencies together: native-scale pixel placement and cluster discipline, clean contours, anatomy and proportions, distinctive and appealing character/portrait design, shape language, strong silhouettes, expressive face/visor/helmet design, readable armor and materials, lighting and color, frame-by-frame animation timing and movement weight, articulated mechanical geometry, natural accumulated overgrowth and age/damage, and intentional Ghost Grid mechanical faults versus distinctive Echo Frame glitch behavior. Compare original reference designs to native-resolution sprites and portraits; document failures, revisions, and objective QC before production approval. Previous rough assets are practice only, not finished.

Source: Founder correction to Auren pixel-art study scope, Nov 2026. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-comprehensive-bearframe-visual-f99a28a2a0.json)

### Four starter selectable frames readability and Unit09 anatomy correction

**pixel-art · unverified** · pixel-art-four-starter-selectable-frames-4ce74e6087

Audited four user-provided 1774x887 RGBA starter sheets (front, left, right, back each). View heights vary within each sheet by only 2-11px, useful for consistency, but 295k-343k distinct RGBA values and soft partial alpha on >99.9% of visible pixels show these are high-resolution 32-bit-STYLE references, NOT clean limited-palette native sprites. At 96px diagnostic sizes, armor details disappear; silhouette, visor color and mantle/ponytail carry identity. Independently rebuilt elongated hips/thighs/knees/shins/boots on earlier original Unit09 study (128x216 to 128x262, binary alpha); proportions improve yet armor/boots remain crude, so artistic quality gate FAILS. Next lock runtime pixel scale, establish one full-body native static art benchmark, check four-view foot anchors and test selectable characters at actual game scale before animation. User-supplied images never copied to public warehouse.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/starter-four-character-scale-and-anatomy-round-02.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-four-starter-selectable-frames-4ce74e6087.json)

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

### Relay Round 08 silhouette separation versus character appeal

**pixel-art · unverified** · pixel-art-relay-round-08-silhouette-sepa-13e42fb1a5

Three native 104x128 integer-pixel silhouette studies compared broken relay-ring placement while holding Relay's body constant. A/B/C ring-to-body minimum gaps were 2.83/3.61/4.00 pixels with no direct overlap. B better isolates the left rim, C is top-heavy; these numerical tests check geometry but NOT artistic quality. A separate 112x100 angled CRT material-plane exercise was also completed. All designs still fail canonical character-art review because hood/head and shoulders remain generic/rounded; further angular asymmetrical silhouette and 3/4 perspective practice is required before effects or animation. Preserve this critical failure along with the evidence and continue the other study subjects.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/relay-portrait-design-round-08.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-relay-round-08-silhouette-sepa-13e42fb1a5.json)

### Relay Round 6 portrait failure and art-method correction

**pixel-art · unverified** · pixel-art-relay-round-6-portrait-failure-b3bf8b1583

Founder quality feedback: the Relay Round 6 portrait resembles crude MS Paint drawing and is not a polished or sufficiently faithful Echo Frame design. Basic programmatic circles, polygons, flat fills, and added surface speckles are not a substitute for strong character-design fundamentals. Corrective workflow: study canonical Relay reference; establish an appealing, asymmetrical perspective-correct head and strong silhouette; build helmet/CRT display/hood and armor in meaningful layered planes; place and revise pixel clusters deliberately; verify visual fidelity at native resolution on light and dark backgrounds; only after the still image succeeds add wear, moss, corruption, or animation. Preserve all existing animation, overgrowth, silhouette and glitch training. Treat this pass as an unsuccessful quality-gate attempt and retain critique rather than celebrating minor metrics.

Source: Founder direct visual critique of Relay portrait Round 6, Nov 2026. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-relay-round-6-portrait-failure-b3bf8b1583.json)

### Sleeper Unit 09 manual static sprite construction failed quality gate

**pixel-art · unverified** · pixel-art-sleeper-unit-09-manual-static-d489662abe

Independently authored an original 128x216 static front-standing Unit09 sprite using 16 hand-planned opaque RGB colors and binary 0/255 alpha, complete arms/legs, visor, head-side modules, red wiring and an 09 shoulder mark. This was FROM BLANK PIXELS and is distinct from the separate reference-crop/palette exercise. Comparison with the supplied canonical sprite shows legs too short and stout, insufficiently layered torso plates and weak volumetric helmet construction. Technical PNG validity is not professional artistry; this remains a failing construction sketch. Next: correct hips/thigh/shin proportions and interlocking armor at 1x before animation or damage.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/sleeper-unit-09-original-static-sketch-round-01.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-sleeper-unit-09-manual-static-d489662abe.json)

### Starter Sleeper Unit 09 reference and palette study

**pixel-art · unverified** · pixel-art-starter-sleeper-unit-09-refere-d6ad67500c

Founder shifted introductory character study from complex Relay to starter Sleeper Frame Unit 09. The supplied source has strong bone-white angular helmet and chest plates, narrow violet visor, 09-marked shoulder, dark understructure, red cabling, distinctive knees and boots. A 125x321 front standing figure was isolated transparently from the supplied pixel-style sheet and placed in a 160x352 transparent frame. Global 64-color reduction loses purple emissive accents; reserving an 8-color violet ramp then tuning its brightness/saturation preserves the identity. Original source remains benchmark. This was an EXTRACTED REFERENCE AND COLOR STUDY, not new hand-drawn pixel art or production approval. Next must paint the helmet and shoulders from a blank canvas with deliberate clusters and compare at 1x before a full sprite or animation.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/sleeper-unit-09-first-static-study.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/pixel-art/pixel-art-starter-sleeper-unit-09-refere-d6ad67500c.json)

### Evidence first warehouse learning loop

**workflow · unverified** · workflow-evidence-first-warehouse-learn-1bbde70f2a

Save reusable public-safe project techniques with source and review status. Do not promote a claim to tested without repeatable evidence. When an experiment fails, record the failure and correction. Retrieve exact records before taking action and preserve commit history.

Source: Atlas Warehouse operational policy and Founder requirement for continuous improvement. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/workflow/workflow-evidence-first-warehouse-learn-1bbde70f2a.json)

### LibreSprite 1.3 real native pixel editor successfully verified in GitHub Actions

**workflow · unverified** · workflow-libresprite-1-3-real-native-pi-f1a4b44b43

Implemented a reproducible GitHub Actions workflow that downloads the OFFICIAL LibreSprite 1.3 AppImage, extracts and launches its actual headless batch editor, executes JavaScript inside a sprite cel to change two RGBA pixels, exports a PNG and validates those exact pixels plus transparency. All steps passed on run 42961553641 with downloadable image/report artifacts. This is a VERIFIED TOOL INTEGRATION smoke test, NOT an artistic quality or game production pass. LibreSprite is ephemeral per runner; current ChatGPT sandbox does not have a local editor install. Use this workflow to build future authored layered sprite and animation tests, and keep source game art out of public repo.

Source: https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/libresprite-editor-integration-v1.md. [Record](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/records/workflow/workflow-libresprite-1-3-real-native-pi-f1a4b44b43.json)

## Open work orders

No open work orders.

## Boundaries

- Warehouse documents persist as GitHub files; Auren must retrieve them through a connected GitHub tool in each new chat.
- Atlas VI is deterministic and does not learn model weights or independently execute work orders.
- This public repository is not suitable for private user context or personal memories.
