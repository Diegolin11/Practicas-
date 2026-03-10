
"""
Docstring for Dia6.Archivos.directorios.directorios

os es sistema operativo
path es para usar directyorios 

chdir lo usamos para entrar a otras carpetas peronecesitamos
la ruta y usar dobles slsh porque python los confunde 

makedirs se usa para hacer nuevas carpetas pero tienes que 
poner la ruta completa de donde quieres que se cree esa 
carpeta 
"""
import os

ruta = os.getcwd()

#change directori entra a otras carpetas
ruta2 = os.chdir('C:\\Users\\diegu\\OneDrive\\Documentos')


#sirve para hacer carpetas
ruta3 = os.makedirs('C:\\Users\\diegu\\OneDrive\\Documentos\\Muriel')


#Elimina carpetas
ruta4 = os.rmdir('C:\\Users\\diegu\\OneDrive\\Documentos\\Muriel')
archivo = open('muris.txt')

print(archivo)
print(ruta)