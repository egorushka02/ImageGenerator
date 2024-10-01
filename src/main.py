import streamlit as st

from model.model_load import create_pipe
from model.inference import get_output


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

@st.cache(allow_output_mutation=True)
def main():
    pipe = create_pipe(model_name='stabilityai/stable-diffusion-xl-base-1.0',
                   custom_pipeline='multimodalart/sdxl_perturbed_attention_guidance')
    data = configure_sidebar()
    main_page(**data)

if __name__ == "__main__":
    main()
    