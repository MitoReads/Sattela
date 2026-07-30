#include <windows.h>
#include <string>

std::string getConfigPath() {
  char buffer[MAX_PATH];
  GetModuleFileNameA(NULL, buffer, MAX_PATH);
  std::string path(buffer);
  size_t pos = path.find_last_of('\\');
  return path.substr(0, pos + 1) + "config.json";
}