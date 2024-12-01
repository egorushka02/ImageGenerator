# AI-Powered Image Generation Chat App

## Introduction

This project presents an AI-powered image generation app with a chat interface, leveraging the power of Stable Diffusion and Streamlit. Users can input prompts, generate images, and view them within a chat window, creating an interactive and intuitive experience.

## Features

- **Chat-based Interface**: Generate images by entering prompts in a chat-like interface.
- **Real-time Image Generation**: Instantly see the images generated based on your prompts.
- **Clear Chat History**: Easily reset the conversation with a single button click.

## Prerequisites

- Python 3.8 or higher
- Streamlit
- Requests library
- Stable Diffusion API server running separately

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ai-image-chat-app.git
   cd ai-image-chat-app
   ```

2. **Install Dependencies**

   ```bash
   pip install streamlit requests
   ```

3. **Start the Stable Diffusion API Server**

   Ensure the Stable Diffusion API server is running as per its documentation.

4. **Run the Streamlit App**

   ```bash
   streamlit run src/main.py
   ```

## Usage

1. **Start the API Server**

   Make sure the Stable Diffusion API server is up and running.

2. **Interact with the App**

   - Enter a prompt in the chat input field.
   - Click "Send" to generate an image.
   - View the generated image in the chat window.
   - Use the "Clear Chat" button to reset the conversation.

## How it Works

- **User Input**: Users input a prompt via Streamlit's chat input.
- **API Request**: The app sends the prompt to the Stable Diffusion API.
- **Image Generation**: The API generates an image and returns it as a Base64 string.
- **Display Image**: The app decodes the string and displays the image in the chat.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Streamlit**: For creating the interactive web interface.
- **Stable Diffusion**: For the powerful image generation model.
- **Contributors**: Special thanks to all contributors who have helped improve this project.
