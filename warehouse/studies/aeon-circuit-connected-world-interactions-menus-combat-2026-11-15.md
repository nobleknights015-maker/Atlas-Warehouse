# AEON CIRCUIT — CONNECTED WORLD / INTERACTIONS / MENUS / COMBAT RESEARCH ARCHIVE
**Date:** 2026-11-15
**Source:** https://github.com/nobleknights015-maker/bearframe-ghost-signal/blob/ghost-signal-engine/docs/AEON_CONNECTED_WORLD_MENUS_COMBAT_BLUEPRINT_20261115.md
**Status:** Research-based implementation design; never treat proposed maps/event engine/full tactical command planning as already implemented.
**Privacy:** PUBLIC. No secrets, no unreleased private story revelations.

## Central finding
Build **one persistent world through many 32×32 authored maps** using the proven Ghost Signal Canvas runtime. Areas form a versioned graph of explicit portals/spawns and map-state deltas; do not build a second field core. The player's exploration, combat, menu, NPC dialogue, evidence and quest state share one immutable campaign state and validated action/event vocabulary.

## World and level design
- Every area earns physical plausibility: original function, power/transport/ventilation, historical decay, current ecosystem and player purpose.
- The old abandoned-planet infrastructure is not automatically a modern Bearframe Foundry. Ancient Sleepers, Echo individuals, Ghost Grid infrastructure and modern Bearframes use distinct canon and visual provenance.
- Prefer an initial noncanonical 6–9-map expedition with staging shelter → overgrown surface → service junction → security/duct branches → archive → relay → return shortcut. Every main path supports save/reload/revisit, clear landmarks and at least one meaningful choice.
- Native 32×32, four cardinal smooth movement, explicit collision vs sight vs sound vs hazards, feet Y-sort and safe spawn facing.
- Transition transaction: validate destination → freeze AI/input → load/instantiate → atomic world-state journal commit → spawn/camera → reveal, or rollback on any failure. Evict assets, never saved world changes.

## Interactions and dialogue
- Shared interaction grammar: notice → approach/facing → prompt → preview/choice → commit → feedback → remember.
- Types: log, NPC/Echo, door, switch, salvage, hazard, checkpoint, security terminal, encounter trigger.
- Authored conditions/effects use a strict allowlist; no JavaScript eval from map JSON. One-shot effects commit by stable event ID exactly once.
- Dialogue and evidence separate observations, testimony, corroborated records, hypotheses. Dialogue actions use conditions/variables, and must not expose restricted canon prematurely.
- Systemic puzzle tradeoff: power a bulkhead but wake a patrol; use maintenance route but cross a live electrical hazard. Quest, map state, security and NPC responses agree.

## Menus
- Keep original Ghost Signal industrial CRT UI. Build an actionable JRPG record: status, party, equipment, items, techniques/skills, quests/evidence, visited map, saves/settings.
- Shared focus/input stack for touch, controller and keyboard. Back/Cancel discards tentative choices; resource deductions happen only after verified confirmed actions.
- Effective equipment stat preview, ancient-modern compatibility, inventory conservation, field heal target choice, quest/knowledge truth and durable save feedback.
- Measure real CSS/device touch targets and text legibility rather than treating native sprite pixels as physical touch size.

## Combat
- Keep current sequential combat as verified baseline. Prototype full-party command assignment → deterministic initiative resolution as a feature flag, with real comparison of battle clarity, taps, resources, and tactical value.
- PSIV official manual supports reference study of command selection, macros, Techniques/Skills and combinations; never copy proprietary code/assets.
- Enemies have authored threat logic and readable telegraph/counterplay. The already verified charged sentry provides guarding/Pulse disruption.
- Build only a few deliberate statuses and one small synergy first; encounter consequences update world and quest state, no repeated rewards for fleeing/bypassing.
- Test attack-only vs smart choice outcomes, defeat/flee/checkpoint, inventory and power continuity.

## Recommended immediate vertical slice
1. Two map files + connected reverse portal/spawn with a real browser and reload test.
2. Author one switch/door/cache + one quest stage with per-map durable event deltas.
3. Expand to 6–9 logically connected maps with a bypass, hazard and shortcut.
4. One conditional Echo dialogue using the same knowledge/quest state.
5. Menus with functional interactions across keyboard/gamepad/touch.
6. Run tactical planning prototype comparison; keep working combat mode until evidence supports upgrade.
7. Canonical 32×32 atlas binding, Android emulator/physical Moto G tests, asset license audit.

## Evidence links
- Tiled Worlds: https://doc.mapeditor.org/en/stable/manual/worlds/
- Tiled JSON and objects: https://docs.mapeditor.org/en/stable/reference/json-map-format/ and https://docs.mapeditor.org/en/stable/manual/objects/
- Tiled terrain: https://docs.mapeditor.org/en/stable/manual/terrain/
- Red Blob A*: https://www.redblobgames.com/pathfinding/a-star/introduction.html
- Sega Phantasy Star IV manual: https://manuals.sega.com/genesismini/pdf/PHANTASY_STAR_IV.pdf
- Xbox accessibility UI focus: https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/113
- Yarn dialogue state: https://yarnspinner.dev/features/
- Game Programming Patterns event queue: https://gameprogrammingpatterns.com/event-queue.html
- Android WebView asset hosting: https://developer.android.com/develop/ui/views/layout/webapps/load-local-content
- W3C target sizes: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Current engine development standards: https://github.com/nobleknights015-maker/bearframe-ghost-signal/blob/ghost-signal-engine/docs/JRPG_DEVELOPMENT_STANDARD.md

**Use the source implementation blueprint for detailed next-action scope, not this compressed archive.** The owner also received an 11,500-word PDF/Markdown report for complete research depth. Preserve all original Ghost Signal UI/mission/save assets; commit real tested integration rather than standalone speculative modules.
