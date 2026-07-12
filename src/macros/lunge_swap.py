from simulate.mouse.left_click import left_click
from utils.precise_sleep import precise_sleep
from simulate.key_press import key_press

def lunge_swap(slots):
  zero_cooldown_slot = slots["zero cooldown"]
  spear_slot = slots["spear"]

  left_click()
  key_press(spear_slot)
  precise_sleep(0.05)
  key_press(zero_cooldown_slot)