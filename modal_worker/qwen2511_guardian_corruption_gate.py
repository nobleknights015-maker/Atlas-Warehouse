"""One-shot QA gate: quantized Qwen-Image-Edit-2511 + Lightning Guardian identity test.

SAFETY-BOUNDED TEST ONLY.
- one A10G container maximum
- retries=0
- startup_timeout=60s
- input timeout=150s
- single-use container
- model/LoRA load happens inside the single method invocation so startup failures cannot respawn-load repeatedly
- one reference, one output, 4 inference steps
No batch or production rollout is authorized from this file.
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
MODEL_ID = "libaya/Qwen-Image-Edit-2511-4bit"
LORA_ID = "lightx2v/Qwen-Image-Edit-2511-Lightning"
LORA_WEIGHT = "Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors"
MODEL_VOLUME = "freeframe-model-cache"
CACHE_DIR = "/cache"
REFERENCE = Path("modal_worker/project_references/guardian_friendly_bramblebuck.jpg")
OUTPUT_PNG = "qwen2511-bramblebuck-identity-test.png"
SEED = 1847
STEPS = 4
TRUE_CFG = 1.0

PROMPT = (
    "Create a clean JRPG battler illustration of this exact Plush Guardian. Preserve the same identity, species, face, "
    "body proportions, silhouette, antlers, colors, fabric construction, stitching, and recognizable design. Keep it "
    "clearly the same character, not a redesign. Use a polished RPG Maker MV/Trinity-level game-art finish, centered "
    "full body, readable battle pose, simple unobtrusive background. No extra limbs, anatomy mutation, species change, "
    "costume replacement, random accessories, text, logo, or additional characters."
)

image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("libgl1", "libglib2.0-0")
    .pip_install(
        "accelerate>=1.0,<2",
        "bitsandbytes>=0.47,<1",
        "diffusers>=0.36,<0.40",
        "peft>=0.17,<1",
        "pillow>=10.4,<12",
        "safetensors",
        "sentencepiece",
        "torch>=2.6,<3",
        "torchvision",
        "transformers>=4.57,<6",
    )
    .add_local_file(str(REFERENCE), remote_path=f"/root/{REFERENCE}")
)

app = modal.App(APP_NAME)
model_cache = modal.Volume.from_name(MODEL_VOLUME, create_if_missing=True)

@app.cls(
    gpu="A10G",
    image=image,
    volumes={CACHE_DIR: model_cache},
    retries=0,
    max_containers=1,
    buffer_containers=0,
    startup_timeout=60,
    timeout=150,
    scaledown_window=2,
    single_use_containers=True,
)
class QwenGuardianGate:
    @modal.method()
    def run(self) -> dict:
        import torch
        from diffusers import QwenImageEditPlusPipeline
        from PIL import Image

        os.environ.setdefault("HF_HOME", CACHE_DIR)
        os.environ.setdefault("HF_HUB_CACHE", f"{CACHE_DIR}/hub")
        gpu_device = torch.cuda.get_device_name(0)

        pipe = QwenImageEditPlusPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=torch.bfloat16,
            cache_dir=CACHE_DIR,
        )
        pipe.load_lora_weights(
            LORA_ID,
            weight_name=LORA_WEIGHT,
            cache_dir=CACHE_DIR,
            adapter_name="lightning",
        )
        pipe.set_adapters(["lightning"], adapter_weights=[1.0])
        pipe.enable_model_cpu_offload()
        pipe.set_progress_bar_config(disable=True)

        raw_ref = REFERENCE.read_bytes()
        source = Image.open(io.BytesIO(raw_ref)).convert("RGB")
        source.thumbnail((768, 768), Image.Resampling.LANCZOS)
        generator = torch.Generator(device="cpu").manual_seed(SEED)

        started = time.monotonic()
        result = pipe(
            image=source,
            prompt=PROMPT,
            num_inference_steps=STEPS,
            true_cfg_scale=TRUE_CFG,
            negative_prompt=" ",
            generator=generator,
        ).images[0]
        elapsed = round(time.monotonic() - started, 3)

        out = io.BytesIO()
        result.save(out, format="PNG")
        raw = out.getvalue()
        return {
            "benchmark": "qwen2511-4bit-lightning-guardian-identity-gate-v4",
            "model": MODEL_ID,
            "lora": LORA_ID,
            "gpu_device": gpu_device,
            "reference_sha256": hashlib.sha256(raw_ref).hexdigest(),
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
