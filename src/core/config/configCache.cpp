#include "config.h"

static json configCache;

json getConfig() {
  if (configCache.empty()) {
    configCache = loadConfig();
  }
  return configCache;
}