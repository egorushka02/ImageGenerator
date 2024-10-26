import torch
from diffusers import StableDiffusionXLPipeline

def create_pipe(model_name: str,
                custom_pipeline: str):
    """
    create StableDiffusion generator pipeline
    """
    device = "cuda" if torch.cuda.is_available else "cpu"
    pipe = StableDiffusionXLPipeline.from_pretrained(
        model_name,
        custom_pipeline,
        torch_dtype=torch.float16
    )

    pipe.to_device(device)
    return pipe