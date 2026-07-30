#include "config.h"

const json defaultConfig = {
  {"Macros", {
    {"Pearl Catch", {
      {"ID", 1},
      {"Enabled", true},
      {"Mod Key", "ALT"},
      {"Key", "Q"},
      {"Slots", {
        {"Pearl", "MOUSE_SIDE_BUTTON_FRONT"},
        {"Wind Charge", "X"}
      }}
    }},

    {"Stun Slam", {
      {"ID", 2},
      {"Enabled", true},
      {"Mod Key", "ALT"},
      {"Key", "W"},
      {"Slots", {
        {"Axe", "2"},
        {"Mace", "1"}
      }}
    }},

    {"Panic", {
      {"ID", 999},
      {"Enabled", true},
      {"Mod Key", ""},
      {"Key", "F4"},
    }}
  }}
};