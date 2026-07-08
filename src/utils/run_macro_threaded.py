import threading
from .run_macro import run_macro

def run_macro_threaded(name, slots, macros):
  threading.Thread(target=run_macro, args=(name, slots, macros), daemon=True).start()