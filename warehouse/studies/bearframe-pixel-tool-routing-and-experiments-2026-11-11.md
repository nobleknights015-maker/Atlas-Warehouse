# Pixel-art workshop — six-plugin and LibreSprite capability map

**Date:** 2026-11-11. **Classification:** DOCUMENTED TOOLS + RESEARCH PLAN. A listed API capability is NOT a verified high-quality animation. No paid generation or private art upload happened in this assessment.

## Discovered tools versus actual access

| Tool | Present in current tool inventory | Useful role | Technical limits / risks |
| --- | --- | --- | --- |
| **LibreSprite 1.3** | GitHub Actions AppImage integration already **technically tested** in Atlas Warehouse | Editable pixel masters, layers, onion skin, tagged frame durations, 1x per-pixel corrections, PNG/sheet/JSON export | Installed ephemerally on GitHub runner, not guaranteed in every chat/container. Existing successful smoke/3-frame edits do not establish artistic quality. Use repo workflow, not photographic warp. |
| **SpriteCook** | MCP actions available and read-only account balance call succeeded | Import owned source art; animate owned asset; create character/preset animation sets; auto-slice; inspect/polish alpha; group work into projects and manifests | Upload uses explicit owner asset IDs; generation can consume credits, usually asynchronous. For walk from idle prepare a real mid-stride source first. Source dimensions/model requirements; animation does not guarantee anatomy/identity. |
| **Pixel Engine** | MCP tools available; read-only balance check succeeded | Edit/animate source pixel sprites; pixelate a high-res still; alpha cleanup; inspect jobs | Animation is paid; the pixelate operation **must not be run on already-pixelated sprites** (might over-reduce grid). Background remover accepts PNG/WebP, not GIF; preserve original alpha masters. |
| **AutoSprite** | MCP tools available and account check succeeded | Turn an existing full-body image into stored character; generate walk/idle/run/attack sheets; retrieve PNG+atlas; top-down/isometric specific workflows | Common side-view output defaults to many 256px frames, far beyond final tiny native-frame targets. Costs credits, requires clean source pose. Visual motion and dimensions must be edited/QA'd before 32px-world integration. Output links can expire; retain durable asset IDs. |
| **Sprite Fusion** | Installed Pixel Art *skill/reference instructions* discovered; **no directly callable Sprite Fusion MCP action** exposed this turn | Documented generate/edit/style-reference/eight-direction/animate API | Do NOT claim API connected or generation tested. It may require environment API auth; no private key should be published to public warehouse. Documented skill availability ≠ verified live API. |
| **MegaScenes Pixel Art Maker** | MCP account call succeeded; model discovery and estimates available | Concept variants, sprites, icons, scenes | Always check the account's current balance and obtain approval before spending credits. Text-to-image outputs are concept/reference until hand-corrected. Never assume transparent pixel sprite on first pass. |
| **Abracadabrax Pixel Art** | Text-to-image preparation action exposed; media generation action available but **not invoked** | Character/item/tile concepts and ideas | Prep does not charge; paid generation requires account/user request. Tool does NOT edit uploaded existing sprites and does not supply native transparent output as a core guarantee. Not the answer for faithfully animating an existing character. |

## Task-to-tool policy

1. **Existing approved source + walking animation:** retain original privately; inspect outline/pose/transparency. Build first mid-stride pose intentionally in LibreSprite; optionally test a **single** owned-source SpriteCook / Pixel Engine / AutoSprite animation after user-approved credit use, then redraw weak frames by hand. Score quality at native 1x, and reject inconsistent limbs/pivots.
2. **Existing source + missing transparency:** do selective alpha-mask work, preserving anatomy and hard edges. Prefer manual/Pillow/LibreSprite isolation for simple backgrounds and compare pixel diffs; use connected cleanup only when it genuinely improves. Keep an untouched original.
3. **New original character (no source):** sketch silhouette and grayscale value shapes, then proper pixel drawing. Generative tools are a *concept accelerator*, not proof of an original, correctly authored native sprite.
4. **Four directional character sheets:** author front/back/left/right, verify unique asymmetry, foot anchors, head display, chest display and matches to exact portrait. Use automated directional tools only for candidate poses; correct perspective manually.
5. **Tileset import:** start from already purchased 32px assets with source license retained; preserve 32px grid, margins and naming. Use sprite/tileset generators only for original supplemental assets; never remap a 48px editor sheet into the RPG by assumption.
6. **UI icons/panels:** outline consistent silhouettes, value hierarchy, original iconographic language and verified 9-slice boundaries before export.
7. **Master, previews, acceptance:** LibreSprite .ase + source asset manifest is canonical edit format; sheet PNG+JSON is runtime source; animated GIF/WebP is QA preview only. Store scripts/checklists in public warehouse; proprietary art and plugin output assets remain outside PUBLIC repository unless publication rights are explicitly cleared.

## Credit and privacy safeguards

- Read-only balance/status operations are safe to query. Do NOT spend credits or import private files during a general research request. Use user-supplied permission for new paid runs and obey account-specific constraints.
- Never paste private API keys or presigned upload URLs into issue comments, GitHub commits, ChatGPT summaries or shell logs.
- Do not assume six installed plugins are six independent *verified* providers. For Sprite Fusion, skill exists but API access is presently unverified; Abracadabrax ability to prepare a job does not mean it can animate an image.
- Store only technical notes and public-safe example pixel art in Atlas Warehouse. Maintain canonical source outside public warehouse as required by the asset's rights.
- Generation jobs can return before completion; poll correct status endpoint, inspect finished output and record asset ID. Do not call "done" when the job merely queued.

## Repeatable training experiments (proposed; none executed by this study)

**Experiment A — hand-built static silhouette:** Design one simple original 32px-world humanoid at candidate 32×64 or 48×64 frame size (frame **not** tile footprint). Check anatomy, hip/knee/ankle, torso, display identity, shoulders, boot stance and readability on light/busy backgrounds. If fail, redraw before proceeding.

**Experiment B — meaningful six-pose walk:** On approved static source, create 6 truly distinct authored frames. Measure heel/root anchoring, support/swing alternating stance, toe clearance, body compensation and loop seam. Color budget and alpha checks do not override visual failure.

**Experiment C — tool A/B:** Using a public-safe original generic character, compare LibreSprite hand edit with one test output from each *currently usable and affordable* animation provider, ensuring same source/prompt, target native geometry, durations and output. Record credits, elapsed, identity score, alpha score, anatomical score, visual and runtime pass/fail. No repeat paid calls for failed models until flaws understood.

**Experiment D — 32px terrain:** Make 3×3 seamless repeats and 16-mask/47-blob/or 16-corner dual-grid samples separately. Validate corner ordering, collision independence, art licensing and actual engine sheet coordinates.

**Experiment E — runtime export:** Export tagged idle/walk sheets from native master; ensure frame metadata, atlas bounds, nearest-neighbor, stable pivot and Android WebView rendering. Verify player root/collision unaffected after saves and screen rotates/sleeps.

## Evidence already on record

- [LibreSprite integration](libresprite-editor-integration-v1.md): actual editor instance ran JavaScript edit and exported verified bytes in GitHub Actions.
- [LibreSprite layered trial](libresprite-layered-idle-study-round-09.md): 3-frame/layer structural checks passed, character-art quality not approved.
- [Source-derived animation round 19](round19-unit09-first-source-based-animations-qa.md): proved packing/gif export, **NOT** an authored compelling walk.
- [SpriteCook workflow skill](https://github.com/nobleknights015-maker/Atlas-Warehouse) is available privately in assistant plugin context but direct portable tool details must be rediscovered on each run.
- [LibreSprite CLI guide](https://libresprite.dev/docs/cli/); [Aseprite source editing](https://aseprite.org/docs/workflow/).

**Next gate:** choose a candidate original, license-safe, full-body source with clean native pixels, then actually execute and critique Experiments A/B. The user specifically requested study and warehouse storage in this assignment, so no unrequested generation or paid plugin use took place.
