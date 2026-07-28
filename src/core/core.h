#pragma once 

#include <Windows.h>
#include <variant>

void leftClick();
void rightClick();
void bindHotkey(int mk, char k, int id);
void handleHotkeys(int hkid);
void keyPress(WORD kc);

WORD resolveKey(const std::string& key);
WORD resolveKey(WORD key);
WORD resolveKey(const std::variant<WORD, std::string>& key);