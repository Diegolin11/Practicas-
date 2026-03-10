# Abrir el archivo en modo escritura (esto reemplaza el contenido)
archivo = open("Prueba.txt", "w")
archivo.write("Nuevo texto")
archivo.close()

# Volver a abrir el archivo en modo lectura
archivo = open("Prueba.txt", "r")
contenido = archivo.read()
archivo.close()

# Imprimir el contenido
print(contenido)


archivo = open('mi_archivo.txt','a')

archivo.write("\nNuevo inicio de sesión")

archivo.close()
archivo = open('mi_archivo.txt','r')

print(archivo.read())
archivo.close()