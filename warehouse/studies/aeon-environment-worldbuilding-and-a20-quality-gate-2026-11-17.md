# Aeon Circuit: 2D Environment Construction, Worldbuilding, and One-Location Acceptance — Research v1
Date: 2026-11-17 (US Central) | Owner: Bearframe Labs / Atlas Warehouse
Classification: public-safe **research and production methodology**, not source art or campaign canon.
Status: research reviewed against referenced publications; **implementation acceptance requires separate runtime evidence**.

## Why this study exists

Past map assembly overemphasized number of zones, generic tiled floors and decorations and underemphasized the believable functions of spaces, the player's moment-to-moment navigation, readable entrances, collisions, and carefully organized artwork. This study is a practice standard for the **original Aeon Circuit: The Silent Wake** JRPG built on the **existing Ghost Signal engine**. It does not approve an unreviewed story, new map, new mission, or new combat mechanic. Licensed pixels, source gameplay screenshots and unreleased narrative remain owner-private.

## 1. Sources and how to interpret them

**Primary methods**: The Level Design Book distinguishes research -> layout -> blockout -> playtest -> environment art -> lighting; it specifically warns that early art passes make structural mistakes costly to repair. Its research chapter recommends looking at real-world facilities, reference breakdowns and layouts rather than selecting random visual references. Sources:
- https://book.leveldesignbook.com/process/overview
- https://book.leveldesignbook.com/process/preproduction/research
- https://book.leveldesignbook.com/process/layout
- https://book.leveldesignbook.com/process/blockout
- https://book.leveldesignbook.com/process/blockout/massing/composition

**Visual hierarchy**: The Level Design Book and Game Developer agree that landmark hierarchy and material contrast matter; they disagree about whether photographic "leading lines" genuinely direct a player. The Level Design Book argues camera-dependent leading-line screenshots are poor proof and favors playtested wayfinding. Treat photography/composition as art-quality tools, not navigation evidence. Sources:
- https://book.leveldesignbook.com/process/blockout/wayfinding
- https://book.leveldesignbook.com/process/env-art
- https://www.gamedeveloper.com/design/composition-in-level-design
- https://www.gamedeveloper.com/art/applying-the-elements-of-design-and-principles-of-design-in-level-art

**Environment fiction**: The Level Design Book differentiates broad worldbuilding (place and history) from room-scale environmental storytelling (what happened here) and from choreography (what visibly happens now). Worch and Smith's GDC environmental storytelling work argues for environments that let players infer events and systems that respond to agency.
- https://book.leveldesignbook.com/process/preproduction/worldbuilding
- https://book.leveldesignbook.com/process/env-art/storytelling
- https://www.worch.com/2010/03/11/gdc-2010/
- https://www.gdcvault.com/play/1025178/Level-Design-Workshop-Designing-for

**Technical references**: Tiled defines tile/object/image layers, custom object properties, collision geometry, and terrain rules. The terrain brush relies on authored corner/edge/mixed sets and may adjust neighboring tiles; it is not a miracle repair tool for incomplete artwork. Godot documents per-tile collision, navigation and occlusion shapes. Unity's pixel-perfect-camera documentation emphasizes a reference resolution and grid-aligned scaling. These are design references; do **not** replace the existing Ghost Signal engine with Tiled/Godot/Unity.
- https://docs.mapeditor.org/en/latest/manual/layers/
- https://doc.mapeditor.org/en/latest/manual/terrain/
- https://docs.mapeditor.org/en/latest/manual/automapping/
- https://docs.mapeditor.org/en/latest/manual/editing-tilesets/
- https://docs.godotengine.org/en/stable/tutorials/2d/using_tilesets.html
- https://docs.unity.com/en-us/engine/6000.5/manual/unity2d/2d-urp/2d-pixelperfect/prep-sprites

**Process and readability**: GDC 2018 participants emphasize contrast, legible wayfinding and rapid scale-prototype testing; an Uncharted environment-artist interview notes that art must occasionally yield to collision and playable clearance. These principles carry across genres but **exact dimensions and density recommendations below are our own acceptance heuristics**, not statements from those sources.
- https://www.gamedeveloper.com/design/gdc-2018-level-design-workshop-an-expert-roundtable-q-a
- https://www.gamedeveloper.com/design/-i-uncharted-4-i-artist-shares-tips-on-making-your-game-more-readable

## 2. Translate worldbuilding into functional spaces

Before dressing any room, write a "facility causality sheet":
1. Original purpose: why was this structure built; who operated it; what machines need power/cooling/maintenance; where do people enter and exit?
2. Operational logic: utility trunk, power source, conduits, access panels, ventilation, personnel routes, restricted zones and secondary maintenance circulation. Functional paths should connect logically. If two consoles serve a generator, provide visible conduit direction or physically plausible adjacency.
3. Historical timeline: pristine intended operation -> period of deterioration -> present state. Show accumulated damage at seams, under leaks, beneath failed machinery, near doors subject to wear. Do not distribute damage/noise uniformly.
4. Player purpose: what is learned, traversed, unlocked or returned to; what should the player recognize in first 3 seconds, in 10 seconds, and after exploring?
5. Lore constraints: ancient, degraded systems and non-compatible technologies should leave different physical traces. Avoid borrowing unrelated modern patterns purely because a sprite looks cool. A sleeper character is not a Bearframe.
6. Story disclosure rule: static artifacts can imply a past event; explicit plot scenes, collectibles and final explanations must remain tied to approved Director's Cut source. No invented clues masquerading as canon.

Output: one-paragraph room function; two-sentence implied history (non-spoiler); functional relation diagram; restricted story boundary.

## 3. Circulation, affordances and orientation

Separate **diegetic circulation** (why a worker would walk there) from **formal circulation** (what path and gate the player actually uses). Design both. The Level Design Book recommends primary/secondary paths and checks whether fiction supports gameplay:
https://book.leveldesignbook.com/process/layout/flow/circulation

For a tiny overhead 32px game:
- A visually dominant entry should visually suggest an entry: frame, threshold, floor wear, state light; never paste a machine over the threshold.
- A functional room has a main work corridor, recognizable machine/work bay, control station, and controlled exit. Player should infer the flow without reading a debug label.
- Draw an access skeleton before textures: entry -> orientation landmark -> operator station -> sealed passage -> destination -> return. Optional alcoves may be added only if they have a purpose.
- Put useful interactions on the near side of the locked door. Mark the destination as unavailable before unlock by changes in signage, light or physical door state; do not fake gating with invisible walls.
- Keep high-priority walkable channels unobstructed by foreground art and sufficiently wide for actual engine collision bounds. Width must be measured in **this engine**, not guessed from generic tile rules.
- A single minimap/screenshot is not path validation. From multiple spawn/camera states, players must see landmarks and be able to reach all authorized floor tiles.
- Find every room's "why do I need to go there?" before placing a decoration. If there is no answer, delete or merge the zone.

## 4. Visual grammar and material palette

Use the real authored asset packs to define a **small, consistent kit-of-parts**, never a random visual asset lottery.
- Architecture: one coherent wall family, corners, joins, door surround, baseboard and bay separation.
- Floor materials: one dominant traversable material, one narrow circulation/threshold material, one hazardous or service surface. Accent floors should follow facilities or machine footprints, not checkerboard randomness.
- Structural massing: strong wall silhouette and room-to-room partitions before props. Show corners, thresholds, support logic and thickness.
- Detail clusters: group related props into legible workstations (machine + conduit + tool + caution surface). Avoid single unrelated junk items evenly sprinkled every 2-3 tiles. One narrative cluster should suggest cause and effect rather than an arbitrary loot pile.
- Negative space: deliberate clear travel corridors provide breathing room and character visibility; blank floors are fine when used intentionally, but vast unbroken empty rectangles are not.
- Detail hierarchy: **one primary focal system** (e.g. relay bank), at most two nearby secondary landmarks, and low contrast supportive microdetail. The focal element should have a visually distinct footprint or lighting treatment even with the HUD removed.
- Color roles: neutral architectural foundation, restrained damage and dirt, fixed interaction accent color, light/shadow accent for route. Avoid highlights on cosmetic items competing with true interactables.
- Weathering logic: corrosion at wet joints, soot near failed vents, impact marks near breached surfaces, accumulated dirt in dead air corners. Repeating the same damage sprite across every tile looks procedural.
- Keep source pixel dimensions/grid proportions. Don't stretch native 32x32 into a 48px pretending to be authored 48px; crop/compose deterministically on the native grid and preserve alpha.

**World texture problem**: Base texture should tile seamlessly and read at play scale; repeated distinctive panel or rust motifs cause obvious repetition. Prefer continuous authentic tile families; if none exist, concentrate a limited handmade variation atlas in low-contrast regions. No Photoshop-style random noise as substitute for actual material design.
https://book.leveldesignbook.com/process/env-art/texturing

## 5. Layering, collision, depth and pixel integrity

Recommended art/gameplay layers (not a demand to change engine APIs):
1. immutable solid collision and static geometry authored first;
2. floor/background art corresponding to that geometry;
3. architecture/walls/structural decor;
4. lower gameplay props with real obstruction if visually impassable;
5. actors and active doors drawn at correct depth;
6. foreground occluders where actor can move behind;
7. lighting, fog, scanners, dynamic VFX, then Ghost Signal HUD.

Every decorative mass must pass this rule: if it appears solid and occupies the player's movement corridor, **either author matching collision or reposition it**. Never permit walking through a large machine while stopping at an invisible empty floor tile. A door's artwork must align with the exact collision opening and the allowed/blocked state. Verify state change in the running engine. Y-sorting must use actual floor-contact points; keep upper parts of tall props as possible foreground occlusion, not indiscriminate overlay.

Test native pixel format: layer width=tileWidth*mapWidth, layer height=tileHeight*mapHeight, nearest-neighbor scale, integer offsets, no bilinear blur. Use crisp rendering at engine canvas size (not just an upscale PNG).

## 6. Lighting: information first, atmosphere second

The Level Design Book recommends iterative global, wayfinding, encounter/gameplay and detail/mood lighting passes:
https://book.leveldesignbook.com/process/lighting

Apply to 2D Aeon as:
- Global: preserve Ghost Signal's existing ambient darkness, shadow, fog, and lamp pipeline.
- Wayfinding: stable, distinguishable lights at door and relay; don't make every unrelated prop bright.
- Gameplay: doorway thresholds and console labels legible during interaction and VFX.
- Atmosphere: localized low-frequency flicker/steam/sparks on machinery, only if available in source VFX and not visually occluding the player.
- Reliability: power-state changes should have a predictable visual response. Avoid rapid flashing and honor reduced-motion / pause where implemented.
- Mobile first: check the actual 480x270 canvas and landscape phone viewport; overly subtle pixel detail may disappear under HUD and scaled lighting.

## 7. Environmental storytelling without writing unauthorized plot

Write a six-field "physical evidence chain" for each set:
- function (what the equipment was used for);
- failure (what physically went wrong);
- evidence (damage, scattered parts, disconnected cable, maintenance tool);
- consequence (blocked access, leak, sparking coil);
- player affordance (inspect, unlock, detour);
- continuity boundary (what details can be implied vs story facts reserved for approved script).

For the review-only A20 service space, a generic noncanonical chain could be: power service bank -> failed line isolation -> cables rerouted toward a locked bay -> console/indicator signals authorization -> bulkhead opens. This is **QA environmental logic**, not a new approved plot point. Never add a new quest, character, scene, lore revelation, or final encounter as decoration.

## 8. Review workflow: geometry before polish, visual proof before mass rollout

**Pass A / narrative and purpose**: facility role, 3 player actions, one visual hero prop, no canon additions, exact source-asset license check.
**Pass B / topology and scale**: sketch regions, entry/exit relation, gate-side controls, 32px metrics, traversable graph. Reachability must pass sealed, opened and reverse travel.
**Pass C / architecture and palette**: wall silhouettes, thresholds, corridors, floor zones, logical machine placement. No scattered filler.
**Pass D / art and readability**: authentic complete kit parts, purposeful clusters, consistent damage and functional floor transitions; compare normal gameplay snapshots at entry, relay, door, destination and return.
**Pass E / functionality**: tests for actual game movement, pause, camera, collision, dynamic door states, HUD, scanner, lighting, browser load, save/Continue, controls. Automated reachability is necessary but not sufficient.
**Pass F / signoff**: screenshot from original Game renderer in real Chromium; label any simulated/in-memory host clearly. Owner must approve before deploying recipe elsewhere. Emulator and physical Moto G are separate gates.

Proposed measurable heuristics (project-defined **not external industry standards**):
- 100% author-designated walkable floor reachable after unlocking; 0 bypass routes before unlock.
- Every required interaction accessible from allowed side in the relevant state.
- No high-salience visual "blocked" object missing matching collision.
- Every main work bay must contain a recognizable landmark/functional relationship, not just a name.
- At least five real in-engine framing samples: spawn, console, locked/open door, far destination, return.
- Native art layers must match entire grid geometry; intentional occlusion tested from both sides.
- Original input, save and HUD source hashes unchanged in the public repo; licensed assets private.

## 9. Concrete anti-pattern checklist

Reject a room if:
- its purpose cannot be described without referring to game mechanics alone;
- large unrelated props sit in the middle of open rectangles, with no work zones;
- repeated tiny machines are pasted over a uniform floor instead of built into stations;
- walls have no plausible continuity or door surrounds float on top of unrelated sprites;
- "maintenance" implies no access around machinery;
- its intended door is visually overlapped by unrelated scenery;
- the player must guess a collision wall or cannot see the active gate;
- the screenshot looks good but walking/turning the camera reveals clipping;
- material palettes mix native 32px tiles and casually resized oversized art;
- success is claimed from counts of assets/maps/tests without visual signoff.

## 10. World-scale rules when one room is approved

Only after owner signoff, reuse **grammar**, not identical scenery: consistent interaction lighting, door semantics, author-owned pixel resolution, architectural massing and evidence chains. Different spaces should emerge from different functions, ages, failures, pressure/access rules, and histories. Worldbuilding should determine which materials can coexist; weathering follows exposure and maintenance history; traversal follows actual facility operations. Do not promote this review-only A20 layout or fiction to canonical campaign by implication.

## 11. A20 revision task (QA-only; pending review)

- Audit the existing **v7 private A20** room, not new maps; preserve original engine/Ghost Signal UI and approved Sleeper.
- Inventory actual available tiles/sprites and their dimensions. Build a visual asset role table: envelope, floor, doorway, relay, machine bank, damage, trim, console.
- Mark each screen region by functional name on a separate designer-facing blueprint; no more than one primary focal asset.
- Adjust structural layout and art: clear arrival axis, relay/control cluster on accessible side, dedicated power equipment bay, continuous service circulation, framed real airlock; reduce floor repeats and useless scatter.
- Attach collision to visible structures; verify the sealed/open/reverse connectivity properties remain.
- Run existing private 11-test fixture, and add project-specific verifiers for at least three objective measures (door/art alignment, repeated texture density or walk-zone clearance, unintended foreground blockage).
- Record real Game-in-Chromium frame(s) and compare before vs after. If browser route workaround is still needed, label its limitations.
- Keep private sprites, story and rendered owner art OUT of the public GitHub Atlas Warehouse and engine repo.

## Source quality and limits

This is an evidence-backed synthesis of GDC/industry articles, maintained engine/editor manuals and a level-design textbook, with our own project-specific translation. General principles from 3D or other engines are **analogies**, not proof they are implemented in Aeon. The suggested numeric acceptance criteria are local engineering decisions requiring actual playtest validation. Static images never prove collision, camera, saved state or runtime lighting. Research alone does not constitute approved implementation.
