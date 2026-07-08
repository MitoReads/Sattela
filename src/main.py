import termcolor
import keyboard
from utils.greet import greet
from config.get_config import get_config
from utils.iter_macros import iter_macros
from macros.perl_catch import perl_catch
from utils.resolve_slots import resolve_slots
from utils.run_macro_threaded import run_macro_threaded
from config.config_path import get_config_path

macros = {
  "Perl Catch": perl_catch
}

greet()

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