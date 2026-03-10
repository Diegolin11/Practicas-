

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
for elemento in registro_ultima_sesion:
    print(f"\t{elemento}")


archivo = open('registro.txt','a')

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
for elemento in registro_ultima_sesion:
    archivo.writelines(f"\t{elemento}")

archivo.close()

archivo = open('registro.txt','r')

print(archivo.read())

archivo.close()
