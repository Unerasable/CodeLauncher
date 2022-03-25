import tkinter as tk
from tkinter import messagebox
from tkinter import *
import json
import os
from PIL import Image, ImageTk
import requests

app_Version = "1.0.0"
jsonFile = "https://unerasable.github.io/application.json"
def check_valid_status_code(request):
    if request.status_code == 200:
        return request.json()

    return False
def get_application_get_url():
    request = requests.get(jsonFile)
    data = check_valid_status_code(request)
    return data
app_URL=get_application_get_url()
checkAppVer = f"{app_URL['codelauncher']['verson']}"
def check():
    if checkAppVer == app_Version:
        pass
    else:
        messagebox.showinfo("Code Launcher", "Code Launcher is out of date! Please update to the latest version.")
        quit()
    if os.path.exists("./assets") == False:
        os.mkdir("./assets")
    if os.path.exists("./assets/locations.json") == False:        
        url = 'https://github.com/Unerasable/CodeLauncher/blob/main/assets/locations.json?raw=true'
        r = requests.get(url, allow_redirects=True)
        open('./assets/locations.json', 'wb').write(r.content)

    if os.path.exists("./assets/vscode.png")==False:
        url = 'https://github.com/Unerasable/CodeLauncher/blob/main/assets/vscode.png?raw=true'
        r = requests.get(url, allow_redirects=True)
        open('./assets/vscode.png', 'wb').write(r.content)
    if os.path.exists("./assets/pycharm.png")==False:
        url = 'https://github.com/Unerasable/CodeLauncher/blob/main/assets/pycharm.png?raw=true'
        r = requests.get(url, allow_redirects=True)
        open('./assets/pycharm.png', 'wb').write(r.content)
    if os.path.exists("./assets/sublime.png")==False:
        url = 'https://github.com/Unerasable/CodeLauncher/blob/main/assets/sublime.png?raw=true'
        r = requests.get(url, allow_redirects=True)
        open('./assets/sublime.png', 'wb').write(r.content)
    if os.path.exists("./assets/github.png")==False:
        url = 'https://github.com/Unerasable/CodeLauncher/blob/main/assets/github.png?raw=true'
        r = requests.get(url, allow_redirects=True)
        open('./assets/github.png', 'wb').write(r.content)
    if os.path.exists("./assets/intellij.png")==False:
        url = 'https://github.com/Unerasable/CodeLauncher/blob/main/assets/intellij.png?raw=true'
        r = requests.get(url, allow_redirects=True)
        open('./assets/intellij.png', 'wb').write(r.content)
    if os.path.exists("./assets/webstorm.png")==False:
        url = 'https://github.com/Unerasable/CodeLauncher/blob/main/assets/webstorm.png?raw=true'
        r = requests.get(url, allow_redirects=True)
        open('./assets/webstorm.png', 'wb').write(r.content)
    if os.path.exists("./assets/eclipse.png")==False:
        url = 'https://github.com/Unerasable/CodeLauncher/blob/main/assets/eclipse.png?raw=true'
        r = requests.get(url, allow_redirects=True)
        open('./assets/eclipse.png', 'wb').write(r.content)

check()


with open("./assets/locations.json", "r") as f:
    locations = json.load(f)
def openVSCode():
    try:
        os.open(locations["vscode"])
    except:
        messagebox.showerror("Code Launcher", "[ERROR]: Visual Studio Code not found! Please make sure you have the correct path in the 'locations.json' file.")
def openPyCharm():
    try:
        os.open(locations["pycharm"])
    except:
        messagebox.showerror("PyCharm Launcher", "[ERROR]: PyCharm not found! Please make sure you have the correct path in the 'locations.json' file.") 
def openSublime():
    try:
        os.open(locations["sublime"])
    except:
        messagebox.showerror("Sublime Launcher", "[ERROR]: Sublime Text not found! Please make sure you have the correct path in the 'locations.json' file.")
def openGithub():
    try:
        os.open(locations["github"])
    except:
        messagebox.showerror("Github Launcher", "[ERROR]: Github not found! Please make sure you have the correct path in the 'locations.json' file.")
def openWebstorm():
    try:
        os.open(locations["webstorm"])
    except:
        messagebox.showerror("Webstorm Launcher", "[ERROR]: Webstorm not found! Please make sure you have the correct path in the 'locations.json' file.")
def openIntelliJ():
    try:
        os.open(locations["intellij"])
    except:
        messagebox.showerror("IntelliJ Launcher", "[ERROR]: IntelliJ not found! Please make sure you have the correct path in the 'locations.json' file.")
def openEclipse():
    try:
        os.open(locations["eclipse"])
    except:
        messagebox.showerror("Eclipse Launcher", "[ERROR]: Eclipse not found! Please make sure you have the correct path in the 'locations.json' file.")


root = tk.Tk()
root.geometry("820x600")
root.title("Code Launcher")
root.resizable(False, False)
root.configure(bg="#36393f")
title=tk.Label(root, text="Code Launcher", bg="#36393f", fg="white", font=("Helvetica", 20)).pack()
vscodeIcon = PhotoImage(file='./assets/vscode.png')
vscodeBtn = tk.Button(root, image=vscodeIcon, bg="#36393f", fg="white", command=lambda: openVSCode()).pack()
pycharmIcon = PhotoImage(file='./assets/pycharm.png')
pycharmBtn = tk.Button(root, image=pycharmIcon, bg="#36393f", fg="white", command=lambda: openPyCharm()).pack()
sublimeIcon = PhotoImage(file='./assets/sublime.png')
sublimeBtn = tk.Button(root, image=sublimeIcon, bg="#36393f", fg="white", command=lambda: openSublime()).pack()
githubIcon = PhotoImage(file='./assets/github.png')
githubBtn = tk.Button(root, image=githubIcon, bg="#36393f", fg="white", command=lambda: openGithub()).pack()
webstormIcon = PhotoImage(file='./assets/webstorm.png')
webstormBtn = tk.Button(root, image=webstormIcon, bg="#36393f", fg="white", command=lambda: openWebstorm()).pack()
intellijIcon = PhotoImage(file='./assets/intellij.png')
intellijBtn = tk.Button(root, image=intellijIcon, bg="#36393f", fg="white", command=lambda: openIntelliJ()).pack()
eclipseIcon = PhotoImage(file='./assets/eclipse.png')
eclipseBtn = tk.Button(root, image=eclipseIcon, bg="#36393f", fg="white", command=lambda: openEclipse()).pack()
root.mainloop()