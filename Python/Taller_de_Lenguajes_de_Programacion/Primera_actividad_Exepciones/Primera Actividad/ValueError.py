
try:
    result = int("abc")  # Intentando convertir una cadena no numérica a entero
except ValueError as e:
    print(f"Error: {e}")
