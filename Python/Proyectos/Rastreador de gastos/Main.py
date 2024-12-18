def visualizar():
    tabla = open("tabla_de_gastos.txt", "r")
    for linea in tabla:
        for letra in linea:
            if letra == ",":
                print("  |  ", end=" ")
            else:
                print(letra, end="")

def agregar():

    tabla = open("tabla_de_gastos.txt", "a")    

    fecha = input("Ingrese la fecha de la compra: \n")
    hora = input("Ingrese la hora de la compra: \n")
    objeto = input("Que compraste? \n")
    proposito = input("Para que era necesario? \n")
    coste_bss = float(input("Cuanto costo? (BS) \n"))
    tasa_paralela = float(input("Cual es la tasa del paralelo del dia de hoy? \n"))
    coste_dolar = round(coste_bss / tasa_paralela, 2)

    confirmacion = input(f"Se agregaran los siguiente datos a la tabla: {fecha},{hora},{objeto},{proposito},{coste_dolar},{coste_bss}, esta seguro de querer añadirlos? (si/no) \n")

    if confirmacion in ["no", "NO", "nO", "No"]:
        print("Proceso cancelado.")
        pass
    elif confirmacion in ["si", "SI", "sI", "Si"]:
        tabla.write(f"\n{fecha},{hora},{objeto},{proposito},{coste_dolar},{coste_bss}")
        print("Compra agregada a la tabla.")



def cls():
    import os
    os.system('cls' if os.name== 'nt' else 'clear')
    return ''

while True:
    seleccion = str(input("\n Bienvenido a tu rastreador de gastos en Python, que accion deseas realizar, (a)gregar, (v)isualizar, (e)liminar: \n"))
    if seleccion == "v":
        cls()
        visualizar()
        input("\nPresiona cualquier tecla para continuar.....")
        cls()
    elif seleccion =="a":
        cls()
        agregar()
        input("\nPresiona cualquier tecla para continuar.....")
        cls()

"""
Todo:
Utilizar la libreria de time para conseguir las fechas y cerciorarse de si la compra se realizo el mismo dia o un dia diferente.
Agregar las funciones:
    -Eliminar
    -Buscar.
    -Calcular el gasto total.