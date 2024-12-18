"""
Pandas es una biblioteca de Python para analisis y visualizacion de datos 
la cual es bastante util, asi que empecemos por lo basico, importemos la 
libreria 
"""

import pandas

"""
Hay que tener en cuenta que tenemos que tener los archivos que vamos a analizar
en la misma carpeta que el script de analisis de datos, por alguna razon
que desconozco no logro hacer que detecte los archivos cuando se encuentran
en otras carpetas, como sea, instauremos nuestra primer cuadro de datos, o 
como decimos en pandas, DATAFRAME
"""

df1 = pandas.read_csv("supermarkets.csv")

""" 
Un documento CSV es un documento Comma Separated Values, simplemente tiene los valores
separados por una coma y asi forma las columnas y demas, es muy intuitivo, ademas, no
difiere mucho de un archivo de texto, de hecho si quisieramos cargar un archivo de 
texto que tuviera esta misma presentacion, podriamos hacerlo facilmente con el mismo
comando de la siguiente manera:
"""

df2 = pandas.read_csv("supermarkets-commas.txt")

"""
Y si quisieses cargar un archivo de texto que no esta separado por comas, simplemente
usa el parametro sep de la siguiente manera: 
"""

df3 = pandas.read_csv("supermarkets-semi-colons.txt", sep=";")

""" Como veras, nada complicado, eso si, para poder cargar archivos de Excel necesitaremos
dos modulos mas del PIP, como lo son openpyxl para cargar archivos Excel mas recientes
y xlrd para cargar archivos Excel viejos, para cargarlos lo podemos hacer de la siguiente
manera:
"""

df4 = pandas.read_excel("supermarkets.xlsx")

"""
Por ultimo pero no menos importante tambien contamos con capacidad para cargar archivos
JSON, que son el tipo de archivo con el cual se mueve la informacion en la red, basicamente.
"""

df5 = pandas.read_json("supermarkets.json")

"""
Tambien tenemos una manera de cambiar la cabecera de los daraframe con un simple comando:
"""

#df6 = pandas.read_csv("supermarkets.csv", header = None)

"""
Y ya con esto no tendriamos una cabecera en el archivo, si queremos agregar una cabecera
propia tendriamos que ingresar una lista de strings en la asignacion, como se muestra a 
continuacion:
"""

#df6.columns = ["A", "B", "C", "D", "E", "F", "G"]

"""
Tambien podemos cambiar la columna de indice de la siguiente manera:
"""

df4.set_index("ID", inplace=True)

"""
Este metodo no modifica el objeto original sino que devuelve un nuevo objeto
de tipo Dataframe, vease una nueva dataframe, donde el nuevo indice sera la
columna que le hayamos pasado como valor, la forma en que podemos hacer que sea
una modificacion directa al objeto original es simplemente colocando como True
el parametro inplace, pero hay que tener cuidado, porque si no utilizamos el 
parametro drop=False, perderemos el anterior indice irremediablemente.
"""

"""
Como filtrar informacion de los dataframes, pues en un pricipio podemos utilizar
el metodo loc en uno de los dataframes, nuevamente este devolvera las posiciones
que le estamos solicitando y no modificara el elemeneto original, y para encontrar
las posiciones que buscamos lo podemos hacer mediante una indexacion, como si fuese 
un matriz, pero en lugar de los numero utilizaremos los nombres de nuestras filas y
columnas, tambien podemos utilizar rangos:
"""

#print(df4.loc["1":"3", "Address":"City"])
#print(df4.loc["3", "City"])

"""
Con el metodo iloc hacemos exactamente lo mismo pero tratamos las filas y las columnas
como si fuesen las de una matriz y no tenemos la necesidad de sabernos los nombres
de las columans con las que estamas tratando
"""
