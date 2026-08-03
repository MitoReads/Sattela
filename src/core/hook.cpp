#include <atomic>
#include <vector>
#include "core.h"

static std::atomic<bool> g_physKeyState[256] = {};
static HHOOK g_hook = nullptr;

// so binding "Shift" matches either physical shift key etc
static void setPhysState(WORD vk, bool down) {
  g_physKeyState[vk] = down;
  if (vk == VK_LSHIFT || vk == VK_RSHIFT) g_physKeyState[VK_SHIFT] = down;
  if (vk == VK_LCONTROL || vk == VK_RCONTROL) g_physKeyState[VK_CONTROL] = down;
  if (vk == VK_LMENU || vk == VK_RMENU) g_physKeyState[VK_MENU] = down;
}

static LRESULT CALLBACK LowLevelKeyboardProc(int nCode, WPARAM wParam, LPARAM lParam) {
  if (nCode == HC_ACTION) {
    KBDLLHOOKSTRUCT* kb = (KBDLLHOOKSTRUCT*)lParam;
    bool isInjected = (kb->flags & LLKHF_INJECTED) != 0;
    bool isKeyUp = (kb->flags & LLKHF_UP) != 0;
    WORD vk = (WORD)kb->vkCode;

    if (!isInjected) {
      bool wasDown = g_physKeyState[vk];
      setPhysState(vk, !isKeyUp);

      // fire only on the down transition, ignore key-repeat
      if (!isKeyUp && !wasDown) {
        for (auto& hk : g_hotkeys) {
          bool modOk = (hk.modVk == 0) || g_physKeyState[hk.modVk];
          if (modOk && hk.keyVk == vk) {
            handleHotkeys(hk.id);
            break;
          }
        }
      }
    }
    // injected keys: pass straight through, don't touch state or match hotkeys
  }
  return CallNextHookEx(NULL, nCode, wParam, lParam);
}

void installHotkeyHook() {
  g_hook = SetWindowsHookEx(WH_KEYBOARD_LL, LowLevelKeyboardProc, GetModuleHandle(NULL), 0);
}