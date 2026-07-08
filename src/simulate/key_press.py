from .mouse.side_button_back import press_side_button_back
from .mouse.side_button_front import press_side_button_front
from .keyboard.keyboard_key_press import keyboard_key_press
from ..utils.resolve_vk import resolve_vk

def key_press(key_str: str):
  if "msb_1" in key_str or "msb_2" in key_str:
    if key_str == "msb_1":
      press_side_button_front()
    elif key_str == "msb_2":
      press_side_button_back()
  
  keyboard_key_press(resolve_vk(key_str))