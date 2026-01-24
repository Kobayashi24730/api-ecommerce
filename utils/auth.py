import json
import threading

lock = threading.Lock()
FILE = "produtos.json"

def read_data():
    with lock:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)

def write_data(data):
    with lock:
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
