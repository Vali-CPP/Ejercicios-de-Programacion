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
            - Agregar una opciona para poder cambiar la musica en cualquier momento. (Se me ocurre principalmente que en el manejo de la excepcion de 
            la interrupcion por teclado, se de la opcion de poder cambiar la musica y que tambien se guarden los minutos y segundos por los que iba el
            pomodoro, para que no sea una opcion de salirse simplemente, sino tambien para poder pausarlo y configurarlo.
"""

class Sonido:
    def __init__(self, objeto_sonido = None):
                self.sonido = objeto_sonido

    def reproducir(self):
        if self.sonido:
            self.sonido.play(-1)

    def pausar(self):
        if self.sonido:
            self.sonido.stop()

    def cambiar(self, objeto_sonido):
        self.sonido = objeto_sonido

class Pomodoro:
    def __init__(self, t_concentracion = 25, t_descanso = 5, n_ciclos = 3, direccion_a_alarma="Audio/.Alarma.wav"):
        self.t_concentracion = t_concentracion
        self.t_descanso = t_descanso
        self.n_ciclos = n_ciclos
        self.alarma = pg.mixer.Sound(direccion_a_alarma)

    def definir_ciclos(self):
        self.ciclos = list()

        for i in range(0, self.n_ciclos):
            self.ciclos.append(["Concentracion", self.t_concentracion])
            self.ciclos.append(["Descanso", self.t_descanso])

    def pasar_ciclo(self):
        self.ciclos = self.ciclo[1:]
        self.n_ciclo -= 1

    def get_ciclo_actual(self):
        return self.ciclos[0]

    def temporizador(self, etapa, duracion):

        duracion *= 60
        duracion 

        for restante in range(duracion, 0, -1):
            print("\r")
            hr, resto = divmod(restante, 3600) #divmod devuelve una tupla del tipo (a/b, a%b)
            min, seg = divmod(resto, 60) #divmod devuelve una tupla del tipo (a/b, a%b)
            print("Tiempo restante de {} {:0>2}:{:0>2}:{:0>2}".format(etapa.lower(), hr, min, seg), end="")
            time.sleep(1)
            limpiar_pantalla()
    
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

    return validacion_int("1)Iniciar un pomodoro\n2)Salir\n: ", "Numero invalido", 0, 2)

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

    decision = validacion_int("?: ", "Elige un numero que este disponible", 0, len(dict_sonidos))

    list_sonidos = list(dict_sonidos.keys())

    if decision - 1 != 0:
        return pg.mixer.Sound(os.path.abspath("Audio/{}".format(dict_sonidos[list_sonidos[decision - 1]])))
    else:
        return None

def crear_pomo():

    t_concentracion = validacion_int("Ingrese el tiempo de concentracion deseado: ", "Tiempo invalido, debe ser mayor que cero", 0)
    t_descanso = validacion_int("Ingrese el tiempo de descanso deseado: ", "Tiempo invalido, debe ser mayor que cero", 0)
    n_ciclos = validacion_int("Ingrese el numero de ciclos a completar: ", "Tiempo invalido, el numero de ciclos tiene que ser mayor a cero", 0)

    p = Pomodoro(t_concentracion, t_descanso, n_ciclos)

    return p

correr = True
sonido_a_reproducir = None

while correr:

    try:
        if menu_inicial() == 1:

            limpiar_pantalla()

            pomo_actual = crear_pomo()
            pomo_actual.definir_ciclos()

            sonido_a_reproducir = Sonido(elegir_ruido())

            while pomo_actual.get_ciclo_actual():

                if pomo_actual.get_ciclo_actual[0] == "Concentracion":
                    sonido_a_reproducir.reproducir()

                pomo_actual.temporizador(pomo_actual.get_ciclo_actual[0], pomo_actual.get_ciclo_actual[1])
                pomo_actual.pasar_ciclo()
                pomo_actual.sonar_alarma()
                limpiar_pantalla()
                print("\nEtapa terminada, pasando a la siguiente etapa.")
                time.sleep(3)
                
                if pomo_actual.get_ciclo_actual[0] == "Descanso":
                    sonido_a_reproducir.pausar()

            limpiar_pantalla()

        else:
            correr = False

    except KeyboardInterrupt:
        print("Reiniciando Programa")
        if sonido_a_reproducir:
            sonido_a_reproducir.stop()
        limpiar_pantalla()


limpiar_pantalla()
