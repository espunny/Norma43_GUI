from fileinput import filename
import tkinter as tk
from tkinter import filedialog, Text, messagebox

import os

from csb43 import csb43, formats

#root es la ventana principal
root = tk.Tk()
root.title('Conversor de Norma43 a Excel v1 - Economía Zero')
root.iconbitmap("myIcon.ico")

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

    filename=filedialog.askopenfilename(initialdir="/", title="Selecciona un fichero", filetypes=(("norma43",".csb"), ("todos los ficheros", "*.*")))
    apps.append(filename)
    
    csbFile = csb43.File(open(filename, "rb"), strict=False)
    o = formats.convertFromCsb(csbFile, 'yaml')
    print(o.yaml)

    # write 'xlsx' format to file
    o = formats.convertFromCsb(csbFile, 'xlsx')
    ficheroSalida= filename + '.xlsx'
    with open(ficheroSalida, "wb") as f:
        f.write(o.xlsx)
        tk.messagebox.showinfo(title='Correcto!', message='El fichero ha sido convertido a Xlsx correctamente')

    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

#creo el objeto canva y se lo asigno a root con pack
canvas = tk.Canvas(root, height=400, width=600, bg="#263D42")
canvas.pack()

#creo un frame y los botones
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)

openFile= tk.Button(root, text="Abrir fichero Norma43", padx=10, pady=5, fg="white", bg="#750000", command=addApp)
openFile.pack()


label = tk.Label(frame, text='Últimos ficheros convertidos a .xlsx')
label.config(font=("Arial", 20))
label.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
