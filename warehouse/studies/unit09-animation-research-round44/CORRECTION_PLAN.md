# All-direction correction and acceptance plan

Status: project recommendations from Round44. S/front and N/back remain approved baselines. No source asset changes in this round. The immediate blocker is W/E whole-body pose integration and both leg silhouettes.

## Direction coverage

| View | Primary drawing check | Occlusion and support check | Preserve |
| --- | --- | --- | --- |
| S/front | Chest/pelvis centerline, consistent thigh volume and head/body ratio; forward leg is not vertically compressed to fake depth | Feet separate clearly, one support role at a time, arm vs thigh ownership, toe-facing readability | Approved S files and identity |
| N/back | Rear pelvis/sacrum chassis volume, calf/heel shapes, hair/back armor identity | Passing foot lift and sole/heel visibility, rear arm overlap, no false splits | Approved N files and identity |
| W/left | Complete near thigh plate, hip-socket relationship, knee/shin/boot contours through contact and passing | Near/far physical leg IDs; heel/forefoot roll; far arm never steals pelvis material | Preferred side design; source reference |
| E/right | Same body plan and phase vocabulary as W, independently drawn asymmetric details | Direction-specific ordering and hidden surfaces; no automatic mirror assumption | Preferred side design; source reference |

All views share character identity, reference camera/style, phase event meanings, ground pivot convention and action metadata. Their pixel drawings and local occlusion differ. Native32px terrain remains the context; sprite dimensions are a separate decision.

## Implementation gates

| Gate | Concrete work | Pass evidence | Failure means |
| --- | --- | --- | --- |
| 0 — Freeze evidence | Archive approved S/N and preferred side design; identify rejected42 and unresolved43 | File hashes plus explicit approval/status ledger | Do not substitute an unapproved master |
| 1 — Model sheet | Mark crown, neck, shoulder, waist, actual pelvis/socket, knee, ankle, heel and toe for S/N/W/E at one chosen native art scale | Annotated reference landmarks; visible silhouette comparison | No arbitrary rig fitting |
| 2 — Ownership | Display identity-colored head/torso/pelvis/arm/leg/boot regions; no automatic nearest-bone segmentation | No pelvis/thigh pixels moving in an arm-only test; correct rest reconstruction | Fix masks and repaint hidden surfaces |
| 3 — Whole-body key poses | Draw contacts A/B and passing A/B; include pelvis, trunk, shoulders, head and feet together | Native-size stills beside matched source poses; solid silhouette and full plate coverage | Stop the cycle; redraw pose |
| 4 — Pixel contours | Correct transitions at waist, socket covers, knee caps and boots; remove conflicting standing pelvis | Before/after ownership and contour inspection, not disconnected-pixel deletion | Do not call shape errors polish |
| 5 — Motion | Add compression/rise, transitions and intentional duration values | Normal-speed and stepped loop; stable volumes and readable weight transfer | No secondary effects yet |
| 6 — World contact | Preview moving root on marked ground with both feet and changing contact modes | Foot patch/contact event inspection and root-speed accounting | Revise cadence/poses; no limb shrink to force pass |
| 7 — Four-view review | Show front/back/sides together at native resolution and integer enlargement | Design consistency; preserved S/N hashes unless separately revised | Do not change all directions to hide a side problem |
| 8 — Real context | Stage beside actual32x32 owner terrain; verify occlusion and final intended display scale | Inline loop on real assets; runtime integration separately verified | No 'game-ready' claim from a bare stage |
| 9 — Transfer | Fit a second character's landmarks, redraw its own contours and armor at each pose | Same events, its own coherent silhouette and stable volumes | Reuse method, not flawed pixels |

No universal numeric width tolerance is imposed on stylized art. Metrics can flag changes, but artistic silhouette acceptance must be visible. Approved originals are references, not automatically physical templates for every chassis.

## Research coverage for other animation families

This is a construction checklist, not a claim that these assets exist or that every family needs all four views at the same priority. Exploration uses four cardinal directions. Action-specific view requirements must be documented rather than silently limited to SE.

| Family | Key body problem | Contact / phase evidence | Direction application |
| --- | --- | --- | --- |
| Idle, subtle organic/glitch idle | Body stays supported; secondary motion does not make arms seize | Stable feet/pelvis; intentional delayed hair/cable movement | S/N/W/E exploration baseline |
| Walk, start, stop, turn | Full-body weight transfer and coherent transitions | Two foot roles, heel/forefoot events, root travel, loop seam | S/N/W/E; no diagonal authoring scope |
| Run/dash | Different support timing and forward balance, not just a faster walk | Intended push-off and any flight/suspension phase | Four-view motion plan before directional production |
| Look-around/head-check | Whole head/hair/visor changes, neck connection and shoulder follow as needed | Gaze lead and settle; no face-only translation | Direction-specific head volume; body support preserved |
| Combat-ready/guard | Balanced stance and clear hand/weapon role | Entry anticipation, stable support, readable held stance | View-specific occlusion/weapon silhouette |
| Melee/weapon attacks | Root/pelvis/trunk/shoulder chain and hand-to-weapon continuity | Anticipation, active strike, impact, follow-through, recovery | Action pose first, effects separate, four-view requirements explicit |
| Cast/charge | Hands and core gesture read without hiding body silhouette | Prepare, channel/hold, release, settle | Effects and emissive overlays separate from anatomy |
| Hit/stagger | Force direction and believable catch of weight | Impact, recoil, support change, settle | Avoid unrelated all-limb jitter |
| Knockdown/recovery | Continuous path of pelvis and spine; no detached or sliding legs | Named hand/knee/foot/body support changes at each stage | Floor staging and body orientation explicit per view |
| Sit/meditate/charge/stand | Actual folded-leg and pelvis volumes; avoid crouching splits | Descent, seat/ground support, hold, unfold, weight transfer | View-specific knee/foot overlap and seating height |
| Pose/gesture/emote | Whole-body attitude and readable arm/head relationship | Preparation and settle; keep planted support | Preserve volume from all required views |

Previously scrapped knees-to-prone, rise-from-knees, arms-crossed and dependent return remain retired. The withdrawn face-only look-around is not restored as a valid asset. Researching how to do an action is not authorization to undo its retirement.

## Repeatable review views

- Intact source next to corresponding posed drawing at the same target character scale.
- Black silhouette and flat material groups before full texture.
- Identity-colored ownership with only one limb moving.
- Onion skins around contact and passing events.
- Joint/contour close-ups, including actual knee/boot drawings rather than bone lines.
- Native-size normal-speed loop, single frames, then integer-enlarged loop.
- Grounded moving-root preview; support events shown independently of root metadata.
- Four-view montage and actual32x32 tile context.
- File/export validation last. Hashes, frame counts and decode checks never replace the art review.

## Stop conditions that prevent another wasted round

A side has a broken waist, missing thigh plate, thin/twisted leg, wrong limb overlap, two conflicting pelvises, a foot pointing the wrong way, or an unrelated torso pose: stop before expanding frames. These are model/pose failures. If only numeric QA passes, do not present the result as meaningful artistic progress. Preserve the failed experiment as evidence with an explicit rejected status, not as an approved reusable method.
