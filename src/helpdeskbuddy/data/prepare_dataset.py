"""Validate a JSONL dataset with instruction/response fields."""
import json
from pathlib import Path
REQUIRED_FIELDS = {"instruction", "response"}

def validate_jsonl(path):
    count = 0
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            record = json.loads(line)
            missing = REQUIRED_FIELDS - record.keys()
            if missing:
                raise ValueError(f"Line {line_number} missing fields: {sorted(missing)}")
            if not str(record["instruction"]).strip() or not str(record["response"]).strip():
                raise ValueError(f"Line {line_number} has an empty instruction/response")
            count += 1
    return count

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default="data/sample/helpdesk_dataset.jsonl")
    args = parser.parse_args()
    print(f"Validated {validate_jsonl(args.path)} records in {args.path}")
