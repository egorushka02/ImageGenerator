import argparse

from model.model_load import create_pipe
from model.inference import get_output



pipe = create_pipe(model_name='stabilityai/stable-diffusion-xl-base-1.0',
                   custom_pipeline='multimodalart/sdxl_perturbed_attention_guidance')

def generate_image(pipe):
    parser = argparse.ArgumentParser(description='add parser arguments')

    parser.add_argument('-r', '-prompt', type=str, help='your prompt')
    parser.add_argument('-s', '-num_inference_steps', type=int, help='number of inference steps')
    parser.add_argument('-g', '-guidance_scale', )
    parser.add_argument('-p', '-pag_scale', type=float, help='scale of the page')
    args = parser.parse_args()

    image = get_output(args.prompt,
                       args.num_inference_steps,
                       args.guidance_scale,
                       args.pag_scale,
                       pipe)
    image.save("image.png")
    return image