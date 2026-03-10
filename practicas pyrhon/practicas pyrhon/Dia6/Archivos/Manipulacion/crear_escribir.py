"""
Docstring for Dia6.crear_escribir
si no pones un argumento al abrir el archivo se coloca en lectura
r lectura
w escritura pero borra lo que tenga el archivo
a deja escribir al final del documento


wrtitelines te deja escribir varias cosas en manera de lista

"""

archivo = open('Prueba.txt','w')

archivo.write("Hola Como estas")

print(archivo.read())
