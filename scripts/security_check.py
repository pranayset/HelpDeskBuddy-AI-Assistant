"""Basic security scan of Git-tracked project files.

This is a preliminary check, not a complete security audit.
"""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

TEXT_EXT = {
    ".py", ".md", ".txt", ".json", ".jsonl",
    ".yaml", ".yml", ".toml", ".ini", ".cfg"
}

BAD_EXT = {
    ".safetensors", ".bin", ".pt", ".pth",
    ".ckpt", ".onnx", ".gguf"
}

SECRET_FILES = {
    ".env", ".env.local", ".env.production",
    "id_rsa", "id_ed25519"
}

PATTERNS = {
    "Hugging Face token": re.compile(r"\bhf_[A-Za-z0-9]{20,}\b"),
    "GitHub token": re.compile(
        r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b"
    ),
    "GitHub fine-grained token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    "Private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}

def git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        capture_output=True,
        text=True
    )

def main():
    result = git("ls-files", "-z")

    if result.returncode:
        print("Run this script inside a Git repository.")
        return 2

    errors = []

    for name in filter(None, result.stdout.split("\0")):
        path = ROOT / name

        if not path.is_file():
            continue

        if path.name in SECRET_FILES or (
            path.name.startswith(".env.")
            and path.name != ".env.example"
        ):
            errors.append(f"Tracked environment/secret file: {name}")
            continue

        if path.suffix.lower() in BAD_EXT:
            errors.append(f"Tracked model/binary file: {name}")
            continue

        if path.suffix.lower() in TEXT_EXT:
            content = path.read_text(encoding="utf-8", errors="ignore")

            for label, pattern in PATTERNS.items():
                if pattern.search(content):
                    errors.append(f"{label} pattern detected in: {name}")

    if git("check-ignore", ".env").returncode != 0:
        errors.append(".env is not ignored by Git.")

    if errors:
        print("SECURITY CHECK FAILED:")
        for error in errors:
            print("- " + error)
        return 1

    print("Basic scan passed for Git-tracked files.")
    print("Manual review of untracked files and Git history is still required.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
