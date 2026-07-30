#include <windows.h>
#include <functional>
#include <set>
#include <unordered_map>
#include <iostream>
#include "core/core.h"
#include "core/config/config.h"

using macroFunc = std::function<void (std::set<std::string>)>;

int main() {
  std::vector<std::string> keys = getKeys("Pearl Catch");

  for (const auto& key : keys) {
    std::cout << key << std::endl;
  }

  return 0;
}