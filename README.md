
# Gradio + Ollama Chat Application

This repository contains a simple Python application that integrates Gradio with the Ollama API to create an interactive chat interface. The app streams responses from the `smollm2` model in real-time, providing a dynamic and responsive user experience.

## Features

- **Real-time chat streaming:** Responses are streamed token by token.
- **Gradio UI:** Simple and user-friendly chat interface built with Gradio.
- **Customizable roles:** The app supports user and assistant roles.

## Requirements

- Python 3.9 or higher
- The following Python packages:
  - `ollama`
  - `gradio`

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:KameniAlexNea/chat-llama.git
   cd chat-llama
   ```
2. Install dependencies:

   ```bash
   pip install ollama gradio
   ```

## Usage

Run the application with the following command:

```bash
python chat.py
```

By default, the app will start on `http://0.0.0.0:7860` and will be accessible from all network interfaces. You can open this URL in your browser or share the host machine's IP address to access the app on other devices within the same network.

## Docker Support

You can also run this application using Docker:

### 1. Build the Docker Image

```bash
docker build -t gradio-ollama-app .
```

### 2. Run the Docker Container

```bash
docker run -p 7860:7860 gradio-ollama-app
```

Access the app at `http://localhost:7860`.

## Code Overview

Here is a brief explanation of the key parts of the code:

- **Model Name:** The application uses the `smollm2` model for chat functionality.
- **`predict` Function:** Handles user input, maintains chat history, and streams responses from the Ollama API.
- **Gradio Chat Interface:** A simple chat UI is created using `gr.ChatInterface`.
- **Server Binding:** The app binds to `0.0.0.0` to allow access from external devices.

### Example Code Snippet

```python
import ollama
import gradio as gr

model_name = "smollm2"
role = ["user", "assistant"]

def predict(message, history):
    result = ""
    history.append([message])
    messages = [
        {"role": role[i], "content": msg} for raw in history for i, msg in enumerate(raw)
    ]

    for token in ollama.chat(
        model_name, messages=messages,
        stream=True
    ):
        result += token.message.content
        yield result

demo = gr.ChatInterface(
    predict,
)

demo.launch(server_name="0.0.0.0")
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with any improvements.

## License

This project is licensed under the [Apache License](LICENSE).

## Acknowledgements

- **Gradio:** For the intuitive and easy-to-use interface library.
- **Ollama:** For the chat model API powering the application.
