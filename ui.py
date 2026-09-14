
import os
import tkinter as tk
import keyboard as kb
import time
from tkinter import *
from tkinter import ttk

def keyboard_listener(path_var, key_var, root):

    cooldown = 2

    path = path_var.get()
    key = key_var.get()

    if key == "":
        root.after(1, lambda: keyboard_listener(path_var, key_var, root))
        return 

    #print("checking key:", repr(key))  # add this

    if kb.is_pressed(key):       
     os.startfile(path)
     if kb.is_pressed(key):
        time.sleep(cooldown)
    root.after(1, lambda: keyboard_listener(path_var, key_var, root))
  