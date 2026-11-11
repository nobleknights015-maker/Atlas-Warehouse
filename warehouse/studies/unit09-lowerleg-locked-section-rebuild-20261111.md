# Unit 09 lower-leg section practice — controlled rebuilds A/B

**Status:** two real native-pixel construction revisions, engineering tests PASS, art-quality gate FAIL, **not animation-ready**.

## Starting point and scope
The most recent v4b static checkpoint created by an hourly automation was not accessible in the active chat runtime or file search, so the test uses a *known older mounted* image, `sleeper09_manual_leg_proportion_v2.png` (128×262, 17 RGBA values including transparent). **Neither candidate should supersede the recent v4b checkpoint.**

## What was done
Inspected the original shins at native pixel scale and enlarged view. Designed two alternate foreleg armor cross-sections rather than drawing a new whole frame. Kept all pixels above row 212 and from row 245 onward, so the actual old knee and boot silhouettes remain unchanged. Remodeled ONLY rows 212–244 to use a darker mechanical joint, a front plate, a side plane and a narrow armor edge/glow channel. A and B differ in panel overlap and seam orientation. A third separate rig overlay shows joint anchors for the older sprite.

## Verified quantitative checks
Both rebuilt images are 128×262 hard-alpha RGBA with unchanged original bbox (27,8,106,262).
- Candidate A: 996 pixels change from older original.
- Candidate B: 1055 pixels change from older original.
- For BOTH: original top rows 0–211 unchanged byte-for-byte, original boot rows 245–261 unchanged byte-for-byte, alpha limited to 0 and 255, original transparent corners retained.
- These are pixel-edit/control tests, NOT measurements of artistic quality.

## Visual evaluation and failure
The earlier original reads as stacked rectangular knees, shins and broad boots. A exposes the knee joint but creates a flat, broad shin shell. B introduces stronger diagonal armor overlap and subtle vents but remains stiff; its knee-seam bands are too horizontal/graphic, the calf taper is too weak, and the full design lacks the detail, body-language and materials of the provided Vera Starter A reference. The lack of a live direct comparison to v4b is a blocker to declaring actual art progress. **Reject both candidates as promotion-ready.**

## Next direction
Recover v4b editable baseline in an environment where its actual pixels are available; do not rebuild from stale older output. On a separate editable shin section layer, make knee plates wrap the leg contour, differentiate a rigid shin front plane from the flexible dark calf/ankle substrate, and preserve boot silhouette while restoring smooth ankle flow. Check actual 1× silhouette against the matching user-provided source and tune shape hierarchy before adding detail. Continue skeleton → sections → visualize → revise loop, not one drawing plus a written critique.

## Privacy
No original Founder/Vera character imagery or derived sprite pixels uploaded to this PUBLIC GitHub repository; only art-method notes and numeric checks. The downloadable local practice ZIP remains in its originating chat, not the Warehouse.
