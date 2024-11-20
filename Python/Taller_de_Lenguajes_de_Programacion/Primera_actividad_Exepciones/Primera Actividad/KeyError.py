
my_dict = {'name': 'Alice', 'age': 25}

try:
    result = my_dict['address']  # Intentando acceder a una clave inexistente
except KeyError as e:
    print(f"Error: {e}")
