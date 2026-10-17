# HelpDeskBuddy AI Assistant — IT Support Troubleshooting

A starter repository scaffold for an AI-assisted IT helpdesk troubleshooting chatbot.

## Important
This ZIP contains example source code and project folders. It does **not** include trained model weights or a fine-tuned adapter. Model access, hardware requirements, and usage terms depend on the model you select.

## Quick start
1. Extract this ZIP.
2. Open a terminal in `HelpdeskBuddy_AI_Assistant`.
3. Create/activate a Python virtual environment.
4. Install dependencies: `pip install -r requirements.txt`.
5. Review `configs/training_config.yaml`.
6. After confirming model access and sufficient hardware, adapt the model loader and chat template for your chosen model, then run `python -m helpdeskbuddy.app` with `PYTHONPATH=src` set.

## Safety
- Never ask for passwords, MFA codes, recovery codes, API keys, or private keys.
- Do not claim that you performed an action or changed a setting.
- Escalate security-sensitive, admin-only, or organization-specific issues to IT.
- Do not commit secrets, private logs, or model weights to GitHub.

## Folders
- `src/helpdeskbuddy/`: application, model loader, inference, prompts, dataset validation.
- `data/sample/`: synthetic sample records.
- `data/raw/` and `data/processed/`: local dataset placeholders.
- `configs/`: starter training configuration.
- `notebooks/`: suggested notebook workflow.
- `docs/`: architecture and safety notes.
- `tests/`: starter validation test.
