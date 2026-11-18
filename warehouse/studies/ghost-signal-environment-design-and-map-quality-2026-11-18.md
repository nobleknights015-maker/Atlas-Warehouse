# Ghost Signal — Level architecture, environmental storytelling and visual quality gate

**Scope:** Standalone Ghost Signal expansion M03–M06. Production methodology reviewed 2026-11-17; archived 2026-11-18 UTC. **State:** research-based guidance; not a declaration of owner visual approval. No paid art is included.

## Key finding
The main failure is **order of operations and spatial coherence**, not asset count. Do not decorate a blank rectangle, scatter purchased props, then attempt to infer a facility from them. A believable gameplay location is organized around occupants, mission purpose, systems, circulation and history. Readability must be judged at the **480×270 game viewport** (about 15×8.4 tiles at 32px), not only a full-map screenshot.

## Mandatory pipeline
1. Freeze engine, M01–M02, controls, UI, original VFX/audio, saves, upgraded sprite generator, existing M03–M06 mission scripts. No M07 until approval.
2. Write a location program: who built/uses the place, physical purpose, function, routes, power, service access, damage, hazards, history and unresolved lore; avoid assigning unknown signal authorship.
3. Draw a **bubble/circulation plan**: main objective path, staff/supply routes, restricted access, landmarks, alternates, spawn/extraction; every room must answer *purpose, cause/history, player action*.
4. Make a native-scale **playable blockout** before art. Test Wraith passage widths, approach tiles, actual door states and M04 escort route.
5. Compose architectural massing from **connected walls, thresholds, room transitions, structural supports and roofs**. A doorway is an intentional opening with continuous joinery, not a machine pasted over the wall.
6. Catalogue licensed sprites by role, native dimensions, footprint, pivot and permissions. Compile only approved game backgrounds in private builds; never publish the owner's raw paid packs.
7. Group medium-scale functional props into logical operating clusters—briefing at command, storage near supply intake, triage by survivor, generator to breaker to gate to antenna. Remove unexplained props.
8. Add directional damage/weather/history only after functions and walls are credible. Show causes and consequences without resolving unverified lore.
9. Render strict layers: terrain, fixed architecture, behind-player fixtures, collision-bearing props, live doors/gates/NPCs/pickups, foreground occlusion, original engine lighting/scan/fog/hazards, HUD.
10. Capture real game frames at spawn, landmark, door, gated transitions, objective and exit, with camera-matched before/after. Inspect original-sized 480×270 and Android landscape HUD.
11. Run Node navigation/mission/save tests, browser gameplay and Android APK; physical Moto G touch/layout/frame-rate test is a separate owner gate. Keep draft PR until actual owner acceptance.

## Object placement contract: build-breaking failures
Maintain a typed registry for all critical entities and art objects: id, type, asset, native width/height, pivot, tile/pixel footprint, collision, visual depth, adjacent wall, game-state-dependent visibility and whether it may be baked. Reserve tiles and approach spaces for doors, terminals, NPCs, evidence, pickups, exit, gates **before** scenery composition.

**Reject art build** when: visual door differs from real traversal; control panel intersects a door aperture/adjacent access clearance; wall art and collision disagree; furniture covers interaction approach; two physical fixtures overlap; multi-tile image is squeezed into 32px; wall joins are disconnected; wires terminate in empty space; background version does not match map geometry; M04 escort fails pathfinding; mission script gate can be bypassed; scenery covers Wraith or HUD.

## Location programs
- **M03 / Director Mira survey outpost:** landing/access → perimeter → exterior field compound → enclosed command/briefing → supply/coupler → survey track → ridge relay. Use outdoor terrain/roads/weather for surface, station art only inside meaningful sheltered modules. Mira accessible in command with no console/door overlap. A service vehicle, power feed, and relay platform must relate physically.
- **M04 / missing survey:** staging → damaged approach → warned hazard → fractured transit/rail → triage/rescue pocket → escorted return. Consistent collapse direction; supports and rubble below damaged structure; medical items clustered; path tested for survivor as well as Wraith.
- **M05 / broken relay:** west access → workshop/spares → breaker/isolation → **physical gate embedded in continuous wall** → utility passage → receiver/antenna. Show power causal chain generator → cable conduit → breaker/gate → transmitter; close/opened doors align with collision.
- **M06 / sealed registry bunker:** entry/order → filter bay → pressure airlock → service hall → observation/breaker → archive → lower passage/receiver → return loop. Six rooms, five actual scripted doors. Avoid visually implying the separate inhabited vault is opened or archive authorship is confirmed.

## Visual review acceptance
Each location needs a coherent silhouette and at least three purposeful subzones (Ghost Signal project criterion), navigable entrances/landmarks, readable foreground/background scale, functional props, distinctive mission material/weather, and a credible history trace. Compare the **same camera positions** before/after. No success claim based only on CI or full-map montage. Environmental artistry and technical correctness require separate gates.

## Sources consulted in original 2026-11-17 research
- Level Design Book: https://book.leveldesignbook.com/process/overview
- Layout, flow and circulation: https://book.leveldesignbook.com/process/layout and https://book.leveldesignbook.com/process/layout/flow/circulation
- Blockout, metrics and wayfinding: https://book.leveldesignbook.com/process/blockout and https://book.leveldesignbook.com/process/blockout/metrics and https://book.leveldesignbook.com/process/blockout/wayfinding
- Environmental storytelling and playtesting: https://book.leveldesignbook.com/process/env-art/storytelling and https://book.leveldesignbook.com/process/blockout/playtesting
- GDC level design workshop: https://www.gamedeveloper.com/design/gdc-2018-level-design-workshop-an-expert-roundtable-q-a
- Hyper Light Drifter 2D world level design: https://www.gamedeveloper.com/design/video-applying-3d-level-design-skills-to-i-hyper-light-drifter-i-s-2d-world
- Environmental storytelling: https://www.gdcvault.com/play/1012647
- Tiled tile/object/image layers: https://docs.mapeditor.org/en/latest/manual/layers/
- Tiled connecting tiles: https://docs.mapeditor.org/en/latest/manual/terrain/
- Heart Machine visual approach: https://blog.playstation.com/archive/2014/03/14/closer-look-hyper-light-drifter-coming-soon-ps4-ps-vita/

**Research limitations:** GDC talk descriptions were available but large slide decks were not fully inspected. The Ghost Signal user screenshots support visual critique; full physical-device QA and final art acceptance remain open.


## Implemented engineering lessons from the next Ghost Signal QA round

**Observed root cause, not merely an art preference:** the owner-only scene compiler had **two methods named `field_architecture`**; the later method silently shadowed the revised authored pass. This is why repeated structural edits were not reliably reflected in screenshots. Consolidate to **one** architecture authoring pass and test its output, never duplicate method names.

**Specific M03 terminal/door error:** an open double-door art sprite was drawn as static scenery and then overlaid by a large bridge display. The revised private compiler excludes that unbound doorway, forbids any live-looking door sprite without a registered scripted door, protects NPC/terminal/door footprints from major art fixtures and rejects stacked duplicate station name signs. A live door's collision, animation and visual frame stay owned by the original engine.

**Reusable public QA gate implemented:** `nobleknights015-maker/bearframe-ghost-signal`, development branch `feature/ghost-signal-expanded-m03-surface-20261117`, commit `61d90976e023565dbac36aa469d223109356f54d`. Added:
- `frontend/quality/ghost-signal-map-program.json` with operational floor-plan purpose, histories, links and anchors for M03–M06.
- `frontend/tools/map-quality-gate.mjs`: mission zone/door/interaction audit, reserved gameplay footprints, owner-art no-overlap manifest checks and SHA-256 scene signatures derived from **real collision grid, props and entities**. Scene dimensions alone no longer establish freshness.
- `frontend/tests/ghost-signal-map-quality-gate.test.mjs`: injected failures for false door art, object over Mira/terminal, oversize sprite footprint, stale scene revision and collision/art mismatch.
- GitHub Actions expansion and Android workflows now run the gate before treating builds as valid.

**Verification scope:** 38 local Node mission/map tests passed; four private scene composition audits passed for 532/679/673/552 original-size placements at that checkpoint; owner-only Android APK v2/v3 signing and embedded map/module hashes verified. [GitHub public regression run](https://github.com/nobleknights015-maker/bearframe-ghost-signal/actions/runs/44225489012) passed. Actual in-engine Canvas2D same-camera before/after frames exist; **full Android physical touch/landscape, HUD screenshots and owner visual approval still pending**. The proprietary flattened art and compiler remain owner-side, not public Warehouse stock. No new missions or engine rewrites.


## Cross-reference policy: Work chat two-game research + Ghost Signal production

**November 18, 2026 production round.** The Work chat's [comprehensive two-game research](https://github.com/nobleknights015-maker/Atlas-Warehouse/blob/main/warehouse/studies/bearframe-two-game-design-research-2026-11-17.md) is now an explicit **independent methodological cross-check** for Ghost Signal Expanded M03–M06. It does not override the approved Ghost Signal handoff, original engine, direct mission scripts or private canon; it is also **not** Aeon Circuit design authority for this game. Research proposals are not shipped features.

**Per-round source order and accountability:** verify live GitHub branch/CI and original M01–M02; read Ghost Signal approved handoff and exact mission scripts; check this Ghost Signal spatial/art study; cross-reference Work handbook sections 01 (world/maps), 02 (Ghost Signal), 04 (events), 05 (presentation), 06 (verification) and 07 (G01–G03 cards); then plan only existing M03–M06 work. Preserve names, story uncertainty, generator, saves, input, UI and engine. Put testable constraints into the map program and CI, then collect real in-game evidence.

**Work-study-derived acceptance cases:**
- **G01 M03:** one playable 480×270 arrival camera identifies Mira and command purpose; legitimate and reachable supply/ridge choices; distinguish exterior apron from sealed interior; view with HUD and original VFX.
- **G02 M04:** test Wraith and survivor outbound/return through the triage facility and hazard states; meaningful cues for damage/medical support and no rescue blockage.
- **G03 M05:** actual closed/open physical gate, breaker approach, transmitter access, save/reload and causal wire/power layout.
- **G03 M06:** all five real doors, pre/post gate stages, archive provenance unknown, receive-only route and west service return.
- **Art-to-runtime parity:** compile native art against exact `mission.buildMap()`, reserved scripted objects and digest; reject fake door paintings, oversized sprite placement, blocked interaction, private licensed raw asset leakage. Signed APK must embed four exact code+scene pairs. Node, browser Chromium, emulator and physical Moto G evidence are *distinct* review levels.

**Implemented and currently verified:** Public Ghost Signal draft development branch commit `d62252956e341e1109027ecdb384864ebb9536aa`, PR #27, adds `frontend/quality/ghost-signal-research-crossref.json` and `frontend/tests/ghost-signal-research-crossref.test.mjs`; narrows the M03 command aperture from six to three 32px cells while retaining mission entities. **43/43 focused local Node tests passed;** [new CI regression passed](https://github.com/nobleknights015-maker/bearframe-ghost-signal/actions/runs/44227845489). Private owner-side compiled scene art was re-authored to distinguish the command room, exterior briefing apron, storage and relay and includes grouped triage equipment. Four scene manifests passed placed-art audits; private Android QA package was signed v2/v3 and hashes verified. The Chromium local host failed due administrator network block, so do not claim a private-art full-browser or phone-HUD capture. Production Game.render() was exercised through Skia Canvas2D, not a physical Moto G.

**Outstanding:** owner inspection, complete browser/UI/mobile comparison with licensed art, physical Android touch/controller, save/continue across objective stages, and production-quality environmental storytelling. Keep the PR draft and stop adding missions. If a later round changes map geometry, regenerate private scenery and rerun all gates; a green test alone never confers visual approval.


## Bolt review cross-check: M05 electrical hazard rendering (verified round)

**Date:** November 18, 2026 UTC; Ghost Signal EXPANDED only, PR #27 draft. Bolt’s read-only source review had five observations; verify each against live source, not the review prose.

1. **Reject as false:** Licensed game backgrounds *are drawn*: the M03–M06 `Game.start` callback assigns a dimension-checked owner-side PNG to `this.base`, which the unchanged `Game.render` draws directly. Do not add duplicate layering over the original Ghost Signal renderer.
2. **Reject as false:** M04 escort-trail reset already happens in `Game.start` and `Game.applySnap`. Do not alter save/recovery without reproducing a distinct issue.
3. **Reject as false:** Existing quality suites and GitHub CI cover structure, stage gates, mission scripts and browser smoke. Extend these tests for a specific regression, rather than duplicating harnesses.
4. **Verified/fixed:** M05 electrical `arcA/B/C` were using the same `type:'jet'` gray steam pixels as M02. [Public development commit `83e6bcf`](https://github.com/nobleknights015-maker/bearframe-ghost-signal/commit/83e6bcf8a507123d92475f3799de1bd55a71078a) adds a scoped visual-only electrical arc renderer with fixed idle, amber warning, and cyan-white active frames; lowFx retains the bright active cue without extra spark motes. The underlying 3.5-second `jetState`, actual damage, save state, Wraith, controls, UI and base M01/M02 steam remain unchanged. Added five focused tests, combined 48/48 local focused mission/map/FX tests passed; [GitHub regression](https://github.com/nobleknights015-maker/bearframe-ghost-signal/actions/runs/44235622946) passed.
5. **Still needs art direction:** M05/M06 functionally similar spaces. Private owner art compiler now draws a continuous relay power bus connected to three hazard branches and a restrained archive circulation line, using privately packaged licensed game backgrounds. No standalone paid pack files in GitHub. Four private map scene digests align to exact collision geometry and owner-art placement manifests were checked; this is not final visual sign-off.

**QA levels:** A locally signed private Android QA APK has v2/v3 signature verification and original M01/M02 / game/save/studio integrity checks. Actual production Ghost Signal modules with a full HUD and licensed backgrounds were inspected in headless Chromium via an *in-memory module-loading harness*, because navigation to localhost or file URLs is restricted. This is real browser Canvas2D rendering, **not ordinary hosted Chrome integration, emulator install, or physical Moto G evidence**. Continue validating the latter independently. Keep PR #27 draft and art pending.
