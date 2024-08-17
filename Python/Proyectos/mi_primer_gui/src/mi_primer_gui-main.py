from tkinter import *


#Creando la ventana
m = Tk()
m.title("Wow esto es mas facil de lo que pensaba")
m.configure(bg="light blue")
m.geometry("800x800")

ejemplo = Label(m, text="Holi uwu, cual es tu nombre?", bg="pink", fg="black")
ejemplo.grid(row=0, column=0)
nombre = Entry(m, width=10)
nombre.grid(row=0, column=1)

#Creando el comportamiento de los botones
def clicked():
    respuesta = "Hola " + nombre.get() + " uwu"
    ejemplo.configure(text = respuesta , fg="red")


#Creando y agregando los botones
#ejemplo = Label(m, text="Holi uwu", bg="light blue").grid(row=0, column=0)
salir = Button(m, text="Enter", fg="white", command=clicked).grid(row=1)

#Este loop es necesario para que la ventana se actulice con cada interaccion
#del usuario, y al parecer para que se ejecute tambien AJAJAJAJ
m.mainloop()
