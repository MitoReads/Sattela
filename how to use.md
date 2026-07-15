# How To Use Sattela

## Config Format

Each macro's config is made up of 4 parts:

1. **Name**: identifies the macro (perl catch, stun slam, etc)
2. **Hotkey**: the key combo(?) that triggers the macro (alt+q, f, etc)
3. **Slots**: labels to identify _what_ item each keybind goes to (wind charge, perl, etc)
4. **Slot keybinds**: the key bound to each slot (msb_f, x, etc)

Example:

```json
"Perl Catch": {
  "hotkey": "alt+q",
  "slots": {
    "perl": "msb_f",
    "wind charge": "x"
  }
}
```

> [!IMPORTANT]
> slot _names_ (perl, wind charge, etc) are fixed and used internally to identify which key to press, do not rename them.

> [!WARNING]
> Numpad keys are not supported.

You may have noticed values like `msb_f`, these refer to mouse side buttons:

| Value   | Meaning                  |
| ------- | ------------------------ |
| `msb_f` | Mouse side button, front |
| `msb_b` | Mouse side button, back  |

Use these anywhere a slot expects a keybind that is bounded to a mouse side button.

## Triggering Macros

Triggering macros are those that perform a non action.

- Perl Catch
- Stun Slam
- Lunge Swap
- Anchor

## Toggling Macros

Toggling macros are those that perform a action continuously until its toggled off.

To use a toggling macro you must press its assigned hotkey to enable it, once you are done with it you must press its assigned hotkey again to disable it.

- Mending
- Crystal Spam