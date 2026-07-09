mouse_side_buttons = {"msb_f", "msb_b"}

def resolve_slots(slots):
  resolved = {}

  for name, key_str in (slots or {}).items():
    key_str = str(key_str) if not isinstance(key_str, str) else key_str
    resolved[name] = key_str.strip().lower()
    
  return resolved