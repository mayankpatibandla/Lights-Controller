import json
import os

lights_path = os.path.join(os.path.expanduser(f"~{os.environ['SUDO_USER']}"), ".lights")
os.makedirs(lights_path, exist_ok=True)

files = {"saved_colors": "saved_colors.json", "saved_patterns": "saved_patterns.json"}
save_data = {}

for key, file in files.items():
    if not os.path.isfile(os.path.join(lights_path, file)):
        with open(os.path.join(lights_path, file), "w", encoding="utf-8") as f:
            f.write("{}")

    with open(os.path.join(lights_path, file), "r", encoding="utf-8") as f:
        save_data[key] = json.load(f)


def save_color(name: str, color: str):
    save_data["saved_colors"][name] = color

    with open(os.path.join(lights_path, files["saved_colors"]), "w", encoding="utf-8") as colors_file:
        json.dump(save_data["saved_colors"], colors_file, indent=2)


def load_color(name: str):
    return save_data["saved_colors"][name]


def save_pattern(name: str, pattern: list[str]):
    save_data["saved_patterns"][name] = pattern

    with open(os.path.join(lights_path, files["saved_patterns"]), "w", encoding="utf-8") as patterns_file:
        json.dump(save_data["saved_patterns"], patterns_file, indent=2)


def load_pattern(name: str):
    return save_data["saved_patterns"][name]
