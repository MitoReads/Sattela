from simulate.mouse.right_click import right_click
from simulate.mouse.left_click import left_click
from simulate.key_press import key_press
import threading
import time

stop_event = threading.Event()
thread = None
is_on_crystal = False

def run(slots):
  global is_on_crystal
  crystal_slot = slots["crystal"]

  if not is_on_crystal:
    key_press(crystal_slot)
    is_on_crystal = True
  
  while not stop_event.is_set():
    if stop_event.wait(0.03):
      break
    right_click()

    time.sleep(0.05)

    left_click()

def start_crystal_spam(slots):
  global thread
  stop_event.clear()
  thread = threading.Thread(target=run, args=(slots,), daemon=True)
  thread.start()

def stop_crystal_spam():
  stop_event.set()

def toggle_crystal_spam(slots):
  global is_on_crystal

  if thread and thread.is_alive():
    stop_crystal_spam()
    is_on_crystal = False
  else:
    start_crystal_spam(slots)