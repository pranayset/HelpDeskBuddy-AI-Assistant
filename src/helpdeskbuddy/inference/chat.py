import torch
from helpdeskbuddy.prompts import SYSTEM_PROMPT


def normalize_history(history):
    messages = []

    if not history:
        return messages

    if isinstance(history[0], dict) and "role" in history[0]:
        for item in history[-8:]:
            role = item.get("role")
            content = item.get("content")

            if role in ("user", "assistant") and isinstance(content, str):
                messages.append((role, content))

    else:
        for turn in history[-4:]:
            if isinstance(turn, dict):
                user_text = turn.get("user")
                assistant_text = turn.get("assistant")
            else:
                user_text, assistant_text = turn

            if user_text:
                messages.append(("user", user_text))

            if assistant_text:
                messages.append(("assistant", assistant_text))

    return messages


def generate_reply(
    message,
    history,
    processor,
    model,
    max_new_tokens=250,
):
    if not message or not message.strip():
        return "Please enter an IT support question."

    messages = [
        {
            "role": "system",
            "content": [
                {"type": "text", "text": SYSTEM_PROMPT}
            ],
        }
    ]

    for role, text in normalize_history(history):
        messages.append({
            "role": role,
            "content": [{"type": "text", "text": text}],
        })

    messages.append({
        "role": "user",
        "content": [{"type": "text", "text": message}],
    })

    inputs = processor.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    )

    input_device = model.get_input_embeddings().weight.device

    inputs = {
        key: value.to(input_device) if torch.is_tensor(value) else value
        for key, value in inputs.items()
    }

    with torch.inference_mode():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
        )

    prompt_length = inputs["input_ids"].shape[1]
    generated_tokens = outputs[:, prompt_length:]

    response = processor.batch_decode(
        generated_tokens,
        skip_special_tokens=True,
    )[0]

    return response.strip() or "No response generated."
