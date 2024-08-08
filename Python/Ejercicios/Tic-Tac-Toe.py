tablero = {"A1":' A1 ', "A2":' A2 ', "A3":' A3 ',
           "B1":' B1 ', "B2":' B2 ', "B3":' B3 ',
           "C1":' C1 ', "C2":' C2 ', "C3":' C3 '}


def drawboard():
    print(f"{tablero["A1"]} | {tablero["A2"]} | {tablero["A3"]}")
    print(f"------------------")
    print(f"{tablero["B1"]} | {tablero["B2"]} | {tablero["B3"]}")
    print(f"------------------")
    print(f"{tablero["C1"]} | {tablero["C2"]} | {tablero["C3"]}")


# def winners():
#    if ():

turno = 0;
print("TIC-TAC-TOE")
drawboard()
while True and turno < 9:
    if (turno % 2 == 0):
        print("\nTURNO DE X")
        recuadro = input("Ingrese el recuadro a marcar: ")
        tablero[recuadro] = ' X '
        turno += 1
        drawboard()
    else:
        print("\nTURNO DE O")
        recuadro = input("Ingrese la recuadro a seleccionar: ")
        tablero[recuadro] = ' O '
        turno += 1
        drawboard()
