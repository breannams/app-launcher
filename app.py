import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []
#functions

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray", fg="white")
        label.pack()

#canvas styling
canvas = tk.Canvas(root, height=700, width=700, bg="teal")
canvas.pack()

frame = tk.Frame(root, bg="pink")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#buttons
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="teal", command=addApp)
openFile.pack()

runAllApps = tk.Button(root, text="Run your Apps", padx=10, pady=5, fg="white", bg="teal")
runAllApps.pack()




root.mainloop()

