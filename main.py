import tkinter as tk
from tkinter import messagebox
from tkinter import *
import json
import os
from PIL import Image, ImageTk

with open("./assets/locations.json", "r") as f:
    locations = json.load(f)
def openVSCode():
    try:
        os.open(locations["vscode"])
    except:
        messagebox.showerror("Code Launcher", "[ERROR]: Visual Studio Code not found! Please make sure you have the correct path in the 'locations.json' file.")
root = tk.Tk()
root.geometry("300x300")
root.title("Code Launcher")
root.resizable(True, True)
root.configure(bg="#36393f")
title=tk.Label(root, text="Code Launcher", bg="#36393f", fg="white", font=("Helvetica", 20)).pack()
vscodeIcon = PhotoImage(file='./assets/vscode.png')
vscodeBtn = tk.Button(root, image=vscodeIcon, bg="#36393f", fg="white", command=lambda: openVSCode()).pack()
root.mainloop()