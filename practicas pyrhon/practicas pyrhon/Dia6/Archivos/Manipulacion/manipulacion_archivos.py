"""
se le llama e/s 
vamos a crear archivos en python
"""
mi_archivo = open('Prueba.txt')

"""
Si usas varias veces readline en lineas separadas
hars que el codigo lea cada una de esas lineas

si usas readlines se imprimira cada linea en forma de una lista 

usar readlines solo en archivos pequeños 
ya que ocupa mucho espacio
"""
#Esto lee nuestro archivo
print (mi_archivo.read())


todas = mi_archivo.readlines()
print(todas)






#es importante dejar esto ya que consume memoria
#es importante cerrarlo
mi_archivo.close

