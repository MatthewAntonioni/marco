import os
import tkinter as tk
import keyboard as kb
import time
from tkinter import *
from tkinter import ttk

def keyboard_listener():

    cooldown = 2

    path = path_var.get()
    if kb.is_pressed("delete"):       
     os.startfile(path)
     if kb.is_pressed("delete"):
        time.sleep(cooldown)
    root.after(1, keyboard_listener)

root = tk.Tk()
root.title("macro manager")

mainFrame = ttk.Frame(root, padding=(3,3,12,12)) 
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

path_var = tk.StringVar()
path_var.entry = ttk.Entry(mainFrame, width=20, textvariable=path_var)
path_var.entry.grid(column=1, row=1, sticky=(W, E))

entry = ttk.Entry(mainFrame, width=20)
entry.grid(column=1, row=2, sticky=(W, E))

keyboard_listener()
root.mainloop()

#make UI nice to look at
#add a toggle button for each marco
#add memory so you dont need to redo your marcos every time you open the program
#add start up on boot capability
#add custom hotkey for each macro
#try to add a button to make a new marco slot (if possible)