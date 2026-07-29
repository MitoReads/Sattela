#include <windows.h>
#include <functional>
#include <set>
#include <unordered_map>
#include "core/core.h"

using macroFunc = std::function<void (std::set<std::string>)>;

int main() {
  registerHotkeys();
}