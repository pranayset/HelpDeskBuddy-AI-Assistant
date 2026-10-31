
import os
import gradio as gr
from dotenv import load_dotenv

from helpdeskbuddy.model.load_model import load_model
from helpdeskbuddy.inference.chat import generate_reply


load_dotenv()

BASE_MODEL = os.getenv(
    "BASE_MODEL",
    "google/gemma-3-4b-it",
)

ADAPTER_DIR = os.getenv("ADAPTER_DIR")

MAX_NEW_TOKENS = int(
    os.getenv("MAX_NEW_TOKENS", "250")
)


print("Loading HelpDeskBuddy AI...")

processor, model = load_model(
    model_id=BASE_MODEL,
    adapter_dir=ADAPTER_DIR,
)

print("HelpDeskBuddy AI loaded successfully.")


def respond(message, history):
    return generate_reply(
        message,
        history,
        processor,
        model,
        MAX_NEW_TOKENS,
    )


demo = gr.ChatInterface(
    fn=respond,
    title="HelpDeskBuddy AI Assistant",
    description=(
        "IT Support Troubleshooting Chatbot | "
        "Gemma 3 4B IT + LoRA"
    ),
    textbox=gr.Textbox(
        placeholder="Ask an IT support question...",
        label="Your question",
    ),
)


if __name__ == "__main__":
    demo.launch(
        share=False,
        debug=False,
    )
