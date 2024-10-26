import streamlit as st

from model.model_load import create_pipe
from model.inference import get_output

import torch
from diffusers import StableDiffusionXLPipeline


st.title("AI Image generator")

def configure_sidebar():
    with st.sidebar:
        with st.form("my_form"):
            prompt = st.text_area("enter prompt:")
            submitted = st.form_submitt_button("Send", type="primary")
        return {
            "prompt": prompt,
            "submitted": submitted
        }
    

def main_page(
        prompt: str,
        submitted: bool,
        pipe
):
    if submitted:
        with st.spinner("in process..."):
            result = get_output(prompt,
                                5,
                                4.0,
                                0.0)
            with st.container():
                st.image(result, "your generated image")

@st.cache_data
def main():
    # pipe = create_pipe(model_name='stabilityai/stable-diffusion-xl-base-1.0',
    #                custom_pipeline='multimodalart/sdxl_perturbed_attention_guidance')
    pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    custom_pipeline="multimodalart/sdxl_perturbed_attention_guidance",
    torch_dtype=torch.float16
)
    data = configure_sidebar()
    main_page(**data)

if __name__ == "__main__":
    main()
    