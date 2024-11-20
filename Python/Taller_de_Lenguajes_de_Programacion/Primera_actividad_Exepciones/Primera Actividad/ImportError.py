
try:
    import non_existent_module  # Intentando importar un módulo que no existe
except ImportError as e:
    print(f"Error: {e}")
