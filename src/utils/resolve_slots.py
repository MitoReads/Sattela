from .resolve_vk import resolve_vk

mouse_side_buttons = {"msb_1", "msb_2"}

def resolve_slots(slots):
  resolved = {}

  for name, key_str in (slots or {}).items():
    key_str = str(key_str) if not isinstance(key_str, str) else key_str
    resolved[name] = key_str.strip().lower()
    
  return resolved