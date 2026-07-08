from .resolve_vk import resolve_vk

mouse_side_buttons = {"msb_1", "msb_2"}

def resolve_slots(slots):
  resolved = {}

  for name, key_str in (slots or {}).items():
    if isinstance(key_str, str) and key_str.strip().lower() in mouse_side_buttons:
      resolved[name] = key_str.strip().lower()
    else:
      resolved[name] = resolve_vk(key_str)
    
  return resolved