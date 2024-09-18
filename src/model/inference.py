import PIL
from model_load import create_pipe

def get_output(prompt: str,
             num_inference_steps: int,
             guidance_scale: float,
             pag_scale: float,
             pipe,
             pag_applied_layers=['m1']) -> PIL.Image:
    """
    generate output using prompt and hyperparameters
    """
    output = pipe(
        prompt,
        num_inference_steps=num_inference_steps,
        guidance_scale=guidance_scale,
        pag_scale=pag_scale,
        pag_applied_layers=pag_applied_layers
    ).images
    return output[0]


