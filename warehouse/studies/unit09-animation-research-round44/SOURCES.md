# Round44 source ledger

Research date: 2026-11-12 (America/Chicago). Primary creator, educator and tool documentation only. Text summaries below are deliberately short. No tutorial images, copyrighted book copies, videos or proprietary art are deposited here. Source principles are distinguished from Bearframe-specific deductions. Twenty-one selected sources were read; this is a scoped research round, not a claim to have exhausted the internet.

## AM_WALK: Animation Mentor — Basic Human Walk Cycle

https://www.animationmentor.com/blog/tutorial-animating-human-walk-cycle/

Access: Read article text; embedded video not watched.

Source takeaway: Plan contacts and breakdowns; hips and chest participate; clean foot translation and roll; arms use overlap.

Project application (our inference): A full-body pose and contact schedule must be solved before decorative armor movement.

## AM_BALANCE: Animation Mentor — Tips and Tricks Volume 2, walk balance section

https://content.animationmentor.com/pdfs/TipsAndTricks_Volume2.pdf

Access: Read walk-balance section of publisher PDF; no redistribution.

Source takeaway: Weight transfer precedes lifting the other foot; pelvis and shoulders coordinate; observe references.

Project application (our inference): Do not splice an unrelated standing trunk onto a stride. A screen-space balance line is a drawing aid, not a full biomechanical proof.

## AM_PRINCIPLES: Animation Mentor — 12 Principles tutorial

https://www.animationmentor.com/blog/tutorial-12-principles-of-animation/

Access: Read article text; not embedded video.

Source takeaway: Clear posing, anticipation, arcs, overlap, timing and solid drawing support believable movement.

Project application (our inference): Build readable action poses before adding secondary hair, cable or glitch motion.

## SAINT_CLUSTER: Pedro Medeiros — Cluster Sketching and Painting

https://saint11.art/pixel_art_articles/article2/

Access: Read article.

Source takeaway: Refine large color clusters; isolated pixels can create noise, though some purposeful details use them.

Project application (our inference): Preserve continuous plate shapes and highlight groups; do not equate connected alpha with readable material.

## SAINT_ANIMATION: Pedro Medeiros — A Basic Aseprite Animation

https://saint11.art/pixel_art_articles/article3/

Access: Read article.

Source takeaway: Animation is ordered progressive images; straight-ahead and key-pose approaches are distinct workflows.

Project application (our inference): A file with eight exposures is not evidence of eight useful poses or a correct loop.

## SAINT_AA: Pedro Medeiros — Anti-Alias and Banding

https://saint11.art/pixel_art_articles/article5/

Access: Read article.

Source takeaway: Pixel placement interprets intended contours; aliasing and anti-alias choices affect readability.

Project application (our inference): Rotated masks need deliberate contour and cluster cleanup; alpha thresholding does not author those contours.

## SAINT_SCALE: Pedro Medeiros — Scaling Pixel Art

https://saint11.art/blog/scaling/

Access: Read article.

Source takeaway: Integer enlargement preserves a pixel grid; reduction needs deliberate repair, and arbitrary scaling changes pixel structure.

Project application (our inference): The prior0.42/0.46 reductions were rough material preparation, not pixel-perfect native art preservation.

## SAINT_STYLE: Pedro Medeiros — Style Consistency

https://saint11.art/blog/consistency/

Access: Read article.

Source takeaway: Keep resolution and visual style coherent; native canvas rendering and controlled enlargement help.

Project application (our inference): A correct leg contour can still look pasted on if its cluster scale and shading differ from the retained torso.

## SAINT_3D: Pedro Medeiros — Using 3D Models as Pixel Art Reference

https://saint11.art/blog/3d-ref/

Access: Read article.

Source takeaway: Rough 3D can help perspective; the author then redraws the result on another layer.

Project application (our inference): A guide rig is useful for posing, not an excuse to ship resampled cutout pieces as finished pixels.

## SAINT_TOPDOWN: Pedro Medeiros — Top Down Walk Cycle

https://www.patreon.com/saint11/posts/top-down-walk-21353953

Access: Read public explanatory text; linked GIF retrieval failed, so image details not claimed.

Source takeaway: Walks communicate personality; secondary hair or ear motion can contribute.

Project application (our inference): Apply secondary motion after the main contact/weight structure is stable.

## ASE_ONION: Aseprite — Onion Skinning

https://aseprite.org/docs/onion-skinning/

Access: Read official documentation.

Source takeaway: Previous and next frames can be shown as drawing references with configurable tint/range.

Project application (our inference): Use onion skin for silhouette continuity, joint arcs and volume, not just alignment of whole frames.

## ASE_ROTATE: Aseprite — Rotate

https://aseprite.org/docs/rotate/

Access: Read official documentation.

Source takeaway: Fast Rotation and RotSprite are available; the documentation describes different results.

Project application (our inference): Try algorithm changes only as preprocessing; neither proves anatomy or eliminates the need to redraw.

## SPINE_BASICS: Spine — Basic Concepts

https://en.esotericsoftware.com/spine-basic-concepts

Access: Read official documentation.

Source takeaway: Bone transforms propagate through a hierarchy, while slots provide independent draw ordering.

Project application (our inference): Physical limb identity, transform hierarchy and occlusion order must be separate data.

## SPINE_MESH: Spine — Mesh Attachments

https://en.esotericsoftware.com/spine-meshes

Access: Read official documentation.

Source takeaway: Mesh topology and edges affect deformation; weights are central; cutting hulls can alias edges.

Project application (our inference): A polygon mask alone is not a deformable skin with designed joint topology.

## SPINE_WEIGHT: Spine — Weights

https://en.esotericsoftware.com/spine-weights

Access: Read official documentation.

Source takeaway: Weights control bone influence; examine maximum motion ranges; rebinding changes stored relationships.

Project application (our inference): Wrong ownership can move pelvis with arm. Test identity-colored parts and extreme bends before texture.

## SPINE_IK: Spine — IK Constraints

https://en.esotericsoftware.com/spine-ik-constraints

Access: Read official documentation.

Source takeaway: IK controls rotations toward targets; bend direction, optional scaling and softness affect the result.

Project application (our inference): Do not solve an unreachable target by silently moving a body socket. Record reach failure and correct the planned whole pose.

## SPINE_SKINS: Spine — Skins

https://en.esotericsoftware.com/spine-skins

Access: Read official documentation including reuse workflow.

Source takeaway: Animations can be reused with attachment sets; similar skins can duplicate attachments and keys.

Project application (our inference): Reuse semantic motion and compatible proportions; a different chassis still needs fit and occlusion review.

## SPINE_REGION: Spine — Region Attachments

https://en.esotericsoftware.com/spine-regions

Access: Read official documentation.

Source takeaway: An attachment can use an image sequence; center and dimension alignment matter.

Project application (our inference): Discrete authored plate/joint drawings can replace excessive continuous image bending.

## PROKO_PELVIS: Stan Prokopenko — Anatomy of the Pelvis

https://www.proko.com/course-lesson/anatomy-of-the-pelvis/

Access: Read lesson notes; no claim premium video/model access.

Source takeaway: Pelvic structure and socket landmarks connect torso and legs; simplified volumes aid posing.

Project application (our inference): For this android, map reference chassis socket locations instead of treating the waist crop line as the hip joint. Human averages are guides, not mandatory character proportions.

## GODOT_FILTER: Godot — CanvasItem texture filtering

https://docs.godotengine.org/en/stable/classes/class_canvasitem.html

Access: Read official documentation; engine is not being changed.

Source takeaway: Nearest reads a nearest pixel; linear blends nearby pixels.

Project application (our inference): Nearest presentation preserves sampled edges but cannot repair distorted source silhouettes.

## GODOT_SPRITES: Godot — 2D Sprite Animation

https://docs.godotengine.org/en/stable/tutorials/2d/2d_sprite_animation.html

Access: Read official tutorial; not an engine choice recommendation.

Source takeaway: Individual frame images and sprite sheets can both form animations.

Project application (our inference): Keep frame assets, timing metadata and ground pivots explicit, independently of the chosen runtime.

## Access limits and excluded material

The Animator's Survival Kit official site could not be retrieved. A third-party full-book PDF appeared in search but was not used as a read source or saved. CMU's motion capture site timed out: no motion data was downloaded, viewed or analyzed. The Saint11 top-down post's public prose was read, but its linked GIF was not inspected. Videos linked by the articles were not watched. No paid course, premium anatomy model, new software purchase, credits or image generation were used. Search snippets from unauthored content farms and generated sprite tools were excluded from the evidence base.
