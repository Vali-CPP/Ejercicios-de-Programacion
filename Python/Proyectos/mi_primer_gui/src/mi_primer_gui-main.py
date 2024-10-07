from tkinter import *
from tkinter import ttk


# Creando la ventana
m = Tk()
m.title("Wow esto es mas facil de lo que pensaba")

ejemplo = ttk.Label(m, text="Holi uwu, cual es tu nombre?")
ejemplo.grid(row=0, column=0)
nombre = ttk.Entry(m, width=10)
nombre.grid(row=0, column=1)


# Creando el comportamiento de los botones
def clicked():
    respuesta = "Hola " + nombre.get() + " uwu"
    ejemplo.configure(text=respuesta)


# Creando y agregando los botones
# ejemplo = Label(m, text="Holi uwu", bg="light blue").grid(row=0, column=0)
salir = ttk.Button(m, text="Enter", command=clicked).grid(row=1)

# Este loop es necesario para que la ventana se actulice con cada interaccion
# del usuario, y al parecer para que se ejecute tambien AJAJAJAJ
m.mainloop()
