import json
import csv
import os

def load_json(filename: str) -> dict:
    base_dir = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base_dir, "test_data", filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def load_csv(filename: str) -> list:
    base_dir = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base_dir, "test_data", filename)
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows