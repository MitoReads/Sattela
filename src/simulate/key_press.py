import win32con
from ctypes import windll

# uses windows api to press and release the given key
def key_press(vk):
  windll.user32.keybd_event(vk, 0, 0, 0)
  windll.user32.keybd_event(vk, 0, win32con.KEYEVENTF_KEYUP, 0)