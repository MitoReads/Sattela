#include <windows.h>
#include <iostream>
#include <variant>
#include "core.h"
#include "config/config.h"

// returns the macro name based on their id
std::string getMacroName(int id) {
  switch (id) {
    case 1:
      return "Pearl Catch";
      break;

    case 2:
      return "Stun Slam";
      break;

    case 3:
      return "Breach Swap";
      break;

    case 999:
      return "EXIT";
      break;

    default:
      return "None";
      break;
  }
}

void registerHotkeys() {
  json config = getConfig();
  json macros = config["Macros"];

  // Loops through every macro
  for (json macro : macros) {
    // registering the hotkey only if the macro is enabled
    if (macro["Enabled"].get<bool>()) {
      std::string modKey = macro["Mod Key"].get<std::string>();
      std::string key = macro["Key"].get<std::string>();

      int id = macro["ID"].get<int>();

      bindHotkey(resolveKey(modKey), resolveKey(key), id);

      // Better logging
      std::string logMessage = getMacroName(id) + " Has Been Bound To ";
      if (!modKey.empty()) {
        logMessage += modKey + "+";
      }
      logMessage += key;

      std::cout << logMessage << std::endl;
    }
  }

  MSG msg;

  while (GetMessage(&msg, NULL, 0, 0)) {
    if (msg.message == WM_HOTKEY) {
      handleHotkeys(msg.wParam);
    }
  }
}