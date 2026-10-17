# Project Architecture

## Goal
Provide concise, safe troubleshooting suggestions for common desktop, network, account, and productivity issues.

## High-level flow
1. A user interface receives the question.
2. Safety instructions set boundaries.
3. A model loader loads the selected base model and, optionally, a PEFT adapter.
4. An inference layer formats the conversation and generates a response.
5. The interface displays the response and supports follow-up questions.

## Components
- `src/helpdeskbuddy/app.py`: Gradio interface scaffold.
- `src/helpdeskbuddy/model/load_model.py`: model/tokenizer loading.
- `src/helpdeskbuddy/inference/chat.py`: response generation helper.
- `src/helpdeskbuddy/prompts.py`: system safety prompt.
- `src/helpdeskbuddy/data/prepare_dataset.py`: JSONL validation.
- `data/sample/helpdesk_dataset.jsonl`: synthetic sample records.
- `configs/training_config.yaml`: starter fine-tuning parameters.

## Limitations
This is a starter scaffold, not a production-ready service. It contains no trained weights. Model access approval, compatible libraries, model-specific chat templates, and sufficient RAM/VRAM may be required. Follow the applicable model terms and license.
