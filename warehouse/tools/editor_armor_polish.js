/* LibreSprite 1.3: controlled native pixel edits in ALL layered frames.
 * This non-canonical art exercise is free of user-supplied character designs.
 */
const s = app.activeSprite;
if (!s || s.width !== 72 || s.height !== 112 || s.layerCount !== 4)
  throw new Error("Expected a 72x112 RGBA sprite with four layers");
const names=["internal_structure","faceted_armor","drapery","signals"];
for (let k=0;k<4;k++)
  if (s.layer(k).name !== names[k] || s.layer(k).celCount !== 3)
    throw new Error("Expected 3 unlinked cels for "+names[k]);
const rgba=(r,g,b,a=255)=>pixelColor.rgba(r,g,b,a);
const bright=rgba(242,234,207), mid=rgba(176,169,155);
const hi=rgba(166,246,239), glow=rgba(60,196,206);
const copper=rgba(189,121,87);
for(let f=0;f<3;f++){
  const armor=s.layer(1).cel(f).image;
  const chassis=s.layer(0).cel(f).image;
  const signal=s.layer(3).cel(f).image;
  [[28,7,bright],[29,7,bright],[38,7,bright],
   [21,31,bright],[22,31,bright],[30,33,bright],
   [31,33,bright],[37,33,bright],[44,90,mid],[46,90,bright],
   [25,90,bright]].forEach(p=>armor.putPixel(p[0],p[1],p[2]));
  chassis.putPixel(31,27,copper);
  signal.putPixel(33,54,f===1?glow:hi);
  signal.putPixel(34,54,f===1?glow:hi);
  signal.putPixel(34,55,f===2?hi:glow);
  if(f===2)signal.putPixel(32,18,hi);
}
console.log("LibreSprite edited 3 layers, 3 cels, no changes to grounded feet");
