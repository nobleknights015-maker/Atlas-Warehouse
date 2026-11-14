# Unit09 Round53 — palette cleanup without changing accepted movement

Owner positively received Round52 and requested sprite cleanup. Preserve successful proportions, enlarged far foot, corrected chest ownership, silhouette and motion. Avoid another rig or body replacement.

Diagnosis: W frame0 had4171 distinct opaque RGB colors in4935 visible pixels. That is a noisy raster surface rather than a compact controlled palette. First cleanup uses an authored26-color palette with separate warm armor, dark understructure, neutral metal, red cable and violet light ramps. Fixed nearest-CIELAB lookup without dithering or frame-adaptive palettes reduces redundant shades while retaining exact pixel ownership and geometry. Do not call this manual cluster redrawing.

Evidence:16 side frames retain full alpha exactly and byte-identical motion metadata. Same lookup applied to layers and original composites yields identical results, protecting occlusion. S/N58 original files each stay unchanged. Independently decoded32 ASE composites match PNGs. Native sheet and enlarged four-pose comparisons reviewed. W0 now uses25 of the26 palette colors. New candidate remains pending owner visual acceptance.

Limits: palette consolidation improves muddy color variation but does not fix inherited jagged knee/shin silhouettes, irregular thin joint clusters or texture motion. Those require deliberate source-pixel/cluster editing while retaining geometry. Do not blur, shrink limbs, replace hips or restart IK. Front/back palette application is deferred until side cleanup direction is accepted. Round52 exact baseline is retained in the private packet for reversible comparison.

Private packet Unit09_Round53_Palette_Cleanup.zip contains baseline and cleaned layered PNGs, approved S/N,26-color palette, scripts, editable ASE, transparent atlas, direct before/after moving previews and QA/hash records. Public repository receives only technical notes. No owner artwork, phone captures, engine or APK changes.
