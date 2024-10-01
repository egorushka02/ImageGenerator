import argparse

from model.model_load import create_pipe
from model.inference import get_output



pipe = create_pipe(model_name='stabilityai/stable-diffusion-xl-base-1.0',
                   custom_pipeline='multimodalart/sdxl_perturbed_attention_guidance')


def generate_image(pipe):    
    image = get_output("detailed, fantasy landscape painting featuring a majestic dragon soaring above a dense forest",
                       15,
                       4.0,
                       0.0,
                       pipe)
    image.save("image.png")
    return image


if __name__ == "__main__":
    generate_image(pipe)