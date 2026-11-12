# Walk cycle failure study — repeat silhouette, fake passing pose, and rigid limb masks (2026-11-12)

**Context:** Generic pixel animation study for Bearframe RPG. No user-supplied character art, source sprites, private documents or third-party copyrighted artwork committed here.

## Verified failure mode
A four-display-frame study used only *three unique underlying body silhouettes*. The two 'passing' slots had an identical alpha shape: effectively **contact A → neutral → contact B → neutral**. Emissive color variation alone does not produce independent passing-step anatomy. Even if both shoes end on the same canvas baseline, this is not the same thing as maintaining a planted foot in game-world coordinates.

The four-frame shorthand should instead deliberately design **contact (leg A), passing (A transfers), contact (leg B), passing (B transfers)** with visible heel lift, toe-off, side-appropriate depth and controlled body bob. Alternatively draw eight fully coherent contact/down/passing/up poses if the scale and art standard justify it.

## What failed in remediation
- Increasing frame delay fixed only pace, not limb continuity.
- Copying neutral arms to every frame 'solved' twitch at the cost of unnatural rigid shoulders.
- Rotating/transplanting complex arm cutouts around guessed pivots produced hip/shoulder seams and accidental overdraw.
- Fixing transparency/alpha does not correct which leg should render in front or how the knee transfers weight.

## Practice and QC standard
1. **Start with 1x bone pivots:** stable pelvis, left/right shoulder/elbow, hip/knee/ankle and each foot ground contact. Keep pixel art canonical but monitor skeleton landmarks.
2. **Pose before polish:** draw complete limb silhouettes and explicit near/far depth per step. All four direction sets must pass 1x readability.
3. **Onion-skin + loop seam:** examine prev, current, next—including last→first—rather than judging a still thumbnail.
4. **World contact test:** collision pivot / shadow anchor is not necessarily the same as the planted foot. Check world displacement synchronized to contact frames, not only constant sprite bounding boxes.
5. **Rig layers:** separate torso, near/far arms, near/far legs, chest/visor glow, effects; no masked slices through neighboring limbs.
6. **Measurable files:** frame dimensions, RGBA alpha, distinct silhouettes, pixel-nearest rendering, named states, durations, sync events, integrity/licensing metadata; compare animation on the engine's landscape phone runtime.

### External documentation
- Aseprite timeline, frames, tags and frame duration: https://www.aseprite.org/docs/animation
- Aseprite onion skin reference: https://www.aseprite.org/docs/onion-skinning/
- LibreSprite four-pose walk example: https://libresprite.dev/guides/walk-cycle/
- Godot per-frame duration and loop metadata: https://docs.godotengine.org/en/stable/classes/class_spriteframes.html

**Status:** Research + quantified source audit completed; fresh corrected hand-drawn walk cycle is **NOT** completed. Preserve existing engine, original assets, and development branches until runtime acceptance checks pass.
