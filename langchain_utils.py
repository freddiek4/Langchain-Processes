# utility functions that I may or may not use later
import hashlib
import json
from functools import lru_cache

def preprocess_text(text):
    # " Hello World " → "hello world"
    return ' '.join(text.strip().lower().split())

def generate_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

@lru_cache(maxsize=128)
def cached_transformation(text):
    processed_text = preprocess_text(text)
    return generate_hash(processed_text)

class Logger:
    def __init__(self, filename="app.log"):
        self.filename = filename

    def log(self, message):
        with open(self.filename, 'a') as file:
            file.write(f"{message}\n")

def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def save_json(data, filepath):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
