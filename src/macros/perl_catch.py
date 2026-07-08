from simulate.key_press import key_press
from simulate.mouse.right_click import right_click

def perl_catch(slots):
  perl_slot: str = slots["perl"]
  wind_charge_slot: str = slots["wind_charge"]

  key_press(perl_slot)
  right_click()
  key_press(wind_charge_slot)
  right_click()