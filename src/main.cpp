#include <windows.h>
#include <functional>
#include <iostream>
#include <set>
#include <unordered_map>
#include "core/core.h"
#include "macros/macros.h"

using macroFunc = std::function<void (std::set<std::string>)>;

// int main()
// {
//   if (!RegisterHotKey(NULL, 1, MOD_CONTROL, 'J'))
//   { // Ctrl+J
//     std::cerr << "Failed to register hotkey! Error code: " << GetLastError() << "\n";
//     return 1;
//   }

//   std::cout << "Registered Ctrl+J\n";

//   MSG msg;
//   while (GetMessage(&msg, NULL, 0, 0))
//   {
//     if (msg.message == WM_HOTKEY)
//     {
//       std::cout << "Hotkey triggered\n";
//       rightClick();
//     }
//   }

//   UnregisterHotKey(NULL, 1);
//   return 0;
// }

int main() {
  std::set<std::string> keys = {
    "k",
    "q"
  };

  pearlCatch(keys);
}