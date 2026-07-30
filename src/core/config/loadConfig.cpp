#include <fstream>
#include <string>
#include <iostream>
#include <filesystem>
#include "../../../lib/json.hpp"
#include "config.h"

namespace fs = std::filesystem;

json loadConfig() {
  std::string configPath = getConfigPath();

  if (fs::exists(configPath)) {
    try {
      std::ifstream file(configPath);
      if (file.is_open()) {
        json configData = json::parse(file);
        file.close();

        if (!configData.empty()) {
          return configData;
        } else {
          std::cout << "Config file is empty, generating defaults."
                    << std::endl;
        }
      }
    } catch (const json::parse_error& e) {
      std::cerr << "Failed to parse config.json (" << e.what()
                << "), generating defaults." << std::endl;
    } catch (const std::exception& e) {
      std::cerr << "Failed to read config.json (" << e.what()
                << "), generating defaults." << std::endl;
    }
  } else {
    std::cout << "Config file not found at " << configPath
              << ", creating with defaults." << std::endl;
  }

  saveConfig(defaultConfig);
  return defaultConfig;
}