import win32con
from ctypes import windll

# uses windows api to press the side back click.
def press_side_button_back():
  windll.user32.mouse_event(win32con.MOUSEEVENTF_XDOWN, 0, 0, 0x01, 0)
  windll.user32.mouse_event(win32con.MOUSEEVENTF_XUP, 0, 0, 0x01, 0)
