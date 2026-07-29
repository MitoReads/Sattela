#include <windows.h>
#include <iostream>
#include <variant>
#include "core/core.h"

void registerHotkeys() {
  if (bindHotkey(MOD_ALT, 'J', 1)) {
    std::cout << "Registered Pearl Catch To Ctrl + Q\n";
  }

  if (bindHotkey(0, resolveKey(std::string("F4")), 999)) {
    std::cout << "Registered EXUT To F4\n";
  }

  MSG msg;

  while (GetMessage(&msg, NULL, 0, 0)) {
    if (msg.message == WM_HOTKEY) {
      handleHotkeys(msg.wParam);
    }
  }
}