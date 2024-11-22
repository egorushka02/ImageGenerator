# Perturbed-Attention Guidance (PAG) Image Generation App

## Overview

This repository contains the implementation of an image generation application that leverages the **Perturbed-Attention Guidance (PAG)** technique, as described in the paper ["Self-Rectifying Diffusion Sampling with Perturbed-Attention Guidance"](https://arxiv.org/abs/2403.17377). The app is designed to generate high-quality images using diffusion models, enhancing the sample quality across both unconditional and conditional settings without requiring additional training or external modules.

## Features

- **High-Quality Image Generation**: Utilizes PAG to improve the quality of generated images, even in unconditional settings.
- **Versatile Guidance**: Applicable to various downstream tasks such as image restoration, ControlNet with empty prompts, and more.
- **No Additional Training Required**: PAG operates without the need for additional training or external modules, making it efficient and easy to integrate.
- **User-Friendly Interface**: Provides a simple and intuitive interface for users to generate images with customizable settings.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   https://github.com/egorushka02/ImageGenerator.git
   cd ImageGenerator
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

To start the image generation application, run the following command:

```bash
python src/main.py
```

### Customizing Settings

The application allows users to customize various settings such as:

- **Guidance Scale**: Adjust the strength of the PAG guidance.
- **Sampling Steps**: Define the number of steps for the diffusion process.
- **Conditional Settings**: Specify conditions such as class labels or text prompts for conditional generation.

### Example Commands

Here are some example commands to generate images with different settings:

- **Unconditional Generation**:
  ```bash
  python src/main.py
  ```

## Results

The application generates high-quality images that demonstrate the effectiveness of PAG in improving sample quality. You can find example generated images in the `results` directory.

## Contributing

We welcome contributions to improve and extend this application. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

Happy image generating! 🎨
