import os
import json
import termcolor
from .config_path import get_config_path
from .save_config import save_config

default_config = {
  "Mace": {
    "Perl Catch": {
      "hotkey": "alt+q",
      "slots": {
        "perl": "msb_1",
        "wind_charge": "x"
      }
    },
    "Stun Slam": {
      "hotkey": "alt+w",
      "slots": {
        "axe": "2",
        "mace": "1"
      }
    }
  }
}

def load_config():
  if os.path.exists(get_config_path()):
    try:
      with open(get_config_path(), "r") as f:
        return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
      termcolor.cprint(f"Failed to read config.json ({e}), generating defaults.")
    
    save_config(default_config)
    return json.loads(json.dumps(default_config))