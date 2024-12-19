def cls():
    import os
    os.system('cls' if os.name== 'nt' else 'clear')
    return ''

while True:
    seleccion = str(input("\n Bienvenido a tu rastreador de gastos en Python, que accion deseas realizar, (a)gregar, (v)isualizar, (e)liminar: \n"))
    if seleccion == "v":
        cls()
        input("\nPresiona cualquier tecla para continuar.....")
        cls()
    elif seleccion =="a":
        cls()
        input("\nPresiona cualquier tecla para continuar.....")
        cls()

"""
Todo:
Utilizar la libreria de time para conseguir las fechas y cerciorarse de si la compra se realizo el mismo dia o un dia diferente.
Ademas, ahora tengo que hacerlo todo orientado a listas, porque la forma que tengo para guardar objetos es un poco rudimentaria.
Agregar las funciones:
    -Eliminar
    -Buscar.
    -Calcular el gasto total.
"""