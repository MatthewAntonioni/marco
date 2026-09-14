from ctypes import windll
import keyboard as kb

SPECIAL_KEYS = {
    'delete': 0x2E,
    'backspace': 0x08,
    'tab': 0x09,
    'enter': 0x0D,
    'shift': 0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'esc': 0x1B,
    'space': 0x20,
    'insert': 0x2D,
    'home': 0x24,
    'end': 0x23,
    'page_up': 0x21,
    'page_down': 0x22,
    'up': 0x26,
    'down': 0x28,
    'left': 0x25,
    'right': 0x27,
    'f1': 0x70,
    'f2': 0x71,
    'f3': 0x72,
    'f4': 0x73,
    'f5': 0x74,
    'f6': 0x75,
    'f7': 0x76,
    'f8': 0x77,
    'f9': 0x78,
    'f10': 0x79,
    'f11': 0x7A,
    'f12': 0x7B,
}

def char_to_vk(char):

    if char.lower() in SPECIAL_KEYS:
        return SPECIAL_KEYS[char.lower()]

    result = windll.user32.VkKeyScanW(ord(char))
    if result == -1:
        return None
    return result & 0xFF

key = input("enter key:")

print(char_to_vk(key))




