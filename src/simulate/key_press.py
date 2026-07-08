from simulate.mouse.side_button_back import press_side_button_back
from simulate.mouse.side_button_front import press_side_button_front
from simulate.keyboard.keyboard_key_press import keyboard_key_press
from utils.resolve_vk import resolve_vk

def key_press(key):
  key_str = str(key) if not isinstance(key, str) else key

  if "msb_1" in key_str or "msb_2" in key_str:
    if "msb_1" in key_str:
      press_side_button_back()
    elif "msb_2" in key_str:
      press_side_button_front()
      pass
    return
  
  keyboard_key_press(resolve_vk(key_str))