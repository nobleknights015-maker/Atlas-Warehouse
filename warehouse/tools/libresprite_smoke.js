/* LibreSprite 1.3 JavaScript: actual editor pixel mutation in batch mode.
 * No Bearframe art is shipped in this smoke test.
 */
const s = app.activeSprite;
if (!s || s.width !== 32 || s.height !== 32) throw new Error("Expected 32x32 test sprite");
const layer = s.layer(0);
const cel = layer && layer.cel(0);
if (!cel) throw new Error("No editable cel in opened PNG");
const img = cel.image;
const existing = img.getPixel(16, 16);
if (pixelColor.rgbaR(existing) !== 48 || pixelColor.rgbaG(existing) !== 53) {
  throw new Error("Unexpected source pixel before edit");
}
img.putPixel(16, 16, pixelColor.rgba(171, 91, 240, 255));
img.putPixel(17, 16, pixelColor.rgba(134, 72, 210, 255));
console.log("LibreSprite edited two actual pixels in layer 0, cel 0.");
