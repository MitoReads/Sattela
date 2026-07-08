import os
import json
import termcolor
from .config_path import get_config_path
from .save_config import save_config

# the default config - my personal hotkeys
default_config = {
  "Macros": {
    "Perl Catch": {
      "hotkey": "alt+q",
      "slots": {
        "perl": "msb_1",
        "wind_charge": "x"
      }
    }
  }
}

# returns the hotkey config taken from config.json file.
def load_config():
  config_path = get_config_path()
  
  if os.path.exists(config_path):
    try:
      with open(config_path, "r") as f:
        config_data = json.load(f)
        if config_data:
          return config_data
        else:
          termcolor.cprint("Config file is empty, generating defaults.", "yellow")
    except (json.JSONDecodeError, OSError) as e:
      termcolor.cprint(f"Failed to read config.json ({e}), generating defaults.", "red")
  else:
    termcolor.cprint(f"Config file not found at {config_path}, creating with defaults.", "cyan")
  
  # File doesn't exist or is invalid - create default
  save_config(default_config)
  return default_config