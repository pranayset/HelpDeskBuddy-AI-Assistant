# Troubleshooting

## Hugging Face 401 / GatedRepoError
Sign in at https://huggingface.co/google/gemma-3-4b-it, complete the access
conditions, authenticate with `hf auth login`, and test downloading `config.json`.
Never print or commit the token.

## Adapter not found
Set `ADAPTER_DIR` in `.env` to a local folder containing both
`adapter_config.json` and `adapter_model.safetensors`. We do not distribute
adapter weights in this repository.

## PEFT / TorchAO incompatibility
Record installed versions before changing packages. Avoid random upgrades of
PyTorch, Transformers, or PEFT. In the reported Colab setup, removing an unused
incompatible optional TorchAO package and restarting the runtime resolved the
adapter injection error.

## CUDA unavailable
Confirm a GPU runtime is enabled and `torch.cuda.is_available()` is true.
Install a PyTorch build compatible with the NVIDIA driver.

## BF16 unsupported
This app stops if BF16 is unsupported. Do not switch to FP16 without checking
numerical stability and validating outputs for NaN/Inf.

## CUDA out of memory
Restart the runtime, avoid loading duplicate model instances, close other GPU
workloads, and lower `MAX_NEW_TOKENS`. Larger GPUs may be required.

## Gradio share URL closes
A `gradio.live` URL is temporary and remains available only while the process
and runtime stay alive. Do not interrupt the serving cell.

## Empty or truncated responses
Check `MAX_NEW_TOKENS`, chat history formatting, model/adapter compatibility,
and the runtime logs.
