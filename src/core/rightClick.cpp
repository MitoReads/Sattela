#include <Windows.h>

void rightClick() {
  INPUT inputs[2] = {};

  // Mouse Down: Right Click
  inputs[0].type = INPUT_MOUSE;
  inputs[0].mi.dwFlags = MOUSEEVENTF_RIGHTDOWN;

  // Mouse Up: Right Click
  inputs[1].type = INPUT_MOUSE;
  inputs[1].mi.dwFlags = MOUSEEVENTF_RIGHTUP;

  SendInput(2, inputs, sizeof(INPUT));
}