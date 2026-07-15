from simulate.key_press import key_press
from simulate.mouse.right_click import right_click
from utils.precise_sleep import precise_sleep

def anchor(slots):
  anchor_slot: str = slots["anchor"]
  glow_stone_slot: str = slots["glow stone"]
  totem_slot: str = slots["totem"]

  key_press(anchor_slot)
  precise_sleep(0.05)
  right_click()

  precise_sleep(0.05)

  key_press(glow_stone_slot)
  right_click()

  precise_sleep(0.05)
  key_press(totem_slot)
  right_click()