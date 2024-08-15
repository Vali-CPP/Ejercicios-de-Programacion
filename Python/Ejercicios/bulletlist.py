#! /bin/python3
# A simple bullet list generator for markdown format

import pyperclip

texto = pyperclip.paste()

lineas = texto.split('\n')

for i in range(len(lineas)):
    lineas[i] = " - " + lineas[i]

texto = "\n".join(lineas)

pyperclip.copy(texto)
