"""Reproduce the research's timing, repeated-frame and RGBA page-footprint audit.
Usage: python audit_v1_pack.py Aeon_Circuit_Six_Unit_Battle_Animations_v1.zip
Requires Pillow; reads the archive without extracting or changing it.
"""
from zipfile import ZipFile
from PIL import Image
import io,json,hashlib,sys
rows=[]
with ZipFile(sys.argv[1]) as z:
    assert z.testzip() is None
    for unit in json.loads(z.read('inventory.json')):
        role=unit['role']; m=json.loads(z.read(role+'/metadata.json')); pages=[]
        for page in m['pages']:
            pages.append(Image.open(io.BytesIO(z.read(role+'/'+page['image']))).convert('RGBA'))
        hashes=[]
        for f in m['frames']:
            x,y,w,h=[f[k] for k in ['x','y','w','h']]
            crop=pages[f['page']].crop((x,y,x+w,y+h))
            hsh=hashlib.sha256(crop.tobytes()).hexdigest()
            assert hsh==f['pixelSha256']
            hashes.append(hsh)
        a=m['clipInfo']['attack'];active=next(e for e in a['events'] if e['frame']==7)
        pixels=sum(p.width*p.height for p in pages)
        rows.append(dict(role=role,attackDurationMs=a['durationMs'],activeMs=active['timeMs'],exposures=len(hashes),uniqueFrames=len(set(hashes)),pagePixels=pixels,rgbaMiB=round(pixels*4/1048576,2)))
print(json.dumps(dict(units=rows,totalRgbaMiB=round(sum(x['pagePixels']*4 for x in rows)/1048576,2),totalUniqueFrames=sum(x['uniqueFrames'] for x in rows),memoryMeaning='RGBA page-footprint estimate, not measured Android allocation'),indent=2))
