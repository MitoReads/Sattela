from simulate.mouse.right_click import right_click
from simulate.key_press import key_press
import time

def mending(slots):
  xp_bottle_slot: str = slots["xp bottle"]

  key_press(xp_bottle_slot)

  for _ in range(64):
    time.sleep(0.03)
    right_click()