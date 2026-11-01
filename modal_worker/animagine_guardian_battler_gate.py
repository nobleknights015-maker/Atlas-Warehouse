"""One-shot bounded QA gate: Animagine XL 4.0 + IP-Adapter Guardian battler test.

One reference, one image, one GPU, zero retries, one container, short timeouts.
"""
from __future__ import annotations

import base64
import hashlib
import io
import json
import os
import time
from pathlib import Path

import modal

APP_NAME = "freeframe-animagine-guardian-battler-gate"
MODEL_ID = "iiYonko/animagine-xl-4.0"
IP_ADAPTER_ID = "h94/IP-Adapter"
IP_ADAPTER_SUBFOLDER = "sdxl_models"
IP_ADAPTER_WEIGHT = "ip-adapter-plus_sdxl_vit-h.safetensors"
IMAGE_ENCODER_SUBFOLDER = "models/image_encoder"
MODEL_VOLUME = "freeframe-model-cache"
CACHE_DIR = "/cache"
REFERENCE = Path("modal_worker/project_references/guardian_friendly_bramblebuck.jpg")
OUTPUT_PNG = "animagine-bramblebuck-battler-test.png"
SEED = 1847
WIDTH = 768
HEIGHT = 768
STEPS = 20
GUIDANCE = 6.0
IP_SCALE = 0.78

PROMPT = (
    "full-body JRPG monster battler, same plush Guardian as reference, preserve species, face, antlers, silhouette, colors, "
    "handcrafted plush texture, clean RPG Maker MV Trinity quality, readable anime game asset, front three-quarter battle pose, "
    "single centered character, simple background, high quality"
)
NEGATIVE = (
    "different species, human, extra limbs, duplicate, mutated anatomy, deformed, cropped, scenery, text, watermark, "
    "photorealistic, fuzzy, noisy, low quality"
)

image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("libgl1", "libglib2.0-0")
    .pip_install(
        "accelerate>=1.2,<2",
        "diffusers>=0.36,<0.40",
        "pillow>=10.4,<12",
        "safetensors",
        "torch>=2.6,<3",
        "transformers>=4.48,<6",
    )
    .add_local_file(str(REFERENCE), remote_path=f"/root/{REFERENCE}")
)

app = modal.App(APP_NAME)
model_cache = modal.Volume.from_name(MODEL_VOLUME, create_if_missing=True)

@app.cls(
    gpu=["L4", "A10G"],
    image=image,
    volumes={CACHE_DIR: model_cache},
    retries=0,
    max_containers=1,
    buffer_containers=0,
    startup_timeout=120,
    timeout=180,
    scaledown_window=2,
    single_use_containers=True,
)
class AnimagineGuardianBattlerGate:
    @modal.enter()
    def load(self):
        import torch
        from diffusers import AutoPipelineForText2Image
        from transformers import CLIPVisionModelWithProjection

        os.environ.setdefault("HF_HOME", CACHE_DIR)
        os.environ.setdefault("HF_HUB_CACHE", f"{CACHE_DIR}/hub")
        self.torch = torch
        self.gpu_device = torch.cuda.get_device_name(0)

        image_encoder = CLIPVisionModelWithProjection.from_pretrained(
            IP_ADAPTER_ID,
            subfolder=IMAGE_ENCODER_SUBFOLDER,
            torch_dtype=torch.float16,
            cache_dir=CACHE_DIR,
        )
        self.pipe = AutoPipelineForText2Image.from_pretrained(
            MODEL_ID,
            image_encoder=image_encoder,
            torch_dtype=torch.float16,
            cache_dir=CACHE_DIR,
        )
        self.pipe.load_ip_adapter(
            IP_ADAPTER_ID,
            subfolder=IP_ADAPTER_SUBFOLDER,
            weight_name=IP_ADAPTER_WEIGHT,
            cache_dir=CACHE_DIR,
        )
        self.pipe.set_ip_adapter_scale(IP_SCALE)
        self.pipe.enable_model_cpu_offload()
        self.pipe.set_progress_bar_config(disable=True)

    @modal.method()
    def run(self) -> dict:
        from PIL import Image

        raw_ref = REFERENCE.read_bytes()
        source = Image.open(io.BytesIO(raw_ref)).convert("RGB")
        source.thumbnail((768, 768), Image.Resampling.LANCZOS)
        generator = self.torch.Generator(device="cuda").manual_seed(SEED)

        started = time.monotonic()
        result = self.pipe(
            prompt=PROMPT,
            negative_prompt=NEGATIVE,
            ip_adapter_image=source,
            width=WIDTH,
            height=HEIGHT,
            num_inference_steps=STEPS,
            guidance_scale=GUIDANCE,
            generator=generator,
        ).images[0]
        elapsed = round(time.monotonic() - started, 3)

        out = io.BytesIO()
        result.save(out, format="PNG")
        raw = out.getvalue()
        return {
            "benchmark": "animagine-ipadapter-guardian-battler-gate-v2-vit-h",
            "model": MODEL_ID,
            "ip_adapter": IP_ADAPTER_ID,
            "gpu_device": self.gpu_device,
            "reference_sha256": hashlib.sha256(raw_ref).hexdigest(),
            "seed": SEED,
            "steps": STEPS,
            "elapsed_seconds": elapsed,
            "output_sha256": hashlib.sha256(raw).hexdigest(),
            "png_base64": base64.b64encode(raw).decode("ascii"),
        }

@app.local_entrypoint()
def main():
    result = AnimagineGuardianBattlerGate().run.remote()
    png = base64.b64decode(result.pop("png_base64"))
    Path(OUTPUT_PNG).write_bytes(png)
    result["output_png"] = OUTPUT_PNG
    print(json.dumps(result, sort_keys=True))
