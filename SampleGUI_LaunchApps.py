from fileinput import filename
import tkinter as tk
from tkinter import filedialog, Text
import os

#root es la ventana principal
root = tk.Tk()
root.resizable(width=False, height=False)
apps = []

if os.path.isfile('save.txt'):
    with open ('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps =  [x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename=filedialog.askopenfilename(initialdir="/", title="Selecciona un fichero", filetypes=(("executables",".exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)



#creo el objeto canva y se lo asigno a root con pack
canvas = tk.Canvas(root, height=700, width=800, bg="#263D42")
canvas.pack()

#creo un frame y los botones
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile= tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps= tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
