list = ['Valiant', 'Es', 'Un', 'Duro', 'En', 'Cagarla', 'Computadoras']
ultimo = int(len(list))
for i in range(0, ultimo - 1):
    print(f"{list[i]}", end=", ")

print(f"and {list[ultimo - 1]}")
