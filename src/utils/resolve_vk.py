import win32api

# msb_f is the front mouse side button and msb_b is the back one.
mouse_side_buttons = {"msb_f", "msb_b"}

def resolve_vk(key_str: str):
  if not key_str:
    return None
  key_str = key_str.strip().lower()
  if key_str in mouse_side_buttons:
    return None
  return win32api.VkKeyScan(key_str) & 0xFF