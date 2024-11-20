
my_list = [1, 2, 3]

try:
    result = my_list[5]  # Intentando acceder a un índice inexistente
except IndexError as e:
    print(f"Error: {e}")
