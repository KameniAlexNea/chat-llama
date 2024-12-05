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