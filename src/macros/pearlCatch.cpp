#include <set>
#include <iostream>
#include <string>
#include "macros/macros.h"
#include "core/core.h"

void pearlCatch(std::set<std::string> keys) {
  for (std::string key : keys) {
    keyPress(key);
  }
}