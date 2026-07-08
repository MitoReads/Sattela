import win32api

# msb_1 is the back mouse side button and msb_2 is the front one.
mouse_side_buttons = {"msb_1", "msb_2"}

def resolve_vk(key_str: str):
  if not key_str:
    return None
  key_str = key_str.strip().lower()
  if key_str in mouse_side_buttons:
    return None
  return win32api.VkKeyScan(key_str) & 0xFF