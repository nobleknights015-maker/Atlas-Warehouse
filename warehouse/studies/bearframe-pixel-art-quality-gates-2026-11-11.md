# Bearframe RPG — Native-pixel art QA and release checklist

**Date:** 2026-11-11. **Status:** proposed documented protocol from professional research, prior failed studies, and current 32px world-tile choice. Tests must be run per asset; this document is not a claim that production art passed.

## Hard gate 0 — provenance and project configuration

- [ ] Original/private PNG or editable .ase master actually identified; no screenshot, chat preview, blurry GIF or repeatedly resized composite used as the sole source.
- [ ] Asset is self-authored or the user's purchased source with license recorded in the private manifest; public GitHub content is cleared for public sharing.
- [ ] Existing **32×32 world tiles are retained** unchanged. Confirm per-source sheet tile width/height, horizontal/vertical spacing, margins, number of images, corner convention and atlas origin. Historical 48px World Editor sheets do NOT silently override this standard.
- [ ] Frame width/height is deliberately chosen for that asset. A sprite can extend above/beside its one-cell collision footprint; sprite size != tile size.
- [ ] Canonical character references and matching portrait ID/visual identity are established; four approved Sleeper selections never share mistaken character art.

## Hard gate 1 — static visual design (review at 1×)

- [ ] Arms, legs, boots, helmet, torso and joints are present and coherent; humanoid anatomy isn't amputated, stubby or disjointed.
- [ ] Helmet/visor, side-head hardware, chest display, asymmetric damage, accessories and hue identity are recognizable.
- [ ] Readable silhouette on white/black/checker/busy world background.
- [ ] Shoulders/hip/knees/shins/feet have credible proportions and armor volumes. Hinges/cables follow mechanical movement; cloth/organic wear are placed intentionally.
- [ ] Big clusters first; shading describes materials; no mushy edge blend, excessive one-pixel islands, smudged screenshot or random surface dithering.
- [ ] Consistent root foot anchor. Front/back/left/right maintain scale, shoulder/hip placement and intentional asymmetries.

**FAIL if:** only color count or PNG validation passes but Vera/artist critique finds generic, deformed or unreadable character art. Compare with [existing technical art failure](libresprite-layered-idle-study-round-09.md).

## Hard gate 2 — actual motion mechanics

- [ ] For walk: identify at least one contact, weight-down, passing and lift/up phase, with opposite foot mirrored/independently corrected.
- [ ] Planted foot stays in the same **world** location during stance; the pelvis translates/weights over support leg rather than both boots sliding.
- [ ] Swing foot lifts, travels and plants; articulated knees, ankles, cables and armor move plausibly. No missing shin, duplicated limb or rigid one-piece wobble.
- [ ] Arm swing counterbalances the legs; torso/head bounce restrained; equipment/cape catches up rather than snapping randomly.
- [ ] Distinct key poses and correct pixel-cluster rework; no photographic mesh/deformation blur.
- [ ] Timing reads as weight/acceleration; frame durations in milliseconds are recorded; final frame loops naturally to first (compare seam visually).
- [ ] Stable alpha bounds and foot pivot; any root displacement intentionally represented in separate metadata.
- [ ] Idle effects, locomotion, attacks, hit reaction, interaction, cutscene glitches each use explicit animation tags.

**FAIL if:** the character merely vibrates or leans while both feet stay fixed. The rejected prior 12-frame "walk" is the negative control.

## Hard gate 3 — mechanical file/atlas checks

- [ ] Master preserved as an editable layered source with known original; exports stored separately as RGBA PNG frame sequence/sheet plus JSON tags and frame durations.
- [ ] All frames have valid positive integer width/height, expected count and consistent cell order; no unintended crop, negative offset or inconsistent root.
- [ ] Alpha outside silhouette is 0; body pixels are intentionally opaque where desired; semitransparent glow is intentional and documented. Identify accidental white/light fringes against light and dark backgrounds.
- [ ] Verify no resampling/blurring between source, generated intermediate and final. Compare palette/color frequencies, nonzero alpha distributions and exact source pixel values when a lossless transform is claimed.
- [ ] Source atlas IDs, sprite-sheet image bounds, frame regions, pivot, timing and direction mapping match engine code. Required rectangle frame coordinates must remain within source image.
- [ ] Nearest-neighbor render and integer-pixel camera/sprite placement are checked at native, 2× and intended device scaling. CSS pixelated alone is not a proof of full pipeline quality.
- [ ] For repeating tiles: horizontal/vertical seam comparisons at 3×3 and 5×5; validate all autotile-mask classes using the intended algorithm.
- [ ] For animated scenery: loop seam/terrain direction continuity and layer painter ordering; visual art does not mutate collision, pathfinder, event or saved state.

**Automatable but insufficient:** width/height, transparent pixel count, unique RGBA count, frame hashes, exact pivot coordinates, loop duration, 1× pixel diff, grid position, border equality, label/tag presence. These do **not** establish natural gait, appealing design or absence of apparent blur.

## Hard gate 4 — gameplay integration

- [ ] Field sprite renders correctly on **actual 32×32 world tiles** with NPC crowding, walkable passages and scenery in front/behind; character may be larger than footprint.
- [ ] Correct movement direction animation selected; idle animation uses independent presentation time, not just save revision/step count.
- [ ] Collider remains anchored to foot/root, event interaction reachable, draw order by foot depth and no visual occlusion errors.
- [ ] Android landscape usable area used, no clipping or unwanted scrolling, readable HUD/buttons, correct pixel density on the target phone.
- [ ] Save/load preserves character identity, animation action if intentionally persistent, party and map state; renderer-only frames never increment journal.
- [ ] Device tests include touch/gamepad, screen rotation restrictions, app minimize/reopen, memory pressure, asset preload, low FPS and motion-heavy scenes.
- [ ] No final "passes" claim until user/physical device or documented equivalent footage confirms all visible properties.

## Review report format (one artifact and one outcome)

- Asset ID and version; source SHA/path/location (private path allowed only in private report), ownership/license, intended role and 32px-world compatibility.
- Reference/portrait ID; editable master file checksum; exported PNG sheet checksum; tag list; frame count/dimensions; direction order; durations.
- Static evaluation: silhouette/anatomy/design/materials/alpha; motion evaluation: planted foot phases, gait loop, pose legibility, continuity; runtime: scene size, device/emulator version, visual proof.
- Each gate PASS / FAIL / NOT TESTED with explanation and exact evidence.
- Document rejection and correction route; never overwrite source; do not conflate "GitHub Actions green" with "beautiful character."

## Recommended training order (reuse every pass)

1. Analyze canonical reference and sample an already-licensed original source **privately**.
2. Produce static 1× front/left/right/back artwork and have it reviewed **before** animation.
3. Author contact/down/passing/up leg poses, then mirrored/opposite contact and missing in-betweens.
4. Validate alternating world-foot contact, body movement and root alignment.
5. Add secondary animation and fault/glow clips with their own tags.
6. Export from LibreSprite; run pixel/frame/metadata validation.
7. Test in current Bearframe engine on existing 32px tiles; evaluate on an actual landscape Android device.
8. Approve only if human art review **and** technical/runtime tests pass. Archive concise critique and verified evidence in Warehouse. Retain failures.

## Credits and privacy

Avoid running paid generation automatically just because six plugins are available. Compare costs and ask where authorization is required. Use public-safe original exercises to test workflows; do NOT publish proprietary source tiles, source images or user-owned character art to this PUBLIC Warehouse. Never commit plugin API keys, asset upload tokens or presigned URLs.

## References

[Saint11 tutorials](https://saint11.org/blog/pixel-art-tutorials/);
[Saint11 pixel clusters](https://saint11.art/pixel_art_articles/article2/);
[Aseprite animation](https://aseprite.org/docs/animation/);
[LibreSprite 1.3 CLI](https://libresprite.dev/docs/cli/);
[MDN canvas smoothing](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/imageSmoothingEnabled);
[Bearframe engine](https://github.com/nobleknights015-maker/bearframe-rpg-engine);
[Atlas LibreSprite reproducible evidence](libresprite-editor-integration-v1.md).
