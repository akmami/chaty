# Chaty

Chaty is a fun library designed to interact with OpenAI's ChatGPT models. It provides a simple interface to generate responses from the models, making it easy to integrate ChatGPT capabilities into your Python applications.

## Features

- Generate responses from ChatGPT models
- Easy-to-use interface
- Supports multiple OpenAI models

## Installation

You can install Chaty directly from GitHub or via PyPI (once it's published).

### Installing via GitHub

To install Chaty from GitHub, clone the repository and install it using `pip`:

```bash
git clone https://github.com/akmami/chaty.git
cd chaty
pip install .
```

## Installing Globally

To install Chaty globally, use the following command:

```bash
pip install . --global-option
```

Make sure you have the necessary permissions to install packages globally on your system.

## Usage

Here is an example of how to use Chaty:

```bash
from chaty.chat import ChatGPT

# Initialize the ChatGPT client
chatgpt = ChatGPT("your-OPENAI-API-token")

# Generate a response
prompt = "Tell me a joke about programming."
response = chatgpt.generate_response(prompt)
print(response)
```

## License

This project is licensed under the BSD 3-Clause License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenAI](https://openai.com/) for providing the GPT models and API.
