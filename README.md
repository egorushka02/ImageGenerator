# ImageGenerator
Simple image generation app

The original Perturbed-Attention Guidance for unconditional models and SD1.5 by Hyoungwon Cho is availiable at hyoungwoncho/sd_perturbed_attention_guidance


This repository is just a simple SDXL implementation of the Perturbed-Attention Guidance (PAG) on Stable Diffusion XL (SDXL) for the 🧨 diffusers library.

Quickstart
Loading Custom Pipeline:

```python
from diffusers import StableDiffusionXLPipeline

pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    custom_pipeline="multimodalart/sdxl_perturbed_attention_guidance",
    torch_dtype=torch.float16
)

device="cuda"
pipe = pipe.to(device)
Unconditional sampling with PAG:image/jpeg

output = pipe(
        "",
        num_inference_steps=50,
        guidance_scale=0.0,
        pag_scale=5.0,
        pag_applied_layers=['mid']
    ).images
Sampling with PAG and CFG:image/jpeg

output = pipe(
        "the spirit of a tamagotchi wandering in the city of Vienna",
        num_inference_steps=25,
        guidance_scale=4.0,
        pag_scale=3.0,
        pag_applied_layers=['mid']
    ).images
```
Example of output
![image](https://github.com/user-attachments/assets/14b856fa-968d-4f68-b13f-4bc6caf44866)
