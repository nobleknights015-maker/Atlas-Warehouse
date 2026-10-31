"""Bounded Z-Image-Turbo challenger benchmark for the failing Tideglass tile case.

This is QA-only. It reuses the production Tideglass prompt contract and the exact
material-specific tidal_silt conditioning anchor, renders one 384x384 source master,
and never authorizes compile or production rollout.
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

APP_NAME = "freeframe-zimage-tideglass-benchmark"
MODEL_ID = "Tongyi-MAI/Z-Image-Turbo"
MODEL_VOLUME = "freeframe-model-cache"
CACHE_DIR = "/cache"
OUTPUT_PNG = "zimage-tidal-silt-output.png"
ASSET_ID = "tileset.tideglass-coast.a5.source.tidal_silt"
ANCHOR_PATH = Path("modal_worker/project_references/tideglass_correction_round/tidal_silt_reference_anchor_256.jpg")
CONDITIONING_PATH = Path("modal_worker/world_asset_pipeline_v2_reference_conditioning.json")
GPU_CANDIDATES = ["L4", "A10G"]
WIDTH = 384
HEIGHT = 384
STEPS = 8
GUIDANCE = 0.0
STRENGTH = 0.6

image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("libgl1", "libglib2.0-0")
    .pip_install(
        "accelerate",
        "diffusers>=0.37.1",
        "pillow>=10.4,<12",
        "safetensors",
        "sentencepiece",
        "torch>=2.6,<3",
        "transformers>=4.51,<6",
    )
    .add_local_python_source("modal_worker")
    .add_local_file(str(ANCHOR_PATH), remote_path=f"/root/{ANCHOR_PATH}")
)

app = modal.App(APP_NAME)
model_cache = modal.Volume.from_name(MODEL_VOLUME, create_if_missing=True)


def build_case() -> dict:
    """Freeze the exact production prompt/seed locally before crossing into Modal."""
    from modal_worker.world_asset_pipeline_v2_flux2_reference_batch import build_repair_rows

    rows, _ = build_repair_rows("tideglass-coast", [ASSET_ID])
    row = rows[0]
    conditioning = json.loads(CONDITIONING_PATH.read_text(encoding="utf-8"))["regions"]["tideglass-coast"]
    prompt = str(conditioning["conditioning_prompt_prefix"]).strip() + " " + str(row["prompt"]).strip()
    anchor_raw = ANCHOR_PATH.read_bytes()
    return {
        "asset_id": ASSET_ID,
        "prompt": prompt,
        "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        "seed": int(row["seed"]),
        "anchor_sha256": hashlib.sha256(anchor_raw).hexdigest(),
    }


@app.cls(
    gpu=GPU_CANDIDATES,
    image=image,
    volumes={CACHE_DIR: model_cache},
    scaledown_window=60,
    timeout=1200,
)
class ZImageTileBenchmark:
    @modal.enter()
    def load(self):
        import torch
        from diffusers import ZImageImg2ImgPipeline

        os.environ.setdefault("HF_HOME", CACHE_DIR)
        os.environ.setdefault("HF_HUB_CACHE", f"{CACHE_DIR}/hub")
        self.torch = torch
        self.gpu_device = torch.cuda.get_device_name(0)
        self.pipe = ZImageImg2ImgPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=torch.bfloat16,
            cache_dir=CACHE_DIR,
        )
        self.pipe.to("cuda")
        self.pipe.set_progress_bar_config(disable=True)

    @modal.method()
    def run(self, case: dict) -> dict:
        from PIL import Image

        required = {"asset_id", "prompt", "prompt_sha256", "seed", "anchor_sha256"}
        if set(case) != required:
            raise ValueError("benchmark case contract mismatch")
        if case["asset_id"] != ASSET_ID:
            raise ValueError("benchmark asset_id drift")
        if hashlib.sha256(str(case["prompt"]).encode("utf-8")).hexdigest() != case["prompt_sha256"]:
            raise ValueError("benchmark prompt hash mismatch")
        anchor_raw = ANCHOR_PATH.read_bytes()
        if hashlib.sha256(anchor_raw).hexdigest() != case["anchor_sha256"]:
            raise ValueError("benchmark anchor hash mismatch")

        reference = Image.open(io.BytesIO(anchor_raw)).convert("RGB")
        source_reference_size = list(reference.size)
        reference = reference.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
        inference_reference_size = list(reference.size)

        generator = self.torch.Generator(device="cuda").manual_seed(int(case["seed"]))
        started = time.monotonic()
        rendered = self.pipe(
            prompt=str(case["prompt"]),
            image=reference,
            strength=STRENGTH,
            width=WIDTH,
            height=HEIGHT,
            num_inference_steps=STEPS,
            guidance_scale=GUIDANCE,
            generator=generator,
        ).images[0]
        elapsed = round(time.monotonic() - started, 3)
        out = io.BytesIO()
        rendered.save(out, format="PNG")
        raw = out.getvalue()
        return {
            "benchmark": "zimage-tideglass-tile-v4-matched-img2img-dimensions",
            "asset_id": case["asset_id"],
            "model": MODEL_ID,
            "gpu_candidates": GPU_CANDIDATES,
            "gpu_device": self.gpu_device,
            "width": rendered.width,
            "height": rendered.height,
            "reference_source_size": source_reference_size,
            "reference_inference_size": inference_reference_size,
            "reference_resize": "lanczos-conditioning-only",
            "steps": STEPS,
            "guidance_scale": GUIDANCE,
            "strength": STRENGTH,
            "seed": int(case["seed"]),
            "prompt_sha256": case["prompt_sha256"],
            "anchor_sha256": case["anchor_sha256"],
            "elapsed_seconds": elapsed,
            "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "production_authorized": False,
            "compile_authorized": False,
            "catalog_wide_launch_authorized": False,
            "png_base64": base64.b64encode(raw).decode("ascii"),
        }


@app.local_entrypoint()
def main():
    case = build_case()
    result = ZImageTileBenchmark().run.remote(case)
    png = base64.b64decode(result.pop("png_base64"))
    Path(OUTPUT_PNG).write_bytes(png)
    result["output_png"] = OUTPUT_PNG
    print(json.dumps(result, sort_keys=True))
