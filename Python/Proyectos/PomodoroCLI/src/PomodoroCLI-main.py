import time
import os

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

def tiempo_a_mostrar(tiempo_actual_list, tiempo_meta_list):
    hr = int(tiempo_meta_list[0]) - int(tiempo_actual_list[0])
    min = int(tiempo_meta_list[1]) - int(tiempo_actual_list[1])
    seg = int(tiempo_meta_list[2]) - int(tiempo_actual_list[2])

    if hr > 0:
        return print(f"{hr} : {min} : {seg}", end=" ")
    elif min > 0:
        return print(f"{min} : {seg}", end=" ")
    elif seg > 0:
        return print(f"{seg}", end=" ")
    else:
        return print("Se acabo el tiempo")

def temporizador(minutos, mensaje_a_mostrar):
    segundos = minutos * 60
    tiempo_meta = time.time() + segundos
    limpiar_pantalla()
    while time.time() != tiempo_meta:
        print(f"{mensaje_a_mostrar}\tTiempo restante: {time.strftime("%M : %S", time.localtime(time.time() - tiempo_meta))}")
    limpiar_pantalla()

verificar_ingreso_tiempo = False

if bienvenida() == 1:
    limpiar_pantalla()
    tiempo_de_enfoque = validacion_int("Duracion de la fase de enfoque en minutos: ", "Caracter Invalido", 0)
    tiempo_de_descanso = validacion_int("Duracion de la fase de descanso en minutos: ", "Caracter Invalido", 0)
    numero_de_pomodoros = validacion_int("Ingrese el numero de etapas de concentracion que tendra el pomodoro: ", "Caracter Invalido", 0)
    print(f"Esta seguro de querer continua con sus {numero_de_pomodoros} Pomodoro(s) de {tiempo_de_enfoque} minuto(s) de enfoque y {tiempo_de_descanso} minuto(s) de descanso?: \n1)Si\n2)No")
    ciclos = [["Concentracion", tiempo_de_enfoque]]
    decision = validacion_int(":", "Caracter Invalido", 0, 2)
    for i in range(0, numero_de_pomodoros - 1):
        ciclos.append(["Descanso", tiempo_de_descanso])
        ciclos.append(["Concentracion", tiempo_de_enfoque])
    for fase in ciclos:
            temporizador(fase[1], fase[0])
else:
    pass

