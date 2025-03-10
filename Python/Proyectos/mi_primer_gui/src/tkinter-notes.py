from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(pies.get())
        metros.set(int(0.3048 * value * 10000.0 - 0.5)/10000.0)
    except ValueError:
        pass


#Primero que todo creamos la ventana principal
root = Tk()
root.title("Ventana Principal - Calculadora")

cuadro_principal = ttk.Frame(root, padding="3 3 12 12")
cuadro_principal.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

pies = StringVar()
feet_entry = ttk.Entry(cuadro_principal, width=7, textvariable=pies)
feet_entry.grid(column=2, row=1, sticky=(W, E))

metros = StringVar()
ttk.Label(cuadro_principal, textvariable=metros).grid(column=2, row=2, sticky=(W, E))

ttk.Button(cuadro_principal, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(cuadro_principal, text="Pies").grid(column=3, row=1, sticky=W)
ttk.Label(cuadro_principal, text="Es igual a").grid(column=1, row=2, sticky=E)
ttk.Label(cuadro_principal, text="Metros").grid(column=3, row=2, sticky=W)

root.mainloop()
