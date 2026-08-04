#include "../../../lib/json.hpp"
#include <vector>
#include <string>

using json = nlohmann::ordered_json;

json loadConfig();
void saveConfig(const json& data);

std::string getConfigPath();
json getConfig();
std::vector<std::string> getKeys(std::string mn);

extern const json defaultConfig;