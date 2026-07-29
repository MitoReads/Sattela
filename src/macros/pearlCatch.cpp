#include <set>
#include <iostream>
#include <string>
#include <Windows.h>
#include "macros.h"
#include "../core/core.h"

void pearlCatch(std::string keys[2]) {
  std::string pearl = keys[0];
  std::string windCharge = keys[1];

  keyPress(pearl);
  rightClick();

  Sleep(50); // 1 tick

  keyPress(windCharge);
  rightClick();
}