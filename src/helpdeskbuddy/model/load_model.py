"""Load a Hugging Face model and tokenizer. Check model access and hardware first."""
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model(model_id="google/gemma-3-4b-it", **kwargs):
    """Return (tokenizer, model); model-specific classes/templates may be needed."""
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, **kwargs)
    return tokenizer, model
