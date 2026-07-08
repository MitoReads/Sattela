def iter_macros(config):
  for category, macros in config.items():
    if not isinstance(macros, dict):
      continue
    for macro_name, data in macros.items():
      if not isinstance(data, dict):
        continue
      hotkey = data.get("hotkey", "")
      slots = data.get("slots", {})
      yield category, macro_name, hotkey, slots