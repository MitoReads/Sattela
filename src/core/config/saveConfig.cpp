#include <fstream>
#include <iostream>
#include <string>

#include "config.h"

void saveConfig(const json& data) {
  std::string configPath = getConfigPath();
  std::ofstream file(configPath);
  if (file.is_open()) {
    file << data.dump(2);  // indent = 2
    file.close();
  } else {
    std::cerr << "Failed to save config to: " << configPath << std::endl;
  }
}
