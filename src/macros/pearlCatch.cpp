#include <set>
#include <iostream>
#include <string>
#include <Windows.h>
#include "macros.h"
#include "../core/core.h"

void pearlCatch(std::set<std::string> keys) {
  auto it = keys.begin();
  auto pearl = *it;
  auto windCharge = *(++it);

  keyPress(pearl);
  rightClick();

  Sleep(2/20);

  keyPress(windCharge);
  rightClick();
}