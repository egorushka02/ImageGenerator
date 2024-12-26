import streamlit as st
import requests
import base64
from io import BytesIO
from PIL import Image

st.title('Generation')
# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display chat messages
for message in st.session_state.chat_history:
    if message['role'] == 'user':
        with st.chat_message("user"):
            st.write(message['content'])
    elif message['role'] == 'assistant':
        with st.chat_message("assistant"):
            img_bytes = base64.b64decode(message['content'])
            st.image(img_bytes, use_column_width=True)

# Get user input
user_input = st.chat_input("You:")

# Process user input
if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append({'role': 'user', 'content': user_input})
    
    # Send API request with a loading message
    with st.spinner('Generating image...'):
        try:
            response = requests.post('https://8000-01jdhv44ydz8fptmq36pp5brmh.cloudspaces.litng.ai/predict', json={'prompt': user_input}, timeout=30)
            response.raise_for_status()
            img_str = response.json().get('image')
            # Store base64 string in chat history
            st.session_state.chat_history.append({'role': 'assistant', 'content': img_str})
            # Remove the loading message and rerun to display the image
            if img_str:
                # Decode the Base64 string to bytes
                img_bytes = base64.b64decode(img_str)

                # Convert bytes data to PIL Image
                img = Image.open(BytesIO(img_bytes))

                # Save the image
                st.image(img, f"your image: {user_input}")
        except requests.exceptions.HTTPError as http_err:
            st.error(f'HTTP error occurred: {http_err}')  
        except Exception as err:
            st.error(f'An error occurred: {err}')
