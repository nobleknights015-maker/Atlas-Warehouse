# Starbound Frontier — Bedrock Worldbuilding Research (2026-11-23)

Public-safe study. Based on the user's private local pack inspection, but no paid pack assets or proprietary binary contents are stored here. Claims in the source retain [PACK], [DOC], [DESIGN], [TEST] labels.

STARBOUND FRONTIER — DEEP RESEARCH & PRODUCTION REFERENCE
Version 1.0 | 2026-11-23
Purpose: Build a cohesive Minecraft Bedrock sci-fi survival add-on compatible with the user-provided Star Odyssey: Beyond Space resource pack. Preserve the core Minecraft loop while making different worlds feel like distinct alien ecosystems. This report is research and production guidance, not a claim of implemented features.

EVIDENCE LABELS
[PACK] Directly inspected in the uploaded .mcpack archive (bbc730fb4d9311a9737b6f49667b4f55.mcpack).
[DOC] Supported by official Minecraft Bedrock creator documentation (links in Sources).
[DESIGN] Our recommendation/inference; not a fact about Star Odyssey or an existing implementation.
[TEST] Requires validation in a real Bedrock world and, when applicable, on Nintendo Switch/Realms.

1. EXECUTIVE FINDINGS
[PACK] This archive contains 3,459 ZIP entries, including 1,244 files under textures/blocks, 652 under textures/items, 434 under textures/entity, 94 under models/entity, 53 under entity, 30 under animations, 9 animation-controller files, 7 render-controller files, 24 fog files, 490 under sounds, and 9 particle files. Manifest version [1,0,50], minimum engine version [1,20,30], type 'resources'; no conventional behavior module in this archive. Several files reveal previous or modified attribution ('Panda's Community') while music credits refer to Odd Block. This does not establish licensing provenance or permission to redistribute.
[PACK] A sample of 1,244 block PNGs found 1,095 at exactly 16×16 pixels; other files include animation strips and higher resolution assets. Thus 16×16 is a robust baseline for matching existing terrain/block material styles, NOT a universal requirement for every model atlas.
[PACK] Directly inspected examples: stone (muted rocky texture), dirt, grassy surface, sand, red_sand (vivid mineral green), iron_block (silver machine-panel appearance), diamond_block (dark blue circular electronic element), redstone_lamp_on (bright cyan strips), furnace_front_on (elongated machine-like animation strip), crafting_table_front (illuminated small machine/control face), stonebrick (manufactured modular wall), glass (dark industrial frame), chest_front (detailed mechanical container), barrel_side (blue segmented metal), sea_lantern (emissive cool technical light), warped_planks (blue paneling), crimson_planks (red paneling), sculk (green circuitry-like organics), shroomlight (bright organic red). These observations are of the provided archive, not screenshots of the live game.
[PACK] biomes_client.json configures biome-specific water and fog colors: e.g., default cyan water (#57a6ba), mangrove swamp green water (#40ae89), jungle yellow-green water (#d6c71b), bamboo jungle cyan (#14A2C5). 24 fog-definition files exist, including desert, forest, icy, jungle, swamp and mesa variations. There are 41 music files under sounds/music and extensive mob sound replacements. Sound and atmosphere are already part of the pack's visual/audio identity.
[DESIGN] The right core promise: 'It is still Minecraft, but you are surviving and building on an alien planet.' Preserve open-ended harvesting, crafting, shelter, farming, mining, combat, villager-like trading, exploration, redstone, construction, and multiplayer.
[DESIGN] The five worlds should vary in terrain, weather/fog, flora, fauna, settlement architecture, resources, ambient audio, hazards, and player activities, while sharing a coherent art bible and recipe grammar.

2. RESOURCE PACK INTEGRATION / ART BIBLE
[PACK] Existing pack replaces many vanilla textures and client-side models. Consequently do not casually replace default vanilla filenames in our add-on; namespace originals as starbound:* and use distinct geometry/animation/render identifiers.
[DESIGN] Three material families: A. lived-in industrial (desaturated graphite, silver, navy, cyan status lights); B. hostile mineral (rust, purple/green crystal, scorched stone, contrasting hazard orange); C. xenobiological (subdued plant tissue with localized luminous spores, teal or warm coral accents). Common block-size pixel density approximates sampled 16×16 block materials; atlas sizes for moving robots may be larger provided pixel clusters and outline language remain compatible.
[DESIGN] Color allocation: 70% functional base material, 20% structural secondary, 10% emissive/identity accents (a design guide, not an exact color histogram). Accent lights signal states: cyan available, amber caution, red dangerous, muted gray inactive. Different factions can vary shape and panel arrangement rather than using color alone.
[DESIGN] Treat visible lighting as a gameplay language, not gratuitous glow. A generator has active/inactive vent animation, a refinery has input/output visual stages, a charged tool communicates battery level, a hostile robot telegraphs charging before firing.
[DESIGN] Model texture strategies: texture pixel clusters should imply bolts, hinges, gaskets, recesses, scratches, and depth. Geometry is reserved for silhouette-changing components (elbows, helmets, chest assemblies, thrusters, antennae, manipulators) rather than hundreds of cubes for micro-detail. Test all assets at ordinary gameplay camera distance and Minecraft default FOV before closeups.
[TEST] Verify actual pack stacking and 3D armor attachables with each player character variant. Confirm original client entities do not cause model/controller conflicts. Test with and without Star Odyssey active; add-on remains functional even if less visually harmonized without it.

3. MINECRAFT GAMEPLAY PRESERVATION: NON-NEGOTIABLES
[DESIGN] First five minutes: spawn, obtain timber/organic structural material, gather stones, craft shelter/tools, encounter passive wildlife, discover mineable mineral. No mandatory narrative gate or forced suit-meter tutorial.
[DESIGN] Keep breaking/placing blocks, standard crafting, furnaces, crops, beds, chests, redstone, conventional survival health/hunger, caves and player-driven building. Sci-fi machinery is optional progression that improves efficiency rather than making vanilla crafting obsolete.
[DESIGN] Equivalent but distinct interactions: alien tree log behaves like log; alien plank/stem works in construction; novel crystal ore is mined with a recognizable pickaxe tier; alien crop grows in stages and provides food/crafting reagents; robotic guard is understandable like a hostile mob but with different telegraphs.
[DESIGN] Progression should branch: builders get decorative blocks and modular furniture, explorers gain scanners and maps, miners get processing, adventurers get mobility and defenses, traders gain reputation optional perks. No single required story campaign.
[DESIGN] Each planet gets basic shelter/food/fuel options; avoid arriving on a barren world where players cannot survive except by carrying a late-game inventory from elsewhere. Some environments are deliberately advanced but provide emergency scavenging routes.

4. WORLD IDENTITY MATRIX — EACH WORLD MUST DIFFER IN AT LEAST SEVEN WAYS
[DESIGN] For every planet/region define (1) silhouette/landform, (2) surface materials, (3) vegetation geometry, (4) fauna movement/ecology, (5) water/sky/fog, (6) hazard, (7) settlement architecture, (8) resource loops, (9) audio, (10) player motivation.

ASTRA PRIME — TEMPERATE FRONTIER (starting world)
Landform: broad rolling hills, eroded mesas, lakes and caves. Palette: charcoal stone, silver metal ruins, cyan water, muted teal grass, selective amber tech. Flora: canopied luminous-leaf alien trees, branching root clusters, edible growths. Fauna: docile six-limbed grazers, burrowing scavengers, nocturnal stalkers. Architecture: prefab colony walls with visible repair patches, modular homes, greenhouses, solar/thermal generators. Gameplay: vanilla-equivalent survival, first settlement trading, first scanner and ore processing; discoveries: old survey posts, crash debris. Audio: wind through mechanical remnants + recognizable animal calls. Risk: nocturnal pack hunters, localized abandoned machinery. This world teaches the basic design grammar.

CINDER — ARID INDUSTRIAL WORLD
Landform: basalt escarpments, wide dry basins, deep mine ravines, slag fields; sparse plants. Palette: oxidized orange/brown, dark steel, sulphur yellow, limited cyan. Flora: thorny mineral-rooted shrubs and heat-resistant tube plants. Fauna: heat-adapted plated scavengers and burrowing ambush predators. Architecture: low bunkers, shaded loading yards, mine heads, overhead cable crossings. Gameplay: high-grade metallurgy, salvage, cooler management in extreme zones, rover traversal, excavating ore veins. Audio: dusty wind, rattling scrap, distant machinery. Danger: collapsing mine machinery, turret remnants, dust events. Ensure hazards are region/weather based rather than constant meter punishment.

NIVALIS — GLACIAL SCIENCE WORLD
Landform: ice shelves, crevasses, frozen lakes, blue subterranean crystal caves. Palette: blue-gray, desaturated white, cool violet/cyan emissives. Flora: frost-lichen and low geothermal blooms. Fauna: thick-shelled aquatic grazers, sub-ice predators, neutral cave illuminators. Architecture: insulated compact labs, thermal vents, pressure corridors, tunnels. Gameplay: thermal shelters, crystal research, underwater/sub-ice expeditions, heat/electrical engineering. Audio: muffled wind, ice stress, distant resonance. Danger: poor visibility, thin ice in designated safe-to-simulate areas, predators at heat sources. Permit ordinary Minecraft movement/building.

VERDANTIS — XENOBIOLOGICAL FOREST
Landform: thick canopy, rooted plateaus, marshy lowlands, enormous fungal trunks, vertical vines. Palette: deep forest green, teal, indigo, luminous warm coral. Flora: spore pods, giant tree roots, flowering ferns, climbable vines. Fauna: aerial gliders, camouflage herbivores, ambush predators, symbiotic insect analogues. Architecture: elevated walkways, lightweight bio-composite dwellings, nutrient stations, living-light panels. Gameplay: farming unique species, botanical crafting, wildlife taming, canopy exploration and trade. Audio: layered insect-like calls, clicks and water, reactive rain. Danger: toxic spore pockets, camouflage predators, flooded sinkholes. Visually organic, never randomly sprinkle sci-fi consoles in trees.

SHATTERED MOON — ANCIENT MACHINE-HAUNTED WORLD
Landform: fractured crater plains, exposed tunnels, floating visual debris sparingly, vast hollow ruins. Palette: near-black basalt, pale dust, metallic gray, purple and red caution lights. Flora: minimal; remnants of synthetic growth. Fauna: mostly autonomous sentries, rare scavenger organisms. Architecture: deeply buried rings, modular ribbed corridors, machine halls, clear navigation loops. Gameplay: endgame salvage, environmental puzzles, tough guardians, rare blueprints. Audio: windless ambience, machinery hum, distant signal pulses. Danger: dormant defenses and localized gravity/energy zones; no nonstop lethal environmental damage. Even here, player blocks can be placed/mined except clearly justified protected puzzle components.

5. TERRAIN, BIOMES AND NATURAL GENERATION
[DOC] Bedrock supports behavior-pack features and feature_rules to distribute plants, ores, and features; structure_template placement and more advanced jigsaw structure systems are documented. Microsoft's Jigsaw documentation describes pools, connectors, and structure sets, including village-style assembly. See Sources.
[DOC] 1.26.30 updated biome terrain surface builders; 1.26.50 graduated custom dimension JSON from experimental; 1.26.50 introduced additional experimental options for custom heights. Stable feature != complete five-planet auto-generation: still validate rules, terrain, destination handling, block palettes, client support, and retention in a live build.
[DESIGN] Recommended plan: First make ONE richly populated alien Overworld with regional differences. Then prototype ONE additional custom dimension with a standard height range and starter terrain, structure rules, fauna and return portal. Grow beyond two only after validation.
[DESIGN] Rule-driven structure sets: multi-building frontier villages assembled from themed pools; mining outposts with shaft access and ore logic; crash sites fitted to open terrain; scientific labs with complete floorplans; rare precursor ruins, preferring cave/mountain conditions. Each piece must have entrance clearance, valid foundation/support, navigation, and no door-terminal collisions.
[DESIGN] Placement logic: distinct frequency bands per structure type, biome/height/slope suitability, bounding boxes/spacing/avoid-overlap, rare landmark cooldown, access paths. Do not force structure spawns in every chunk.
[DESIGN] Decorate in meaningful spatial bands: distant silhouette -> major structure/landform -> accessible routes -> resource clusters -> small set dressing. Avoid noise-driven random material patches, arbitrary crates, and props pasted over functional doors.
[TEST] Generate multiple different seeds with same configuration, test 1,000+ chunks when computationally available, confirm spawn rarity and biome suitability. Inspect maps manually at ground level (not just overhead) and test survival traversal, mining, and farming.

6. PLAYER CHARACTER AND NPC MODEL DESIGN
[DESIGN] Preserve standard player skeleton/equipment usability and Star Odyssey player visuals unless users explicitly request a custom player model. New NPCs should read as Minecraft-height humanoids in the block world, not miniature cartoons or giant action figures; use 16-pixel-ish material language, not a photorealistic mismatch.
[DESIGN] Anthropomorphic player-like robots: ~1.7–2.2 block tall for common civilian frames, narrower shoulders for researchers and broad protective armor for security types; height is a design guide, not engine pixel units. Distinct heads with practical optics, side sensor/ear modules, joint pivots, articulated elbows and knees, and recognizable work equipment.
[DESIGN] Four occupation archetypes: ENGINEER (visor + tool harness, repair/inspect loops), SURVEYOR (foldout scanner, maps, binocular behavior), TRADER (satchel, market-stall loop, inventory/trades), GUARD (armor/weapon silhouette, patrol-alert-attack). More variants should reuse rigs and texture/material atlases while altering meaningful silhouette components.
[DESIGN] Each NPC needs a daily role and a home/work anchor. Low-cost AI: schedule idle -> walk to workplace -> perform short work animation -> trade/interaction -> rest. Prioritize active settlement simulation near players; freeze or abstract faraway activity.
[DESIGN] Civilian robots are friendly/neutral until provoked; hostile factions convey allegiance through consistent optics, color, signage, and sound. Faction identity through architecture and utility: industrial faction uses functional hazard striping and heavy loaders; explorers use portable white/navy composite shells; ancient machines use worn layered geometric structures.
[DOC] Bedrock custom entities combine behavior definition, client entity, geometry, materials, textures, animations and controllers; render controllers can change visuals based on entity state. Use modular well-namespaced identifiers and animation-driven state matching.
[TEST] Validate 1st/3rd-person scale, hitboxes, pathfinding around doors, beds, water and slopes, equipment grip positions, walking cycles, right/left mirroring if applicable, despawn/persistence, collisions and multi-owner interactions.

7. ALIEN CREATURES AND ENEMIES
[DESIGN] Creatures should be ecologically legible: specify habitat, diet/resource need, time of activity, movement, behavior, player interaction, useful drops and danger communication before model production. Not every new mob should be hostile.
[DESIGN] Starter ecosystem example: ASTRA grazer (passive herd, fiber drop, grass feeding); root crawler (neutral scavenger, digs at night, defensive when crowded); dusk stalker (hostile ambush predator, flees bright light); maintenance drone (neutral in powered settlements, hostile if damaged) — four mobs with distinct niches.
[DESIGN] CINDER: plated burrower, dust skitter, rogue survey drone; NIVALIS: ice-shelf swimmer, thermal vent crawler, dormant defense drone; VERDANTIS: canopy glider, spore feeder, vine ambusher; SHATTERED MOON: crawler sentry, shielded survey orb, heavy relic guardian. Production can reuse underlying rigs selectively but cannot substitute pure recolors for mechanical differences.
[DESIGN] Combat quality ladder: silhouette recognition (what is it?), telegraph (what will it do?), counterplay (how do I react?), arena affordance (terrain/cover), readable hit reaction, distinct loot/utility, scaling via mechanics rather than HP inflation.
[DESIGN] Examples: a sentry laser paints a narrow warning line before firing; a tunneler makes surface dust/vibration before emergence; a shielded robot opens its core during cooldown; a glider descends only at low light. Avoid instant invisible hits and unavoidable stun loops.
[DESIGN] Mob spawn matrix by world/biome/time/light/proximity to settlements; limit densities, keep vanilla-style passive/hostile balance, and avoid cluttering every chunk. Use common/uncommon/rare tiers. Preserve nighttime surprise and quiet daylight spaces.
[TEST] Behavior tests for pathfinding, invulnerability exploits, damage sources, retreat, target acquisition and drops; check player difficulty settings, multiplayer targeting and low-end hardware entity budgets.

8. SCI-FI INDUSTRY, FARMING, TRAVEL AND BUILDING
[DESIGN] Machines are made of actual placeable blocks/structured multi-block assemblies; recipe chains remain learnable (raw ore -> processed component -> crafted upgrade). Every new block should have clear player break/place rules, drops and recipe path.
[DESIGN] Starter machines: generator -> battery -> fabricator/refinery. Redstone integration where possible. Optional advanced fabrication should not make stone furnaces, chests, crafting tables and crops useless.
[DESIGN] Power network implementation: chunk-aware adjacency graph, capped breadth-first changes, cache connected components, only reevaluate on placement/break, tick actual production at interval, persist inventories/energy. Keep interfaces physically legible with powered/unpowered states.
[DESIGN] A rover should increase exploration range, not replace Minecraft travel. Preserve foot travel, boats, minecarts and exploration hazards. Future spacecraft should deliver players to biome/dimension destinations; only implement fully free-flight once navigation/collision saves are solved.
[DESIGN] Farming across worlds: each planet gets renewable crops, moisture/light/temperature rules simple enough for players to learn, food crafting and decorative options. Allow greenhouse growth or transported saplings to help colonies feel customizable.
[DESIGN] Basic new-world survival resources should include: a plant-based building material, a stone-like material, at least one edible/renewable food source, and an early source of light. Players should not require a spaceship to import everything after arriving.

9. SOUND, ATMOSPHERE AND VISUAL DIFFERENTIATION
[PACK] Existing archive has 24 fog files and biome-specific water/fog configuration, 490 sound files including extensive entity/mob replacements and 41 music files. These are built-in references; do not bundle originals into distributable new add-on without permissions.
[DESIGN] Each planet needs a four-layer ambient profile: background bed (wind/ocean), foreground wildlife calls, rare environmental cues, location-specific machine hum. Silence and quieter sections matter as much as music.
[DESIGN] Planet signature distances: Astra has warm/cyan lakes and distant colony lights; Cinder has low orange haze with distinct red silhouettes; Nivalis has low-saturation blue fog and polar reflective surfaces; Verdantis has warm humid haze and glowing lowland vegetation; Shattered Moon has sparse atmospherics with sharp long-range geometric shapes.
[DESIGN] Keep readability: maintain adequate contrast for ore outlines, mobs on terrain, interactive doors, night visibility and buildable surfaces. Colorblind cues must supplement colored lights with icon/shape/motion.
[TEST] Observe in rain, clear, morning, night, caves, Nether/End if modified, and with Star Odyssey pack enabled at intended stack priority.

10. STRUCTURE AND SETTLEMENT WORLD-BUILDING GRAMMAR
[DESIGN] The starting village should be assembled from (A) a town center/trade node, (B) housing, (C) farm/food production, (D) workstation district, (E) defenses, (F) roads, and (G) utility links. Each building visibly supports a villager/robot occupation.
[DESIGN] Settlement density: village squares encourage walking; roads trace terrain rather than straight grid everywhere; powered areas have cables/generators; industrial areas have loading paths and storage; homes have doors, beds, furnishing and lighting; farms have water/nutrients and crop access.
[DESIGN] Structures should be usable and upgradeable by players. Make construction materials obtainable, avoid unbreakable scenery outside special puzzle nodes, and preserve typical survival access to crafting/trading/looting.
[DESIGN] Create structure kits with geometric constraints (door clearance 2+ blocks, route walkability, foundations, no lava spill, chest accessibility, player spawn clearance), thematic kit rules (outer wall materials, roofs, windows, floor), and rare modules (tower, greenhouse, hangar). Follow Minecraft's 'readable village' hierarchy.
[TEST] On 10+ seeds: inspect village footprints, cliff overlap, water clipping, path continuity and combat navigation. Test NPC schedules in naturally generated instances and player-modified village states.

11. DATA/TECHNICAL ARCHITECTURE
[DOC] Use behavior pack for custom blocks/entities/items/worldgen/scripts and separate resource pack for original art. Create namespaced assets. Follow cooperative add-on guidelines to avoid overriding vanilla identifiers and resource conflicts.
[DOC] Current Bedrock creator docs document custom dimensions JSON and current scripting modules. Version pinning matters; identify exact minimum game version, stable Script API dependencies, and any experiments before coding. Not all documentation features are guaranteed to work identically in Realms or on Switch.
[DESIGN] Suggested project layout:
behavior_packs/starbound_frontier_BP/{manifest.json,entities,spawn_rules,blocks,items,recipes,loot_tables,features,feature_rules,structures,worldgen,dimensions,scripts}
resource_packs/starbound_frontier_RP/{manifest.json,entity,models/entity,textures,animations,animation_controllers,render_controllers,particles,sounds,texts}
project_docs/{STYLE_GUIDE,PLANET_MATRIX,ENTITY_BIBLE,WORLDGEN_RULES,COMPATIBILITY_MATRIX,QA,CONTINUITY_HANDOFF}.md
[DESIGN] Content data should be table-driven: biome profile -> blocks/features -> spawn tables -> structure pools -> loot -> trades -> story events. Avoid per-planet copy-pasted code with small differences; centralize variants and common functions.
[DESIGN] Save/world state: identity of NPCs, home anchors, trades/reputation, machine energy, mission states, player discoveries, travel return points; guard against repeated spawns, duplicate loot and deadlocks.
[TEST] Baseline diagnostic builds: run JSON parse/schema, broken reference scan, missing texture/model references, duplicate identifiers, animations targeting absent bones, loot recipes, structure bounding volumes, creation of .mcaddon, in-game smoke tests. Profile worst-case loaded settlement with several players and vehicles. Claims of compatibility need a test record, not inference.

12. PRODUCTION ART PIPELINE
[DESIGN] Before modeling, create one-page art briefs for categories: civilian android, combat machine, alien herbivore, predator, generator, rover, settlement kit. Briefs include concept silhouettes, 3–5 reference materials, pixel dimensions, palette, bone rig, required animations, interactions, in-world scale, and performance budget.
[DESIGN] Implement four-angle review for important creatures/vehicles; screenshot at 1× game scale; A/B evaluate against Star Odyssey terrain; tweak geometry before polishing texture. Check walk cycles for foot sliding, joint disconnection, off-axis faces, idle stillness, weapons clipping, death frames.
[DESIGN] Keep species readable through primary shape before adding texture detail. For a peaceful grazer, a low broad torso and steady gait; for hostile hunter, forward-leaning limbs and punctuated attack telegraph; for a guard bot, heavy chest/shoulder armor and stable planted feet.
[DESIGN] Add animation state diagrams: idle -> walk -> work -> react -> recover for civilians; idle -> alert -> windup -> fire/strike -> cooldown -> retreat for enemies. Audio/particles synchronize to exact action keyframes.

13. DEVELOPMENT PRIORITIES — MOST IMPACT PER HOUR
P0. Reality check: Test compatibility of existing resource pack and current add-on in Minecraft Bedrock; audit existing Work project instead of rebuilding.
P1. Single living Astra frontier region with 2 contrasting biomes, two natural structure types, 3 useful alien mobs, one village archetype and a coherent progression from stone to a generator. This proves 'Minecraft but alien.'
P2. Finish an art-quality benchmark set: one civilian NPC, one hostile robot, one peaceful alien creature, one machine, one rover, one naturally generated settlement; screen review against pack.
P3. Add village schedules/trades, procedurally placed ruins, drop tables, exploration rewards, farming loop, and atmospheric sound.
P4. Add industrial chain + rover + cooperative multiplayer QA and world persistence.
P5. Prototype Cinder as second region/dimension with unique materials, hazard and architecture; demonstrate it is mechanically distinct, not a recolor.
P6. Expand other planets in the same way; no empty mass-generated planets.

14. ACCEPTANCE CHECKLIST
- New world loads with resource pack and add-on, no content errors or broken visuals.
- First 10 minutes are survivable using familiar Minecraft mechanics.
- New blocks can be mined/placed and fit pixel density.
- Structures spawn in suitable places on new chunks, not every chunk, with accessible entrances and pathways.
- NPCs actually trade/work/return home; roles are visible.
- Mobs have distinct behaviors, hitboxes, drops, and natural spawn conditions.
- Each planet has identifiable terrain, flora, fauna, settlements, ambient sound, risk, and gameplay reward.
- Machines actually process resources/power and survive reloads.
- Draw distance, low-end phone and Switch/Realms scenarios documented rather than assumed.
- All screenshot evidence comes from the actual running game, not concept art.
- Copy of third-party Star Odyssey resources is not bundled into distributable pack.

15. SOURCES — PRIMARY TECHNICAL REFERENCES
Official Minecraft Creator World Generation: https://learn.microsoft.com/en-us/minecraft/creator/documents/world-generation?view=minecraft-bedrock-stable
Official Jigsaw Structures: https://learn.microsoft.com/en-us/minecraft/creator/documents/structures/introductiontojigsawstructures?view=minecraft-bedrock-stable
Official Feature Rules: https://learn.microsoft.com/en-us/minecraft/creator/reference/content/featurerulesreference/examples/featurerulescomponents/feature_rules_document?view=minecraft-bedrock-stable
Official Custom Dimensions Tutorial: https://learn.microsoft.com/en-us/minecraft/creator/documents/scripting/custom-dimension-api-tutorial?view=minecraft-bedrock-stable
Official 1.26.50 Creator Changelog: https://learn.microsoft.com/en-us/minecraft/creator/documents/update1.26.50?view=minecraft-bedrock-stable
Official 1.26.30 Creator Changelog: https://learn.microsoft.com/en-us/minecraft/creator/documents/update1.26.30?view=minecraft-bedrock-stable
Official Entity Modeling/Animation: https://learn.microsoft.com/en-us/minecraft/creator/documents/entitymodelingandanimation?view=minecraft-bedrock-stable
Official Animation Overview: https://learn.microsoft.com/en-us/minecraft/creator/documents/animations/animationsoverview
Official Render Controllers: https://learn.microsoft.com/en-us/minecraft/creator/documents/animations/animationrendercontroller
Official Cooperative Add-On Design: https://learn.microsoft.com/en-us/minecraft/creator/documents/practices/guidelinesforbuildingcooperativeaddons?view=minecraft-bedrock-stable
Official Creator Docs Portal: https://learn.microsoft.com/en-us/minecraft/creator/
Community Bedrock Wiki World Generation: https://wiki.bedrock.dev/world-generation/world-generation-intro.html
Community Bedrock Wiki Biomes: https://wiki.bedrock.dev/world-generation/biomes
Marketplace product third-party listing (identity, not proof of uploaded archive provenance): https://www.minecraftpal.com/marketplace/item/8ea7ade9-9063-4dd4-8fbd-2d30636a6fea/star-odyssey-beyond-space

16. RECOMMENDED NEXT WORK CHAT DIRECTIVE
'Use Starbound_Frontier_Deep_Research_2026-11-23.txt and the actual Star Odyssey pack as constraints. Audit the existing addon files. Do not start a new website or engine. Implement the P1 living frontier region: two contrasting biome identities, functional natural village/ruin generation, an NPC with actual schedule/trading, two ecologically distinct animals, one hostile machine, and a functional power/refining loop. Test real survival, spawns, pathing, saves and resource-pack compatibility. Provide actual .mcaddon, source, verification, screenshots if Minecraft ran, and an updated handoff. Preserve Minecraft's normal mechanics and freedom.'