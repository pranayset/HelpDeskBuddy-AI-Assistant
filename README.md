# HelpDesk AI Assistant for IT Support Troubleshooting

**HelpDeskBuddy** is an AI-assisted chatbot project designed to help users troubleshoot common IT support issues through clear, step-by-step guidance. Example topics include office VPN connectivity, Windows troubleshooting, account and access issues, and basic network connectivity.

> **Project status:** Update this section to reflect your current implementation status (for example, *in development*, *prototype*, or *tested locally*). Features that depend on a trained adapter or a downloadable model will only work after the required model files and configuration are available.

## Table of Contents

- [Project Overview](#project-overview)
- [Goals](#goals)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup](#setup)
- [Dataset Format](#dataset-format)
- [Model and LoRA Adapter](#model-and-lora-adapter)
- [Run the Application](#run-the-application)
- [Troubleshooting](#troubleshooting)
- [Safety and Limitations](#safety-and-limitations)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

## Project Overview

HelpDeskBuddy explores how a language model can assist with first-line IT support by turning common troubleshooting questions into practical, easy-to-follow instructions. It is intended as a learning and portfolio project demonstrating an AI support workflow, a chat interface, and a potential parameter-efficient fine-tuning pipeline.

The chatbot is an aid—not a replacement for an organization's IT service desk, approved procedures, or an administrator.

## Goals

- Provide concise troubleshooting steps for common IT issues.
- Demonstrate an AI chat interface using Gradio.
- Organize example support conversations in a consistent dataset format.
- Explore model customization with Hugging Face Transformers and PEFT/LoRA.
- Keep the code modular so data preparation, model loading, training, and the user interface can be maintained separately.

## Features

Depending on which components have been configured and tested, the project may include:

- A chat interface for entering IT support questions.
- Step-by-step responses for common support scenarios.
- Conversation context for follow-up questions.
- A dataset preparation workflow using instruction/response examples.
- An optional LoRA fine-tuning workflow.
- Configurable model and training settings.

Only describe a feature as fully implemented after you have verified it in your copy of the project.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Gradio | Chat interface |
| PyTorch | Model execution and training |
| Hugging Face Transformers | Tokenization and model loading |
| PEFT / LoRA | Parameter-efficient model fine-tuning |
| TRL | Supervised fine-tuning utilities, if used by the training script |
| `datasets` | Dataset loading and processing, if used |
| `bitsandbytes` | Optional quantization support, where compatible |
| JSONL | Example training data format |

The exact package versions and hardware requirements depend on the model, Python version, and the scripts in your checkout.

## Project Structure

A suggested structure for this project is shown below. Your actual files may differ; keep the README synchronized with the repository you publish.

```text
HelpDeskBuddy_AI_Assistant/
├── README.md
├── requirements.txt
├── .gitignore
├── configs/
│   └── training_config.yaml
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
│       └── helpdesk_dataset.jsonl
├── notebooks/
├── outputs/                       # Generated locally; normally not committed
└── src/
    └── helpdeskbuddy/
        ├── app.py
        ├── data/
        │   └── prepare_dataset.py
        ├── model/
        │   └── load_model.py
        └── training/
            └── train_lora.py
```

If your `app.py` is located at `src/helpdeskbuddy/app.py`, run it from the repository root using the command shown below.

## Requirements

- A supported Python version compatible with all packages in `requirements.txt`.
- Git, if cloning or publishing the repository.
- Internet access for the initial download of model files, unless the model is already cached locally.
- Sufficient RAM, disk space, and—depending on the model and precision—GPU memory.
- Hugging Face access and any required permissions for the selected model.

**Windows note:** Use a supported Python release (commonly Python 3.10–3.12 for broad ML-package compatibility, subject to the package versions you choose). Before installing PyTorch or other machine-learning packages, verify the Python version and choose package versions that support it. Newer Python releases may not yet have compatible prebuilt wheels for every dependency.

## Setup

### 1. Get the project files

If the repository is published on GitHub:

```bash
git clone <https://github.com/pranayset/HelpDeskBuddy-AI-Assistant>
cd HelpDeskBuddy_AI_Assistant
```

Replace the placeholder with your actual repository URL. If you already have the project as a ZIP file, extract it first and open a terminal in the extracted project root.

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If Python 3.11 is not installed, use a Python version supported by your selected package versions. If PowerShell blocks activation, consult the Python documentation or run the environment's Python executable directly.

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 4. Install dependencies

If `requirements.txt` contains compatible, tested package versions:

```bash
python -m pip install -r requirements.txt
```

PyTorch installation commands vary by operating system, Python version, and CPU/CUDA configuration. If installation fails, use the official PyTorch installation selector and then install the remaining project dependencies. Avoid installing packages into a different Python environment from the one used to run the app.

## Dataset Format

The example dataset uses JSON Lines (`.jsonl`), with one JSON object per line. A simple example:

```json
{"instruction":"I cannot connect to the office VPN.","response":"Check that your internet connection is working. Confirm that you are using your organization's approved VPN client and sign-in method. If the issue continues, record the error message and contact your IT support team."}
{"instruction":"My computer has no network connection.","response":"Check whether Wi-Fi or Ethernet is enabled. If permitted, reconnect to the approved network and restart the network adapter. If other devices are also affected or the issue persists, contact IT support."}
```

Guidelines for dataset examples:

- Use synthetic or properly authorized data; do not include real users' personal information.
- Never include passwords, authentication codes, access tokens, private keys, or confidential company information.
- Keep each line valid JSON and use consistent field names.
- Validate the dataset before training.
- Review examples for accuracy, clarity, and safe escalation advice.

The training script must be configured to read the same field names used by the dataset.

## Model and LoRA Adapter

The project has explored the `google/gemma-3-4b-it` model and PEFT/LoRA. Model loading APIs, processor requirements, quantization options, and compatible package versions can change. Confirm the implementation in `src/helpdeskbuddy/model/load_model.py` and the current model documentation before running it.

If your application expects a locally trained adapter, make sure that:

1. The training run completed successfully.
2. The expected adapter configuration and weight files exist.
3. The adapter path in the configuration or application matches the actual path.
4. The base model and adapter are compatible.
5. You have the required model access and have accepted any applicable model terms.

For example, an adapter directory might be named `outputs/deskbuddy_lora/final_adapter`, but use the path actually produced by your training script. Do not commit large model weights or private credentials to GitHub unless you have deliberately reviewed the size, permissions, and applicable terms.

## Run the Application

From the repository root, activate the virtual environment and run:

```powershell
python src/helpdeskbuddy/app.py
```

If your project instead has an `app.py` in the repository root, use:

```bash
python app.py
```

Follow the local URL printed by Gradio in the terminal. The app will only start if the imports, model configuration, required model files, and other dependencies are set up correctly.

For a local smoke test, try a harmless question such as:

> I cannot connect to the office VPN. What should I check first?

Verify that the app returns a response, that follow-up messages behave as expected, and that it does not request secrets or claim to perform actions it cannot actually perform.

## Troubleshooting

### `ModuleNotFoundError: No module named 'gradio'` (or another package)

Install dependencies in the same environment used to launch the app:

```powershell
python -m pip install -r requirements.txt
```

Check which interpreter is running:

```powershell
python --version
python -m pip --version
```

### `No matching distribution found for torch`

This commonly indicates that the selected Python version, operating system, architecture, or package index does not have a compatible PyTorch wheel. Check the supported versions on the official PyTorch site, create an environment with a supported Python version, and install the matching build.

### Model or adapter files cannot be found

Check the configured model ID and adapter path. Confirm that downloads completed and that the expected adapter files are present. A directory name alone does not mean a successful training run created an adapter.

### The model returns an empty or poor response

Check the model and processor loading code, prompt/chat-template format, input tokenization, generation settings, and adapter compatibility. Test the base model separately from the adapter. Review terminal logs for warnings or numerical errors.

### GPU unavailable or insufficient memory

A GPU is optional only if your selected model and configuration can run on CPU within available resources. Larger models may be too slow or memory-intensive on a low-resource laptop. Consider using a hosted notebook with an available GPU, a smaller compatible model, or inference-only testing. GPU availability is not guaranteed by a free hosted service.

### Dependency installation fails on Windows

Use a supported Python version and a fresh virtual environment. Install dependencies in small groups to identify incompatible packages, and prefer compatible prebuilt wheels over attempting complex source builds on a low-resource machine. Keep a record of the working versions in `requirements.txt`.

## Safety and Limitations

- The chatbot can produce incorrect, incomplete, or outdated troubleshooting advice.
- Verify instructions against your organization's approved IT policies and procedures.
- Do not enter passwords, one-time codes, recovery codes, tokens, personal data, or confidential business information.
- Do not run destructive commands, change security settings, bypass access controls, or perform administrative actions unless explicitly authorized and guided by your IT team.
- Escalate suspected security incidents, malware, data loss, account compromise, or business-critical outages to the authorized support team.
- The chatbot does not actually reset accounts, open tickets, change network settings, or access company systems unless those integrations are explicitly implemented and securely authorized.
- Model use is subject to the selected model's license/terms, access requirements, and hardware constraints.

## Future Improvements

Potential next steps include:

- Add automated dataset validation and unit tests.
- Evaluate responses against a held-out set of support scenarios.
- Add structured logging that avoids storing sensitive user content.
- Add clear escalation paths and confidence-aware responses.
- Document tested Python and package versions.
- Improve accessibility and error handling in the Gradio interface.
- Add integrations only with proper authentication, authorization, and audit controls.

## Contributing

Contributions and suggestions are welcome. Before submitting a change:

1. Keep changes focused and explain their purpose.
2. Test the relevant script or workflow.
3. Do not include secrets, private datasets, or large generated model files.
4. Update this README when setup instructions or project behavior changes.

---

**Maintainer:** Pranay Setu  
**Project:** HelpDesk AI Assistant for IT Support Troubleshooting  
