
perro = 3

try:
    result = perro.age  # Error: El atributo 'age' no existe en la clase MyClass
except AttributeError as e:
    print(f"Error: {e}")
