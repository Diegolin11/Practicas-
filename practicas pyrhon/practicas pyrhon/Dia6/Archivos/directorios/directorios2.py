import os

"""
tambien puedes pedir el nombre de base el archivo o la carpeta en la que }
estas trabajando de esta manera

"""

ruta = 'C:\\Users\\diegu\\OneDrive\\Documentos\\muris.txt'

elemento = os.path.basename(ruta)
elemento2 = os.path.dirname(ruta)
elemento3 = os.path.split(ruta)
print(elemento)