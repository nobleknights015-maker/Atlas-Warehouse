# Bearframe all-cardinal pixel animation research — Round44

This is a research and forensic audit, not an art revision. It covers S/front, N/back, W/left and E/right, whole-body animation and the later character/action transfer method. No approved character frames, engine code, APK or saves were modified. Front/S and back/N remain the user-approved visual baselines. Revision42 side work was rejected; revision43 is a closer two-contact-pose experiment with an unresolved body integration problem, not an approved side walk.

## What actually went wrong

The evidence supports multiple interacting failures, not one missing tutorial or one magic rig setting.

1. **The source anatomy was not the constraint.** Mask fragments were fitted to independent rig targets instead of authoring whole poses that retained the reference's pelvis, thigh plates, shins and boots. Source ownership was initially wrong, including pelvis/thigh regions in a supposed far-arm mask. Renaming masks did not restore material volume.
2. **A guide skeleton was treated as final pixel artwork.** Nearest-sampled rotation of cutouts preserves some numerical properties but changes contours and color clusters. Fixed axis lengths cannot prove visible leg thickness, plate continuity, correct occlusion or human body coherence.
3. **The supposed upper-body lock retained more than the upper body.** In revision43 the old torso layer contains old pelvis material through row95 and is composited over the new complete walking lower body. A blanket byte lock froze a conflicting pose. Preserving design and preserving every old-pose pixel are different constraints.
4. **Reference scales and rest poses were mixed.** Revision42 used uniformly reduced contact-pose thigh/shin material and unscaled standing-pose boots. Each part could be individually plausible while the assembled source scale, foot orientation, socket locations and shading did not agree.
5. **The latest splice has a phase and pose problem.** Revision43 pairs standing-derived torso/arms with a long contact stride. The prior response identified uprightness as the cause without measuring trunk orientation; that was too confident. The confirmed issue is incompatible source poses and pelvic overlap. Exact tilt, socket placement and arm phase must be established from matched landmarks, not guessed from appearance.
6. **Numeric checks were promoted beyond their meaning.** Connected alpha only detects disconnected islands. A singleton pixel line can connect a mangled leg. A zero-drift declared sole point can be constructed to pass while the boot slides, the wrong foot supports, or the waist is incoherent. Export readback is file integrity, not artistic acceptance.
7. **The work expanded before its underlying pose was right.** Rebuilding an entire eight-frame cycle, packaging it and calling remaining failures 'polish' repeatedly multiplied rejected geometry. Body-plan and silhouette errors are blocking failures.
8. **The reference itself must be interpreted.** A standing sheet, a three-pose detail sheet and a six-pose row are different inputs. Their drawings can differ in details and proportions. Six source poses must not be described as a fully authored eight-pose cycle. Extracting the whole original sheet changes more than the legs, which the user explicitly rejected.

## Measured local audit

These values come from audit_assets.py and audit_results.json, not internet sources.

- In revision39 the actual hip socket relocation from its source position plus bob is0–1.002586px in both side directions. The earlier claim that the solver simply shortened the legs was not an adequate verified explanation. The code can change along-axis image sampling when target segment lengths differ, but fixed-length later variants still failed; visible distortion is broader than bone length.
- In revision43 the old torso overdraws72 opaque pixels of the W new lower silhouette and101 of E. The overlap occupies rows76–95.
- The old torso layer has136 W and130 E opaque pixels at y84 or below. This is why treating the whole layer as an untouchable torso lock is unsafe.
- Overlap itself is necessary and these counts do not mean every one of those pixels is wrong. They identify the region needing pose-aware ownership and contour inspection.
- Front/S and back/N:58 files each in revision41 are byte-identical to the corresponding approved copies in revision43. This verifies preservation, not new physical acceptance.
- The audit image isolates old torso, new lower art, their red-marked intersection and the composite. The image and private artwork stay in the owner's evidence packet, not the public warehouse.

## The corrected technical model

### Anatomy, ownership and occlusion are separate

Store physical left/right limb IDs, semantic part IDs and view-specific near/far roles. 'Leading foot' is not 'near leg'. A leg passing forward does not automatically become the foreground leg. Render order depends on camera orientation and local overlap; it is not determined by a bone's array index or the frame number.

Use a distinct ownership map for head/hair, neck, ribcage, waist, pelvis belt, hip socket covers, upper legs, knee covers, lower legs, boots and arms. Armor that bridges a joint may require a separate cover layer rather than being baked into both parts. Masks must be viewed with identity colors, with no texture hiding a wrong assignment. The source is an image, not automatically a reliable anatomical segmentation.

The pelvis should be posed as a coherent connecting volume. The hip socket is inside that volume; the waistline is not the socket. Map socket and surface landmarks to the actual character. Human anatomy lessons help structure the drawing but do not override this android's reference proportions or mechanical joints. [PROKO_PELVIS]

### A hidden rig may guide the work

A correct bind setup needs pivots, rest-pose relationships, influence ownership, joint padding, topology if using a mesh, and view-specific draw order. A polygon cutout is not automatically a skin. Unpainted hidden areas cannot be recovered by rotating visible fragments; they need source-supported reconstruction or drawing.

Rigid plates should keep their shape and rotate around plausible joints. Flexible understructure can connect them, but it must not turn into a visible generic stick skeleton. Avoid large image warps across hard armor. For extreme bends or new overlaps, choose or draw alternate whole joint/plate images. The same pose should still read correctly with all rig guides hidden. [SPINE_BASICS, SPINE_MESH, SPINE_WEIGHT, SPINE_REGION]

Spine documentation is a conceptual reference, not a recommendation to buy or switch to Spine. It does not establish that our existing masks or topology are correct. IK helps place feet, but its reach, bend direction and optional scaling need deliberate control. A failed target should trigger correction of the planned body pose; silently moving a socket, stretching armor or deleting silhouette pixels is not a fix. [SPINE_IK]

### Author a whole pose, not independent half-bodies

Keep the chosen design: head, hair, visor, armor language, proportions and feminine baseline. Preserve approved S/N files as baselines. For the rejected sides, upper-body *design* is protected; its translation, shoulder/pelvis relationship and occlusion may need pose-aware changes. Do not change an approved direction under the label of research.

Solve root/ground, pelvis, ribcage, neck/head and limbs in one reference pose. Transfer the weight before lifting the other foot. The contact pose and the weight-bearing passing pose are different tasks. Small torso and shoulder adjustments may be sufficient; a large generic forward lean is not automatically correct. [AM_WALK, AM_BALANCE]

For the sides the long limb silhouettes and fore/aft relationships are conspicuous. Front/back project much of the same movement toward/away from the camera; they need their own drawings and foreshortening. They are not side sprites squeezed horizontally or vertically. User approval of S/N is retained; it is not dismissed as an error merely being hidden.

### Draw and check pixel clusters at final art resolution

Choose one explicit native character scale before building the cycle. Canvas padding is not character resizing. Native32x32 terrain does not force32x32 character frames. Any later map-size redraw is its own art decision.

Nearest sampling avoids blur but does not preserve the structure of reduced or rotated clusters. Non-integer reduction drops and redistributes pixel information. Repeated transforms compound the problem. Use a guide once, then redraw the intended contour and main color groups. Correct near-leg width, thigh plate coverage, knee silhouette, shin shape and boot toe/heel before adding texture. Avoid random orphan pixels, flashing highlights and jagged plate edges that change topology every frame. RotSprite is a possible editing aid, not a correctness certificate. [SAINT_CLUSTER, SAINT_AA, SAINT_SCALE, ASE_ROTATE]

A rough 3D or 2D pose guide can help perspective, but the source creator's workflow explicitly includes redrawing; rendering a guide and scaling it down is not a final-art method by itself. No new generated illustration is required to fix this. [SAINT_3D]

### Whole-body walk timing and contacts

Use the phase scaffold: contact A, compression A, passing A, rise A, contact B, compression B, passing B, rise B. These are motion events, not a mandatory eight-frame export. A restrained JRPG cycle may use fewer drawings with intentional holds. Do not insert a standing pose solely because it is the first cell on a sheet. Identify the correct cyclic order and seam from which foot supports and which leg advances.

Maintain one phase clock across directions. Hips and shoulders have a coordinated relationship; arms counter the relevant leg rather than sharing an arbitrary sine. Head/hair/cables follow the body with restrained offsets after the main motion works. Uniform100ms per drawing is a review default, not researched physical timing. Film24fps examples must not be copied as an engine requirement. [AM_WALK, SAINT_ANIMATION, SAINT_TOPDOWN]

Define a support event and an actual heel/forefoot contact patch. During an interval with a stable planted point, world_root(t) + projected_local_contact(t) stays fixed. Heel-to-toe roll changes the relevant contact point; do not apply a fixed-point assertion across incompatible contact modes. Test both moving-root and treadmill displays, with visible ground marks and an unambiguous ground line. A shadow is a readable cue, not proof that support mechanics pass.

Engine travel and animation cadence are separate contracts. If one32px tile takes T seconds, the cycle schedule must be matched to that travel deliberately, not by assuming one cycle always equals one tile. Up/down may have different projected foot arcs but should not silently run at different gameplay speeds. No engine integration was performed in this round.

## Human-like mechanical and feminine motion

This is a project art direction, not a biological law. Preserve the feminine motion already preferred by the user. Build it from the character's posture, cadence, balance, arm carriage and reference stance. Do not use exaggerated hip swaying, leg thinning, extra narrow stepping or a generic stereotype as an automatic 'female' switch. Rigid chassis plates remain rigid; joint timing and controlled follow-through can carry the human quality. Degraded Echo/Ghost Grid irregularities are character-specific and should not be added to every Sleeper or practice frame.

The later masculine set can reuse semantic phases, ground events, source annotations and quality gates. A different body plan needs its own landmark fit and silhouette drawings. Color swaps, mirroring an asymmetric chassis, or one shared limb mesh are not reliable universal retargets. Skin reuse documentation shows a mechanism, not proof that anatomically incompatible sprites can share all deformations. [SPINE_SKINS]

## Decision

The next implementation is a pose-to-pose, whole-body correction on the preserved side design. Existing source images are evidence and material reference; cutout rotation is not the final drawing process. A rig may help establish landmarks, but every major contact/passing pose must hold the actual silhouette and armor coverage at native size. Only after this passes should the full loop be expanded. The explicit implementation gates and all-four-direction/action coverage are in CORRECTION_PLAN.md. Research does not mean the side animation is now fixed.
