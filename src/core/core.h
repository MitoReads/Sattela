#pragma once

#include <Windows.h>
#include <set>
#include <string>
#include <variant>
#include <vector>

struct HotkeyBinding {
  WORD modVk;
  WORD keyVk;
  int id;
};

extern std::vector<HotkeyBinding> g_hotkeys;

void bindHotkey(int mk, WORD k, int id);
void handleHotkeys(int hkid);

void leftClick();
void rightClick();
void pressSideButton(std::variant<WORD, std::string> kc);
void keyPress(std::variant<WORD, std::string> kc);

WORD resolveKey(const std::string& key);
WORD resolveKey(WORD key);
WORD resolveKey(const std::variant<WORD, std::string>& key);

void registerHotkeys();

void installHotkeyHook();