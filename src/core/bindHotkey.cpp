#include <windows.h>
#include <iostream>
#include "core.h"

/**
 * @param mk the key modifier, MOD_ALT, MOD_CONTROL, 0
 * @param k the key, k, e, etc.
 * @param id the hotkey's id, can not be the same as another hotkey's id
 *
 * the function sets a keybound for the key combo given to it.
 */
bool bindHotkey(int mk, char k, int id) {
  if (!RegisterHotKey(NULL, id, mk, k)) return false;
  return true;
}