from pathlib import Path
"""
Aca path lib cambia las cosas al ser una libreria 
usas read text pero ya no es neceario abrir ni cerrar 
un archivo
"""
carpeta= Path('C:/Users/diegu/OneDrive/Documentos/muris.txt')
#nos da el nombre del archivo
print(carpeta.name)


#Nos dice de que tipo es el documento
print(carpeta.suffix)

#Nos da el nombre del archivo
print(carpeta.stem)

#Lee el archivo
print(carpeta.read_text())