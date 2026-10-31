# HelpDeskBuddy AI Assistant

**AI-powered IT Support Troubleshooting Assistant using Gemma 3 4B IT, PEFT/LoRA and Gradio.**

HelpDeskBuddy is an AI-assisted chatbot that provides step-by-step guidance for common IT support issues, including Windows troubleshooting, DHCP, DNS, Active Directory and network connectivity.

> **Project status:** Working prototype. Model loading, LoRA adapter integration, inference and Gradio interaction have been tested in Google Colab. Independent deployment and reproducibility testing are still required.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Run the Application](#run-the-application)
- [Synthetic Dataset](#synthetic-dataset)
- [Model and LoRA Adapter](#model-and-lora-adapter)
- [Troubleshooting](#troubleshooting)
- [Security and Limitations](#security-and-limitations)
- [Contributing](#contributing)

## Project Overview

HelpDeskBuddy explores how a language model can assist first-line IT support technicians by generating practical troubleshooting guidance.

The application uses modular Python components for model loading, conversation inference, safety prompts and the Gradio interface.

It is a learning and portfolio project, not a replacement for an organization's authorized IT service desk.

## Features

- Gemma 3 4B IT base model integration.
- PEFT/LoRA adapter loading.
- Gradio conversational interface.
- Conversation history support.
- Modular model-loading and inference code.
- Synthetic IT support dataset.
- Troubleshooting and security documentation.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| PyTorch | Model execution |
| Transformers | Model and processor loading |
| PEFT | LoRA adapter integration |
| Gradio | Chat interface |
| Accelerate | Model execution support |
| Hugging Face Hub | Model access |
| python-dotenv | Environment configuration |
| JSONL | Synthetic support dataset |

## Architecture

```mermaid
flowchart TD
    A[User] --> B[Gradio ChatInterface]
    B --> C[Root app.py]
    C --> D[Inference Module]
    E[Safety Prompts] --> D
    F[Conversation History] --> D
    G[Environment Configuration] --> C
    D --> H[Model Loader]
    H --> I[Gemma 3 4B IT]
    H --> J[PEFT LoRA Adapter]
    I --> K[Generated Response]
    J --> K
    K --> B
