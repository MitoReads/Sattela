import json
from .config_path import get_config_path

def save_config(data):
  with open(get_config_path(), "w") as f:
    json.dump(data, f, indent=2)