import json
import os

lights_path = os.path.join(os.path.expanduser(f"~{os.environ['SUDO_USER']}"), ".lights")
os.makedirs(lights_path, exist_ok=True)

files = {
    "saved_colors": "saved_colors.json",
    "saved_patterns": "saved_patterns.json",
    "last_configuration": "last_configuration.json",
}
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


def delete_color(name: str):
    del save_data["saved_colors"][name]

    with open(os.path.join(lights_path, files["saved_colors"]), "w", encoding="utf-8") as colors_file:
        json.dump(save_data["saved_colors"], colors_file, indent=2)


def load_color(name: str):
    return save_data["saved_colors"][name]


def list_colors():
    return save_data["saved_colors"].keys(), save_data["saved_colors"].values()


def save_pattern(name: str, colors: list[str], brightness: int):
    save_data["saved_patterns"][name] = {"colors": colors, "brightness": brightness}

    with open(os.path.join(lights_path, files["saved_patterns"]), "w", encoding="utf-8") as patterns_file:
        json.dump(save_data["saved_patterns"], patterns_file, indent=2)


def delete_pattern(name: str):
    del save_data["saved_patterns"][name]

    with open(os.path.join(lights_path, files["saved_patterns"]), "w", encoding="utf-8") as patterns_file:
        json.dump(save_data["saved_patterns"], patterns_file, indent=2)


def load_pattern(name: str):
    return save_data["saved_patterns"][name]


def list_patterns():
    return save_data["saved_patterns"].keys(), save_data["saved_patterns"].values()


def save_last_configuration(colors: list[str], brightness: int):
    save_data["last_configuration"] = {"colors": colors, "brightness": brightness}

    with open(os.path.join(lights_path, files["last_configuration"]), "w", encoding="utf-8") as last_configuration_file:
        json.dump(save_data["last_configuration"], last_configuration_file, indent=2)


def load_last_configuration():
    return save_data["last_configuration"]
