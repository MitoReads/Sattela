from simulate.mouse.right_click import right_click
from simulate.key_press import key_press
import threading

stop_event = threading.Event()
thread = None
is_on_bottle = False

def run(slots):
  global is_on_bottle
  xp_bottle_slot: str = slots["xp bottle"]

  if not is_on_bottle:
    key_press(xp_bottle_slot)
    is_on_bottle = True
  
  while not stop_event.is_set():
     # wait() blocks up to 0.03s but returns early (True) if stopped mid-wait
    if stop_event.wait(0.03):
      break
    right_click()

def start_mending(slots):
  global thread
  stop_event.clear()
  thread = threading.Thread(target=run, args=(slots,), daemon=True)
  thread.start()

def stop_mending():
  stop_event.set()

def toggle_mending(slots):
  global is_on_bottle

  if thread and thread.is_alive():
    stop_mending()
    is_on_bottle = False
  else:
    start_mending(slots)