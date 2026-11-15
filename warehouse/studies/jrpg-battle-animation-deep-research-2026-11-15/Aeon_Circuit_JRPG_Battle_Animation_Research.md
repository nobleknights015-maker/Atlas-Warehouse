# Aeon Circuit: JRPG Battle Animation Research

**Enemies, player characters and NPC party members**  
**Research date:** 15 November 2026  
**Status:** Source-grounded production guide and audit. Proposed changes have not been implemented.  
**Baseline audited:** creator commit `fd4f006d8c5c160403190dcb16a87854686987ec` and Six Unit Battle Animations v1.

## 1. The finding that changes the work

A JRPG battle animation is a staged relationship between an acting character, an intended target, the visible effect, the target's response, and the return to a readable battle state. A moving arm with a muzzle flash is one component. Even a mechanically sound component can look weak when it is presented alone or has no convincing opponent response.

For Aeon Circuit, the next production unit should be **one finished exchange between an attacker and a target in the intended battlefield view**. It should include a normal hit, a miss and a guarded hit. Expanding another catalogue of isolated motions before this exchange works would multiply the current shortcomings.

The existing creator has useful engineering: stable registration, timed exposures, one-shot completion, fixed-length support solving, authored equipment sides, event markers, frame-local action origins and reproducible atlas exports. Keep these. Its current content is a technical animation candidate, not the final JRPG presentation standard. Source-code and pixel-integrity tests establish different facts from artistic acceptance or player understanding.

The three roster categories need a common presentation contract, with different animation priorities. Player characters need responsiveness, recognizability and skill identity. Enemies need understandable intent, credible impact and readable vulnerability. NPC party members need the same visual competence as other party actors, plus distinct choices and personality; their AI or guest status does not justify lower-quality poses.

**Evidence boundary:** Sources below include developer-authored articles, an interview with the actual development studio, original artist teaching and official tool documentation. Retail gameplay was not captured or measured frame by frame. Embedded videos were not watched in full; video-description references are labeled accordingly. Proposed millisecond budgets are our starting hypotheses, not extracted Phantasy Star or Sea of Stars timings. No commercial game sprites, code or sound assets were copied.

## 2. What the reference games and tools actually teach

Sabotage's creative director describes turn-based decisions, timed actions, multi-character combinations, interruptible enemy preparations and party swapping. These features make animation timing part of battle communication, rather than decoration. This documents Sea of Stars' design, not a requirement that Aeon Circuit adopt timed button presses or its entire combat model. [S01, S02]

Acquire's Octopath Traveler II interview connects changes in character proportions to the room available for action, and describes the camera difficulties of mixing flat pixel characters with dimensional backgrounds. It supports deciding the battle view and pose readability together. It does not mean Aeon Circuit needs a 3D engine, HD-2D lighting or extreme camera rotations. [S03, S04]

The Octopath Traveler 0 developers describe each recruited character as requiring artwork, pixel art, abilities and effects. The useful production lesson is to budget a recruit as a functioning kit, not as a portrait plus a walking sheet. No specific budget or team size from that game is transferred to this project. [S05]

RPG Maker MZ documents a compact actor-motion sheet with three patterns per motion and separate loop/one-shot playback. Its enemy-image standard is a different asset contract. These are examples of how a JRPG tool can separate character motion from battle effects; the layout is not a universal JRPG format, and it does not automatically animate an enemy sheet in our engine. [S06, S07]

RPG Maker MV's animation editor independently places effects around a target's head, center, feet or the screen, with scheduled sound/flash timings. This is useful evidence for separate target anchors and effect timelines. MV documentation is cited as MV behavior, not as a claim about MZ's current effect implementation. [S08]

Slynyrd's original pixel-art lessons distinguish fighting stance, punch mechanics, directional weapon use, rapid striking motion and settling. His top-down attack examples give different timings to different weapons while preserving the physical weapon hand. These are action-game examples whose principles must be adapted to queued JRPG combat, not copied as universal timings. [S09-S12]

## 3. Choose the battlefield view before drawing the complete roster

There are three viable families of presentation. Our recommendation is to compare the first two in a static battle mock-up, then lock one primary view before redrawing full battle libraries. This report does not decide the user's final camera or change the engine's existing UI.

| Presentation | Primary asset needs | Strength for Aeon Circuit | Production cost or risk |
| --- | --- | --- | --- |
| Rear-party, front-facing enemy composition | Party backs or rear three-quarter battle poses; enemy front/three-quarter poses | Strong fit for the requested Phantasy Star influence; large, readable enemy acting | Party hand/tool contact needs careful foreshortening; portraits/UI carry some expression |
| Opposing side or three-quarter formations | Party and enemies face each other across the stage | Easy to read melee distance, weapons, blocks and projectile paths | Pure profiles can flatten humanoids; mirrored asymmetric equipment is unsafe |
| Battle staged directly in the exploration scene | Formation placement, local depth, broad angle coverage, environment-aware staging | Strong exploration-to-combat continuity | Occlusion, navigation, camera and per-angle art requirements grow substantially |

Slynyrd's JRPG landscape article explicitly reserves central space for front-facing monsters and lower foreground space for rear-facing heroes in a Phantasy Star IV-inspired composition. That is an artist's documented reference design, not direct measurement of Sega's original animation implementation. [S13]

A camera contract should state the ground-plane projection, main enemy and party facing, formation slots, allowable camera movement, sprite scale, effect depth layers, UI exclusion regions and the widest supported boss. Test the tallest unit, smallest unit and longest weapon together. A camera that fits a small humanoid may hide a crawler's target point or clip a large halo.

Four cardinal exploration directions do not establish that four cardinal battle views are sufficient or necessary. A fixed rear-party battle can need an authored rear three-quarter hero pose absent from a cardinal sheet. Conversely, a fixed side battle need not spend the full art budget on unseen north/south battle attacks. Preserve the established four-direction exploration contract and author battle views according to the chosen camera.

## 4. Battle-ready poses are acting, not a standing sprite with a glow

A useful battle idle shows readiness and the character's method of fighting. It establishes the starting silhouette, balance, weapon grip, gaze and preferred distance. It is the pose to which the player will repeatedly return, so its identity matters more than the amount of continuous movement.

For a guarded ancient chassis, readiness might be a lowered center, shield slightly forward and a protected core. A precise survey unit can keep the probe stable while the head acquires a target. An unstable Echo can show an occasional interrupted correction rather than a full-body shake. A hovering archive unit can stabilize its lantern while its manipulators settle at different speeds. These are proposed acting directions, not additional lore or approved abilities.

Slynyrd treats the fighting idle as an important expression of personality and builds attacks out of the established stance. His example's particular martial style and human anatomy are not universal templates for our androids. [S10, S11]

Use a black silhouette test at the actual gameplay size. The viewer should identify the facing, primary weapon and action intent without glow effects. Then test values and color over light terrain, dark ruins and busy backgrounds. When the body motion is unclear without an effect, adding a larger effect usually hides the problem.

Make three deliberately different key poses first: preparation, decisive action and recovery. Add a distinct contact/impact pose when needed. Avoid filling sixteen evenly spaced exposures before the key poses communicate. A smear or a held frame can carry more useful information than several small arm-angle changes.

## 5. Timing: distinguish responsiveness, telegraphing and spectacle

Three clocks must be considered separately: simulation/decision time, the presentation sequence's elapsed time, and the artist's exposure durations. A game can render smoothly at 60 Hz while displaying a body pose for 80 ms. Sixteen exported exposures do not imply sixteen distinct poses or one particular quality level.

Animation Mentor describes contrasting holds and spacing as tools for rhythm and weight. Arc System Works' Guilty Gear Xrd presentation describes deliberately hand-posed limited animation instead of automatic interpolation for its particular visual goal. Neither source says every game should remove interpolation everywhere. For our pixel-art bodies, deliberate exposure selection is preferable to assuming more smooth samples will create stronger acting. [S15, S38]

There is an important context conflict in the teaching: Saint11's minimal action-game attack discussion favors immediate visible action to avoid input delay, while general anticipation teaching emphasizes preparing the viewer. These address different needs. A queued JRPG command can acknowledge input immediately with selection feedback, then present a short, readable wind-up. A dangerous enemy's tell may need substantially more warning than a routine player jab. [S14, S37]

**Proposed initial timing experiments, not industry rules:**

| Action class | Preparation | Fast action / travel | Impact emphasis | Recovery | Initial whole-action target |
| --- | --- | --- | --- | --- | --- |
| Routine player melee | 80-160 ms | 50-120 ms, plus approach if needed | 30-60 ms local hold | 120-220 ms | About 450-800 ms with repositioning |
| Routine enemy strike | 160-300 ms | 60-140 ms | 40-70 ms | 160-280 ms | About 650-1,000 ms |
| Precise ranged shot | 100-220 ms | 40-90 ms firing; separate travel | 30-60 ms | 100-200 ms | About 500-900 ms including flight |
| Support / repair action | 120-240 ms | 180-350 ms delivery or field | Clear receive/cure beat | 120-220 ms | About 650-1,200 ms |
| Heavy signature / boss action | 250-600 ms or a turn-level tell | 80-200 ms per major beat | 50-100 ms, used sparingly | 250-500 ms | About 1,000-2,400 ms |

The phase ranges are experiments, not sums that every action must reach. Some overlap: the shooter can recover while the projectile is in flight. Repeated normal attacks should stay economical; uncommon signature moves can spend more screen time. A large machine can convey weight through recoil, delayed secondary motion and balance rather than making every phase slow.

Never use one shared duration array for every weapon. A thrust, shield bash, pulse beam, thrown device and area field should have different accents. Do not use the same lengthy setup for every repeated enemy action merely because a boss once needed a readable tell.

## 6. The complete exchange: actor, transport, contact, result

A battle action needs at least five coordinated tracks: actor motion; projectile, trail or area effect; target response; audio; and presentation/UI feedback. Camera emphasis is an optional sixth track. A single sprite clip cannot by itself specify the whole exchange.

For melee, stage a plausible reach. In a formation battle this may be a brief advance to an attack point, a pose with authored reach, a contact event and a return. If a stationary long-range slash effect carries the attack instead, the fiction should make that clear. Do not make a short hand movement across a large empty screen gap appear to physically strike an enemy.

For ranged attacks, separate launch from arrival. The muzzle event creates the projectile or beam. A projectile impact event belongs to its arrival at the target, not automatically to the shooter's firing frame. A beam can connect much sooner than a slow orb, but its target reaction still needs a deliberate common event.

For support actions, show who gives and who receives. The healer may gesture while a repair drone or field travels; the recipient receives a positive response and state feedback, without a damage recoil. An item needs its own throw/use/receive grammar. The recipient can remain still if the field itself clearly explains the outcome.

**Proposed shot example:** preparation 0-160 ms; aim hold 160-280; discharge at 320; projectile flight 320-480; target contact at 480; short impact hold 480-530; target recoil/recovery 530-780. Shooter recovery can finish earlier. This example illustrates separate events, not a final committed animation.

## 7. Player-character requirements

The playable Sleeper is not a modern Bearframe. Preserve the established identity, chassis, damage and silhouette. A new animation should not silently repair the old core, replace body parts or introduce modern equipment. Weapon changes need compatible grips and action poses while retaining the same character design.

The player library should cover battle entry, ready idle, selected/command acknowledgement, normal attacks by supported weapon family, skill preparation, skill release, item use, guard entry/hold/exit, light/heavy hit reactions, evade, downed state, allowed revival/restart, escape and victory/relief. Add low-power or critical-condition acting when it is a real persistent state. Do not create every possible action for every weapon before identifying the actual playable kit.

A normal weapon action should be the fastest path to proving quality. Choose one actual intended weapon and one actual intended enemy silhouette. Author the grip, stance, target point, contact and return. The hand should not slide around the weapon between frames. A visible muzzle must clear fingers and armor. A long weapon needs the off-hand socket and shoulder/hip contribution; it cannot be treated as a recolored short blade.

Skill identity should be expressed through more than effect color. A precise shot, area scan, disruptive pulse, emergency repair and risky overload should differ in posture, targeting pattern and timing. Reuse a compatible preparation pose when it genuinely fits, but do not make every ability the same arm raise with a new ring.

The protagonist's action response must remain understandable when sound is muted and when effects are reduced. If timed inputs are eventually adopted, author an obvious stable action cue and test its actual input window. Timed inputs are a separate game-design decision, not assumed by this animation plan. [S01]

## 8. NPC party members, guests and support actors

Separate the actor's identity from its controller. A player-selected companion, an AI-controlled guest and a temporary allied unit can use the same animation vocabulary. AI chooses an action; the presentation system should receive the same typed request and produce the same quality of result.

| Ally function | Distinct acting priority | Required exchange evidence |
| --- | --- | --- |
| Defender / protector | Weight, interposition, readable shield coverage | Ally threatened, protector enters, shield intercepts, protected ally spared the hurt pose |
| Precision attacker | Stable aim and economical motion | Target acquired, correct muzzle path, delivery, localized recoil |
| Repair / support specialist | Attention toward the recipient and controlled tool contact | Source-to-recipient connection, positive receive state, clear completion |
| Disruptor | Preparation with a distinct failure/interruption vocabulary | Enemy channel visibly destabilizes, cancellation reaction, state change shown |
| Mobile striker | Anticipatory lean and committed approach/return | Formation origin retained, valid attack point, no sliding or instant teleport |
| AI guest | Predictable intent and restrained non-commanded acting | The guest's action reads clearly without stealing the player's selection focus |

These functions are animation design categories. They do not assign unapproved jobs to canonical characters or reveal story content. A recruitable Echo or Ghost Grid unit should retain its existing mechanical identity when changing teams. Hostility and allegiance are gameplay relations; they are not excuses to mirror away a physical tool or remove a malfunction.

Support allies need active, specific motions. Repairing can involve stabilizing a receiver, engaging a tool, a brief transfer pulse and releasing contact. A protective intervention can use a short slide or step to an intercept slot and a braced hold. The target should not flinch first and then have a shield appear afterward.

Party swaps need exit, clear-slot and enter/settle events, even when the movement itself is brief. An offscreen reserve can use a minimal entrance, but the incoming unit's stance, condition and weapon must match its actual battle state. Do not reset a critical-condition actor to a healthy idle merely because it entered the formation. Sabotage's account of free party swapping is a useful example of a system that makes these transitions part of combat flow. [S01]

## 9. Enemy animation requirements by encounter role

An enemy needs enough motion to communicate what the player can understand and respond to. It does not automatically need the same number of clips as a permanent player character. A simple stationary turret can be convincing with a strong acquisition pose, recoil, disable reaction and destruction; a transforming boss may need several entirely separate state libraries.

Routine enemies should have a readable idle, at least one distinctive attack, hit response and exit/downed outcome. Add a tell, stagger, guard, exposed state, interrupt reaction and special move only when the encounter actually uses them. If an enemy has a meaningful counter, shield, weak point or charge, those conditions need visible states rather than silent stat changes.

| Enemy type | What sells its action | Common failure to reject |
| --- | --- | --- |
| Heavy biped | Support shift, equipment-led anticipation, recoil absorbed through chassis | Everyone remains rigid while only a forearm rotates |
| Slender machine | Precise acquisition, controlled extension and deliberate reset | Slow floppy motions that imply a heavy body |
| Six-leg crawler | Credible support polygon, body compensation, tool/head independence | Biped motion pasted onto a body with six sliding legs |
| Hovering / orbital unit | Stable ground projection, controlled offset, consistent core/ring depth | Entire sprite bobbing randomly or core swapping front/back depth |
| Turret / anchored device | Mount resistance, charge/readiness cue, localized recoil | Feet or base moving despite an anchored design |
| Swarm / small unit | Cohesive group direction and a legible attack source | So many overlapping trails that the target disappears |
| Boss / multi-part machine | Phase-specific silhouette, weak-point state and subsystem consequences | A larger normal-enemy animation with more screen shake |

Enemy tells should communicate an action category: broad sweep, single-target shot, area charge or support call. They need not reveal every exact numerical result. If the player is allowed to interrupt a channel over several turns, the channel needs a sustainable hold/loop and an explicit cancel transition. A one-shot charge that returns to idle is not enough.

Do not force large vulnerability gestures onto attacks that cannot be interrupted or avoided. Riot's clarity discussion is useful here: the visual attention and implied interaction should match the move's actual significance. This is our adaptation of a competitive-game clarity principle to turn-based battles. [S30]

## 10. Hit, miss, guard, resistance and defeat are different outcomes

A common source of weak battle presentation is using the same target shake for every result. Define an outcome vocabulary before adding more attack variants.

| Result | Body response | Effect / UI response |
| --- | --- | --- |
| Ordinary hit | Local recoil in the received direction, then settle | Contact spark/sound and ordinary result text |
| Heavy or critical hit | Greater interruption or a distinct recovery, if appropriate | More concentrated emphasis; clear critical marker, not only a bigger number |
| Miss | Evasion, graze posture or no contact response | Projectile passes or effect fails to connect; explicit miss feedback |
| Guard / shield block | Braced shield and absorption through support | Effect at the shield surface, reduced/blocked outcome; no simultaneous full hurt pose |
| Resistance / immunity | Minimal body interruption or distinct deflection | Distinguishable resisted/immune feedback; avoid promising a damaging hit |
| Absorption / healing | Positive receive or recharge response | Incoming energy resolves into the recipient; no damage shake |
| Stagger / break | Persistent vulnerable pose or disrupted balance | Clear entry and recovery beats, weak-point/state indicator |
| Lethal result | Recoil into the appropriate collapse/destruction/disable | Defeat after the impact; cleanup follows the correct corpse/disable policy |

A small machine might lose stabilization; a heavy chassis may buckle; a boss subsystem can go dark while the body stays active. Not every machine should kneel and not every defeat should explode. A recruitable or repairable unit's downed state must remain distinct from irreversible destruction. This report does not decide which story entities can be revived.

Never start the target's damage recoil before contact. Anticipatory defense is different from an involuntary hit response. Animation Mentor explicitly warns about inadvertent pre-hit motion when keys are aligned carelessly. [S14]

Reaction strength should have a clear relationship to the result. If a powerful-looking effect deals zero damage because of immunity, communicate the immunity at the same time; do not let the apparent impact imply that the HP display is broken.

## 11. Multi-hit, multi-target and cooperative moves

A multi-hit move has multiple impact events, not one damage event replayed by a looping clip. Give every strike a stable hit identifier and decide which strike owns the strongest emphasis. A fast sequence of four equal full-screen freezes can make a light combo feel slower than a heavy attack.

For a fan of projectiles, separate target assignment from screen position. Record each target's delivery rule and impact point. A sweep can stagger target reactions in the path order; a burst can resolve all targets together. Whichever rule is chosen must match both the visible effect and battle resolution.

Cooperative moves require shared choreography. Put both actors on a common action timeline, with explicit start slots, approach points, preparation holds, hand-off/contact events, strike order and return slots. A pairing needs compatible grips and body dimensions. Two independently played attack clips started at the same time are not automatically a convincing combo.

Use a synchronization point: the first actor can reach and hold a preparation pose until the second is ready. Then a shared release event starts the joint motion. Provide a cancel path if a participant becomes unavailable before commitment. If the game does not allow that interruption, presentation should finish the already-committed result consistently.

For an area heal, avoid stacking identical opaque effects over each party member. One shared field plus small recipient-specific receive cues can make the action clearer. For a line attack, show the path and resolve only the valid targets in that path. These are design recommendations requiring a combat-scene test, not currently implemented features.

## 12. Status conditions need persistent presentation rules

Battle states should outlive the entry animation when gameplay says they do. Guard consists of enter, hold and exit. Channeling consists of prepare, sustain, release or cancel. Downed consists of collapse, downed hold and an allowed exit. A debuff may have a small overlay plus a changed idle, rather than endlessly replaying a dramatic reaction.

Proposed priority rules: destruction/downed overrides ordinary readiness; a meaningful stagger interrupts idle or noncommitted preparation; a damage reaction can briefly override a guard only when the result calls for it; status overlays should not erase the silhouette or weapon. Freeze/pause policies must be explicit for body, effects, camera and audio.

Effects can use layered tracks, but layering is not the same as permission to stack incompatible poses. Spine describes animation layers and mixing, while Godot documents state transitions and one-shot nodes. The portable lesson is to specify ownership, entry/exit and priority rather than letting whichever clip finished last decide the actor's state. We are not adopting those runtimes just because their documentation is useful. [S17, S22]

Low-power acting should be restrained and character-specific: slower stabilization, a delayed hand reset, a shortened glow cycle, a persistent asymmetrical load. Avoid losing sight of the active action under constant glitch effects. Echo malfunction can be more conspicuous than Ghost Grid degradation, while both remain old, damaged systems rather than pristine modern units.

## 13. Effects, sound and camera: coordinated emphasis

Build four effect classes separately: local source effects; transport such as beams/projectiles; target contact effects; and persistent fields/status effects. A muzzle flash can stay attached to a moving weapon. A launched projectile normally must detach. A target spark follows the target's impact anchor. A floor field uses a ground point. These coordinate spaces should never be inferred from the filename alone.

Riot's VFX teaching emphasizes satisfaction with restraint, thematic coherence and readability across an entire roster. Its clarity article connects attention hierarchy to gameplay importance and asks that projectile direction remain legible. Apply that by giving ordinary moves compact effects and reserving dominant effects for meaningful events. [S29, S30]

Use value contrast and shape before increasing brightness. A disruption effect can use broken geometric segments; a precise shot can use a narrow directional trail; a repair can use inward convergence. Color is supporting information. A viewer should not need to distinguish two similar hues to understand hit versus heal.

Audio should have different jobs: selection acknowledgement, preparation, release, travel, impact and resolution. Schedule the impact sound with contact, not with the start of an arbitrary attacker clip. Cache short sounds; unlock audio through the supported user interaction flow and measure actual phone latency. MDN's Web Audio guidance is relevant to loading, user control and autoplay handling; it does not guarantee identical latency on all devices. [S33]

Use brief, local impact holds deliberately. Sakurai's official video description confirms that his hit-stop discussion concerns techniques in Smash Bros. Ultimate; the video was identified as further study, not watched or used here to extract timings. Our proposed 30-70 ms experiments come from our own intended pacing, not that video's measured data. [S39]

Camera movement should reveal action, preserve orientation and return to a reliable framing. A normal hit often needs no camera shake. A heavy boss strike can use a small directional movement, while an optional ultimate might deserve a short reframing. Do not rotate flat sprites into obviously paper-thin angles merely because the camera can move. Acquire documents that flat art and camera rotation require joint consideration. [S03]

## 14. Pixel-art construction and legitimate reuse

Use the procedural rig for proportions, stable sockets, contact planning and a blocking pass. Then correct the silhouette, weapon path, foreshortening, joint overlap and texture clusters at important poses. Where the projected arm becomes a tiny compressed sliver, an authored forearm/hand shape may read better than the mathematically exact projection.

Physical lengths are valuable construction constraints. A controlled smear or silhouette correction can deliberately depart from literal geometry for one exposure; it should not cause unexplained design drift. Lock the source proportions and clearly label these exceptions. Never fix a poor attack by randomly stretching every limb through the whole clip.

Slynyrd's punch lesson puts primary motion before small clothing detail; his directional weapon lesson deliberately preserves weapon-hand identity and varies timing by weapon. These support blocking first and protecting asymmetry. They do not require our frame count, dimensions or a particular art style. [S11, S12]

Separate reusable layers: body construction, pose family, equipped weapon and grip, condition layer, cloth/growth response, action effect and camera plan. Reuse a compatible body pose across a family when it holds up visually. Give different topology its own controller: biped, crawler, hovering ring and asymmetrical manipulator are not interchangeable rigs.

Do not horizontally mirror an entire asymmetric character as the default way to obtain the opposing battle side. A shield, cannon, damage site or missing plate can change apparent screen side while staying on the same physical side. Authored near/far variants and explicit draw order preserve that distinction. Spine's separation of attachments and draw order is a useful model for this data relationship. [S18, S21]

World and battle sprites may have different art sizes and camera demands. Preserve the world's native 32x32 terrain grid; it does not impose a 32x32 battle-frame canvas. A taller character can share a one-tile collision footprint. Choose battle scale after a real composition test, not by repeatedly rescaling a finished sheet.

## 15. The presentation contract the creator and engine need

Keep combat rules authoritative. The action request should identify actor, targets, skill, equipment, outcome policy and an action-instance identifier. The presentation plan should reference immutable or otherwise controlled results, while the game applies state changes according to its chosen resolution point. The sprite renderer must not independently reroll hit or damage.

A proposed action definition should contain: entry state; preparation and sustain clips; release marker; delivery policy; one or more impact markers; result-specific reactions; effect attachments and coordinate spaces; sound cues; camera permissions; movement/return anchors; exit state; cancellation rules; and playback-speed behavior.

Use different identifiers for `release`, `contact`, `result_presented` and `action_complete`. The existing `cannon.emit` is useful for launch, but does not establish where or when the opponent is hit. A sustained field can remain active after its caster has returned to ready; conversely, a projectile still in flight should not accidentally complete a whole action if turn sequencing requires its arrival.

Spine events and Godot method tracks demonstrate scheduling semantic work on timelines; Spine's callback documentation also explains event behavior during mixing. Our implementation should have explicit policy for duplicate, suppressed and interrupted events. A plain frame number alone cannot express that policy. [S19, S20, S23]

Use idempotent event keys such as `(actionInstance, hitIndex, targetId, eventKind)`. If a render frame is skipped, dispatch events crossed in the elapsed interval, in deterministic order, once. If animation speed changes, preserve the event order and the intended interaction rules. A seek, pause or preview replay must not apply gameplay damage again.

Target anchors should include ground, center/core, head, guard surface, effect receive point and optional weak point. Actor sockets include weapon muzzle, grip(s), hands and tool tips. Camera conversion happens once through a documented transform. The renderer, effect system and result UI must agree on that conversion.

The creator should preview this contract with two actors, a formation stage and a simple controlled result selector. It needs play, pause, step, normal/fast speed and outcome variants. Arbitrary game code should not execute inside an art preview. Godot's note that method events are not executed during editor preview is a useful precedent for that separation. [S23]

## 16. Audit of our actual v1 battle library

The audit ran the current factory functions and timing module, and inspected the actual archive. The figures below are measurements of our own output, not estimates of another game's implementation.

| Audited property | Measured v1 result | Meaning |
| --- | --- | --- |
| Roles | Six | Bulwark, Breaker, Keeper, Surveyor, Archivist, Relay |
| Standard attack exposures | 16 for each role | Export count is uniform, regardless of action character |
| Standard attack duration | 1,640 ms for every role | All six attacks share the same timing array |
| Active attack marker | Frame index 7 at 740 ms | All six release at the same authored moment |
| Attack entry/exit | Neutral to neutral | No distinct battle-ready pose is established by this clip contract |
| Battle vocabulary | Idle plus seven action names | Does not cover a complete player/ally skill kit or outcome matrix |
| FX | Local ring/core effect around one origin | Transport, target contact and result response are separate missing scene work |
| Exported exposures | 2,880 including idle | 480 per role; includes repeated images and holds |
| Unique full-frame RGBA hashes | 1,843 | There are 1,037 repeated frame exposures in the archive |

The long shared attack duration is not automatically wrong for every individual action. The problem is that it is imposed on fundamentally different actions. The precise probe and a heavy shield strike currently have the same release timing and total duration.

The biped body channels mainly change drop, short travel, arm angles/spread, head bow and light level. They do not yet provide a convincing set of torso/hip twists, weapon-specific body breakdowns and stepping approaches. The support solver intentionally keeps soles fixed; that is useful for a planted shot, but should not prevent an authored lunge that transfers support to a new foot plant.

Guard and charge are standalone one-shots returning to neutral. They cannot represent a guard maintained over an opponent's turn or an enemy channel sustained until it is interrupted. The library's down/recover seam is useful, but a single crouched power-down pattern should not become the only enemy defeat language.

The preview shows isolated actors acting in parallel. It does not validate one attacker meeting one target at the correct distance, nor a projectile arriving, a defended hit, a missed hit, a healing recipient, or a cooperative move. These omissions explain why a technically valid export still falls short of the requested JRPG battle feel.

**Keep:** tested timing serialization, equipment identities, clean alpha, support diagnostics, source recipes, hand-edit preservation, one-shot playback, atlas bounds and exported origins. **Rework:** battle poses, weapon-specific timing, contact breakdowns, outcome reactions, persistent states and the battle-scene preview. **Do not do:** delete the v1 baseline or repeatedly adjust Industrial Echo's protected rear cloth as a side effect of this research.

## 17. Mobile memory and runtime cost

The archive is 7,805,328 bytes, roughly 7.8 MB in decimal units. Its 29 atlas pages occupy a much larger uncompressed pixel footprint.

| Role | Atlas pages | RGBA page footprint |
| --- | --- | --- |
| Bulwark | 4 | 59.75 MiB |
| Breaker | 5 | 67.43 MiB |
| Keeper | 4 | 47.64 MiB |
| Surveyor | 4 | 54.45 MiB |
| Archivist | 6 | 81.21 MiB |
| Relay | 6 | 82.27 MiB |
| All six | 29 | 392.76 MiB |

This is `sum(pageWidth * pageHeight * 4) / 1,048,576`, assuming four uncompressed RGBA bytes per page pixel. It is **not measured Android process memory**, GPU allocation or proof of a crash. Actual image formats, browser storage, copies and caching can change observed memory. It is enough evidence to reject the assumption that the ZIP's file size is its runtime memory cost.

Do not preload the whole catalogue. Load the actors and action pages required by the current encounter, retain a bounded nearby cache and release unused battle resources according to actual runtime behavior. Deduplicate repeated exposures by referring to one pixel rectangle with multiple durations, while preserving metadata that may differ even when pixels match. Trimming and tighter packing must retain ground anchors, socket coordinates and source-canvas offsets.

Compare fixed-frame pages, deduplicated packed atlases and any carefully designed reusable effect pages on the actual Moto G target. An initial measured budget is more useful than a universal texture-size promise. Separate persistent actor memory, temporary FX memory, decoded image buffers and rendering intermediates.

MDN recommends caching repeated canvas drawing and minimizing redundant work. Our adaptation is to bake and cache approved art rather than rerasterize every procedural pixel for every actor during combat. Timestamp-based progression also matters: rendering frequency must not determine action speed. [S31, S32]

## 18. A production matrix instead of one vague complete flag

| Asset group | Core presentation | Conditional additions | Acceptance focus |
| --- | --- | --- | --- |
| Playable Sleeper | Ready, weapon normal, real skill kit, item, guard, hurt, down, allowed restart, escape, victory | Weapon-family variants and persistent low-power state | Recognizable protagonist, fast normal action, accurate equipment |
| Permanent party companion | Same functional coverage for actual abilities | Protect/intercept, support receive/give, substitution, cooperative moves | Personality and kit identity equal to other party actors |
| AI guest | Ready, actual allowed actions, reactions and exit | Arrival/help/departure and scripted restrictions | Understandable contribution without hijacking player control |
| Routine enemy | Idle, actual attack(s), hurt, defeat/disable | Tell, guard, break and vulnerability when gameplay uses them | Intent, readable result and encounter economy |
| Elite / boss | Role-specific core plus meaningful phase states | Transformation, subsystem hits, interrupted signature, multiple hit anchors | Causal phase changes, composition and readable threat |
| Neutral world NPC | Existing world actions | Battle set only if it can actually participate | No blanket requirement to build unused battle libraries |

Mark requirements at the ability and outcome level. A checklist entry named `attack` should reference a real weapon/skill and say whether hit, miss, guard and lethal outcomes were reviewed in the stage. A character can be technically exported yet visually pending, scene-integrated yet physically untested, or art-approved yet missing an ability. Store those states separately.

This is how permanent recruits avoid becoming apparently finished after receiving only a walking sheet and one generic attack. It also prevents spending time creating a revive animation for an enemy that can never be revived.

## 19. A practical authoring workflow

1. **Fix the scene contract.** Produce a static rear-party composition and a side/three-quarter alternative using existing approved art where suitable. Test UI, boss space and small-screen readability; obtain the camera choice before mass authoring.
2. **Write an action card.** Identify actor, target, equipment, intent, key poses, distance, delivery, result variants, sound and exit state. Keep it to one action, not a whole imagined skill tree.
3. **Block the exchange.** Use flat silhouettes and a simple opponent. Establish preparation, attack, actual contact and recovery. Approve those before adding weathering, light pulses or expensive effects.
4. **Check mechanics.** Solve grips/support and credible weapon paths. Deliberately transfer support for steps rather than forcing all attacks to use fixed feet. Preserve physical left/right identity.
5. **Tune exposures and spacing.** Hold the important information; shorten the unimportant travel between poses. Compare normal and fast playback. Do not interpolate away the decisive silhouette.
6. **Add target outcomes.** Test hit, block and miss immediately. Add critical, stagger, heal or lethal variants when the action supports them. Check that no target reacts early.
7. **Add effects and audio.** Keep source, transport and contact distinct. Make the action readable in body-only, effect-only and combined playback. Match sound to events.
8. **Polish native pixels.** Correct joint overlaps, contour chatter, disconnected growth, weapon grips and texture crawl. Review actual-size pixels over the real battle background.
9. **Export and independently inspect.** Verify pixels, dimensions, timing, events, trim offsets, anchors and origins. Reopen the editable project and reproduce the baked output.
10. **Integrate and review a real encounter.** Play enough repeated ordinary turns to detect fatigue and enough special cases to find overlap/priority bugs. Test the physical target device before declaring runtime acceptance.

Spine's pose-to-pose workflow and Aseprite's frame/layer/cel/tag tools support this staged process. They are authoring references; this plan does not require purchasing a new runtime or replacing the working creator. [S16, S26-S28]

## 20. Proposed first three complete exchanges

**Exchange A: player weapon versus a guarded heavy.** Use the actual chosen player design and one real weapon. Show a clean normal hit, a shield block and a miss. The heavy's shield must meet the incoming path before the player's contact beat. The player returns to an authored battle-ready pose, not an exploration stand. Success means the three outcomes are distinguishable without reading the damage number.

**Exchange B: enemy cannon versus a party actor.** Build acquisition, preparation, release, detachable delivery, contact, target recoil and both recoveries. Then add the resisted outcome and a lethal result. The projectile must reach the target before damage acting; the barrel and grip must stay mechanically plausible. Use the action timeline diagram as a timing experiment, not as a locked prescription.

**Exchange C: NPC ally repairs or protects a teammate.** Choose a real planned support action once the kit is confirmed. A repair has source/recipient cues and no damage recoil. A protective intervention has an intercept point, a sustained brace and the protected ally's appropriate response. Success means this action reads as support rather than a recolored attack.

After these exchanges work in the selected camera, derive compatible variants for the six machine test designs. Next prove a crawler exchange, a hovering/orbital exchange and one multi-target or cooperative action. This preserves the existing technical work while correcting the presentation before it spreads across the roster.

## 21. Acceptance gates that code tests cannot replace

**Art gate:** at gameplay size, identify actor, facing, weapon, action category and target. Preparation/contact/recovery silhouettes must be distinct. The character must retain its design. Source effects must not hide a weak body pose. A reviewer should be able to explain what happened without knowing which clip name was selected.

**Causality gate:** target response follows contact; a miss does not produce a full hit effect; a block occurs on the guard surface; a heal produces a positive receive response; defeat follows the lethal result. Multi-hit and area effects match the number/order of actual outcomes.

**State gate:** sustained guard/channel/down states persist correctly. Cancellation before and after commitment follows a documented policy. An action does not return a downed target to normal idle merely because another clip ended. Swaps retain condition and identity.

**Data gate:** exports preserve timing, explicit loop semantics, attachment spaces, collision/ground separation, events and edit flags. Unknown attachment accuracy for a painted edit is reported as unknown rather than fabricated. Pixel reconstruction proves the export, not the acting.

**Runtime gate:** ordinary and effect-heavy encounters work in the engine with real assets. Pause, fast mode, skipped render frames, scene interruption, target removal and repeated actions do not duplicate outcomes. Frame-time and memory behavior are measured on the physical target device.

**Presentation gate:** camera, UI, damage text, audio and effects agree. Party members do not obscure the current target. Distinguish action acknowledgement from long compulsory spectacle. Review repeated normal attacks, not only one isolated impressive move.

These gates should be separate fields in the asset ledger. The v1 technical suite remains useful evidence under the data/mechanics gates; it does not satisfy all six gates automatically.

## 22. Motion controls and final-display review

Provide reduced camera shake and effect-intensity options without removing the information needed to understand an action. Keep important cues in shape, pose and UI as well as color/audio. A game-speed option must preserve semantic events and any approved timing-input policy.

Review flashes in the final scene, including simultaneous effects and looped previews. W3C discusses frequency, area, contrast and final viewing conditions; Microsoft XAG 117 discusses user control over distracting motion and camera movement. These references guide a review process. A tiny source sprite or a renderer unit test cannot certify a full battle scene. [S34, S35]

For a restrained ancient-tech look, most actions can rely on a crisp local accent, directed travel and a clear target response. The occasional conspicuous malfunction can be meaningful because the rest of the presentation stays controlled. Constant full-body flicker would weaken both readability and the intended distinction between Echo and other units.

## 23. Required creator changes and implementation order

**Priority 0 - establish the visual target:** stage camera presets, battle-ready pose support and paired-actor preview. Keep old projects unchanged. Add a visual quality status independent from `export verified`.

**Priority 1 - model complete actions:** action definitions that reference body clips, transport, target outcomes and stage movement. Add preparation/sustain/release/cancel states, multiple attachment anchors and explicit return/exit states. Preserve inert art-preview events; do not run arbitrary user callbacks.

**Priority 2 - improve content:** redraw key poses for the selected camera, introduce weapon-specific timing and supported stepping, add result-specific reactions, then finish the actual player and companion ability kits. Use the three complete exchanges before expanding the catalogue.

**Priority 3 - optimize delivery:** exact-pixel deduplication, explicit trim offsets, encounter-scoped asset loading and separate reusable FX. Preserve provenance and editable authoring sources. Measure real decoded memory rather than making a promise from ZIP size.

**Priority 4 - runtime and device review:** one real encounter, then multi-target, combo, interruption and repeated-fight stress cases on the engine and Moto G. Only after these checks should an asset's ledger say battle-presentation approved and runtime accepted.

The research recommends a correction to the workflow, not abandoning the creator. Its tested technical foundations can remain. The missing layer is coordinated, camera-specific performance built around actual JRPG actions, targets and outcomes.

## 24. Source register and scope notes

Reference IDs point to the companion `sources.json`, which records the exact URL, source type and inspection depth. The register distinguishes substantive pages, partial/search excerpts and further-watch descriptions. No frame counts for retail games are claimed from descriptions alone. Sources are grouped by practical use rather than ranked as universal authorities.

### Developer and JRPG presentation evidence

- **S01:** Thierry Boulanger / Sabotage, *A closer look at the turn-based combat in Sea of Stars*, PlayStation Blog, 2022. Primary developer article; inspected text on timed hits, enemy locks, combinations and swapping.
- **S02:** Sabotage, *Sea of Stars press kit*. Official feature description; not a measured animation breakdown.
- **S03:** Acquire interview, *Octopath Traveler II builds a bigger, bolder world in its stunning HD-2D style*, Unreal Engine, 2023. Direct developer answers about proportions, actions and camera constraints.
- **S04:** Square Enix, *8 things you need to know about Octopath Traveler II*. Official overview of expanded character animation and camera presentation.
- **S05:** Square Enix, *Octopath Traveler 0 developer interview*. Inspected direct developer excerpt about recruited-character asset workload.
- **S06:** RPG Maker MZ, *Side-View Character Standards*. Actual documented actor-sheet/playback conventions.
- **S07:** RPG Maker MZ, *Asset Standards*. Distinguishes ally and enemy image folders; no third-party animated-enemy claims.
- **S08:** RPG Maker MV, *Animation Settings*. Target-relative effects and scheduled sound/flash data; explicitly MV.

### Original animation and pixel-art teaching

- **S09:** Raymond Schlitter / Slynyrd, *Pixelblog 9: Melee Attacks*. Stance, weight, timing, overshoot and gameplay context.
- **S10:** Slynyrd, *Pixelblog 52: Idle Fighting Stance*. Readiness and personality; example-specific anatomy/style is not generalized to all characters.
- **S11:** Slynyrd, *Pixelblog 53: Punches and Kicks*. Main motion, reference and subsequent clothing/detail treatment.
- **S12:** Slynyrd, *Pixelblog 56: Top Down Character Attack Animation*. Asymmetry, attack phases and weapon-dependent timing; not imported assets.
- **S13:** Slynyrd, *Pixelblog 62: Landscape Backgrounds*. A documented front-enemy/rear-hero JRPG composition.
- **S14:** Chris Hurtt / Animation Mentor, *Anticipation*. Action preparation and unintended pre-hit reactions.
- **S15:** Animation Mentor, *Timing and Spacing*. Written explanation inspected; embedded full lesson not watched.
- **S16:** Esoteric Software, *Animating*. Pose-to-pose and iteration workflows.
- **S37:** Pedro Medeiros / Saint11, *Simple Attack Animation*. Public author excerpt on immediate action-game response; used with its original context.
- **S38:** Junya Motomura / Arc System Works, *Guilty Gear Xrd* GDC presentation. Primary PDF's indexed animation slide excerpt inspected; full PDF fetch timed out. Used only for the stated limited-animation/interpolation principle.
- **S39:** Masahiro Sakurai, *Eight Hit Stop Techniques*. Official video description inspected; listed for further viewing, not counted as a watched lesson or a timing-measurement source.

### Runtime, effects, export and review evidence

- **S17-S21:** Esoteric Software documentation on applying animation, slots, events, callbacks/mixing and JSON timelines.
- **S22-S25:** Godot documentation on AnimationTree, track types, SpriteFrames and AnimationPlayer.
- **S26-S28:** Aseprite documentation on animation, slices/pivots and sprite-sheet export.
- **S29-S30:** Riot's VFX art education and *Clarity in League*; adapted as clarity principles, not as a demand to copy League's visual style or combat system.
- **S31-S33:** MDN on animation timestamps, canvas optimization and Web Audio practice.
- **S34-S35:** W3C flash guidance and Microsoft's visual-distraction/motion guideline.
- **S36:** Effekseer-hosted recorder tutorial. Older tutorial inspected for the concept of recording effects to sheets and handling alpha; no current-version UI promises or tool installation.

### Limitations and excluded material

Sega's official Phantasy Star IV manual index was located, but its page-image URLs could not be retrieved successfully in this session. It is recorded as a retrieval limitation and was not used to claim specific animation poses, battle mechanics or timings. GDC motion-reference slides whose full PDF exceeded the browsing limit were not treated as fully read. Secondary summaries and scraped timing tables were excluded as authorities where original artist/developer sources were available.

The research is complete as a production guide and v1 audit. The proposed action sequencer, new camera-specific artwork, memory optimizations, complete player/companion kits and engine integration remain work to implement and validate.

## 25. Exact source URLs

- **S01: Sabotage: Sea of Stars combat**  
  https://blog.playstation.com/2022/07/07/a-closer-look-at-the-turn-based-combat-in-sea-of-stars/

- **S02: Sabotage: Sea of Stars press kit**  
  https://sabotagestudio.com/presskits/sea-of-stars/

- **S03: Acquire: Octopath Traveler II developer interview**  
  https://www.unrealengine.com/developer-interviews/octopath-traveler-ii-builds-a-bigger-bolder-world-in-its-stunning-hd-2d-style?lang=en-au

- **S04: Square Enix: 8 things about Octopath Traveler II**  
  https://www.square-enix-games.com/en_US/news/octopath-traveler-ii

- **S05: Square Enix: Octopath Traveler 0 developer interview**  
  https://www.square-enix-games.com/en_US/news/interview-octopath-traveler-0-developers-talk-town-building-ultimate-techniques-more

- **S06: RPG Maker MZ: Side-View Character Standards**  
  https://rpgmakerofficial.com/product/MZ_help-en/01_11_02.html

- **S07: RPG Maker MZ: Asset Standards**  
  https://rpgmakerofficial.com/product/MZ_help-en/01_11_01.html

- **S08: RPG Maker MV: Animation Settings**  
  https://rpgmakerofficial.com/product/MV_Help/page/01_08_09.html

- **S09: SLYNYRD: Pixelblog 9 - Melee Attacks**  
  https://www.slynyrd.com/blog/2018/9/8/pixelblog-9-melee-attacks

- **S10: SLYNYRD: Pixelblog 52 - Idle Fighting Stance**  
  https://www.slynyrd.com/blog/2024/9/26/pixelblog-52-idle-fighting-stance

- **S11: SLYNYRD: Pixelblog 53 - Punches and Kicks**  
  https://www.slynyrd.com/blog/2024/11/25/pixelblog-53-punches-and-kicks

- **S12: SLYNYRD: Pixelblog 56 - Top Down Character Attack Animation**  
  https://www.slynyrd.com/blog/2025/5/23/pixelblog-56-top-down-character-attack-animation

- **S13: SLYNYRD: Pixelblog 62 - Landscape Backgrounds**  
  https://www.slynyrd.com/blog/2026/5/27/pixelblog-62-landscape-backgrounds

- **S14: Animation Mentor: Anticipation**  
  https://www.animationmentor.com/blog/anticipation-the-12-basic-principles-of-animation/

- **S15: Animation Mentor: Timing and Spacing**  
  https://www.animationmentor.com/blog/tutorial-animate-with-timing-and-spacing-in-mind/

- **S16: Spine: Animating**  
  https://en.esotericsoftware.com/spine-animating

- **S17: Spine: Applying Animations**  
  https://en.esotericsoftware.com/spine-applying-animations

- **S18: Spine: Slots**  
  https://en.esotericsoftware.com/spine-slots

- **S19: Spine: Events**  
  https://en.esotericsoftware.com/spine-events

- **S20: Spine: AnimationState callbacks**  
  https://en.esotericsoftware.com/spine-unity-events

- **S21: Spine: JSON export format**  
  https://en.esotericsoftware.com/spine-json-format

- **S22: Godot: Using AnimationTree**  
  https://docs.godotengine.org/en/stable/tutorials/animation/animation_tree.html

- **S23: Godot: Animation Track Types**  
  https://docs.godotengine.org/en/stable/tutorials/animation/animation_track_types.html

- **S24: Godot: SpriteFrames**  
  https://docs.godotengine.org/en/stable/classes/class_spriteframes.html

- **S25: Godot: AnimationPlayer**  
  https://docs.godotengine.org/en/stable/classes/class_animationplayer.html

- **S26: Aseprite: Animation**  
  https://aseprite.org/docs/animation/

- **S27: Aseprite: Slices**  
  https://aseprite.org/docs/slices/

- **S28: Aseprite: Sprite sheets**  
  https://aseprite.org/docs/sprite-sheet/

- **S29: Riot: Art Education - Visual Effects**  
  https://www.riotgames.com/en/artedu/visual-effects

- **S30: Riot: Clarity in League**  
  https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/

- **S31: MDN: requestAnimationFrame**  
  https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame

- **S32: MDN: Optimizing canvas**  
  https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Optimizing_canvas

- **S33: MDN: Web Audio API best practices**  
  https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Best_practices

- **S34: W3C: Three Flashes or Below Threshold**  
  https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html

- **S35: Microsoft XAG 117: Visual distractions and motion settings**  
  https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117

- **S36: Effekseer-hosted Quick Tutorial: Recorder**  
  https://effekseer.github.io/QuickTutorial_Tool/QuickTutorial_en.html

- **S37: Saint11: Simple Attack Animation**  
  https://www.patreon.com/saint11/posts/simple-attack-6837623

- **S38: Junya Motomura: Guilty Gear Xrd GDC presentation**  
  https://www.ggxrd.com/Motomura_Junya_GuiltyGearXrd.pdf

- **S39: Masahiro Sakurai: Eight Hit Stop Techniques**  
  https://www.youtube.com/watch?v=tycbMSjDDLg

