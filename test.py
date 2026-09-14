import keyboard as kb
import tkinter as tk

root = tk.Tk()

def listener():
    kb.is_pressed("delete")
    root.after(1, listener)

listener()
root.mainloop()