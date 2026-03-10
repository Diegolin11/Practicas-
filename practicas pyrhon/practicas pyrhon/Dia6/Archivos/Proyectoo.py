import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(),"Recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

def inicio():
    system("cls")
    print('*' * 50)
    print('*' * 5 + " Bienvenido al administrador de recetas "+'*' * 5 )
    print('*' * 50)
    print('\n')
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total de recetas = {contar_recetas(mi_ruta)}")

    
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion: ")
        print("""
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear Categoria Nueva
        [4] - Eliminar categoria
        [5] - Eliminar categoria
        [6] - Salir del Programa """)

        eleccion_menu = input()
    return (eleccion_menu)

menu = 0

if menu == 1:
    #Mostrar categorias
    #elegir categoria
    #Mostrar recetas
    #elegir recetas 
    #leer recetas 
    #volver a inicio 
    pass
elif menu ==2:
    #Mostrar categiruas 
    #Elegir categoria
    #crear receta nueva
    #volver a iniciio
    pass
elif menu == 3:
    #Crear categoria
    #Volver a inicio
    pass
elif menu == 4:
     #Mostrar categorias
    #elegir categoria
    #Mostrar recetas
    #elegir recetas 
    #eliminar recetas 
    #volver a inicio
    pass
elif menu == 5:
    #Mostrar categoria 
    # elegir categoria
    # eliminar categoria
    #  volver a inicio 
    pass
elif menu == 6:
    #Finalizar programa
    pass





