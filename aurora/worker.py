"""Standalone Aurora text-to-image worker. No Plushbound imports."""
import io,json
from pathlib import Path
import modal
app=modal.App("aurora-pony-text2img-isolated")
img=modal.Image.debian_slim(python_version="3.11").pip_install("torch==2.5.1","diffusers==0.35.2","transformers==4.46.3","accelerate==1.2.1","huggingface_hub==0.36.0","safetensors==0.5.3","Pillow==11.1.0")
cache=modal.Volume.from_name("aurora-text2img-model-cache",create_if_missing=True)
@app.function(image=img,gpu="L4",timeout=1200,max_containers=1,scaledown_window=60,volumes={"/models":cache})
def generate(prompt:str,negative:str,steps:int,seed:int)->bytes:
    import torch
    from diffusers import StableDiffusionXLPipeline,EulerAncestralDiscreteScheduler
    from huggingface_hub import hf_hub_download
    filename=hf_hub_download(repo_id="LyliaEngine/Pony_Diffusion_V6_XL",filename="ponyDiffusionV6XL_v6StartWithThisOne.safetensors",local_dir="/models/checkpoint")
    cache.commit()
    pipe=StableDiffusionXLPipeline.from_single_file(filename,torch_dtype=torch.float16,use_safetensors=True,add_watermarker=False)
    pipe.scheduler=EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
    pipe.to("cuda")
    generator=torch.Generator(device="cuda").manual_seed(seed)
    with torch.inference_mode():
        result=pipe(prompt=prompt,negative_prompt=negative,num_inference_steps=steps,guidance_scale=6,width=1024,height=768,generator=generator).images[0]
    output=io.BytesIO();result.save(output,format="PNG");return output.getvalue()
@app.local_entrypoint()
def main(preset:str="controlled",output:str="outputs/controlled.png",steps:int=28,seed:int=123456):
    if not 1<=steps<=35: raise ValueError("steps out of range")
    presets=json.loads((Path(__file__).parent/"presets.json").read_text())
    if preset not in presets: raise ValueError("unknown preset")
    args=presets[preset]
    png=generate.remote(args["prompt"],args["negative_prompt"],steps,seed)
    path=Path(output);path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(png)
    print("Aurora generated",preset,path)
