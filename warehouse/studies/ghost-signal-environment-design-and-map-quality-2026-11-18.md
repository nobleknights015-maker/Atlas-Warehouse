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
