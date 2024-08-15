#! /bin/python3
tablero = {"A1":' A1 ', "A2":' A2 ', "A3":' A3 ',
           "B1":' B1 ', "B2":' B2 ', "B3":' B3 ',
           "C1":' C1 ', "C2":' C2 ', "C3":' C3 '}


def drawboard():
    print(f"{tablero["A1"]} | {tablero["A2"]} | {tablero["A3"]}")
    print(f"------------------")
    print(f"{tablero["B1"]} | {tablero["B2"]} | {tablero["B3"]}")
    print(f"------------------")
    print(f"{tablero["C1"]} | {tablero["C2"]} | {tablero["C3"]}")


def winners(board):
    for i in range(1, 4):
        if tablero[f"A{i}"] == tablero[f"B{i}"] == tablero[f"C{i}"]:
            return True
    i = 1
    if (tablero[f"A{i}"] == tablero[f"A{i+1}"] == tablero[f"A{i+2}"]) or (tablero[f"B{i}"] == tablero[f"B{i+1}"] == tablero[f"B{i+2}"]) or (tablero[f"C{i}"] == tablero[f"C{i+1}"] == tablero[f"C{i+2}"]):
        return True
    if tablero["A1"] == tablero["B2"] == tablero["C3"]:
        return True
    if tablero["A3"] == tablero["B2"] == tablero["C1"]:
        return True
    
 
turno = 0;
print("TIC-TAC-TOE")
drawboard()
while True and turno < 9:
    if (turno % 2 == 0):
        print("\nTURNO DE X")
        recuadro = input("Ingrese el recuadro a marcar: ")
        recuadro = recuadro.upper()
        tablero[recuadro] = ' X '
        turno += 1
        drawboard()
        if winners(tablero):
            print("\nGANO EL JUGADOR X")
            break
    else:
        print("\nTURNO DE O")
        recuadro = input("Ingrese la recuadro a seleccionar: ")
        tablero[recuadro] = ' O '
        recuadro = recuadro.upper()
        turno += 1
        drawboard()
        if winners(tablero):
            print("\nGANO EL JUGADOR O")
            break
