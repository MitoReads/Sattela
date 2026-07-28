#include <windows.h>
#include <iostream>
#include "core/core.h"

/**
 * @param mk the key modifier, MOD_ALT, MOD_CONTROL, MOD_IGNORE_ALL_MODIFIER
 * @param k the key, k, e, etc.
 * @param id the hotkey's id, can not be the same as another hotkey's id
 *
 * the function sets a keybound for the key combo given to it.
 */
void bindHotkey(int mk, char k, int id) {
  if (!RegisterHotKey(NULL, id, mk, k)) std::cout << "Hotkey";
}