#Primero importamos la libreria que incluye las expresiones regulares.
import re
#Ahora creamos un objeto con las caracteristicas
#las expresiones regulares de un numero de telefono.
phoneNumberPattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberPattern.search('My number is 415-555-4242.')
print(f'Phone Number found: {mo.group()}')
