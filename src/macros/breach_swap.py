from simulate.mouse.left_click import left_click
from utils.precise_sleep import precise_sleep
from simulate.key_press import key_press

def breach_swap(slots):
  sword_slot = slots["sword"]
  breach_mace_slot = slots["breach mace"]

  left_click()
  key_press(breach_mace_slot)
  precise_sleep(1/20)
  key_press(sword_slot)