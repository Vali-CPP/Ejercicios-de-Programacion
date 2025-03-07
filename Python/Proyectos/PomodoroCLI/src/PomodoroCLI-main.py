import time
import sys
import os
import subprocess
import pygame as pg

pg.mixer.init()

"""
             TODO
             - Investigar como integrar una base de datos rudimentaria en un CSV para asi mantener un track de la cantidad de tiempo que se ha trabajado
             diariamente.
             - Agregar una interfaz grafica de usuario para manejar absolutamente todo, creo que este es uno de los pasos mas importante, mas adelante podremos agregar la base de datos.
"""

class Pomodoro:
    def __init__(self, t_concentracion = 25, t_descanso = 5, n_ciclos = 3, direccion_a_alarma="./Audio/.Alarma.wav"):
        self.t_concentracion = t_concentracion
        self.t_descanso = t_descanso
        self.n_ciclos = n_ciclos
        self.alarma = pg.mixer.Sound(direccion_a_alarma)

    def definir_ciclos(self):
 
        self.ciclos = list()

        for i in range(0, self.n_ciclos):
            self.ciclos.append(["Concentracion", t_concentracion])
            self.ciclos.append(["Descanso", t_descanso])

    def temporizador(self, etapa, duracion):

        duracion *= 60

        for restante in range(duracion, 0, -1):
            print("\r")
            hr, resto = divmod(restante, 3600)
            min, seg = divmod(resto, 60)
            print("Tiempo restante de {} {:0>2}:{:0>2}:{:0>2}".format(etapa.lower(), hr, min, seg), end="")
            time.sleep(1)
            limpiar_pantalla()

    def get_ciclos(self):
        return self.ciclos
    
    def sonar_alarma(self):
        self.alarma.play()

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def validacion_int(mensaje_peticion, mensaje_de_error = "Caracter invalido", limite_inferior = -999, limite_superior = 999):
    while True:
        try:
            int_validado = int(input(mensaje_peticion))

            if int_validado <= limite_inferior:
                print("El numero es muy bajo")

            elif int_validado > limite_superior:
                print("El numero es muy alto")

            else:
                return int_validado

        except ValueError:
            print(mensaje_de_error)

def menu_inicial():

    limpiar_pantalla()

    return validacion_int("1)Iniciar un pomodoro\n2)Salir\n:", "Numero invalido", 0, 2)

def elegir_ruido():

    limpiar_pantalla()

    dict_sonidos = {"Ninguno" : None}
    contador = 1

    print("Indica el ruido blanco que deseas reproducir:")

    for sonido in os.listdir("Audio"):
        sonido_sin_ext = sonido[:-4]
        if not sonido.startswith("."):
            dict_sonidos.setdefault(sonido_sin_ext, sonido)

    for sonido in dict_sonidos.keys():
            print("{} - {}".format(contador, sonido))
            contador += 1

    decision = validacion_int("?:", "Elige un numero que este disponible", 0, len(dict_sonidos))
   
    list_sonidos = list(dict_sonidos.keys())

    if decision - 1 != 0:
        return os.path.abspath("Audio/{}".format(dict_sonidos[list_sonidos[decision - 1]]))
    else:
        return None


correr = True
sonido_a_reproducir = None

while correr:

    try:
        if menu_inicial() == 1:

            limpiar_pantalla()

            t_concentracion = validacion_int("Ingrese el tiempo de concentracion deseado:", "Tiempo invalido, debe ser mayor que cero", 0)
            t_descanso = validacion_int("Ingrese el tiempo de descanso deseado:", "Tiempo invalido, debe ser mayor que cero", 0)
            n_ciclos = validacion_int("Ingrese el numero de ciclos a completar:", "Tiempo invalido, el numero de ciclos tiene que ser mayor a cero", 0)

            pomo_actual = Pomodoro(t_concentracion, t_descanso, n_ciclos)
            pomo_actual.definir_ciclos()

            sonido_a_reproducir = elegir_ruido()

            if sonido_a_reproducir:
                sonido_a_reproducir = pg.mixer.Sound(sonido_a_reproducir)

            for fase in pomo_actual.get_ciclos():

                if sonido_a_reproducir and fase[0] == "Concentracion":
                    sonido_a_reproducir.play(-1)

                pomo_actual.temporizador(fase[0], fase[1])
                pomo_actual.sonar_alarma()
                limpiar_pantalla()
                print("\nEtapa terminada, pasando a la siguiente etapa.")
                time.sleep(2)
                
                if sonido_a_reproducir and fase[0] == "Concentracion":
                    sonido_a_reproducir.stop()

            limpiar_pantalla()

        else:
            correr = False

    except KeyboardInterrupt:
        print("Reiniciando Programa")
        if sonido_a_reproducir:
            sonido_a_reproducir.stop()
        limpiar_pantalla()


limpiar_pantalla()
