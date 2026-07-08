from .load_config import load_config

config = None

# return a cashed dict containing the hotkey config.
def get_config():
  global config

  if config is None:
    config = load_config()
  return config