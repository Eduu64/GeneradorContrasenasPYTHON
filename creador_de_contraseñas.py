import random
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk

Letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]}{|;':\",./<>?"

def fabricar():
    global contraseña
    contraseña = ""
    for n in range(LENGTH.get()):
        contraseña += random.choice(Letras)
    resultado.config(text="Contraseña: %s" % contraseña)

def copiar():
    if contraseña:
        gui.clipboard_clear()
        gui.clipboard_append(contraseña)
        tkinter.messagebox.showinfo(title="Copiado", message="Contraseña copiada al portapapeles.")
    else:
        tkinter.messagebox.showerror(title="Error", message="Primero genere una contraseña.")

gui = tk.Tk()
gui.title('Generador de contraseñas')
gui.geometry("400x150")

LENGTH = tk.IntVar()

labelLENGTH = tk.Label(gui, text="Longitud:").grid(row=0, column=0, pady=10, padx=10)
entryLENGTH = tk.Entry(gui, textvariable=LENGTH, width=5).grid(row=0, column=1)

generarboton = tk.Button(gui, text="Generar", command=fabricar).grid(row=0, column=2,padx = 10, pady=10)

resultado = tk.Label(gui, text="Contraseña: ")
resultado.place(x=10, y=90)

boton_copiar = ttk.Button(gui, text="Copiar", command=copiar)
boton_copiar.place(x=10, y=120)

gui.mainloop()
