from simulate.key_press import key_press
from simulate.mouse.left_click import left_click
from utils.precise_sleep import precise_sleep

def stun_slam(slots):
  axe_slot: str = slots["axe"]
  mace_slot: str = slots["mace"]

  key_press(axe_slot)
  left_click()
  precise_sleep(1/20)
  key_press(mace_slot)
  left_click()