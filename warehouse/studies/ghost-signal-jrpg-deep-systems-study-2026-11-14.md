<!-- Atlas Warehouse archived public-safe research copy.
Original: https://github.com/nobleknights015-maker/bearframe-ghost-signal/blob/ghost-signal-engine/docs/JRPG_DEEP_SYSTEMS_STUDY_20261114.md
Source blob SHA: 9bb3176d15e275fa16c6c1e48870ce85146030a6
Research is design guidance, not proof of runnable gameplay or device testing.
Authoritative engine development branch: ghost-signal-engine.
-->

# BEARFRAME / GHOST SIGNAL ENGINE — DEEP JRPG SYSTEMS STUDY
**Research revision:** 2026-11-14, v1.0
**Authorized branch:** ghost-signal-engine
**Status:** design and technical research only — recommendations, not claims of implemented or device-tested gameplay
**Core question:** How do we make Bearframe play and feel like a deliberately designed science-fiction JRPG, not a stealth game with generic RPG components bolted on?

## Executive assessment

A proper JRPG is not defined by a list of features. It is defined by connected decision loops. The player explores a coherent place, receives information, encounters risk, plans a party response, spends limited resources, gets a meaningful consequence, develops characters, and returns to the world with changed possibilities. The UI, pacing, audiovisual feedback, story state, maps, and persistence must express one continuous game.

The central recommendation is a **Phantasy Star IV-inspired, authored-encounter, four-direction, smoothly traversed science-fiction JRPG** built on Ghost Signal's working world engine. Retain full Ghost Signal stealth as a context-specific exploration mode. Modernize encounter readability and pacing, with lessons from Sea of Stars, Chrono Trigger and Octopath Traveler; do not copy their exact systems. Respect the approved Ghost Signal visual language. Preserve its original game, main branch, frozen baseline, missions, saves and standalone Sprite Studio.

**A critical implementation gap:** current rpg-combat.js uses simple sequential commands and basic lowest-HP AI. That qualifies as a unit-testable tactical prototype, not Phantasy Star IV-style party command planning, combination combat, meaningful skill identities or encounter authoring. Current rpg-menu-model.js is a content model, not a playable menu; hybrid-session.js is not mounted into the original map renderer. Do not report these as full JRPG integration.

## 1. Research method and evidence levels

Four evidence classes:
1. **Primary game manuals**: SEGA Phantasy Star II and IV instruction manuals for equipment, battle commands, menus, skill resources, party ordering and save rules.
2. **Developers discussing their own games**: Sabotage Studio on Sea of Stars combat/traversal and post-release revisions; Chrono Trigger developer interview for authored encounter presentation; Square Enix on Octopath's Break/Boost.
3. **Game design analysis and academic work**: Chrono Trigger structural/encounter analysis, Zeboyd Games' JRPG pacing discussion, UC Santa Cruz research connecting quest design and level design.
4. **Project-grounded facts**: Ghost Signal source/PRD, the independent old engine's party-combat module, earlier disassembly/replay findings, and Revision 4.10 canonical Bearframe universe reference (privately supplied; not copied into public repository).

A design proposal is **not** a verified fact about another game's internal implementation. The earlier reverse-engineering notes identify observed PSIV dispatch, initiative-shortlist and save events; they do **not** prove an entire combat engine's formulas. No proprietary game code or copyrighted assets are copied.

## 2. Reference comparison — what we should actually learn

| Reference | Observed design contribution | Suitable for Bearframe | What not to inherit blindly |
|---|---|---|---|
| Phantasy Star II | Party management, healing/technique attrition, dangerous dungeons, strategy before combat, equipment and saving as expedition preparation | Resource pressure; meaningful loadouts; ancient hostile terrain; consequences carried between battles | Grindy random encounters, repeated uneventful corridors, frictional save access |
| Phantasy Star III | Multi-generation consequences, varied playable party combinations and story paths | Deep-time archaeological mystery and choices with lasting effects; a world that remembers | Forced marriage/generational protagonist replacement; wide branching without capacity to author/QA it |
| Phantasy Star IV | Commands queued across a party, distinct TP Techniques and limited-use Skills, position/order, macros, combinations, strong character presentation | Main tactical template; prepared tactics; specialist roles; discovered coordinated actions | Undocumented formulas, opaque combo discovery or randomness that hides strategic outcomes |
| Chrono Trigger | Visible/embedded encounters, authored battle introductions, meaningful exploration and character synergies | Enemy placement and fights integrated into map geometry, interaction and pacing | Its entire ATB/battle presentation as a compulsory requirement |
| Sea of Stars | No random encounters/grinding, low resource pool, useful small kits, type locks, quick swaps; exploration as a first-class pillar | Readable intentions, unique abilities, varied crafted fights, strong out-of-combat interaction | Mandatory timing minigames, jumping/climbing, identical mana locks or 3D lighting; not appropriate to every scene |
| Octopath Traveler | Weaknesses, shields and bankable Boost Points create setup/payoff | Learnable vulnerabilities and tactical resource timing | Another full resource economy stacked on top of macros, combos and stealth |
| Ghost Signal | Real-time stealth, four-direction smooth movement, camera, collision, scan/noise/detection, evidence, checkpoints, cohesive UI | **Foundation** — retain the functioning exploration/stealth system and approved interface | Existing mission logic as the only possible map/quest model |

Primary reference evidence:
- PSII official manual includes strategy-versus-fight selection, HP/TP/status display, equipment/hand choices, recruiting, saving and supplies.
- PSIV official manual includes Camp/Item/State/Order/Talk/Macro, distinct Skills vs Techniques, full-party command selection, action-order-dependent combinations and escape risks.
- Sea of Stars developer details no random encounters/grinding, low MP and restoring MP through attacks, locks, timed hits, combos and boost; its 2024 update changes combo persistence and mystery locks after playtesting. This illustrates that even good RPG mechanics need iterative correction.
- Chrono Trigger developer interview describes manually designed environmental battle introductions; the later design analysis identifies visible, avoidable encounters as an exploration benefit.
- PSIII's branch-generational structure is an instructive narrative device, not a mandated mechanic.

## 3. Seven connected gameplay loops

### A. Moment-to-moment (seconds)
Move smoothly in one of four cardinal directions, inspect an interesting object, avoid a hazard or detect a hostile. Controls and animation must give immediate, legible feedback. Camera and pathfinding must not obstruct interactions. Four directional animations are sufficient.

### B. Exploration (1–5 minutes)
Follow environmental clues, read a map, inspect machinery, open a route, find an optional alcove, or enter a local stealth perimeter. A room should contain at least one reason to care: information, navigation choice, mechanic, resource, story consequence or discovery. No corridors purely to increase walking time.

### C. Encounter (1–4 minutes, provisional)
A visible threat, environmental trap or authored event creates a decision: avoid, investigate, negotiate when supported, remain hidden, manipulate machinery or fight. The consequence must carry forward. Battles should be readable and fast enough to prevent repeated trash fights from consuming the journey.

### D. Expedition (10–25 minutes, provisional)
Move from a safe staging area through a dangerous sector, consume resources, unlock a shortcut/checkpoint, and choose to proceed or retreat. The cost of pressing onward is an important Phantasy Star inheritance. Timings are initial test hypotheses, not universal targets.

### E. Character growth (chapter scale)
Experience unlocks options, not just bigger numbers. A new weapon, ancient module or learned skill enables a new tactic or route. A Frame's persistent flaw can be an identity/ability rather than something automatically erased by upgrades.

### F. Story/world state
The game records what the player discovered, what they changed, who they helped, and what they failed to do. Context-specific party reactions and NPC/terminal records acknowledge events. Quests must live in spatial context.

### G. Campaign continuity
Saves preserve enough deterministic world/party/combat state to restore a coherent place. No contradictory doors, respawned unique NPCs, doubled rewards or silently reset stealth alarms.

**Cross-loop requirement:** each meaningful feature must connect to at least two loops; otherwise it risks being isolated decoration.

## 4. World and exploration architecture

Ghost Signal remains the single authority for field movement, tile grid, collision, camera and presentation. Extend it behind a small mode interface rather than cloning a second movement engine.

Proposed data ownership:
- WorldSession: current map ID, coordinates, facing, camera, party follow positions, authored NPC states, interactive objects, obstacle/door states, flags, quest facts, region policy and environmental state.
- EncounterDirector: authored trigger conditions and outcomes; makes an explicit request to enter combat, avoid, negotiate, chase or alert.
- CombatSession: the deterministic battle snapshot and event log; never moves the field actor independently.
- Presentation: Ghost Signal original UI components plus matching new RPG panels, no new unrelated skin.
- PersistentRecords: versioned serialized game state and deterministic replay seed, committed at safe boundaries.

Native world grid remains 32×32; characters can be visually taller than 32 without changing collision footprint. Movement is four-way and smoothly interpolated; do not require diagonal sprite sets. Use feet-aligned coordinates for collision and spawn, not sprite image top-left. Navigation mesh/graph is optional; collision and event regions must be data-driven and coordinate-consistent.

Use authored doors, power relays, hidden terminals, rotating machinery, sound/noise surfaces, alarms, lighting, persistent destruction, one-way routes, physical shortcuts, and optional detours. Each piece of traversal design should either teach, test, surprise or contextualize a mechanic. Sea of Stars demonstrates the importance of treating traversal as designed play; its exact climbing/jumping moveset is **not** mandated for Bearframe.

Navigation/traversal test cases: narrow doors; corners; two NPCs in doorways; diagonal-touch inputs resolving to cardinal directions; map edges; stealth zone boundaries at sub-tile coordinates; collision under slow/fast frame times; mobile virtual D-pad vs controller; cutscene return and camera reattachment; door state persisted on reload.

## 5. Encounters: authored before procedural

Recommendation: default **visible/author-triggered** encounters; random encounters only if explicitly justified by a particular story/mechanical zone, never as a generic substitute for encounter composition.

Every enemy archetype should have:
- A role (scout, suppressor, sentinel, healer, summoner, jammer, armored guardian, etc.).
- Readable intent/counterplay (pose, warning HUD, sound, scan information).
- At least one exploitable weakness **and** one behavior the player cannot trivialize by holding Attack.
- A plausible relationship to its environment, patrol, power supply and faction.
- A retreat/flee policy and a persistence/respawn policy.
- A clear reward or consequence appropriate to the mission, not automatic XP farming.

Use three encounter bands:
- Teaching: demonstrate a single counter or mechanic without punishing ignorance harshly.
- Combination: test two familiar mechanics together.
- Mastery: demand purposeful action selection, resource budgeting or an environment-specific choice.

Boss encounters should expose phase changes driven by state (power relay, shield type, sensor awareness, damaged actuator) rather than just larger HP. The player must be able to infer what changed.

**Stealth is not a battle funnel.** Detection behavior is authored: patrol escalation, search, chase, alarm, blocked access, forced withdrawal or optional battle. A stealth scene can be solved through movement, environmental interaction and evidence without combat. Security AI remains active under Ghost Signal's genuine patrol/line-of-sight model; battle transitions must retain it for restoration.

## 6. Combat — recommended design contract

### Chosen direction to prototype
Favor a **PSIV-like planning phase and deterministic round resolution**, with an accessible quick-command/macro option; compare in playtesting against a one-character-at-a-time alternative. This is a design hypothesis supported by manuals and observed historical references, not yet an approved final balance scheme.

Proposed loop:
1. **Encounter context**: display enemy identity/intent, party and environmental factors; any ambush/surprise modifier is visible.
2. **Plan**: for each capable party member choose attack, special technique, limited-use frame action, item, guard, scan/analyze, swap (if allowed), or flee. Show affordability and valid targets before confirmation.
3. **Review**: optional editable command queue and macro preset, with accessible undo/back.
4. **Resolve**: freeze intentions and derive initiative with a saved deterministic random seed, speed and explicit statuses; process ordered action events.
5. **Interrupt / combination**: scripted synergy can form if defined compatible abilities resolve inside an authored window. Failed combos have clear reasons; do not silently eat resources.
6. **Reaction**: enemy telegraphed action fires or is interrupted/mitigated by the player's choice, not omnisciently rewritten.
7. **Round end**: status decay, environmental hazard effect, cooldowns, retreat, end conditions and new intent generation.
8. **Results**: reward XP, drops, equipment/quest flags, security consequences and return to the original world at exactly the retained logical position.

Candidate action data: actor ID, action ID, target IDs, costs, target shape, priority, move tags, action conditions, cancelability and narration/audio event ID. Combat state should include phase, turn/round, commanded actions, RNG seed, actors, buffs/debuffs, enemy intent, environment rule, log and provisional rewards. **Every action validates before costs are committed.**

### Ability kits
Small differentiated kits beat large duplicated spell catalogs. A practical initial design target is 3–5 meaningful actions per party member, plus basic item/guard/interact commands. Avoid implementing dozens of barely distinct attacks. Abilities need roles such as:
- Armor-piercing strike against old plating.
- Signal disruption to delay targeted scanner attacks.
- Coolant repair with limited applicability and predictable cost.
- Cover/guard to protect a lower-integrity Frame.
- Chassis instability discharge: strong but requires setup, may carry a future downside.
- Paired technique when two members' capabilities align.

The above are **design examples**, not new canon events or final named abilities.

### HP/energy/status economy
Separate durability (HP/integrity) from energy for abilities, and from special limited-use systems where justified. PSIV's distinction between TP and limited Skills is a strong model, but adding a third resource must justify its cognitive load. Avoid mandatory persistent weapon degradation in every battle unless testing proves it improves decisions rather than punishing exploration.

Deterministic damage, defense, target/range and immunity rules must be documented and unit-tested. Randomness needs bounds, a seed, and fairness tests; never make critical survival decisions hinge on an undisclosed 30% failure. Enemy intent and resistances can be partially discovered by scanning, reading logs or observing behavior rather than exposed universally.

### Enemy AI
The current lowest-HP-only selector is too generic. Recommend **authored priority policies** such as:
- Patrol droid focuses first detected attacker, then line-of-sight target.
- Suppressor pressures support/repair units and telegraphs it.
- Damaged legacy construct follows an obsolete maintenance directive, perhaps ignoring threats near a power source.
- Alerted sentry can summon reinforcements if a relay remains active.
- Intelligent enemy may defend or disengage at low integrity.

AI should not read future player choices. Introduce varied policy weights and a deterministic seeded tie-break; enforce cooldowns and no impossible actions. At least two distinct player tactics should be viable per authored encounter.

### Formations and switching
Party order should matter tactically but avoid forcing spreadsheet micromanagement. Simple front/rear protection, one active leader for field interaction, and clear support abilities may suffice. Switching should retain status and resource rules, cost defined upfront, and party roster consistency across save/load.

### Macros and combos
PSIV's macros are meaningful because they **compose planned actions**. Add presets only after the underlying round/planning and abilities function. Macro commands must be revalidated against current MP/EP, item quantity, status, available targets and enemy presence. No invisible auto-pilot that plays indefinitely without meaningful choice. Combination rules should be a small authored catalog: IDs, compatible tags, order/adjacency window, animation cue, cost, effect and interruption behavior. Make discoveries persistent and understandable in the UI.

### How to reject shallow combat
Combat prototype fails if:
- Attack spam wins every normal fight with no meaningful loss.
- Every enemy chooses the weakest party member regardless of context.
- Items and skills are mathematically inferior to attacking.
- A battle lasts longer only because the enemy has more HP.
- A combo has only a damage bonus without a strategic purpose.
- A defensive action is never useful.
- The outcome of a status/skill cannot be predicted from UI cues.
- Battle return changes map coordinates or wipes stealth/quest state.
- Automatic difficulty scaling erases the value of progression.

## 7. Party, equipment and progression: lore-specific constraints

Revision 4.10 establishes distinct modern Bearframe and ancient Echo/Ghost Grid lineages. The player Sleeper is an ancient system, **not a modern Bearframe**. Sleeper cores are old and degraded; compatible chassis parts may replace old hardware, but a modern Foundry-compatible upgrade must not be casually installed as if all equipment shares one bus. A damaged identity or ancient VI core should never be fixed by equipping a common loot drop.

Model:
- Stable unit identity and species/technology lineage.
- Immutable or tightly authored core-compatibility class.
- Replaceable chassis components with compatibility tags.
- Weapon as a dedicated equipped item; **weapon changes alone may visibly change the player Frame** under the established visual rule, unless owner changes that contract.
- Story/quest flags separate from generic progression.
- Experience: unlock skills/attributes while protecting each Frame's distinct role.
- Statuses: identity interruptions, glitches, corrosion, scan interference, overheat, immobilization; each condition has specific audiovisual and gameplay meaning.
- Recruitment as a durable relationship/state rather than a generic party slot. Do not equate Echo personhood with NPC ownership or inventory.
- Optional party switching, not required full-roster micromanagement.

Party design questions to answer through playtests: how many active units fit a 480×270 interface? Is 3 or 4 tactically legible? When can inactive members change? Are support abilities usable out of combat? Does a damaged Frame remain meaningful instead of being penalized until replaced?

**Progression tuning:** establish an expected number of authored encounters per expedition, an expected XP budget, a few clear equipment changes and explicit optional rewards. Avoid requiring pure grinding to survive a mandatory boss. An optional deeper ruin may reward preparation or mastery without arbitrarily blocking the main critical route.

## 8. Dungeon, quest and story engineering

RPG research on quest/level patterns emphasizes the interdependency of level design and quest structure. Each authored map must be designed alongside its mission objective, NPC behavior, encounter order, secrets and player information. A quest is not just a list of flags.

Recommended content structure:
- Region -> sectors -> rooms/cells -> interactive entities -> authored events.
- Event predicates include flags, evidence, quest stage, faction disposition, party composition, device status, time/alert state and prior outcomes.
- Event effects are atomic and idempotent: grant item once, unlock path once, mark evidence once, spawn/despawn actor once.
- Companion reactions are conditional and not dumped into generic banter loops.
- Mysteries preserve uncertainty. Unidentified ancient systems do not supply definitive exposition on unknown creators because the engine wants to fill a lore database.
- Dialog can branch locally with later callbacks. Choices need visible stakes but not necessarily a binary good/evil label.
- Field logs, scans and anomalies advance understanding and can solve puzzles or change encounter tactics.

Suggested map pacing:
- Introduce a unique environmental visual/signature.
- Give a small safe inspection opportunity.
- Teach or reinforce one interaction.
- Present a navigational fork and an optional reward.
- Make the first threat readable.
- Escalate with a stealth/puzzle/combat combination.
- Provide a shortcut or recovery point.
- End with revelation, mechanical consequence or choice—not always a boss fight.

Stealth areas should feel like places within the same world: seamless entrance/exit, same player position, same camera rules, real dynamic security actors, and persistent detection consequences.

## 9. Interface / interaction grammar

**NON-NEGOTIABLE:** preserve the original Ghost Signal interface as the visual and interaction specification, not merely as an aesthetic inspiration. Exact baseline source (index.html, css/game.css, ui.js and Sprite Studio) remains frozen. Keep 480×270 logical viewport, sharp pixels, Silkscreen/VT323, existing palette, squared panels, red accent, scanlines and current title/pause/dialog/terminal/CASE-file hierarchy.

Add RPG screens using this grammar:
- A compact STATUS panel with HP/energy/equipment context.
- PARTY roster cards and active ordering.
- ITEMS list with category, count, item effect, eligible target and confirmation.
- EQUIPMENT with compatibility, stat delta, left/right/slot constraints and clear invalid reasons.
- SKILLS with cost, target/effect and unavailable states.
- QUESTS / FIELD RECORD with known objective, evidence, maps and context rather than a generic fantasy quest journal.
- BATTLE COMMANDS with readable active unit, enemy intent, target cursor, resource costs, queued macro/turn order and undo.
- SAVE/LOAD with slot/revision, map, playtime, party summary, checksum-recovery warning, and manual/auto distinctions.

An ordinary UI test must be able to run from touch only, gamepad only, keyboard only and after switching control devices mid-menu. Focus must not jump off-screen; Back must reverse the last decision without consuming an item/turn. No text should be clipped at the target phone's landscape viewport. Retain original controls for original missions.

## 10. Persistence is part of gameplay correctness, not an add-on

Use separate namespaced RPG saves; never migrate the original bearframe_ghost_signal_* localStorage data without an explicit, tested migration operation.

Minimum RPG save schema:
- Save metadata/version, integrity/hash, stable install/session ID, sequence/revision and timestamps (diagnostic; not gameplay RNG).
- Map/location/facing, player/party roster and active party.
- HP/EP/statuses/skill uses, equipment, inventory and currencies.
- Quest/event flags, NPC states, puzzle state, evidence/logs, discoveries and unlocks.
- Environmental/security state: patrols/alarms, disabled devices, one-shot triggers and cleared encounters.
- Persistent battle phase/turn/order/actor state/seed and pending action if mid-battle saving is supported; otherwise forbid saves except atomic safe points.
- Derived stats recomputed from authoritative source definitions, not divergent serialized caches.
- A clear migration path for version changes and rollback or quarantine on invalid versions.

Implement atomic writes using dual journal slots (existing RPG adapter is a beginning), but actually test serialization, corrupt-write fallback, full app-kill/relaunch, Android update, old versions and two game slots. Journal integrity protects against accidental corruption, not malicious modification. Browser localStorage alone does not guarantee survival of app uninstall or storage clearance; native app-private records/export are still necessary for release targets.

Tests must include:
- Save after picking unique evidence and reload (no duplication).
- Save after equipment swap and reload (no double weapon).
- Save at stealth alert and reload (AI remains coherent).
- Transition into and out of battle (correct tile, enemy persistence, temporary combat status cleanup).
- Save from safe corridor near a door then reload (no collision deadlock).
- Failed write/low storage, corrupted newest record fallback, migration from prior app build.
- Process death mid animation/choice/battle, cold launch.
- Consistent signing for update installation, no key bundled in public repository.

## 11. Android architecture and performance

The current Ghost Signal engine is an HTML5 Canvas game; the existing Android scaffold uses WebViewAssetLoader for a stable local HTTPS-like origin, which Android recommends over file URLs. Treat it as an initial development host, not production-grade durable saving.

Android support requirements:
- Correct landscape layout and immersive safe areas on Moto G (2025), 4 GB RAM; do not assume Chicago timezone or specific screen shape matters to layout.
- Four-direction physical controller input and responsive virtual D-pad; controls remain inside viewport at all aspect ratios/safe-area insets.
- Reliable audio unlock, suspend/resume, app backgrounding and recreation.
- Readable font size and optional accessibility mode without restyling the default visual grammar.
- Main thread frame budget; no synchronous massive tile baking after every room change; avoid allocations in per-frame render and cache procedural layers.
- Stable camera and collision under variable dt; ensure engine does not tunnel through walls or multiply input after pauses.
- Measured FPS and input latency on physical device; sustain consistent play more important than an unproven peak.
- 30+ minute real-phone save, heat and memory soak; cold-start, process-kill and update flows.
- Offline fonts and all needed owned/licensed assets locally bundled or handled consistently. Never publish the user's commercial asset ZIPs or third-party game data.

Differentiate Android native activity/WebView state from game save state. WebView history restoration does not serialize a JRPG's authoritative world state by itself.

## 12. Audit of current Ghost Signal Engine modules (2026-11-14)

| Current module | What exists | Study finding / next needed step |
|---|---|---|
| game.js | Working original field simulation, stealth AI, camera, collisions, mission API and old snapshots | Retain as runtime foundation; define adapter hooks before changing main loop |
| area-policy.js | Pure rectangular zone lookup | Needs persistent authored map registry, event triggers and named regions without implicit combat |
| hybrid-session.js | Pure state transitions and authored detection outcome; isolated | Needs runtime handshake with actual drones, world state and battle UI |
| encounter-handoff.js | Cloned field snapshot and restoration contract | Add explicit allowable mutations/quest effects; deterministic pending events; duplication protection |
| rpg-combat.js | Attack, pulse, guard, repair, item, flee and deterministic speed order | Prototype only; redesign from combat specification once action pipeline/AI/roles are authored |
| old engine framework/party-combat.js | Deterministic round-based multi-actor combat with skill catalog, status, seeded PRNG and validation | Evaluate as tested algorithms, not as a core replacement; avoid simultaneous conflicting combat authorities |
| rpg-party.js | Active units, equipment, inventory and simple XP | Add equipment compatibility and core/chassis restrictions, formation, level tables and equipment preview |
| rpg-menu-model.js | Data content for seven RPG tabs | Not presented in live game; actual navigation/targeting/inventory actions and UX tests missing |
| rpg-save.js | Two records, checksums and fallback | Needs durable game-session integration and native storage/export, migration/version testing |
| gamepad.js / input.js | Four-cardinal poll and additive support | Needs physical controller testing and focus semantics for newly mounted RPG panels |
| android/ | WebView debug-host source | Build, install, lifecycle/save, offline fonts and release signing unverified |
| Original Ghost Signal /studio | Working independent sprite editor | Keep unchanged; use exported art only through tested adapter, not imported editor runtime |

**Concrete defect candidates to audit, not assert as confirmed runtime bugs:**
- rpg-combat's round order is based on speed only and lacks PSIV-like planned party commands.
- Its enemyDecision always targets lowest proportional HP; this will become repetitive.
- Its current repair/item actions do not yet represent the entire typed skill, target and equipment economy.
- Need guarantee that a stale action or invalid target cannot change mutable state.
- Need prove that the dual save records cannot commit divergent partial inventory/world outcomes across a battle boundary.
- No proof of full browser/game integration or physical Android performance.

## 13. Integration sequence governed by design evidence

### Phase 0: Lock and verify the base
Run the complete Node suite and browser visual/smoke test for original Missions 01/02 and standalone Sprite Studio. Document screenshots, frame hashes, movement, save and load. Keep original main/baseline unchanged.

### Phase 1: Author a playable **RPG test sector**, not campaign content
A compact non-canonical test room/corridor using the actual Ghost Signal renderer, native 32px tiles, one interactable object, a recover point, an authored area policy and visible threat. Four-way walking, collision, party status, menu, save and restore must work.

### Phase 2: Build one **excellent encounter**, not twenty generic ones
Create an enemy with readable intent and counterplay plus two party archetypes with distinct abilities. Compare planned-round model against sequential actions. Record command count, duration, damage/EP distribution, repeated-action frequency, user confusion and failure recovery. Add meaningful non-battle exit from one stealth risk.

### Phase 3: Extend to an expedition loop
Two connected rooms + optional branch; one shortcut, one hazard, one scanning/evidence puzzle and a second encounter that combines previously learned rules. State persists across all transitions.

### Phase 4: Add robust party systems
Loadouts with compatibility, active roster, out-of-combat use, equipment previews, progression tables, appropriate stat scaling and a few authored synergies. No arbitrary grind loops.

### Phase 5: Integrate complete interface and persistence
New panels/command selection use frozen Ghost Signal style. Save/load context and input focus are end-to-end tested. Add in-game continuity after UI interruption, app suspend, corruption and update.

### Phase 6: Android proof
Build debug APK and run on the target-class phone. Evaluate frame pacing, touch/gamepad, safe areas, audio, long save soak and scene performance. Package private owner art legally; do not claim ship-ready until owner-visible acceptance and signing.

## 14. Required acceptance test matrix (not yet executed)

Combat: action legality; resource nonnegativity; exact one action per unit where required; RNG reproducibility; target invalidation; initiative tie; KO skip; guard duration; poison/status ticks; target switch; interrupt/reaction; run permitted/denied; combo success/fail; boss phase; victory/defeat/draw; reward once; party down on retrieval; no stranded UI.

Exploration/stealth: uninterrupted walking; solid walls and doors; camera; four-direction animation; zone enter/leave; patrol sight/LOS; hide/search; scan/noise; alarms; noncombat escape; transition to battle; return at same coordinates; actor persistence; optional route; collect evidence; switch maps; safe backtracking.

Economy/party: equip swap with item conservation; incompatible ancient vs modern equipment; two-handed vs accessory slots if chosen; clear stat delta; XP and level threshold; skill unlock; reserve member switch; revive/repair limits; combat inventory reconciliation; no duplication on retry.

UI: exact original UI source lock; title/pause/settings/casefile/terminal untouched; new panels match fonts/layout; gamepad focus; D-pad; controller reconnect; touch selection; Back/Undo; no invisible targets; complete dialog text; contrast and font scaling.

Save: legacy Ghost Signal save remains readable; RPG slot schema; dual record fallback; bad checksum; schema upgrade; full game snapshot; partial write; Android process death; phone restart; signed app update; long soak; offscreen quit/restore; storage quota; export/import when implemented.

Performance: 32px render; pixel snapping; no blur; camera ease; 4GB RAM; sustained FPS; thermal effect; audio glitch; context loss; slow frames; prolonged scene transitions; no leaks in 30+ minutes.

## 15. Research questions requiring a playable experiment (not guesses)

1. Is a PSIV-style party-wide command planning phase more readable/fun than immediate per-character turns on a small landscape screen?
2. Is a 3-member or 4-member active party better for Ghost Signal's 480×270 HUD?
3. Which resources create meaningful tension without exhausting exploration—EP, limited Skill uses, a shared combo meter, or combinations of these?
4. Should encounter weaknesses be signaled by scan, observation, retrieved archives or UI icons? What percentage should remain mysterious?
5. How much battle density is appropriate between safe checkpoints before exploration feels punitive?
6. Can stealth and combat share threat states without letting the player cheese alarms by entering/leaving battle?
7. Can the approved interface accommodate long skills/equipment names with native pixel fonts on the target phone?
8. Do the existing gamepad menu additions preserve focus/confirm/back semantics in every old modal and new RPG screen?
9. How do equipped weapons visibly change the player sprite without requiring complete 4-direction rerenders per item?
10. Which owner-licensed assets are appropriate to each environment, and which can be packaged privately without redistribution rights conflict?

## 16. Proposed design decisions (recommendations, pending practical validation)

**Adopt for the test slice:** Original Ghost Signal field engine and UI; 32x32 tiles; cardinal smooth movement; visible authored encounters; specific stealth zones; persistent world consequences; deterministic action pipeline; differentiated 2–3-member tactical party; limited ability kits; no mandatory grinding; concise equipment compatibility; separate robust saves.

**Prototype and measure, not assume:** PSIV planned rounds, editable macros, combination attacks, scan-revealed weaknesses, limited-use vs EP resource split, free/turn-cost party swapping, formations, optional timing bonuses.

**Reject for this project by default:** Generic JRPG blue window skins; universal random battles; eight-direction requirements; replacing Ghost Signal stealth with combat; a second independent player movement simulation; universal modern hardware upgrades for ancient cores; mandatory equipment wear; unexplained damage formulas; save formats that break existing Ghost Signal keys; wide branching without corresponding authoring/testing capacity.

## 17. Sources and direct reference links

Official or primary manuals and developer sources:
- [SEGA Phantasy Star IV original manual](https://manuals.sega.com/genesismini/pdf/PHANTASY_STAR_IV.pdf) — pages 8–19 menu/order/macro/Technique/Skill/combat/combination rules.
- [SEGA Phantasy Star II original manual](https://www.sega.jp/mdmini2/en/assets/manual/pdf/EU_Phantasy-Star-II.pdf) — party, equipment, resource economy, save slots, fight/strategy commands.
- [Sabotage Studio: A closer look at Sea of Stars turn-based combat](https://blog.playstation.com/2022/07/07/a-closer-look-at-the-turn-based-combat-in-sea-of-stars/).
- [Sabotage Studio: Sea of Stars Combat 2.0 update](https://blog.playstation.com/?p=398214).
- [Sea of Stars level designer on traversal](https://blog.playstation.com/?p=382678).
- [Square Enix Octopath I/II Break and Boost](https://www.square-enix-games.com/en_US/news/octopath-traveler-i-and-ii-now-available-current-console-platforms).
- [Chrono Trigger developer interview, translated](https://shmuplations.com/chronotrigger/).

Analysis/research:
- [Chrono Trigger's Design Secrets — Victoria Earl](https://www.gamedeveloper.com/design/-i-chrono-trigger-i-s-design-secrets).
- [The Zeboyd Games Approach to JRPG Design — Robert Boyd](https://www.gamedeveloper.com/design/the-zeboyd-games-approach-to-jrpg-design).
- [Situating Quests — Smith et al., ICIDS 2011](https://users.soe.ucsc.edu/~ejw/papers/smith-situating-quests-icids-2011.pdf).
- [Phantasy Star III generational design overview](https://www.mobygames.com/game/7749/phantasy-star-iii-generations-of-doom/).
- [Phantasy Star IV technical combo notes (secondary)](https://www.pscave.com/pspages/psiv/combos.html).

Platform:
- [Android WebViewAssetLoader](https://developer.android.com/reference/androidx/webkit/WebViewAssetLoader).
- [Android WebView state management](https://developer.android.com/develop/ui/views/layout/webapps/managing-webview).
- [MDN Gamepad API](https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API).
- [Microsoft game accessibility guidelines](https://learn.microsoft.com/en-us/windows/uwp/gaming/accessibility-for-games).

Project source:
- [Ghost Signal engine status](ENGINE_STATUS_20261114.md) and [Hybrid baseline](HYBRID_ENGINE_BASELINE.md).
- [Old engine's Phantasy Star research notes](https://github.com/nobleknights015-maker/bearframe-rpg-engine/blob/main/reference/FINDINGS.md).
- [Old engine's deterministic party-combat module](https://github.com/nobleknights015-maker/bearframe-rpg-engine/blob/main/framework/party-combat.js).

**Method limitations:** This is source/manual/developer/technical-code research, not a hands-on playthrough of all cited games in the current session. The actual feel, pacing, tactical balance, and Android experience must be evaluated in a playable test sector. Source descriptions and suggested numbers are not performance guarantees. The supplied Bearframe lore archive informs constraints but is not redistributed here.

## Final study rule

Before adding a subsystem, ask: **What decision does this create for the player? How does the world acknowledge its outcome? How does the UI teach it? How does it survive saving and loading? How is it measured with a real gameplay test?** If the answer is unclear, do not add the subsystem merely because other RPGs include it.
