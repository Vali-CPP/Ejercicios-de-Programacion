"""

    with open("Hola mundo.txt", "w") as hola:
    hola.write("hola mundo")

"""

import pandas

""" Aqui estamos accediendo a los diferentes tipos de archivos que podemos leer con la libre de PANDAS"""
df1 = pandas.read_csv("supermarkets.csv")
df2 = pandas.read_json("supermarkets.json")

""" Cuando vamos a leer un archivo de Excel necesitamos especificar la hoja en especifico que queremos leer, por defecto tenemos la hoja
    numero 0 """
df3 = pandas.read_excel("supermarkets.xlsx", sheet_name = 0)
df4 = pandas.read_csv("supermarkets-commas.txt")

""" A la hora de leer un archivo de texto, siempre lo va a leer como un archivo csv, pero si no esta separado por comas
    tenemos que especificar el separador como esta colocado en la parte de abajo """
df5 = pandas.read_csv("supermarkets-semi-colons.txt", sep=";")

""" Hay algunos archivos en los cuales no tendremos cabeceras, en estos casos podemos hacer dos cosas, la numero uno es indicar que lo lea sin
    cabecera de esta manera
    df4 = pandas.read_csv("supermarkets-commas.txt", header = None)
    """
    

""" Podemos obtener los datos de las diferentes columnas de nuestras bases de datos utilizando el metodo 
    iloc y colocando el punto de inicio y final, como si fuese un rango 

        print(df5.iloc[0:3, 1:3])
"""
