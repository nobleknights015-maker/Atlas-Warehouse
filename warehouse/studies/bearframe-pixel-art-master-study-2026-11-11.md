# Bearframe RPG — Comprehensive pixel-art master study

**Date:** 2026-11-11. **Evidence:** sourced professional research + existing warehouse inspection. NOT proof of professional art skill or approval of any produced sprite.

**Scope:** native pixel drawing, reference adaptation, anatomy, four directions, animation, mechanics, tilesets, color, lighting, VFX, typography, file formats, atlas imports, Android display, tooling, QA and licensing. Public warehouse stores **methods only**, not the user's purchased assets, ZIP contents or privately supplied character art.

## 0. Source-of-truth resolution

The active Bearframe RPG uses purchased **32×32 world tiles**, confirmed by the Founder, and the portable engine diagnostic uses tileSize=32. A historical warehouse record titled "Bearframe runtime terrain tilesheet geometry" prescribes a **48×48**, 384×768, 8×16 format for World Editor v1. **That is not the active Bearframe game tile size.** Treat it as a separate legacy tilesheet/editor contract, with NO automatic migration. "32-bit-style JRPG" is an aesthetic target, not an instruction to use large tiles or anti-aliased photographic scaling. The character source canvas may be taller than one 32px floor cell; collision footprint and foot anchor remain independent of visible sprite dimensions.

## 1. Drawing foundation and design

1. **Pixel clusters:** Sketch coherent large color masses before detailing. Every cluster should clarify volume, edge, material, expression or motion. Random dots and disconnected subclusters create visual noise. Saint11 advocates large-cluster-first sketching.
2. **Silhouette:** Start with one-color thumbnails at intended game size, assess negative space between limbs, recognizable helmet/shoulder/boot topology, and silhouette against dark/light/busy backgrounds. Full humanoid anatomy requires both legs, arms, feet, and plausible articulation. No "stubby limb" shortcuts.
3. **Contours and line rhythm:** Construct curves from intentional stair-stepped runs and clean diagonals, not resampled smooth curves. Avoid tangents where armor plates, legs, capes and hair accidentally merge. Selective outlines should reinforce depth; don't indiscriminately thicken everything.
4. **Color theory/value:** Assign distinct functional ramps for bone-white armor, dark mechanics, fabrics, rust, foliage, colored screens, emissive glows and selective accents. Preserve contrast hierarchy, hue relationships, colorblind and low-brightness readability. A rigid universal palette cap is not established; favor controlled purposeful colors over noise.
5. **Shading and material form:** Before scratches, model faceted helmet, torso planes, hips, thighs/shins, boots, shoulders and hands with convincing volumes. Armor, cable, fabric, CRT/glass, exposed machinery and vegetation need different light behavior and texture clusters.
6. **Anti-aliasing/banding/dithering:** Draw deliberate pixel AA only when it improves edge readability. Avoid shaded strips mirroring outlines ("banding") and blanket dithering. Do NOT bilinear/bicubic-warp the entire pixel master: nearest-neighbor cannot recover pixels already softened by interpolation.
7. **Portrait versus field sprite:** Build a detailed portrait for selection/story but *redraw* the game sprite for the intended native size. A tiny averaged screenshot is not hand-authored pixel art. Approved portrait identities must match playable sprite identities exactly.
8. **Bearframe visual canon:** Humanoid android Frames with technological chest and side-head displays. No animal/bear ears unless specified. Four Sleeper starters retain individualized approved palettes, armor, cloak/scarf/ponytail/wear and violet/cyan features; Echo-style glitch animations are separate, not permission to add new permanent damage.

## 2. Original art and anatomical animation

9. **Articulated anatomy:** Plan neck/shoulder/elbow/wrist and hip/knee/ankle linkage; armor plates overlap joints without disconnected hinges. Track segment length, hand silhouettes, boot volume and cloth attachment. Rig calculations are guides; final clusters must be edited intentionally.
10. **Directional views:** Approve coherent front/left/right/back static views before animating. Align heel baseline/root and character identity in each view. Mirroring an asymmetric Frame can put shoulder text, damage or equipment on the wrong side. Retain per-direction labels.
11. **Walking cycle:** Build contact, down, passing, up and opposite-contact leg states. A short 4–6 frame stylized cycle can work if the **actual** poses differ; 8 frames may give smoother mechanics. A 12-frame vibrating static stance does not count. Check planting/lifting, weight transfer, opposite arm swing and natural head/torso stabilization.
12. **World-space stance:** Foot in support phase remains fixed relative to the ground while pelvis/body advances. Swing foot clears ground, travels on an arc and plants with a believable forward reach. Any slip must be **intentional damage characterization**, not an implementation artifact.
13. **Timing/spacing:** Frame durations can differ. Acceleration, anticipation, holds and follow-through communicate weight. Preview the loop seam, reverse or ping-pong where appropriate; extra duplicated frames do not fix lack of key poses. Use tagged clips (idle/walk/run/attack/guard/hit/recovery/KO).
14. **Idle animation:** A small breath/helmet tilt, occasional blink, antenna/LED flicker or fabric shift can communicate life while feet remain stable. Idle is NOT a substitute for gait mechanics.
15. **Combat poses:** Prepare weapon/hand/target line and clear anticipation, strike, contact, recoil, return. An effects layer may accent impact but must not hide the decisive pose. Body rotation/grounding matter more than excess particles.
16. **Mechanical faults:** Core and visor glitches, freezes, desync, short actuator stutters and recovery are **separate** timed clips, preserving design and original wear. Distinguish intentional malfunction of Echo-style Frames from bad frame registration.
17. **More-than-two legs:** Map each physical limb, alternating support sets, moving chassis and stable stance points. Avoid overlaps that imply missing legs or reverse-bending joints. Validate foot anchors and far-side readability frame by frame.
18. **Subpixel concept:** Convey fractional apparent motion by *redrawing* integer-pixel clusters frame to frame; do not use soft image warping to interpolate the rendered sprite.

## 3. World art, visual effects and interface

19. **32px tilesets:** Import the user's existing 32×32 art without resizing. Document source sheet margins, spacers, tile order and license; support multi-cell objects with independent collision. Keep 48px editor sheets in their historical format unless explicitly converted as a separate pipeline.
20. **Seamless terrain:** Test 3×3/5×5 repetitions, isolated island, inner/outer corner, L/T/plus shapes, roads, water banks, cliffs, bridges and edges on real neighboring tiles. Seamless edges alone do not guarantee convincing terrain patterns.
21. **Autotiles:** Four-neighbor Wang edges, 16-piece dual-grid corners and 47-mask "blob" autotiles are DIFFERENT indexing algorithms. Do not shuffle sources into a guessed order; document bit masks and transition priorities. Test corner/topology cases before decorating.
22. **Depth/collision:** Render base terrain → ground decals → Y/foot-sorted actors → canopy/foreground. Collision and event triggers come from world data, not from decoration colors or alpha. The engine's layered-scene tests are evidence of technical composition, not of polished world maps.
23. **Environmental loops:** Water flow, fire, steam, grass, rain, snowfall, clouds and LED signals should cycle seamlessly. Prevent flashing seams, incoherent flow directions, scale mismatches or random flicker. Keep scene animation time separate from deterministic world/save state.
24. **VFX:** Build readable buildup/contact/dissipation phases, palette contrast and local opacity. Track anchors to target/action. Reserve additive glow for effects when appropriate; hard silhouette armor edges must stay crisp.
25. **UI, portraits, typography:** Learn 9-slice panels, scalable menus, crisp icons, readable status indicators, original game-consistent font metrics and mobile safe-area layouts. Test bright/dim outdoors and actual landscape gameplay.
26. **Camera/sprite occlusion:** Pixel-snap source and destination coordinates, sort actors from feet/root, cull offscreen tiles/effects, and profile dense maps. More detailed art is not better if it destroys navigational contrast.

## 4. Exporting and engine compatibility

27. **Editable masters:** Keep a native layered .ase / .aseprite document, palettes, named layer roles, actual per-frame cels, frame tags and durations. Export independently as RGBA PNG frames and sprite sheet + JSON; GIF is a preview, not the canonical source.
28. **Alpha correctness:** Character body edges generally need deliberately drawn hard pixels, but controlled partial alpha is valid for glow/fog. Examine both white and black checkerboards and prevent white fringes. Reject accidental alpha halos; don't blanket-threshold intentional VFX.
29. **Nearest-neighbor at every resize:** No image interpolation for native sprite transformations. In the browser Canvas set imageSmoothingEnabled=false. In CSS, image-rendering:pixelated may help but integer-scale rendering with pixel snapped geometry is the strongest visual guarantee. A smooth original screenshot is *not* rendered sharp merely by setting nearest neighbor later.
30. **Atlas geometry:** Verify every source rectangle is within bounds; keep frame size and foot pivot stable or supply correct per-frame trim offset. Avoid texture bleeding between neighbors with appropriate padding/extrusion if sampling/filtering requires it. Check source and output pixel-equivalence where possible.
31. **Motion playback and performance:** Rendering frames may run on a presentation clock even while the saved gameplay state is unchanged. Pause/throttle hidden/backgrounded views, handle device sleep/resume, verify 30/60 Hz frame pacing and low-memory recovery. Do not claim physical Android success based solely on a green compile.
32. **Source rights:** Purchased art belongs in private/user-authorized workflows, not public Atlas Warehouse. Preserve license/credit manifest and avoid uploading modified packs, commercial assets or character source to PUBLIC GitHub.

## 5. Our GIF failure: retained as a negative benchmark

- Screenshot/rescaled source, then global smooth warp, then repeated resizing: irreversibly softened clusters and partial-alpha fringes.
- No true alternating contact/pass/plant cycle; boots stayed fixed while legs distorted. Increasing frames/FPS/sharpness cannot repair the absent poses.
- No native 1× side-by-side frame critique and no verified clean original PNG before processing.
- Required correction: actual editable source → clean static pose → first full keyframe silhouettes → planted foot/hip arc proof → pixel cleanup → native tagged sheet → GPU/Canvas phone test → visual approval.

## 6. Research references

Authoritative/native:
- [Saint11 pixel tutorial library](https://saint11.org/blog/pixel-art-tutorials/) — human walk, top-down walk, idle, banding, tiles, effects and 9-slice.
- [Saint11 cluster sketching](https://saint11.art/pixel_art_articles/article2/); [anti-aliasing and banding](https://saint11.art/pixel_art_articles/article5/).
- [Lospec beginning pixel art](https://lospec.com/articles/pixel-art-where-to-start/), [curated cluster tutorials](https://lospec.com/pixel-art-tutorials/tags/clusters).
- [Aseprite animation docs](https://aseprite.org/docs/animation/), [sprite structure](https://www.aseprite.org/docs/sprite/), [color modes](https://www.aseprite.org/docs/color-mode/), [sheet export](https://aseprite.com/docs/sprite-sheet/), [source files](https://aseprite.org/docs/files).
- [LibreSprite v1.3 animation](https://libresprite.dev/docs/animation/), [CLI](https://libresprite.dev/docs/cli/); verify CLI usage against the 1.3 binary in our GitHub runner.
- [Godot stable 2D animation](https://docs.godotengine.org/en/stable/tutorials/2d/2d_sprite_animation.html) and [TileSets](https://docs.godotengine.org/en/stable/tutorials/2d/using_tilesets.html) — transferable concepts, NOT a proposal to switch engines.
- [MDN Canvas smoothing](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/imageSmoothingEnabled) and [MDN image-rendering](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering).

Project evidence:
- [LibreSprite confirmed integration](libresprite-editor-integration-v1.md) — technical tested, visual quality not approved.
- [Layered LibreSprite trial](libresprite-layered-idle-study-round-09.md) — editor/alpha tests passed, design review failed.
- [Round 19 source-based Unit09 poses](round19-unit09-first-source-based-animations-qa.md) — source derived, no full independent authored walk, not game ready.
- [Engine CI and source](https://github.com/nobleknights015-maker/bearframe-rpg-engine).

**Signoff hierarchy:** sourced/researched ≠ editor mechanics tested ≠ visually excellent ≠ physically device accepted ≠ production approved. Preserve failure notes as rigorously as successes.
