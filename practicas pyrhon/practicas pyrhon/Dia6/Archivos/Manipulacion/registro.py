
archivo = open('registro.txt', 'w')

archivo.write("\n")
archivo.close()


archivo = open('registro.txt', 'a')

registro_ultima_sesion = [
    "Federico\t",
    "20/12/2021\t",
    "08:17:32 hs\t",
    "Sin errores de carga"
]

archivo.writelines(registro_ultima_sesion)
archivo.close()

archivo = open('registro.txt', 'r')
print(archivo.read())
archivo.close()
