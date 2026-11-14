# Echo Frame and Ghost Grid generator integration study

Date: 2026-11-14. Scope: deep research, code audit, independent mathematical experiments, and a staged implementation specification. This is not a completed generator expansion or game-ready art approval.

## Decision

Extend the native procedural generator using **family-specific rigs, typed modular attachments, explicit view definitions, and family-specific motion controllers**. Preserve the existing painter, project editor, exports, and manually edited frames. Bake approved results to sprite sheets for gameplay. Do not replace the working generator with a universal humanoid skeleton, a collection of palette swaps, a new game engine, or automatic crops from the supplied concept sheets.

The key separation is:

- **Identity and lore:** what the unit is; its individual history and possible Echo continuity symptoms.
- **Body family:** what joints and structural sockets it has.
- **Role and equipment:** what tools, sensors, rings, banners, and appendages fit that structure.
- **Motion:** how that topology moves and supports itself.
- **Condition:** stable structural damage, surface wear, overgrowth, and authored malfunction behavior.
- **Presentation:** native field/battle resolution, four facing views, draw order, anchor, and footprint.

These are separate data axes. A random condition or palette should not redefine topology or silently rewrite a character's identity.

## Evidence and boundaries

The inspected generator checkpoint is `nobleknights015-maker/bearframe-ghost-signal@fdea3ffef7fb2e7e5baa9e829b2448fbae25a7fa`, branch `sprite-studio-sleek-copy`. Its recorded verification is 26 native and 30 Chromium browser checks at run 43617085619. Original main remains `f6f8f09b7d6c452f158a67473ac35c2fb374da6f`.

A read-only check of the separate `ghost-signal-engine` branch resolved to `0a5096640773c7da223cbb8666deb25e15422a7b`. This study does not mutate that branch or claim future engine commits have the same state. Always re-check the consuming loader before integration.

Project canon was checked against the supplied `Bearframe_Lore_Bible_Revision_4_10_Master.md`, particularly sections 46–49 and the later illustrative-profile reconciliation. The original document and original artwork are not republished in this research folder. External documentation and papers are recorded individually in `sources.json`; the bracketed source IDs below map to exact URLs and short notes. Findings labelled recommendation are our synthesis, not instructions issued by the source authors.

Previous Warehouse records consulted include the anchored six-leg stance study, Round28 knee-plane correction, and the current tapered-chassis checkpoint. Earlier studies explicitly distinguish numeric checks from visual acceptance; preserve that distinction.

## Canon and reference interpretation

Echo denotes disrupted personal identity continuity in an ancient synthetic person; Ghost Grid describes an ancient infrastructure ecology. They are not interchangeable classifications. A damaged Grid mechanism does not automatically become an Echo. Shared historical engineering does not imply common allegiance, hostility, or a single manufacturer.

Echo symptom classes—Fragment, Repeat, Split, Drift, Residual, Corrupt, Fusion—must remain separate from chassis families. They may coexist and change. They are not seven robot species or seven mandatory movement presets. Do not infer hostile gameplay behavior from identity damage.

Legacy Echo styling uses patched industrial construction, exposed structure, obsolete interfaces and uneven replacements. Do not impose modern Bearframe insignia or the chest-plus-ear display package as universal Echo/Grid traits. Weathered ivory may appear on a reference without turning it into modern Bearframe uniform armor. Ring arrays are optional equipment, not a faction-wide requirement.

The supplied Palinode, Oracle, Vestige, Cathedra, Murmur and heavy-sentinel references demonstrate a design space. They are not a finite roster, proof of completed encounters, or permission to invent new historical contacts. New unnamed variants are procedural design examples until separately approved as characters.

## 1. What the existing code actually does

Paths below are relative to the inspected generator repository.

| Area | Existing behavior | Integration implication |
|---|---|---|
| `frontend/public/studio/lib/machine-rig.js` | Parts have IDs, parents, local pivots, rest rotation, shape, color role and z. Inverse-transform rasterization yields hard alpha. | Reuse the rasterizer; introduce validated family definitions and an evaluated pose layer before painting. |
| `evalPart` | Sinusoidal rotation/translation, positive sine lift, deterministic frame-index jitter, glow, ring spin, and eased one-shot offsets. | Adequate channels for accessories and simple authored mechanisms; they do not implement stance contacts, support transfer, IK, or joint limits. |
| `renderRig` | Recursive parent transforms; sorting by static z; left mirrors right if absent; absent views can fall back to another view. | Keep legacy behavior, but require explicit view and mirror policy for new asymmetric families. Validate parent graphs before recursion. |
| Machine surfaces | Plate, taper, disc, ring, cable, banner, glass, texture. Rust/wear/moss largely use part-local procedural coordinates. | Add intentional silhouettes/material masks rather than only more noise. Keep texture imports separate and unchanged. |
| Machine rings | Elliptical surface with angular segment identity; split front/back shapes are possible. Broken segments depend on wear being nonzero. | Give new rings explicit physical damage independent of weather amount, shared identity across halves, and authored angular closure. |
| Presets | Heavy Sentinel, Hexapod Cartography Engine, Archive Sentinel, Micro-drone, Custom blank. | These are useful foundations, not a finished catalogue of all required families. |
| Machine editor | Presets, surface style, weather, palette, per-part JSON and channels. | Add a constrained family/role/module editor; retain advanced JSON editing with validation. |
| `sprite-sheet.js` | Project format v2, two sets, baked cells, edited-cell protection. Machine battle frames are 1.5 times design dimensions. | Version any new authoring data; preserve v2 and hand edits. Do not reinterpret old projects automatically. |
| `buildSheet` | A long horizontal sequence of all clips, direction rows, one bottom-center anchor. | Large machines need paged export and explicit registration metadata. A canvas bottom is not always the physical ground plane. |
| Existing game renderer | Fixed FW/FH slicing and destination offsets in `js/game.js`; FW=32, FH=56 in `js/art/wraith.js`. | New sheets need a metadata-aware consumer. Export success does not demonstrate in-game compatibility. |

Additional code risks: machine part Apply currently checks ID presence and shape, not full parent acyclicity, unique IDs, dimensions, or channel compatibility. Renaming an ID does not comprehensively remap dependent animation/parent references. Some channel IDs legitimately exist only in one view, so validation must distinguish a missing target in one view from a target absent across every compatible view. Preset builders can share object references between views; audits and compilers should normalize through independent immutable data, not mutate aliased builder objects.

### Repeatable characterization results

Run `audit-generator.mjs` against the pinned checkout. Full output is `generator-audit.json`.

- 960 frame cases rendered; each was rendered twice with **zero repeated-render hash mismatches** in this local native-canvas environment. This does not prove cross-browser bit identity.
- Authored production presets generally contain down, up and right views; left is mirrored. The blank preset also lacks up. No duplicate IDs, missing parents or parent cycles were found in these preset views.
- A 48-unit overscan probe, preserving scale and translating each root once, found content beyond the original frame in 28 heavy-sentinel direction/action combinations, 20 hexapod combinations, 10 archive-sentinel combinations, and 4 drone combinations. Blank had none. Counts include outer outlines; intentional departure effects need explicit classification. This finite probe is a lower-bound diagnostic, not a proof that every possible extreme has been sampled.
- Idle/walk analytical cycle endpoint comparisons reached differences of 307, 124 and 941 pixels respectively for heavy, hexapod and archive examples. This compares evaluation at phase zero and one, not the last discrete frame to the first. It flags nonclosing channels/material patterns for inspection; it does not establish that every visible loop is unacceptable.
- Current hexapod battle export: **6528 × 288**, 7,520,256 uncompressed RGBA bytes. Archive battle export: **6528 × 528**, 13,787,136 bytes. PNG file size is not decoded memory size. These widths motivate paging, even when the current Canvas implementation accepts them.
- The current humanoid `legIK` helper has lengths 8 and 8.5. A reachable target (4,12) preserves them. A target (0,100) leaves the endpoint outside reach and gives a measured second segment about 92.00056. Targets inside the inner reach boundary, including the root, also fail. Existing tested normal poses are a narrower valid domain; the helper must be made robust before accepting arbitrary proportion/pose sliders.

These are newly characterized gaps, not contradictions of the earlier checks: the earlier suite did not establish these properties.

## 2. Proposed family catalogue

These are implementation families, not new lore factions. Start with six useful topologies; add others only with an actual design need.

| Family | Reference role | Required geometry | Primary movement | First review proof |
|---|---|---|---|---|
| Legacy biped / industrial Echo | Murmur, relay workers | Root, pelvis, articulated spine, neck/head, two independent arm chains, two legs; optional packs and tool sockets | Upright or hunched walk with contact support; equipment-specific gestures | Neutral plus complete walking cycle in four directions; upper/lower body identity intact |
| Heavy biped | Heavy Sentinel / security construct | Broad trunk, large shoulders, heavy arms, fixed-size boots; optional weapon sockets | Longer weight transfer, deliberate acceleration and impact recovery | Weighted contacts and recovery, no knee reversal or sliding planted boot |
| Six-leg crawler | Palinode-style cartographer | Six persistent leg IDs with coxa mounting positions, femur/tibia chains, spine/deck and mast | Tripod, ripple or wave gait with explicit duty factor | Six-leg debug pass, contact timeline and world-motion preview |
| Orbital core | Oracle-style analysis node | Core, lens socket, independent ring planes, panel IDs, banner mounts | Hover translation, constrained core attitude, independent orbital motion | Front/back ring occlusion and a closed idle loop |
| Suspended archive spindle | Vestige-style archive intelligence | Tall spindle/lantern, two or more utility chains, halo supports, optional escort anchors | Hover/drift, tool manipulation and controlled settling | Ground projection stays registered while body height changes |
| Asymmetric relay custodian | Cathedra-style repair intelligence | Offset optic housing, unequal manipulators, relay spine and suspended equipment | Hover plus arm-specific reach and tool actions | All four authored views preserve the same left/right equipment identity |

A Velis-like hooded slender custodian can be a legacy-biped body with compatible archive modules if its joint structure fits; a unique silhouette does not automatically require an entirely new animation solver. Conversely, a new limb count or locomotor topology does require a new family definition. Do not promise automatic retargeting between a biped and crawler.

## 3. Data and assembly contract

Recommendation: retain `kind: machine`, but make a new family compiler opt-in. Compile a versioned UnitSpec into an evaluated rig suitable for the existing painter. Keep raw legacy rigs on their exact old path.

A UnitSpec should contain explicit versions, a stable unit ID, family ID, style profile, dimensions/proportions, view policy, module instances, palette/material roles, motion profile, condition profile, and separate export/runtime registration. Every generated part gets a namespaced ID such as `leg.LF.tibia.plate`; those names do not change when its color or damage changes.

Separate **bone/socket graph** from **render slots**. A tool attaches to a wrist socket; its depth is defined by the current view's slot order. Cloth anchored at a shoulder does not become a shoulder bone, and far-arm pixels never own the belly. Spine's documented skin and slot concepts illustrate this separation [S01,S02]. This is an architectural adaptation, not a decision to adopt its editor or runtime.

A module definition should declare compatible families, required sockets, provided sockets, slot group, view assets/shapes, rest offsets, bounding envelope, mass hint for posing, and allowed actions. An optic cluster can vary its lens count; a drill can replace a compatible hand tool. A module requiring a missing parent fails assembly with a useful message. It must not float at world origin or quietly attach to the torso.

Use JSON Schema for basic enum/range/required/conditional checks [S18]. Add semantic validation for graph cycles, duplicate IDs, unavailable sockets, unsupported actions, and mutually exclusive modules. A schema alone cannot determine whether the rendered thigh looks correct.

### Proposed metadata sketch (design only)

```json
{
  "authoringSchema": "bearframe-unit-spec",
  "authoringVersion": 1,
  "family": "legacy-industrial-biped",
  "familyVersion": 1,
  "unitId": "study-industrial-01",
  "identity": {"lineage": "legacy", "echoSymptoms": []},
  "viewPolicy": {"directions": ["down", "up", "right", "left"], "mirror": "explicit-only"},
  "modules": [
    {"instanceId": "tool.right", "moduleId": "survey-probe", "socket": "arm.right.wrist"}
  ],
  "motion": {"controller": "grounded-biped", "profile": "cautious", "seed": 17},
  "condition": {"seed": 19, "structuralDamage": [], "malfunctions": []},
  "registration": {
    "field": {"sourceSize": [64, 80], "groundAnchorPx": [32, 72]},
    "footprintTiles": [1, 1]
  }
}
```

The dimensions above illustrate the contract; they are not approved final sprite sizes or automatic changes to the established 32-pixel world tile grid. Do not expose fictitious generated identity/history as canon.

### Variation that is meaningful and reproducible

Prefer curated ranges and validated combinations. Vary silhouette before surface detail: trunk aspect, shoulder architecture, head position, arm function, ring plane and tool arrangement. Then vary material, fixed repairs, fabric shape, corrosion and rooted growth. Finally apply motion personality. Show family/role filters and a stable seed; provide per-category locks so an acceptable body can survive equipment or surface revisions. Store the resolved module list and recipe versions, not just a seed whose output may change after an update.

## 4. Grounded locomotion and IK

Two-bone IK has an inner and outer reachable radius and two bend solutions [S04]. The implementation must clamp the **effective endpoint** to that reach annulus, return both requested and solved targets, and keep the bend plane/sign stable. Merely clamping a distance while retaining an unreachable ankle breaks segment length. Joint limits and collision constraints still need an additional policy; an unconstrained exact endpoint is not necessarily an acceptable mechanical pose. Spine's IK documentation also demonstrates target-driven foot/hand control and the distinction between target and bone hierarchy [S03].

For limbs with more joints, FABRIK is a candidate constrained offline solver, not a requirement for every limb [S05]. Two-bone legs should stay analytic unless a third independent joint is actually needed. A hexapod can use a horizontal coxa yaw plus a planar femur/tibia solution, then project into the selected view. Screen-space depth compression must not be mistaken for a change in physical segment lengths.

### Foot locking and root motion

A planted foot is stationary in the world, not necessarily in an in-place sprite preview. During stance, body-relative foot motion cancels root travel. During swing it moves forward and lifts. Store stride distance and contact events. Match runtime playback phase to travelled distance; otherwise a correct in-place cycle slides at the wrong movement speed. Keep the legacy export until the new consumer can read these fields.

The independent experiment uses a backward linear stance and a Hermite swing whose horizontal endpoint derivatives match stance. A quartic height arch starts and ends at zero height and vertical velocity. This is our small illustrative model, not a copied robot controller and not a final artistic gait. It eliminates a position discontinuity seen in the old anchored-stance notes. Acceleration, turning, slopes, stop/start contacts, and damaged limbs require more work.

### Six-leg support schedules

The hexapod research distinguishes tripod (three stance legs), quadruped/ripple-style support (four), and wave (five), with different stance fractions [S06]. Use that as a geometric plausibility guide. It does not require simulating real robot dynamics in a JRPG.

Keep persistent physical leg identities: LF, LM, LR, RF, RM, RR. A standard alternating tripod uses LF/RM/LR against RF/LM/RR. View projection changes which appears near; it must not relabel or swap the actual limb. A slower wave is a useful candidate for a cautious massive survey machine. Select the gait for the specific unit, rather than assigning every ancient crawler the fastest tripod.

For damaged support, recalculate or author a compensating schedule and body lean. Fault-tolerant research explicitly considers the failed leg's position relative to the support geometry [S07]. Randomly deleting a foot and keeping every original contact phase is not sufficient. Test ground-plane support geometry before camera projection. Three visible pixels/legs are not proof that the projected center of mass is inside a valid support polygon.

Heavy and hunched bipeds similarly need authored support transfer. A bent spine modifies the body above the pelvis; it must not stretch or shorten legs to reach arbitrary targets. Test boots at normal size and a flat-contact pose before adding scars, cloth or effects.

## 5. Floating families, rings, limbs and cloth

Use a stable **ground projection/root anchor** for game placement. Hover height, body roll, lens aim, rings and arm chains are local motions above it. A hover cycle is not a biped walk with its feet removed. A hovering archive unit can move while its lantern hangs downward and its tool arms reach independently.

Represent each ring with radius, plane/orientation, thickness, segment count, material-panel IDs, damage mask, spin phase and light pattern. Compute front/back occlusion consistently for its plane. For a simple nonintersecting tilted ellipse, split back arc before the body and front arc after it; for more complex interleaving use authored depth groups or per-segment depth classification. Static global z alone cannot express every crossing. Do not implement a full 3D scene solely to solve one reference.

Broken panels, rust and attached data tags belong to material-panel IDs. They travel with the ring rather than regenerate in screen coordinates. A complete turn closes a nonuniform ring; a partial turn only closes when all visible material and damage patterns share that symmetry. Otherwise bake a longer cycle or author a controlled hold. The current ring channel can advance three panels per clip; lights may repeat while irregular breaks do not. Test geometry, physical panel identity and illumination separately.

Cloth and cables attach to sockets, with a stationary root and delayed tips. For field scale, a few authored curves and phase offsets usually give more control than an unrestricted cloth simulation. If spring motion is used, deterministic absolute-time evaluation or fixed-step pre-baking is necessary. Damped-spring and fixed-timestep references explain settling and reproducibility [S13,S14]. Random-access export must not depend on whether frame seven was requested before frame two. Warm up stateful simulations and cache a cycle; do not run mutable simulation from a painter called in arbitrary editor order.

Keep broad readable banner/hood folds; damage is part of their mask. Do not animate shading independently from the fabric's silhouette. Avoid global body jitter to sell every failure: hold an arm, pause a ring motor, restart a lens scan, or let a cable settle after a delayed action.

## 6. Pixel-art quality and condition layering

Native procedural painting stays useful, but exact concept fidelity requires intentional silhouettes and selective pixel cleanup. Saint11's cluster method emphasizes coherent masses before small detail [S08]; the tutorial collection includes silhouette, animation, fabric and looping topics [S09]. Recommendation: approve a flat-color family silhouette in four directions, then armor layers, then wear. Dense noise should not compensate for a missing structural design.

Rasterize at the actual native field or battle target with consistent logical coordinates. Preserve subpixel geometry internally; snap using a documented final pixel-center rule. Render attachment and joint positions from the same solved pose, not independently rounded coordinate streams. Preserve the tested old painter for legacy projects.

Disable image smoothing when scaling previews [S12]. This preserves hard pixels but does not prevent topology changes, crawling single pixels, or disappearing narrow panels under rotation. Aseprite documents alternative rotation algorithms [S19]; neither a new resampler nor hard alpha alone guarantees attractive art. For key armor orientations, curate native parts/pose corrections. Avoid multiplying near-identical raster angles that only add shimmer.

Separate structural damage (missing plate, seized joint, replaced limb) from surface condition (rust, chips, scorch, moss). Structural damage affects geometry and potentially motion. Surface marks use stable part-local seed/masks; arbitrary ID renames must not repaint a character. Overgrowth attaches at seams and accumulated surfaces, follows the owning part, and has a readable outer silhouette. Reserve important negative space around knees, hands, tools and ring interiors. Review on light, dark and busy backgrounds at 1× and nearest enlarged size.

Motion symptoms should be bounded, authored and independently selectable from lineage and role. Repetition is an event sequence or held pose, not necessarily violent random displacement. Preserve the game's existing flicker/reduced-effect setting and offer nonflashing expressions of malfunction. W3C's flash criteria are a useful reference for reviewing effects [S20]; this study does not certify accessibility conformance.

## 7. Animation semantics and actions

Separate a clip's role from its literal old UI name. Define capabilities such as locomote, scan, manipulate, strike, ranged attack, charge, stagger, shutdown and recover. A hover family maps locomote to drift; a cartographer maps scan to optic/probe motion; a heavy security unit maps strike to its actual equipped arm. If a drill replaces a hand, a hand-wave clip is unavailable unless adapted and reviewed.

Model an action as anticipation, active/impact, and recovery with explicit duration and events. Locomotion and visual accessory cycles can be layered, but a one-shot defeat must finish and hold rather than restart because the idle loop wraps. Godot's documented separation of animation data, state control, filtered layers and one-shots provides a useful design reference [S15]. We are applying the separation to this JavaScript tool, not migrating the project to Godot.

Use named event times for impact, scan pulse and support contact. Baked frame metadata should preserve durations/holds. An action being listed in a dropdown does not prove it has meaningful channels for the selected machine. Test the actual capabilities before exposing a preset as animation-complete.

## 8. Export, registration, game integration and performance

Keep art size, ground anchor, collision footprint, interaction bounds, effect bounds, and draw-sort point distinct. Palinode's giant ring can overhang its support footprint. A floating unit has a ground projection even when no part touches that point. A tall lantern does not become a tiny tile solely to fit a character slot.

For new exports, record clip/direction/frame rectangles, source size, optional trim offset, ground anchor in source-pixel coordinates, per-frame durations, loop/one-shot behavior, contact/action events, stride metadata and footprint. If trimming is enabled, preserve registration using source dimensions plus trim offsets. Aseprite's slices and JSON export and Pixi's frame/trim/anchor fields demonstrate existing approaches [S10,S11,S16]. A Bearframe metadata anchor is in pixels; adapters must not confuse it with a normalized anchor used by another API.

Replace unbounded horizontal strips with bounded atlas pages or per-clip sheets. A proposed 2048-pixel page target is a conservative engineering choice, not a guarantee of support or performance. Measure the target WebView's actual limits and memory behavior. The current renderer is Canvas 2D; WebGL limit queries are relevant only if a WebGL consumer/adapter is used. WebGL documentation cautions against assuming desktop capabilities or unlimited memory [S17]. Do not claim a Moto G test from a desktop canvas run.

At runtime, load baked images and metadata. Do not perform the per-pixel machine rasterizer for every NPC every frame. Cache compiled poses/atlases by resolved recipe, seed, renderer version and resolution. Keep current/nearby families resident and unload unused battle assets. Avoid decoding every possible generated variant at startup. A 6528×528 RGBA sheet is about 13.15 MiB for base pixels before duplicate canvases, engine copies or any mipmaps; a small compressed PNG does not remove that cost.

The inspected game renderer currently slices the Wraith layout using fixed dimensions and offsets. The new adapter needs metadata lookup, proper ground registration, culling bounds, collision footprint and sorting behavior. Preserve existing Ghost Signal HUD, controls, stealth and four-direction movement. Add a separate test scene with a humanoid, large crawler and floater before connecting content to gameplay. Re-check the engine branch at integration time; this research records a snapshot rather than claiming no adapter exists forever.

## 9. Compatibility and migration

New authoring structure should use an explicit versioned wrapper and compiler; keep project container v2 until a real new schema is needed, then add an intentional migration with fixtures. Do not bump a number without implementing how old data is read. Unknown future versions must fail clearly or open read-only rather than silently discarding fields.

Old rigs stay on the old renderer. New families opt into new controllers. Keep known-good seed recipes and frame hashes pinned to their renderer version. Saving/reopening preserves compiled settings, manually edited cells and overrides. Regenerate-unedited remains the default. A deliberate body-family replacement should show what happens to edits and allow keeping the old project as a separate checkpoint.

Do not add a paid runtime or new external hosted generation service as a hidden dependency. The researched Spine concepts can guide our own data model without importing its runtime. Its repository has specific licensing terms, as does Aseprite source [S21,S22]; these sources were studied, not bundled into this generator. The independent experiment files here are original small mathematical probes.

## 10. Acceptance gates and implementation order

| Stage | Work | Gate before advancing |
|---|---|---|
| 0 — Baseline | Preserve copy branch, original main, existing pixels, saves, edited cells and exports. Add characterization fixtures for findings above. | Old 26/30 suites still pass, and new diagnostics reproduce pinned failures. |
| 1 — Rig safety and registration | Validate graph/IDs/sockets; stable physical IDs; reachable-target policy; explicit root and bounds metadata; clipped-effect classification. | Invalid graphs fail clearly; finite poses and fixed lengths across valid/clamped targets; no unexpected bounds loss. |
| 2 — Assembly contract | Versioned family definitions and compatible modules; explicit views, slots and mirror policy; save resolved recipes. | Deterministic assembly and roundtrip; missing sockets/actions rejected; no silent replacement of hand edits. |
| 3 — One legacy industrial biped | Murmur-inspired unnamed study: hunch, asymmetric tools, corrected feet, restrained malfunction. | Four-direction native silhouette and motion review, contact/occlusion checks, no belly-owned arm pixels. |
| 4 — One crawler | Palinode-inspired six-leg controller, tripod then slower support gait, ring/material identity. | Persistent six-leg identities, continuous contacts, world-motion test, support debug view and bounds. |
| 5 — One orbital core | Oracle-inspired core, independently oriented rings, banners and hover. | Full-depth view review, loop closure, fixed ground anchor and tool/module compatibility. |
| 6 — Suspended/asymmetric families | Vestige/Cathedra-style structural variants and tool actions; extend heavy biped using stage-3 principles. | Authored left/right views, intentional proportions and equipment identity; full action coverage for supported capabilities. |
| 7 — Engine and Android proof | Metadata adapter, paged sheets, mixed-scale scene, collision/sort tests, target-device measurements. | No cropped limbs/rings, stable registration, working touch/controller flow, measured frame time and decoded-memory behavior. |
| 8 — Controlled catalogue expansion | Curated modules/ranges and condition presets within proven family contracts. | Owner visual acceptance of reference variants; regression fixtures for every approved recipe. |

Suggested automated checks: graph validity, finite transforms, socket existence, bone lengths, joint bounds, near/far ID consistency, planted-foot world drift, contact schedules, loop position/velocity continuity, stable ring panel damage, source/trim registration, atlas page limits, save roundtrip, and pixel-exact legacy fixtures. Raster length tolerances should account for final pixel rounding; mathematical tolerances and visual silhouette checks are different tests.

Suggested visual checks: native silhouette, grayscale/value separation, front/back identity, both side views, passing/contact poses, cloth/armor intersections, profile tool identity, weight/anticipation/recovery, and the final in-game composite. For a giant unit, inspect against the actual tile scene. Legibility and canon fidelity need human review; automated geometry is necessary but insufficient.

## 11. Independent experiments and limits

`kinematic-experiments.mjs` is deliberately outside production. Results are in `experiment-results.json`:

- 3,200 analytic-chain probes, including unreachable/near-root targets and both bend signs; maximum segment-length error approximately 5.41e-14 in the tested range.
- 1,200 schedule samples for each of tripod, ripple and wave; expected support counts 3, 4 and 5.
- Body-relative stance cancels the assumed constant root velocity; maximum measured world drift approximately 3.55e-15.
- Join position gap across an epsilon around contact/cycle boundaries below 3.2e-6.
- 310 integer-turn ring-point closure checks.

These experiments establish the stated numerical properties of a small model. They do not establish attractive raster art, joint-angle validity, collision-free motion, static/dynamic physical stability, cloth simulation, device performance, complete animation coverage, or final generator integration. The support-count experiment does not compute a center-of-mass support polygon. A bounded FABRIK or angle-limit prototype remains future work. Keep this record as tested research with **implementation and art acceptance pending**.

## Reproduce

Use Node and the inspected project's installed `@napi-rs/canvas` dependency. The first script reads modules from the explicit project path; it does not write to that checkout.

```sh
node audit-generator.mjs /absolute/path/to/bearframe-ghost-signal generator-audit.json
node kinematic-experiments.mjs experiment-results.json
```

`generator-audit.json` includes the exact audited commit. To reproduce that snapshot, use the isolated generator commit listed above, rather than an evolving engine branch. Native runtime versions are captured in `environment.json`. The optional manifest refresh command is `python make-manifests.py /absolute/path/to/bearframe-ghost-signal`. Full source URLs and the claim-to-source map are in `sources.json`. `integration-plan.json` is the machine-readable handoff.
