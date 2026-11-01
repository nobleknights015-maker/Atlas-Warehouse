"""One-shot QA gate: Qwen-Image-Edit-2511 Guardian -> Corrupt Guardian.

Uses an existing project reference already committed to the FreeFrame branch.
This is deliberately one image only: no batch, no production rollout.
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

APP_NAME = "freeframe-qwen2511-guardian-gate"
MODEL_ID = "Qwen/Qwen-Image-Edit-2511"
MODEL_VOLUME = "freeframe-model-cache"
CACHE_DIR = "/cache"
REFERENCE = Path("modal_worker/project_references/guardian_friendly_bramblebuck.jpg")
OUTPUT_PNG = "qwen2511-bramblebuck-corrupt-test.png"
SEED = 1847
STEPS = 40
TRUE_CFG = 4.0

PROMPT = (
    "Edit this exact Plush Guardian into its corrupted counterpart while preserving the same creature identity, "
    "species, face, body proportions, silhouette, antlers/horns, clothing or adornment structure, and recognizable "
    "design features. The result must clearly be the same Guardian, not a new creature. Add Plushbound corruption "
    "through damaged stitching, frayed fabric, dark invasive thread growth, cracked charm-like details, restrained "
    "unstable magical energy, and a more hostile expression. Keep the design polished, readable, coherent, and "
    "JRPG character-art quality. Do not mutate anatomy, add extra limbs, change species, replace the costume, "
    "introduce random objects, or redesign the character from scratch. Keep a simple unobtrusive background."
)

image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("libgl1", "libglib2.0-0")
    .pip_install(
        "accelerate>=1.0",
        "diffusers>=0.36.0",
        "pillow>=10.4,<12",
        "safetensors",
        "sentencepiece",
        "torch>=2.6,<3",
        "transformers>=4.57,<6",
    )
    .add_local_file(str(REFERENCE), remote_path=f"/root/{REFERENCE}")
)

app = modal.App(APP_NAME)
model_cache = modal.Volume.from_name(MODEL_VOLUME, create_if_missing=True)


@app.cls(
    gpu="H100",
    image=image,
    volumes={CACHE_DIR: model_cache},
    scaledown_window=60,
    timeout=1800,
)
class QwenGuardianGate:
    @modal.enter()
    def load(self):
        import torch
        from diffusers import QwenImageEditPlusPipeline

        os.environ.setdefault("HF_HOME", CACHE_DIR)
        os.environ.setdefault("HF_HUB_CACHE", f"{CACHE_DIR}/hub")
        self.torch = torch
        self.gpu_device = torch.cuda.get_device_name(0)
        self.pipe = QwenImageEditPlusPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=torch.bfloat16,
            cache_dir=CACHE_DIR,
        )
        self.pipe.to("cuda")
        self.pipe.set_progress_bar_config(disable=True)

    @modal.method()
    def run(self) -> dict:
        from PIL import Image

        raw_ref = REFERENCE.read_bytes()
        reference_sha = hashlib.sha256(raw_ref).hexdigest()
        source = Image.open(io.BytesIO(raw_ref)).convert("RGB")
        generator = self.torch.Generator(device="cuda").manual_seed(SEED)

        started = time.monotonic()
        result = self.pipe(
            image=[source],
            prompt=PROMPT,
            num_inference_steps=STEPS,
            true_cfg_scale=TRUE_CFG,
            generator=generator,
        ).images[0]
        elapsed = round(time.monotonic() - started, 3)

        out = io.BytesIO()
        result.save(out, format="PNG")
        raw = out.getvalue()
        return {
            "benchmark": "qwen2511-guardian-corruption-gate-v1",
            "model": MODEL_ID,
            "gpu_device": self.gpu_device,
            "reference": str(REFERENCE),
            "reference_sha256": reference_sha,
            "prompt_sha256": hashlib.sha256(PROMPT.encode("utf-8")).hexdigest(),
            "seed": SEED,
            "steps": STEPS,
            "true_cfg_scale": TRUE_CFG,
            "width": result.width,
            "height": result.height,
            "elapsed_seconds": elapsed,
            "output_sha256": hashlib.sha256(raw).hexdigest(),
            "production_authorized": False,
            "batch_authorized": False,
            "png_base64": base64.b64encode(raw).decode("ascii"),
        }


@app.local_entrypoint()
def main():
    result = QwenGuardianGate().run.remote()
    png = base64.b64decode(result.pop("png_base64"))
    Path(OUTPUT_PNG).write_bytes(png)
    result["output_png"] = OUTPUT_PNG
    print(json.dumps(result, sort_keys=True))
