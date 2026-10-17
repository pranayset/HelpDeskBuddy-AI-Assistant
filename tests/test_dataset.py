from pathlib import Path
from helpdeskbuddy.data.prepare_dataset import validate_jsonl

def test_sample_dataset_validates():
    sample = Path("data/sample/helpdesk_dataset.jsonl")
    assert validate_jsonl(sample) >= 1
