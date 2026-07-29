#pragma once 

#include <Windows.h>
#include <set>
#include <string>
#include <variant>
#include <variant>

void leftClick();
void rightClick();
bool bindHotkey(int mk, char k, int id);
void handleHotkeys(int hkid);
void keyPress(std::variant<WORD, std::string> kc);
void pressSideButton(std::variant<WORD, std::string> kc);


WORD resolveKey(const std::string& key);
WORD resolveKey(WORD key);
WORD resolveKey(const std::variant<WORD, std::string>& key);

void registerHotkeys();