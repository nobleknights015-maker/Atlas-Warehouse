# World and battle animation: creator research and implementation

15 November 2026. This round covers animation authoring, locomotion, timing, events, registration, export and verification for the native Bearframe creator. It extends the previous Echo/Grid integration study rather than treating its old pending statuses as current code. The existing game/engine is not changed. Public documentation and first-party animation teaching are evidence; recommendations below are our synthesis. Embedded videos were not watched, whole websites were not exhaustively searched, and commercial runtimes/source art were not imported.

## 1. Result and boundary

The two new heavy defenders now have a four-direction 12-frame walk at8fps. Their shoulder armor, body, physical equipment sides and anchored growth are retained. Leg contacts drive the gait; the upper body carries a restrained compression and loaded arms swing less. Both Bulwark and Breaker use the same validated topology with equipment-dependent arm amplitudes. Old Industrial Echo, its owner-requested back-fabric coverage, crawler/orbital paths, original heavy preset, and slender/suspended studies are not replaced.

The creator also gains explicit loop/one-shot playback, per-frame holds, inert event markers, validated timing persistence and matching timing exports. These are foundations for world and combat authoring, not a claim that every unit's complete battle library exists. Slender walking, distinct weapon actions, hitboxes, real damage, sound playback and the engine consumer still require separate work and visual approval.

## 2. What the research says—and what it does not

Saint11 describes frame sequences, pose-to-pose construction and per-frame time as separate concerns [S01]. Animation Mentor's walk breakdown separates contact, compression, passing and rise; it also cautions against sliding feet [S02]. Its large-character article emphasizes body-led travel and layered/offset motion [S03]. Timing/spacing teaching explains why identical intervals and uniform motion are insufficient to communicate every action [S04]. Anticipation prepares an audience for a meaningful action rather than requiring the same stock wind-up everywhere [S05].

These sources inform a process. They do not prescribe our exact twelve frames,66% duty,20-pixel foot span, shield amplitude or JRPG camera projection. Those values are authored design choices, exposed in code and tested below. Our current weight shift is a stylized kinematic pose, not a center-of-mass/rigid-body simulation.

## 3. Findings in the actual creator

At the preceding checkpoint, `world-varieties.js` deliberately exposed idle only for grounded designs. There was no heavy gait controller. `machine-rig.js` could evaluate legacy oscillators but not contact-lock a new heavy biped. Its banner material phase multiplied the cycle by0.7, so a pose could close while the cloth's lighting pattern did not. That is now an opt-in material fix for the heavy tabard; untouched old assets keep their old path.

Preview selected `floor(absoluteClock*fps)%frames`, so every animation looped, selecting a clip could start mid-cycle, and held frames were not representable. Frame export used1000/fps for every atlas cell. Events, terminal holds and custom durations were absent. Optional supported-clip lists already prevented new studies from presenting imaginary combat motion. That capability boundary is retained and the new-world motion selector now offers only implemented controller types.

These are code-audit findings, not claims about all animation tools. The source changes and tests are in the same repository as this report.

## 4. Heavy locomotion model

`heavy-motion.js` separates contact scheduling, sagittal two-bone solving, view projection and rendering. Each physical leg has a stable L/R identity. During stance, a20-unit body-relative foot span advances linearly opposite world travel. Duty is0.66; opposite phases differ by0.5. At least one foot is therefore supporting the body throughout the sampled cycle. Swing uses a cubic Hermite return matching the stance endpoint velocity, plus a smooth bounded lift. The authored travel per cycle is20/0.66, approximately30.303 design pixels.

The thigh and shin solve with fixed lengths20 and19. The body lowers slightly during walking so the normal foot targets remain reachable without full-extension popping. Side views preserve those solved lengths exactly. Front/back views project depth into screenY at0.28 and use small lateral knee separation. Their painted segment lengths are projected lengths, not a claim of elastic armor or equal apparent length in every view.

The boots stay flat. A subtle extra issue was found: a shoe's local horizontal toe offset rotates with its parent shin even when shoe rotation is counter-rotated. The controller inverse-transforms that offset so the sole does not bob off the floor. Ground registration stays fixed; body compression does not move the exported sort/ground anchor.

The controller returns diagnostics for physical lengths, contact state and screen ankle/sole positions. Analytic support, stance cancellation and reach tests are separate from image inspection. Mathematical contact is not proof that the armor overlap or gait character looks attractive.

## 5. Travel speed and the camera contract

A moving actor and an in-place walk must share phase. For a uniform default cycle, world speed is strideLength/currentClipDuration. The default is approximately20.202 design pixels per second at12frames/8fps. The view projection maps that distance to signed screen travel; these are presentation values, not a requirement that tile collision use the sprite's overhanging armor bounds. Convert design units into the consuming game's world scale deliberately.

The translated-floor preview applies the exported stride while drawing the actual baked pose. Green markers identify stance contacts. It intentionally resets actor position after three cycles; that demonstration reset is not a walk-loop seam. Separate first/end-phase comparisons test the loop itself.

If an author adds unequal holds to a locomotion clip, the runtime must advance root displacement using the same frame-phase schedule. Advancing the root at a constant rate while freezing a foot frame causes sliding. The creator exports frame durations and indices so a future consumer can reconstruct that mapping. It does not silently turn custom holds into a physically validated gait. Reference cycle timing in the rig is labelled reference timing, not a command to override edited clip durations. Godot's root-motion documentation provides a useful separation between animation travel and actor movement [S11].

## 6. Rig safety, equipment and draw order

Spine's IK documentation separates target solving from FK authoring and documents reach/softness concerns [S06]. Its slots documentation separates attachment order from parent bones [S07]. We apply those concepts to our own JavaScript renderer rather than adding Spine. Parents establish motion inheritance; they do not establish visible attachment or correct occlusion.

A shield remains physical-left and a cannon physical-right when the unit turns. Body families, roles and history remain distinct. New authoring should declare required sockets and supported actions before reusing a pose. A six-leg gait cannot be copied to a biped. A long relay manipulator is not automatically compatible with a short humanoid arm. Unity's humanoid retargeting documentation itself depends on a configured structural mapping [S22]; it is not evidence that arbitrary topology transfer is automatic.

For the existing Industrial Echo, owner preference is authoritative: rear cloth covers the arms. This research does not reopen that sprite. New battle actions must author view-specific depth and then inspect both side views, including shields, weapons, cloak overlap and actual contact poses.

## 7. Timing, holds and one-shots implemented

`clip-timing.js` converts a clip into absolute durations and frame start times. Omitted timing preserves the old uniform-FPS loop behavior. Explicit `durationsMs` requires one positive finite value per frame. Explicit `loop:false` plays once and holds the final frame. Event records require a valid frame and a bounded nonempty name. The interval helper reports events crossed between times, including loop boundaries, without firing callbacks.

The creator's Timing & events panel edits these properties. A custom duration list overrides uniform FPS. Frame-count changes clear custom durations and rescale event positions; this is stated in the UI. Resizing a looping clip uses cycle fractions; resizing a one-shot uses its endpoint span. Pausing preserves the playback clock, switching clips starts at their beginning, and returning from a hidden tab does not consume hidden-tab time. One-shots stop at their terminal pose instead of restarting. Pressing Play again restarts a completed one-shot.

Godot SpriteFrames distinguishes speed, relative frame duration and loop mode [S10]. Pixi distinguishes looping playback, completion and frame-time objects [S23]. Our contract uses explicit milliseconds. It does not pretend that similarly named fields across engines use identical units. MDN advises time-based requestAnimationFrame progression [S18].

## 8. Events and battle authoring

Animation events should mark authored moments, not infer impacts from a random preview frame. Spine and Unity describe timeline events for actions handled by application code [S08,S21]; Godot also distinguishes editor preview from method execution [S13]. Our creator displays and exports inert markers only. It never evaluates user code, applies game damage, plays an asset path, or invokes arbitrary functions from event JSON.

The heavy walk includes left/right contact markers at frames0 and6. Future battle clips should explicitly identify anticipation, active contact/emission, and recovery. A muzzle marker can request a separate beam/effect in the consuming engine. A shield contact should coincide with the actual shield pose. Hit reactions should follow the impact rather than accidentally telegraphing it. Defeat should settle and remain down, with a recover animation only when the gameplay state allows it.

Recommended first complete action per family:

| Family | First authored action | Specific proof |
|---|---|---|
| Heavy Bulwark | Brace/block, then shield strike | Physical-left shield coverage, planted stance, impact marker |
| Heavy Breaker | Aim, charge, emission, recoil | Muzzle registration, physical-right cannon, recoil recovery |
| Slender custodian | Scan/probe interaction | Reach and tool contact, no invented fast generic punch |
| Industrial Echo | Role-specific tool use | Existing accepted body and cloth remain intact |
| Crawler | Probe scan/drone dispatch | Six leg contacts and overhanging array remain registered |
| Orbital core | Focus/emission | Ring/core depth, terminal charge hold, detached effects |
| Archive/relay | Manipulator reach/archive operation | Unequal limbs retain identity, lantern and banner mounts persist |

These are implementation requirements, not completed animations or newly approved lore. Each action needs posing and visual review; a marker alone does not make it finished.

## 9. Material continuity and pixel quality

Our painter inverse-transforms native pixels and uses hard alpha. Keep armor outline, value grouping and negative spaces readable at1x, then inspect enlarged with nearest-neighbour presentation [S19]. Review light, dark and actual terrain contexts. A native mathematical joint can be correct while its few-pixel knee plate reads as broken. Pixel cleanup therefore follows mechanics rather than replacing them.

The heavy tabard opts into an integer-turn material cycle. Its shape sway and light pattern now both close. The legacy0.7-cycle behavior stays available for untouched assets. Damage and growth are part-local; they should not regenerate randomly every frame. Rooted moss should share a visible solid mount and inherit it. Ring segment identity should be shared across front/back surfaces. Weapon flashes and glitches require separate review at final display size, not a claim of accessibility from a tiny preview. W3C's flash guidance is a review reference [S20], not a certification of these assets.

## 10. Save/export and runtime boundaries

The project container remains version2. Old clips without new timing fields remain valid. Optional rig capabilities stay opt-in. Baked frame edits remain protected by Regenerate unedited. Old saved standing studies are not silently replaced with a new recipe; select the updated preset into a separate project to obtain the new default walk set.

Both strip metadata and paged-atlas metadata now contain absolute per-frame timing, clip duration, loop mode and event times. Atlas frames use their actual hold durations. New world-unit exports also include family/role/stage, design size and motion-unit labels. Ground anchor, tile footprint, drawn bounds and future hitboxes stay distinct. Aseprite's animation/tags/sheet/slice documentation illustrates separate clip organization, images and registration metadata [S14–S17]. Spine JSON similarly demonstrates event/draw-order timelines as data [S09]. Our output is the creator's own format, not a claim of direct interchange with those tools.

Gameplay should use baked sheets/atlases rather than rerasterizing every skeletal pixel for every NPC. Retain the bounded pages already implemented. Cache nearby assets, measure decoded memory and target-device frame time, and avoid preloading every possible variant. These recommendations require a real consuming-engine test; this round does not change the engine branch or assert Moto G performance.

## 11. Verification and limits

Repeatable checks in `motion-timing-checks.mjs` cover600 support samples,192 limb/sole checks across both roles and four views,16 exact rendered loop-end comparisons, phase-consistent stance cancellation, normal reach, hold boundaries, one-shot endpoints, multi-loop event intervals, invalid timing rejection, event rescaling, atlas/strip metadata and save roundtrip. Native pixel tests elsewhere preserve the old renderer, other families and owner-requested Echo fabric.

Browser tests select a heavy preset, open the real walk clip, edit holds/events/loop mode, wait for its last frame to stop, save the project, reopen it and inspect timing fields. Numeric checks, actual editor checks, raw previews and owner approval are separate evidence layers.

Not established: dynamic stability/COM, slopes, acceleration/turn transitions, every arbitrary proportion, arm collision avoidance, all-family retargeting, final armor cleanup, complete battle actions, exported game playback or device performance. The gait is a supported flat-plane prototype with a fixed authored body, not a universal animator.

## 12. Implementation roadmap after this checkpoint

First obtain owner feedback on the heavy walk and its translated-floor proof. If accepted, pin the recipe and pixel fixtures. Then implement one role-specific heavy action through anticipation, active event and recovery with a genuine terminal pose; review its baked output in the game consumer. Build the slender gait with its own dimensions and motion personality rather than force-scaling the heavy controller. Reuse timing/events/validation/export across families, while retaining separate locomotor topology controllers.

Only after these proofs should catalogue expansion expose broader proportion/equipment controls. For malfunctions, use authored holds, misses, interrupted gestures and restrained local errors rather than random whole-body shaking. Continuity symptoms and faction/identity remain separate from a chassis and from gameplay hostility. The creator is an authoring tool; attractive, canon-appropriate motion remains a design and review task.

## Source registry and reproduction

`sources.json` records23 first-party/primary pages, their topic and application, including which were inspected as excerpts. Failed page fetches are listed separately and are not counted as evidence. No paid runtime was downloaded or bundled.

Run the creator's native and Chromium suites from `frontend`. Generate the four-direction walk and translated-floor PNG sequences with `make-heavy-walk-review.mjs` and `make-heavy-travel-review.mjs`. Encode GIF delays alternating120/130ms to represent125ms per frame on average, without duplicating the first pose at the end. Creator/export timing remains exactly125ms. The travel demonstration resets after three cycles. `verification.json` records this round's exact tested source commit and CI run.
