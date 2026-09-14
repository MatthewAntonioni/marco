import os
import tkinter as tk
import keyboard as kb
import time
from tkinter import *
from tkinter import ttk
import ui
import test3

root = tk.Tk()
root.title("macro manager")

mainFrame = ttk.Frame(root, padding=(3,3,12,12)) 
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

path_var = tk.StringVar()
path_var.entry = ttk.Entry(mainFrame, width=20, textvariable=path_var)
path_var.entry.grid(column=1, row=1, sticky=(W, E))

key_var = tk.StringVar()
key_var.entry = ttk.Entry(mainFrame, width=20, textvariable=key_var)
key_var.entry.grid(column=2, row=1, sticky=(W, E))


ui.keyboard_listener(path_var, key_var, root)
root.mainloop()

#make UI nice to look at
#add a toggle button for each marco
#add memory so you dont need to redo your marcos every time you open the program
#add start up on boot capability
#add custom hotkey for each macro
#try to add a button to make a new marco slot (if possible)