
import math

try:
    result = math.exp(1000)  # Intentando calcular una exponencial muy grande
except OverflowError as e:
    print(f"Error: {e}")
