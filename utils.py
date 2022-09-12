import json

def load_candidates_from_json(path) -> list[dict]:
    with open (path, 'r', encoding = 'utf-8') as file:
        return json.load(path)

print(load_candidates_from_json(path))