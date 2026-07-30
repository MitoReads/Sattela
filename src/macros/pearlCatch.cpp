#include <vector>
#include <string>
#include <Windows.h>
#include "macros.h"
#include "../core/core.h"

/**
 * Pearl Catching is when you throw an ender pearl into the air and a windcharge after inorder to make them hit each other in the air and give you an y level advantage 
 */
void pearlCatch(std::vector<std::string> keys) {
  std::string pearl = keys[0];
  std::string windCharge = keys[1];

  keyPress(pearl);
  rightClick();

  Sleep(50); // 1 tick

  keyPress(windCharge);
  rightClick();
}