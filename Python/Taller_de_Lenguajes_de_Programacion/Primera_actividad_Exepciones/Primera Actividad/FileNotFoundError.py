try:
    with open('archivo-inexistente.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")
