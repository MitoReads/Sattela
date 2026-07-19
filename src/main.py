import termcolor
import keyboard
import win32api
import win32process
from utils.greet import greet
from config.get_config import get_config
from utils.iter_macros import iter_macros
from macros.perl_catch import perl_catch
from macros.stun_slam import stun_slam
from macros.mending import toggle_mending
from macros.lunge_swap import lunge_swap
from macros.crystal_spam import toggle_crystal_spam
from macros.anchor import anchor
from macros.breach_swap import breach_swap
from utils.resolve_slots import resolve_slots
from utils.run_macro_threaded import run_macro_threaded
from config.config_path import get_config_path

def set_realtime_priority():
  try:
    process = win32api.GetCurrentProcess()
    win32process.SetPriorityClass(process, win32process.REALTIME_PRIORITY_CLASS)
    termcolor.cprint("Priority set to realtime for better performance.", "green")

  except:
    termcolor.cprint("Failed to set realtime priority.", "red")

macros = {
  "Perl Catch": perl_catch,
  "Stun Slam": stun_slam,
  "Mending": toggle_mending,
  "Lunge Swap": lunge_swap,
  "Crystal Spam": toggle_crystal_spam,
  "Anchor": anchor,
  "Breach Swap": breach_swap
}

greet()

set_realtime_priority()

config = get_config()
bound_any = False

for category, macro_name, hotkey, raw_slots in iter_macros(config):
  if not hotkey or not hotkey.strip():
    termcolor.cprint(f"[{category}] '{macro_name}' has no hotkey configured, skipping.", "yellow")
    continue

  if macro_name not in macros:
    termcolor.cprint(f"[{category}] '{macro_name}' has a hotkey, but no function in the code, skipping.", "yellow")
    continue

  slots = resolve_slots(raw_slots)

  keyboard.add_hotkey(
    hotkey,
    lambda mn=macro_name, s=slots, ma=macros: run_macro_threaded(mn, s, ma)
  )

  termcolor.cprint(f"[{category}] '{macro_name}' bound to: {hotkey}", "green")

  bound_any = True

if not bound_any:
  termcolor.cprint("No macros are configured!", "red")
  termcolor.cprint(f"Edit {get_config_path()} and set a 'hotkey' for the macros you want enabled, to disable enabled macros empty their 'hotkey'", "cyan")
  termcolor.cprint("Example: \"hotkey\": \"alt+q\"", "cyan")

termcolor.cprint("press f4 to exit", "cyan")
keyboard.wait("f4")