cosas = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def aniadirloot(diccionario, lista):
    i=0
    while i < len(lista):
        diccionario.setdefault(lista[i], 1)
        i += 1


def mostrarInventario(diccionario):
    print("Inventario: ")
    cantidad = 0
    for key, value in diccionario.items():
        print(f"{key} {value}")
        cantidad += 1
    print(f"Son un total de {cantidad} cosas.")

mostrarInventario(cosas)
print("HAS DERROATDO A UN DRAGON")
aniadirloot(cosas, dragonLoot)
mostrarInventario(cosas)
