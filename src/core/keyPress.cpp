#include <Windows.h>
#include <variant>
#include <string>
#include "core.h"

/**
 * @param kc Keycode, can be a string or a VK
 */
void keyPress(std::variant<WORD, std::string> kc) {
  INPUT inputs[2] = {};

  // Key Down
  inputs[0].type = INPUT_KEYBOARD;
  inputs[0].ki.wVk = resolveKey(kc);

  // Key Up
  inputs[1].type = INPUT_KEYBOARD;
  inputs[1].ki.wVk = resolveKey(kc);
  inputs[1].ki.dwFlags = KEYEVENTF_KEYUP;

  SendInput(2, inputs, sizeof(INPUT));
}