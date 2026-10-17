"""Basic Gradio UI scaffold. Set PYTHONPATH=src and confirm model access first."""
import gradio as gr
from helpdeskbuddy.model.load_model import load_model
from helpdeskbuddy.inference.chat import generate_reply

MODEL_ID = "google/gemma-3-4b-it"
MAX_NEW_TOKENS = 160

def main():
    tokenizer, model = load_model(MODEL_ID)
    def respond(message, history):
        return generate_reply(message, history, tokenizer, model, MAX_NEW_TOKENS)
    gr.ChatInterface(fn=respond, title="HelpDeskBuddy — IT Support Troubleshooting", description="Ask about common IT issues. Never enter passwords or verification codes.").launch()

if __name__ == "__main__":
    main()
