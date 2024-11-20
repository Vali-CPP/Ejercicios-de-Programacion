
try:
    result = 10 / 0  # Intentando dividir por cero
except ZeroDivisionError as e:
    print(f"Error: {e}")
