#include <set>
#include <iostream>
#include <string>
#include "macros/macros.h"
#include "core/core.h"

void pearlCatch(std::set<std::string> keys) {
  auto it = keys.begin();
  auto pearl = *it;
  auto windCharge = *(++it);

  keyPress(pearl);
  rightClick();
  keyPress(windCharge);
  rightClick();
}