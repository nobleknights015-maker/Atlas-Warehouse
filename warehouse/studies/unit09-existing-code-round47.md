# Unit09 existing-code test, Round47

## Outcome
Executed scikit-image 0.26.0 PiecewiseAffineTransform and nearest-neighbor warp on private Unit09 S/N/W/E raster inputs. This is a bounded deformation integration test, NOT a finished or owner-approved walk. Revision45 remains the art checkpoint; approved front/back originals unchanged.

## Homework applied
Use a coherent whole-body reference pose. Preserve identity, fixed upper-body pixels, a planted near ankle, original two-link bone lengths, and rigid corner groups for thigh/shin/boot material. Anatomical controls are manually specified and remain provisional. Keep camera depth independent of which leg leads. Do not treat numeric checks as artistic acceptance.

## Reproducible measured results
- All four views: identity changed pixels 0; exact integer translation mismatch 0.
- Simple knee-only warp showed local stretch/compression (singular values approximately 0.832 to 1.187). Therefore generic warping alone is insufficient.
- Rigid-group test: 8 exposures each W/E, 0 inverted triangles; top80 rows unchanged; phase0 pixel-exact.
- Max within-group corner-pair distance error: W 3.20e-14 px; E 5.51e-14 px.
- Max planted near-ankle control error: W 7.11e-15 px; E 1.43e-14 px.
- These are CONTROL geometry measurements, not proof every interior armor pixel stays rigid, no foot sliding, or good animation.
- Initial bidirectional root motion exceeded a source leg's reach; assertion stopped it. Reduced motion schedule to a reachable one-sided flex. Bone lengths were not shortened to force the result.

## Critique and limits
Native playback and decoded frame review performed. Small shifts preserve the coherent contact-pose anatomy better than prior limb cutouts, but pixel shimmer remains around knee/calf outlines. The test only oscillates a contact pose. It neither alternates support nor creates missing surfaces. Manual native contour and opposite-step pose authoring remain necessary. Do not present this as completed walking or promote to master.

## Other implementation tested
Jarvis73 Moving-Least-Squares NumPy rigid implementation, upstream img_utils.py blob 32733c548bc93ae15d704f081e252c02f530f777 (MIT), retained unmodified with LICENSE in private evidence packet. Our integration's identity test changed S4196 N4096 W4007 E4041 pixels. A separately named rounding adapter reduced errors to S3 N3 W3 E2 but still failed exact identity. Not selected. This result diagnoses this integration/quantization, not every use of MLS. gpytoolbox ARAP was NOT executed (import missing scs; wheel did not expose expected ARAP). Puppet-warp README inspected only, not run.

## Reproduce
Private packet contains inputs, scripts, pins, output PNGs/GIFs and result JSON. Install requirements.txt; run:
python3 run_existing_code.py
python3 run_rigid_plate_test.py
The relative .deps_round47 lookup is optional; normal installed packages work. The original MIT MLS source is included with license; scikit-image is a dependency, not copied source. No private source artwork is published in this public guide.

## Primary sources
- https://scikit-image.org/docs/stable/auto_examples/transform/plot_piecewise_affine.html
- https://scikit-image.org/docs/stable/api/skimage.transform.html
- https://github.com/Jarvis73/Moving-Least-Squares
- https://github.com/sgsellan/gpytoolbox
- https://github.com/mikecokina/puppet-warp
