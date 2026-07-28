#include <Windows.h>
#include "core/core.h"

void leftClick() {
  INPUT inputs[2] = {};

  // Mouse Down: Left Click
  inputs[0].type = INPUT_MOUSE;
  inputs[0].mi.dwFlags = MOUSEEVENTF_LEFTDOWN;

  // Mouse Up: Left Click
  inputs[1].type = INPUT_MOUSE;
  inputs[1].mi.dwFlags = MOUSEEVENTF_LEFTUP;

  SendInput(2, inputs, sizeof(INPUT));
}