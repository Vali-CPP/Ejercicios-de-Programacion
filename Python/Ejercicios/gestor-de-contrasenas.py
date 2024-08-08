#! /bin/python3
"""Este proyecto sera un gestos de contrasenias simples
no sera completamente seguro, pero funcionara para entender el funcionamiento
simple de este tipo de programas"""

import sys
import pyperclip

CONTRASENAS = {}

if len(sys.argv) < 2:
    print("El uso de este programa es el siguiente: python3 pw.py [nombre de la cuenta] - para ingresar el nombre al que desea relacionar la contrasenia")
    sys.exit()
cuenta = sys.argv[1]

while True:
    opcion = int(input("1)Ingresar/Editar contrasena.\n2)Copiar contrasena.\n3)Salir.\nOpcion:"))
    if opcion == 1:
        contrasenia = input("Ingrese la contrasena: ")
        if cuenta not in CONTRASENAS.keys():
            CONTRASENAS.setdefault(cuenta, contrasenia)
            print("Contrasena guardada con exito")
        else:
            CONTRASENAS[cuenta] = contrasenia
            print("Contrasena guardada con exito")
            sys.exit()
    elif opcion == 2:
        if cuenta not in CONTRASENAS:
            print(f"No hay ninguna cuenta llamada {cuenta}, asegurese de ingresar la cuenta exactamente como aparece en la lista")
            sys.exit()
        pyperclip.copy(CONTRASENAS[cuenta])
        print(f"La contrasena para la cuenta {cuenta} fue copiada al portapapeles")
    elif opcion == 3:
        sys.exit()
    else:
        print("Opcion incorrecta, intente de nuevo")
