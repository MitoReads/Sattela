import win32con
from ctypes import windll

# uses windows api to press the side front click.
def press_side_button_front():
  windll.user32.mouse_event(win32con.MOUSEEVENTF_XDOWN, 0, 0, 0x02, 0)
  windll.user32.mouse_event(win32con.MOUSEEVENTF_XUP, 0, 0, 0x02, 0)