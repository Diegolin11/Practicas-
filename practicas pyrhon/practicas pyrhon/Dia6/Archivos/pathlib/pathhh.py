"""path nos ayuda a abrir cualquier ruta 
no imprta el os en el que estemos trabajando 

el slash esta ahora invertido / asi es como lo lee 
mac y linux
"""

from pathlib import Path

carpeta = Path('C:/Users/diegu/OneDrive/Documentos')
archivo = carpeta / 'muris.txt'

mi_archivo = open(archivo)

print(mi_archivo)