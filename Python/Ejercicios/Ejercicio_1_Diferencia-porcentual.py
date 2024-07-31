print("Diferencia porcentual entre dos cantidades")
cant_ini = float(input("Ingrese el dato inicial: "))
cant_diff = float(input("Ingrese el dato final: "))
resultado = ((cant_ini - cant_diff) * 100) / cant_ini 
print(f"La diferencia porcentual entre las dos cantidades es de un %{resultado}")
