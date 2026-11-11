#!/usr/bin/env python3
"""Tests layered LibreSprite native art-editor output. Quality is judged separately."""
from pathlib import Path
from PIL import Image
import struct,json
D=Path("training_run")
def header(p):
  raw=p.read_bytes()
  assert struct.unpack_from("<H",raw,4)[0]==0xA5E0,"ASE magic invalid"
  return struct.unpack_from("<HHH",raw,6)
def main():
  assert header(D/"input_layers.ase")==header(D/"edited_layers.ase")== (3,72,112)
  sheet=Image.open(D/"editor_sheet.png").convert("RGBA")
  assert sheet.size==(216,112),sheet.size
  data=json.loads((D/"editor_sheet.json").read_text())
  frames=data["frames"]
  frames=list(frames.values()) if isinstance(frames,dict) else frames
  frames=sorted(frames,key=lambda fr:fr["frame"]["x"])
  assert len(frames)==3 and all(fr["frame"]["w"]==72 and fr["frame"]["h"]==112 for fr in frames)
  images=[sheet.crop((i*72,0,(i+1)*72,112)) for i in range(3)]
  for i,img in enumerate(images):
    img.save(D/("edited_frame_%d.png"%i))
    assert img.getpixel((0,0))[3]==0
    assert set(img.getchannel("A").getdata()).issubset({0,255})
    assert img.getpixel((31,27))==(189,121,87,255)
    assert img.getpixel((33,54))==((60,196,206,255) if i==1 else (166,246,239,255))
    assert img.getpixel((28,7))==(242,234,207,255)
  # No unexpected foot skating, clipping, or per-frame changes to the grounded soles.
  for frame in images[1:]:
    for y in range(101,112):
      for x in range(72):
        assert frame.getpixel((x,y))==images[0].getpixel((x,y)),(x,y)
  changes=[sum(a!=b for a,b in zip(images[0].getdata(),im.getdata())) for im in images]
  assert 15<changes[1]<600 and 15<changes[2]<600,changes
  colors=len(set(sheet.getdata()))
  assert colors<=20,colors
  report={"passed":True,"tool":"LibreSprite 1.3 JS native cels",
    "size_per_frame":[72,112],"frames":3,"preserved_layers":4,
    "source_kind":"generic public-safe original training automaton",
    "frame_delta_pixels":changes,"colors_including_transparent":colors,
    "ground_unchanged_y":[101,111],"alpha": [0,255],
    "artistic_quality_passed":False,
    "caveat":"technical integration and frame registration only; not polished game artwork"}
  (D/"editor_validation.json").write_text(json.dumps(report,indent=2)+"\n")
  print(json.dumps(report,indent=2))
if __name__=="__main__":main()
