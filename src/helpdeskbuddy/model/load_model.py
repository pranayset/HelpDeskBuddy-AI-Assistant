
import torch
from transformers import AutoProcessor, Gemma3ForConditionalGeneration
from peft import PeftModel


def load_model(
    model_id="google/gemma-3-4b-it",
    adapter_dir=None,
):
    """Load Gemma 3 4B IT and its trained LoRA adapter."""

    if not adapter_dir:
        raise ValueError("ADAPTER_DIR must be configured.")

    processor = AutoProcessor.from_pretrained(model_id)

    base_model = Gemma3ForConditionalGeneration.from_pretrained(
        model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        attn_implementation="sdpa",
    )

    model = PeftModel.from_pretrained(
        base_model,
        adapter_dir,
    )

    model.eval()

    return processor, model
