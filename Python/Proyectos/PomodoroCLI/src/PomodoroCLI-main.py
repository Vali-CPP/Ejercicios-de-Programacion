import time
import os

def convertir_int_seguro(variable_a_convertir, mensaje_de_error):
    try:
        variable_convertida = int(variable_a_convertir)
        return variable_convertida
    except ValueError:
        print(mensaje_de_error)

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def bienvenida():
    limpiar_pantalla()
    print("Bienvenido a tu aplicacion de Pomodoro, dime que hacer: \n1)Iniciar un pomodoro\n2)Salir")
    while True:
        try:
            decision = int(input("?:"))
            if decision >= 3 or decision < 1:
                print("Numero incorrecto")
            else:
                return decision
        except ValueError:
            print("Eso no es un numero")

        


if bienvenida() == 1:
    limpiar_pantalla()
    tiempo_del_pomodoro = input("Cuanto tiempo va a durar este pomodoro?:")
else:
    pass

