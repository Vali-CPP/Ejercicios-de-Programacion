tablero = [['0', '|', ' ', '|', ' ',],
           ['-', '+', '-', '+', '-',],
           [' ', '|', ' ', '|', ' ',],
           ['-', '+', '-', '+', '-',],
           [' ', '|', ' ', '|', ' ',]]


def drawboard():
    for i in range(0, 5):
        print("\n")
        for j in range(0, 5):
            print(tablero[i][j], end=' ')

# def winners():
#    if ():

turno = 0;
print("TIC-TAC-TOE")
drawboard()
if (turno % 2 == 0):
    print("\nTURNO DE X")
    fila = int(input("Ingrese la fila a seleccionar: "))
    columna = int(input("Ingrese la columna a seleccionar: "))
    tablero[fila][columna] = 'x'
    turno += 1
    drawboard()
else:
    print("\nTURNO DE O")
