import yaml
import os

CONFIG_PATH = "config.yaml"
_config_data = {}

def load_config():
    global _config_data
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError("⚠️ config.yaml nicht gefunden.")
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        _config_data = yaml.safe_load(f)
    return _config_data

def get_config():
    return _config_data

def reload_config():
    return load_config()
