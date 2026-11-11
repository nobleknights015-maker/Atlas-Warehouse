# Bearframe Pixel Art Study — Round 06: Relay Portrait Design

Status: TRAINING, NOT PRODUCTION-APPROVED. This is a public-safe research/method record; no private conversation or reference images are stored here.

## Initial defect
Round 05 flattened Echo-L118 "Relay" into a nearly symmetrical, rounded frontal helmet. Despite cleaner pixel clusters, it lost the original character's angled CRT display, asymmetric torn hood, broken relay ring, layered scarf, and shoulder architecture. A technically clean sprite can still be poorly designed.

## Research
- Pedro Medeiros, Character Design 1 (2016): silhouette and story before detail: https://www.patreon.com/saint11/posts/character-design-7530899
- Pedro Medeiros, Portraits (2017): portrait structure, proportions, reference: https://www.patreon.com/saint11/posts/portraits-8693396
- Pedro Medeiros, Cluster Sketching (2021): begin with big intentional color clusters: https://saint11.art/pixel_art_articles/article2/
- Pedro Medeiros, Basic Shading (2021): model directional planes, avoid pillow shading: https://saint11.art/pixel_art_articles/article4/

## Experiment performed (November 2026)
An original 144 × 144 RGBA training portrait was constructed from manually authored integer-pixel polygon/line edits in Python/Pillow, rather than AI image generation, reference resizing, or tracing. Four layers of design feedback:
1. Black silhouette of ring, hood, CRT-head, scarf and shoulders.
2. Angled bone and metal planes, off-axis CRT signal, chest light, violet fabric.
3. Rooted seam-moss, chipped armor, attached cracks and oxidation.
4. Display-only timing corruption, with held body, in six irregularly timed frames.

QA: exact 144x144 RGBA; binary alpha, no antialiasing; 25 colors; visible silhouette bbox (8,3,134,144); 13,547 opaque pixels. Checked at true 1x against pale and dark backgrounds. Native drawing source: relay_portrait_shape_lab_v6.py from Round 06 project chat; user can recover that file from the chat. Images intentionally remain in the training session, not the public warehouse.

## Observed improvement and failure
- Better reference-specific outline and detail hierarchy than frontal Round 05. Character reads as hood + tilted CRT + separated broken ring at native scale.
- Still too rounded compared with Relay's angular, dimensional original helmet. CRT face should feel more rectangular and oblique. The shoulder scarf hides too much of the mechanical structure; growth is still too sparse.
- Glitch animation demonstrates only localized display corruption, NOT convincing locomotion or body malfunction.
- Coordinate/alpha validation is not artistic approval and is NOT evidence of professional mastery.

## Next exercises
Draw an explicit 3/4 planar helmet with a sharper oblique CRT quadrilateral; reserve negative space around broken ring. Practice paired shoulder armor/scarf folds and natural moss that grows from seams. Compare 1x silhouettes before texture. Continue all existing animation, gait, anatomy, materials, degradation and glitch behavior studies.

Memory cross-links:
- pixel-art-comprehensive-bearframe-visual-f99a28a2a0
- lore-ghost-grid-and-echo-frame-anci-e08d91cd6e
- pixel-art-native-pixel-art-training-and-84bb0587a8
