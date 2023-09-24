import json
import os

path = os.path.join(os.path.expanduser("~"), ".lights")
os.makedirs(path, exist_ok=True)

with open(os.path.join(path, "saved_colors.json"), "r", encoding="utf-8") as f:
    saved_colors_data = json.load(f)


def save_color(name: str, color: str):
    saved_colors_data[name] = color
    with open(os.path.join(path, "saved_colors.json"), "w", encoding="utf-8") as f:
        json.dump(saved_colors_data, f, indent=4)
