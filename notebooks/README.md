# Suggested Notebook Workflow

1. `01_dataset_inspection.ipynb` — inspect JSONL fields, empty records, duplicates, and safety.
2. `02_load_base_model.ipynb` — verify model access and test short inference.
3. `03_lora_finetuning.ipynb` — configure training only on compatible hardware.
4. `04_save_reload_adapter.ipynb` — save the adapter and verify it reloads.
5. `05_inference_evaluation.ipynb` — test common issues, unsafe requests, and escalation behavior.

Do not commit notebook outputs containing tokens, personal information, private logs, or model weights.
