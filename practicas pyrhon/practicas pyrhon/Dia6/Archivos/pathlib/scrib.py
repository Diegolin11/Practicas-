"""
Docstring for Dia6.Archivos.pathlib.scrib
pathlib se usa para crear o mover archivos 
enumerar archivos 
creear rutas basadas en strings

path se puede usar para unir paths 

ademas de entrar al archivo padre usando parent 
y te va llevar a donde se almacena dicho archivo 
o carpeta en la ruta 

"""

from pathlib import Path


base = Path.home()
guia = Path(base,"España","Madrid",Path("Barcelona","Sagrada_Familia"))

print(base)
print (guia.parent)