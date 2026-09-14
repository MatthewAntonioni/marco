import tkinter as tk
import win32con
import win32gui
import ctypes
import threading

root = tk.Tk()
root.title("hotkey test")
label = tk.Label(root, text="Waiting for hotkey...")
label.pack(padx=20, pady=20)

HOTKEY_ID = 1
VK_DELETE = 0x2E

def listen():
    if not ctypes.windll.user32.RegisterHotKey(None, HOTKEY_ID, 0, VK_DELETE):
        print("Failed to register hotkey")
        return
    while True:
        msg = win32gui.GetMessage(None, 0, 0)
        if msg[1][1] == win32con.WM_HOTKEY:
            print("Hotkey pressed!")

root.update()  # force the window to actually draw before starting the thread
threading.Thread(target=listen, daemon=True).start()
root.mainloop()