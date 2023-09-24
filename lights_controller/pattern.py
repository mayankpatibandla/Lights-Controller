import json
import os

path = os.path.join(os.path.expanduser("~"), ".lights")
os.makedirs(path, exist_ok=True)

files = {"saved_colors": "saved_colors.json", "saved_patterns": "saved_patterns.json"}
save_data = {}

for key, file in files.items():
    if not os.path.isfile(os.path.join(path, file)):
        with open(os.path.join(path, file), "w", encoding="utf-8") as f:
            pass
    with open(os.path.join(path, file), "r", encoding="utf-8") as f:
        save_data[key] = json.load(f)


def save_color(name: str, color: str):
    save_data["saved_colors"][name] = color
    with open(os.path.join(path, files["saved_colors"]), "w", encoding="utf-8") as f:
        json.dump(save_data["saved_colors"], f, indent=2)


def save_pattern(name: str, pattern: list[str]):
    save_data["saved_patterns"][name] = pattern
    with open(os.path.join(path, files["saved_patterns"]), "w", encoding="utf-8") as f:
        json.dump(save_data["saved_patterns"], f, indent=2)
