import termcolor

def run_macro(name, slots, macros: dict):
  macro = macros.get(name)

  if macro is None:
    termcolor.cprint(f"No macro found for '{name}', skipping.")
    return
  macro(slots)