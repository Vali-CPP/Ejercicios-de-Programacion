import time
import sys
import os
import subprocess

class Pomodoro:
    def __init__(self, t_concentracion = 25, t_descanso = 5, n_ciclos = 3):
        self.t_concentracion = t_concentracion
        self.t_descanso = t_descanso
        self.n_ciclos = n_ciclos

    def definir_ciclos(self):

        self.ciclos = list()

        for i in range(0, self.n_ciclos):
            self.ciclos.append(["Concentracion", t_concentracion])
            self.ciclos.append(["Descanso", t_descanso])

    def temporizador(self, etapa, duracion):

        duracion *= 60

        for restante in range(duracion, -1, -1):
            limpiar_pantalla()
            print("\r")
            hr, resto = divmod(restante, 3600)
            min, seg = divmod(resto, 60)
            print("Tiempo restante de {} {:0>2}:{:0>2}:{:0>2}".format(etapa.lower(), hr, min, seg), end="")
            time.sleep(1)
            limpiar_pantalla()

    def get_ciclos(self):
        return self.ciclos


def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def validacion_int(mensaje_peticion, mensaje_de_error = "Caracter invalido", limite_inferior = -999, limite_superior = 999):
    while True:
        try:
            int_validado = int(input(mensaje_peticion))
            if int_validado <= limite_inferior or int_validado > limite_superior:
                print("El numero es muy bajo y/o alto")
                limpiar_pantalla()
            else:
                return int_validado
        except ValueError:
            print(mensaje_de_error)

def bienvenida():
    limpiar_pantalla()
    return validacion_int("Bienvenido a tu aplicacion de Pomodoro, dime que hacer: \n1)Iniciar un pomodoro\n2)Salir\n:", "Numero invalido", 0, 2)

if bienvenida() == 1:

    limpiar_pantalla()

    t_concentracion = validacion_int("Ingrese el tiempo de concentracion deseado:", "Tiempo invalido, debe ser mayor que cero", 0)
    t_descanso = validacion_int("Ingrese el tiempo de descanso deseado:", "Tiempo invalido, debe ser mayor que cero", 0)
    n_ciclos = validacion_int("Ingrese el numero de ciclos a completar:", "Tiempo invalido, el numero de ciclos tiene que ser mayor a cero", 0)

    pomo_actual = Pomodoro(t_concentracion, t_descanso, n_ciclos)
    pomo_actual.definir_ciclos()

    for fase in pomo_actual.get_ciclos():
        pomo_actual.temporizador(fase[0], fase[1])
        "Etapa terminada, pasando a la siguiente etapa."
        subprocess.Popen(["~/notificacion_de_finalizacion.sh"], shell=True)
else:
    sys.exit()
