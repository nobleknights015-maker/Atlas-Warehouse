"""Aurora isolated Modal image-to-image worker. No Plushbound imports or deployments."""
import io, json
from pathlib import Path
import modal
APP_NAME="aurora-pony-img2img-isolated"
MODEL_ID="LyliaEngine/Pony_Diffusion_V6_XL"
MODEL_FILE="ponyDiffusionV6XL_v6StartWithThisOne.safetensors"
app=modal.App(APP_NAME)
image=(modal.Image.debian_slim(python_version="3.11")
       .pip_install("torch==2.5.1","diffusers==0.35.2","transformers==4.46.3",
                    "accelerate==1.2.1","huggingface_hub==0.36.0",
                    "safetensors==0.5.3","Pillow==11.1.0"))
cache=modal.Volume.from_name("aurora-pony-model-cache",create_if_missing=True)
@app.function(image=image,gpu="L4",timeout=1200,max_containers=1,scaledown_window=60,volumes={"/models":cache})
def generate(source:bytes,prompt:str,negative:str,strength:float,steps:int,seed:int)->bytes:
    import torch
    from PIL import Image
    from huggingface_hub import hf_hub_download
    from diffusers import StableDiffusionXLImg2ImgPipeline,EulerAncestralDiscreteScheduler
    if len(source)>16_000_000: raise ValueError("Reference image too large")
    if not 0.15<=strength<=0.85 or not 1<=steps<=35: raise ValueError("Invalid parameters")
    filename=hf_hub_download(repo_id=MODEL_ID,filename=MODEL_FILE,local_dir="/models/pony-xl")
    cache.commit()
    pipe=StableDiffusionXLImg2ImgPipeline.from_single_file(filename,torch_dtype=torch.float16,use_safetensors=True,add_watermarker=False)
    pipe.scheduler=EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
    pipe.to("cuda")
    src=Image.open(io.BytesIO(source)).convert("RGB")
    src.thumbnail((768,768),Image.Resampling.LANCZOS)
    w=max(512,round(src.width/64)*64);h=max(512,round(src.height/64)*64)
    src=src.resize((w,h),Image.Resampling.LANCZOS)
    generator=torch.Generator(device="cuda").manual_seed(seed)
    with torch.inference_mode():
        result=pipe(prompt=prompt,negative_prompt=negative,image=src,strength=strength,num_inference_steps=steps,guidance_scale=6,generator=generator).images[0]
    out=io.BytesIO();result.save(out,format="PNG");return out.getvalue()
@app.local_entrypoint()
def main(reference:str="reference.png",preset:str="controlled",output:str="result.png",strength:float=0.35,steps:int=28,seed:int=123456):
    root=Path(__file__).parent
    ref=Path(reference)
    if not ref.is_file(): raise FileNotFoundError("Missing reference.png. No GPU inference started.")
    presets=json.loads((root/"presets.json").read_text())
    if preset not in presets: raise ValueError("Unknown preset")
    if Path(output).resolve()==ref.resolve(): raise ValueError("Do not overwrite reference")
    args=presets[preset]
    data=generate.remote(ref.read_bytes(),args["prompt"],args["negative_prompt"],strength,steps,seed)
    Path(output).parent.mkdir(parents=True,exist_ok=True)
    Path(output).write_bytes(data)
    print("Aurora generated",preset,output)
