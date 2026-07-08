import json
from .config_path import get_config_path

# writes the data into the config.json file, usually used to generate the default config.
def save_config(data: dict):
  with open(get_config_path(), "w") as f:
    json.dump(data, f, indent=2)