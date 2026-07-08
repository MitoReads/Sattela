import sys
import os

# checks if the app is running as a .exe or directly from python
def get_config_path():
  if getattr(sys, "frozen", False):
    base_dir = os.path.dirname(sys.executable)
  else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

  return os.path.join(base_dir, "config.json")