import streamlit as st
import requests
import base64

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display welcome message
st.write("Welcome to the Stable Diffusion Chat! Type a prompt and click Send to generate an image.")

# Display chat history
for message in st.session_state.chat_history:
    if message[0] == 'user':
        st.write(f"You: {message[1]}")
    elif message[0] == 'bot':
        st.image(message[1], use_column_width=True)

# User input form
with st.form(key='chat_form'):
    user_input = st.text_input('You: ', key='input_message')
    submitted = st.form_submit_button('Send')

if submitted and user_input.strip() != '':
    # Append user message to chat history
    st.session_state.chat_history.append(('user', user_input))
    
    # Send API request
    try:
        with st.spinner('Generating image...'):
            response = requests.post('http://localhost:8000/predict', json={'prompt': user_input}, timeout=10)
        
        if response.status_code == 200:
            img_str = response.json()['image']
            img_bytes = base64.b64decode(img_str)
            st.session_state.chat_history.append(('bot', img_bytes))
        else:
            st.write(f"API Error: {response.status_code} - {response.text}")
    
    except requests.exceptions.RequestException as e:
        st.write(f"An error occurred: {e}")

# Clear chat button
if st.button('Clear Chat'):
    st.session_state.chat_history = []