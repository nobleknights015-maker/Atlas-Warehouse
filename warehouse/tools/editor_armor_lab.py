#!/usr/bin/env python3
"""Generic, non-canonical 72x112 sprite with 4 layers / 3 frames.
Creates a real .ase file for LibreSprite practice. This is NOT user artwork.
"""
from pathlib import Path
from PIL import Image, ImageDraw
import struct, zlib, json

DIR=Path("training_run"); W,H=72,112; FRAMES=3
NAMES=["internal_structure","faceted_armor","drapery","signals"]
C={"ink":"#141a23","dark":"#28303b","steel":"#505b65",
   "bone0":"#6e6b62","bone1":"#b0a99b","bone2":"#dad2ba",
   "bone3":"#f2ead0","cloth0":"#404657","cloth1":"#6e7687",
   "copper":"#bd7957","glow0":"#155264","glow1":"#3cc4ce",
   "glow2":"#a6f6ef"}
def poly(d,color,points): d.polygon(points,fill=C[color])
def line(d,color,points,w=1):d.line(points,fill=C[color],width=w)
def box(d,color,coords):d.rectangle(coords,fill=C[color])

def layer_image(layer,frame):
    im=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    if layer==0:
        poly(d,"ink",[(28,20),(44,20),(50,32),(46,62),(51,72),(43,78),(25,75),(23,52)])
        poly(d,"dark",[(28,26),(42,26),(45,53),(39,68),(29,65)])
        # Real multi-jointed limbs and stable feet
        poly(d,"ink",[(26,71),(35,73),(32,96),(30,106),(16,107),(18,101)])
        poly(d,"ink",[(41,73),(48,70),(53,94),(59,107),(42,109),(41,99)])
        poly(d,"dark",[(25,77),(32,77),(29,99),(22,102)])
        poly(d,"dark",[(42,77),(47,76),(51,101),(45,104)])
        poly(d,"ink",[(17,29),(24,28),(26,50),(22,67),(20,77),(13,76),(12,69),(16,52),(12,42)])
        poly(d,"ink",[(46,29),(54,29),(60,45),(56,62),(63,75),(58,80),(51,76),(48,58)])
        poly(d,"dark",[(17,37),(22,37),(21,56),(17,62)])
        poly(d,"dark",[(50,38),(54,40),(56,55),(52,63)])
        poly(d,"ink",[(22,9),(27,4),(42,4),(48,11),(49,22),(45,26),(26,25),(20,18)])
        poly(d,"dark",[(25,10),(31,7),(41,9),(46,16),(42,22),(27,22)])
        poly(d,"dark",[(29,22),(42,22),(41,31),(30,30)])
    elif layer==1:
        # Faceted helmet (head), overlapping plates and deliberate material faces
        poly(d,"bone0",[(20,12),(28,4),(34,5),(32,15),(27,19),(21,18)])
        poly(d,"bone2",[(22,11),(28,5),(33,6),(31,13),(25,17)])
        line(d,"bone3",[(24,10),(29,6),(31,7)])
        poly(d,"bone0",[(34,4),(43,7),(48,13),(45,18),(36,13),(30,17)])
        poly(d,"bone2",[(36,6),(42,8),(46,13),(42,14),(35,12),(32,16)])
        line(d,"bone3",[(36,6),(41,9)])
        poly(d,"bone1",[(22,18),(28,18),(27,23),(23,21)])
        poly(d,"bone1",[(44,18),(48,18),(47,23),(44,24)])
        box(d,"ink",(47,17,52,23));box(d,"bone0",(49,18,51,21))
        # Shoulders and torax, angled triangular construction
        poly(d,"bone0",[(20,29),(25,30),(28,36),(24,43),(14,41),(13,35)])
        poly(d,"bone2",[(18,31),(24,31),(26,36),(23,39),(16,38)])
        line(d,"bone3",[(18,31),(23,31)])
        poly(d,"bone0",[(46,28),(54,31),(59,37),(56,43),(49,44),(43,36)])
        poly(d,"bone1",[(47,30),(52,32),(56,37),(53,40),(47,39)])
        line(d,"bone3",[(48,30),(52,32)])
        poly(d,"bone0",[(28,30),(42,30),(46,36),(41,46),(30,46),(24,36)])
        poly(d,"bone2",[(29,31),(39,31),(43,35),(39,40),(29,40),(27,35)])
        poly(d,"bone3",[(30,32),(37,32),(40,34),(31,35)])
        poly(d,"bone0",[(29,42),(41,42),(38,51),(30,50)])
        poly(d,"bone1",[(31,43),(39,43),(37,48),(32,48)])
        poly(d,"bone0",[(25,54),(31,50),(40,50),(46,55),(43,64),(37,67),(28,64)])
        poly(d,"bone1",[(27,54),(32,52),(39,52),(43,56),(39,60),(30,60)])
        poly(d,"bone0",[(25,65),(35,68),(43,64),(47,68),(41,74),(29,74),(23,68)])
        poly(d,"bone2",[(27,66),(34,69),(43,66),(40,71),(29,71)])
        # Thighs, shins, rigid boots
        poly(d,"bone0",[(24,71),(31,75),(29,85),(21,85),(20,80)])
        poly(d,"bone2",[(23,74),(29,76),(27,81),(22,82)])
        poly(d,"bone0",[(41,74),(47,71),(52,81),(48,86),(43,85)])
        poly(d,"bone1",[(43,75),(47,74),(49,81),(45,83)])
        poly(d,"bone0",[(21,87),(28,85),(31,91),(28,103),(18,103),(19,94)])
        poly(d,"bone2",[(22,89),(27,88),(28,92),(25,100),(20,101)])
        poly(d,"bone0",[(43,87),(49,86),(53,99),(57,104),(45,106),(42,100)])
        poly(d,"bone2",[(44,89),(48,89),(51,99),(46,103)])
        poly(d,"bone0",[(17,102),(29,102),(29,108),(16,108),(15,105)])
        poly(d,"bone1",[(19,104),(27,104),(27,106),(17,106)])
        poly(d,"bone0",[(45,103),(56,103),(59,106),(58,109),(43,109),(41,106)])
        poly(d,"bone1",[(45,105),(55,105),(57,107),(44,107)])
        # Arm shields and differentiated hands
        poly(d,"bone0",[(15,43),(20,42),(23,55),(20,65),(14,65)])
        poly(d,"bone1",[(16,45),(19,45),(21,55),(19,62),(16,62)])
        poly(d,"bone0",[(49,43),(55,43),(58,58),(55,67),(49,64)])
        poly(d,"bone1",[(50,45),(53,46),(55,56),(52,63)])
        poly(d,"bone0",[(13,69),(19,68),(21,74),(18,81),(13,79)])
        poly(d,"bone0",[(54,68),(60,69),(62,76),(58,81),(54,78)])
        line(d,"bone1",[(15,75),(15,79)])
        line(d,"bone1",[(18,76),(18,80)])
        line(d,"bone1",[(57,76),(57,80)])
    elif layer==2:
        sway=frame-1
        poly(d,"cloth0",[(49,31),(53,34),(56,42),(54+sway,53),(59+sway,67),(56+sway,76),(52+sway,71),(49,61)])
        poly(d,"cloth1",[(51,36),(54,41),(53+sway,53),(57+sway,66),(54+sway,70),(52,60)])
        line(d,"bone0",[(52,39),(53+sway,53),(56+sway,65)])
        poly(d,"cloth0",[(23,35),(26,39),(24,50),(22,55),(19,52),(21,43)])
        line(d,"cloth1",[(24,39),(22,49),(21,52)])
        line(d,"copper",[(47,44),(46,49),(48,55)],2)
        line(d,"copper",[(23,83),(21,87),(20,90)],2)
    elif layer==3:
        if frame!=1:
            line(d,"glow1",[(26,17),(32,20),(36,18),(42,17)])
            line(d,"glow2",[(31,19),(33,20),(35,19)])
        else:
            line(d,"glow0",[(26,17),(32,20),(36,18),(42,17)])
        box(d,"glow1" if frame!=1 else "glow0",(49,18,50,20))
        poly(d,"glow0",[(34,52),(37,54),(34,57),(31,54)])
        box(d,"glow1" if frame!=1 else "glow0",(33,54,35,55))
        box(d,"glow1",(51,55,52,57))
    return im

def chunk(t,body): return struct.pack("<IH",len(body)+6,t)+body
def layer_chunk(name):
    n=name.encode()
    return chunk(0x2004,struct.pack("<HHHHHHB",3,0,0,W,H,0,255)+b"\0"*3+struct.pack("<H",len(n))+n)
def cel_chunk(i,im):
    return chunk(0x2005,struct.pack("<HhhBHh",i,0,0,255,2,0)+b"\0"*5+
                 struct.pack("<HH",W,H)+zlib.compress(im.tobytes(),9))
def make():
    DIR.mkdir(exist_ok=True)
    all_frames=[]
    for f in range(FRAMES):
        layers=[layer_image(i,f) for i in range(4)]
        all_frames.append(layers)
        composite=Image.new("RGBA",(W,H))
        for li in layers:composite.alpha_composite(li)
        composite.save(DIR/("input_frame_%d.png"%f))
    frames=[]
    for f,layers in enumerate(all_frames):
        chunks=([layer_chunk(n) for n in NAMES] if f==0 else []) + [cel_chunk(i,im) for i,im in enumerate(layers)]
        body=b"".join(chunks)
        frames.append(struct.pack("<IHHH",16+len(body),0xF1FA,len(chunks),180)+b"\0"*2+
                      struct.pack("<I",len(chunks))+body)
    head=bytearray(128)
    struct.pack_into("<IHHHHH",head,0,128+sum(len(x) for x in frames),0xA5E0,FRAMES,W,H,32)
    struct.pack_into("<I",head,14,1)
    struct.pack_into("<H",head,18,180)
    head[34]=1;head[35]=1
    (DIR/"input_layers.ase").write_bytes(bytes(head)+b"".join(frames))
    print("Generated four-layer ASE and three reference RGBA frames",W,H,NAMES)

if __name__=="__main__":make()
