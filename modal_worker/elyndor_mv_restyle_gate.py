from __future__ import annotations

import base64, hashlib, io, json, time
from pathlib import Path
import modal

APP_NAME = "elyndor-mv-restyle-gate"
MODEL_ID = "Tongyi-MAI/Z-Image-Turbo"
SOURCE_B64 = Path("modal_worker/project_references/elyndor_mv_restyle_test_source.jpg.b64")
OUTPUT_PNG = Path("elyndor-mv-restyle-gate.png")
OUTPUT_JSON = Path("elyndor-mv-restyle-gate.json")
SIZE = 384
SEED = 1847
STEPS = 8
STRENGTH = 0.30
GUIDANCE = 0.0

PROMPT = """Restyle the supplied RPG Maker MV outdoor terrain sample while preserving its exact spatial layout, terrain boundaries, tile geometry, transitions, and material placement. This is image-to-image repainting, not redesign. Render clean polished Plushbound Legends first-area Elyndor terrain: bright meadow grass, readable packed earth/path surfaces, clean gray cobble/stone, subtle handcrafted fabric/plush character, restrained stitch-like detail, cohesive sunny JRPG palette. Preserve broad shapes and edge positions. Keep surfaces simple and readable at 48x48. No new objects, perspective, horizon, composition changes, random micro-noise, fuzzy static, grain carpet, speckle fields, repeated pebble wallpaper, photoreal texture, excessive detail, dramatic lighting, text, borders, labels, or UI."""

image = (modal.Image.debian_slim(python_version="3.11")
    .apt_install("git")
    .pip_install("torch>=2.5","transformers>=4.46","accelerate>=1.1","safetensors>=0.4","sentencepiece>=0.2","protobuf>=5","Pillow>=10","git+https://github.com/huggingface/diffusers.git"))
app = modal.App(APP_NAME)
model_cache = modal.Volume.from_name("freeframe-model-cache", create_if_missing=True)

@app.function(image=image, gpu=["L4","A10G"], timeout=1800, volumes={"/cache": model_cache})
def render(source_png: bytes) -> dict:
    import torch
    from PIL import Image
    from diffusers import ZImageImg2ImgPipeline
    src = Image.open(io.BytesIO(source_png)).convert("RGB")
    if src.size != (SIZE,SIZE):
        src = src.resize((SIZE,SIZE), Image.Resampling.LANCZOS)
    pipe = ZImageImg2ImgPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.bfloat16, cache_dir="/cache")
    pipe.to("cuda")
    generator = torch.Generator(device="cuda").manual_seed(SEED)
    started = time.time()
    result = pipe(prompt=PROMPT, image=src, width=SIZE, height=SIZE, strength=STRENGTH, num_inference_steps=STEPS, guidance_scale=GUIDANCE, generator=generator).images[0]
    elapsed = time.time()-started
    buf=io.BytesIO(); result.save(buf, format="PNG")
    return {"png_b64":base64.b64encode(buf.getvalue()).decode("ascii"),"gpu":torch.cuda.get_device_name(0),"elapsed_seconds":round(elapsed,3),"size":list(result.size)}

@app.local_entrypoint()
def main():
    if not SOURCE_B64.exists(): raise RuntimeError(f"Missing Elyndor MV source: {SOURCE_B64}")
    source=base64.b64decode("".join(SOURCE_B64.read_text().split()), validate=True)
    result=render.remote(source)
    output=base64.b64decode(result.pop("png_b64")); OUTPUT_PNG.write_bytes(output)
    metadata={"benchmark":"elyndor-mv-restyle-gate-v1","production_authorized":False,"compile_authorized":False,"model":MODEL_ID,"source_sha256":hashlib.sha256(source).hexdigest(),"output_sha256":hashlib.sha256(output).hexdigest(),"prompt_sha256":hashlib.sha256(PROMPT.encode()).hexdigest(),"strength":STRENGTH,"steps":STEPS,"guidance_scale":GUIDANCE,"seed":SEED,**result}
    OUTPUT_JSON.write_text(json.dumps(metadata,indent=2)+"\n")
    print(json.dumps(metadata,indent=2))
