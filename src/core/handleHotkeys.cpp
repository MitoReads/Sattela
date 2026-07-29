#include <set>
#include <string>
#include <iostream>
#include <cstdlib>
#include "../macros/macros.h"

/**
 * @param hkid the hotkey's id, will be used to assign a function to it.
 * 
 * uses the hotkey's id to decide what function will be called upon press.
 */
void handleHotkeys(int hkid) {
  std::string keys[2] = {"MOUSE_SIDE_BUTTON_FRONT", "X"};

  switch (hkid) {
  case 1:
    pearlCatch(keys);
    break;
  
  case 999:
    exit(0);
    break;
  
  default:
    std::cout << "Unknown Hotkey\n";
    break;
  }
}