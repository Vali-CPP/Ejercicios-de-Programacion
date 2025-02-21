""" Como sabras en los diferentes sistemas de archivos de los 3 principales sistemas operativos con lo que contamos hay una ligera diferencia, el slash que se utilizar para dividir las carpetas en las direcciones de los rachivos es diferente, back slash (\) para Windows y forward slash (/) para Linux y Mac, en la libreria OS de Python tenemos una forma de crear direcciones de archivos absolutas de manera independiente del sistema operativo con el metodo join de la clase path"
"""

import os

os.path.join("usr","bin", "spam")

"""
    Esta linea nos devolvera una direccion de archivos dependiendo del sistema, pero siempre que los strings que se le pasen esten bien, no hay ningun problema
"""


