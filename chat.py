import ollama
import gradio as gr

model_name = "smollm2"


def predict(message, history):
    result = ""
    messages = (history or []) + [{"role": "user", "content": message}]

    for token in ollama.chat(
        model_name, messages=messages,
        stream=True
    ):
        result += token.message.content
        yield result

demo = gr.ChatInterface(
    predict,
    #type="messages"
)

demo.launch()