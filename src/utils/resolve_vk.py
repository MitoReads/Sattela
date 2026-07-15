import win32api
import win32con

# msb_f is the front mouse side button and msb_b is the back one.
mouse_side_buttons = {"msb_f", "msb_b"}

# Special keys that don't have character representations
special_keys = {
    'caps_lock': win32con.VK_CAPITAL,
    'capslock': win32con.VK_CAPITAL,
    'tab': win32con.VK_TAB,
    'enter': win32con.VK_RETURN,
    'return': win32con.VK_RETURN,
    'shift': win32con.VK_SHIFT,
    'ctrl': win32con.VK_CONTROL,
    'control': win32con.VK_CONTROL,
    'alt': win32con.VK_MENU,
    'esc': win32con.VK_ESCAPE,
    'escape': win32con.VK_ESCAPE,
    'space': win32con.VK_SPACE,
    'backspace': win32con.VK_BACK,
    'delete': win32con.VK_DELETE,
    'insert': win32con.VK_INSERT,
    'home': win32con.VK_HOME,
    'end': win32con.VK_END,
    'page_up': win32con.VK_PRIOR,
    'pgup': win32con.VK_PRIOR,
    'page_down': win32con.VK_NEXT,
    'pgdn': win32con.VK_NEXT,
    'up': win32con.VK_UP,
    'down': win32con.VK_DOWN,
    'left': win32con.VK_LEFT,
    'right': win32con.VK_RIGHT,
    'f1': win32con.VK_F1,
    'f2': win32con.VK_F2,
    'f3': win32con.VK_F3,
    'f4': win32con.VK_F4,
    'f5': win32con.VK_F5,
    'f6': win32con.VK_F6,
    'f7': win32con.VK_F7,
    'f8': win32con.VK_F8,
    'f9': win32con.VK_F9,
    'f10': win32con.VK_F10,
    'f11': win32con.VK_F11,
    'f12': win32con.VK_F12,
}

def resolve_vk(key_str: str):
    if not key_str:
        return None
    
    key_str = key_str.strip().lower()
    
    # Check for mouse side buttons
    if key_str in mouse_side_buttons:
        return None
    
    # Check for special keys (like caps_lock)
    if key_str in special_keys:
        return special_keys[key_str]
    
    # For regular characters, use VkKeyScan
    try:
        return win32api.VkKeyScan(key_str) & 0xFF
    except TypeError:
        # If it fails, log the unknown key
        print(f"Warning: Unknown key '{key_str}'")
        return None