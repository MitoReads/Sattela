#include <Windows.h>
#include <string>
#include <vector>
#include "../core/core.h"
#include "macros.h"

/**
 * Stun Slamming is when you disable your opponent's shield mid air and hit them with a mace
 */
void stunSlam(std::vector<std::string> keys) {
  std::string axe = keys[0];
  std::string mace = keys[1];

  keyPress(axe);
  leftClick();

  Sleep(50);  // 1 tick

  keyPress(mace);
  leftClick();
}