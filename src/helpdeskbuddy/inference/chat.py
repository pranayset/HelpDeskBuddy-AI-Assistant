"""Minimal text-generation helper; adapt to the selected model's chat template."""
import torch
from helpdeskbuddy.prompts import SYSTEM_PROMPT

def generate_reply(message, history, tokenizer, model, max_new_tokens=160):
    turns = [SYSTEM_PROMPT]
    for user_text, assistant_text in (history or [])[-4:]:
        turns.append(f"User: {user_text}\nAssistant: {assistant_text}")
    turns.append(f"User: {message}\nAssistant:")
    prompt = "\n\n".join(turns)
    inputs = tokenizer(prompt, return_tensors="pt")
    device = next(model.parameters()).device
    inputs = {key: value.to(device) for key, value in inputs.items()}
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=True, temperature=0.7, pad_token_id=tokenizer.eos_token_id)
    generated = output[0][inputs["input_ids"].shape[-1]:]
    return tokenizer.decode(generated, skip_special_tokens=True).strip()
