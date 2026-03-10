

nombres = ['Juan','Jorge','Adrian','Arsenico','Diego','Francisco','Daniel']
for indice, nombre in enumerate(nombres):
    if nombre.startswith('D'):
        print(f"este nombre inicia con D {nombre}")
    else:
        print(f"Este nombre: {nombre} esta en la posicion\n {indice}")


words = "Python"

#Aca lo que hace es que hace una lista con la palabra words y depsues la enumera letra por letra 
lista_indice = list(enumerate(words))
print(lista_indice)


nombres2 = ['Muriel','Michelle','Juan','Michael','Papá','Adis','Atenco']
#Aca lo que puedes pedir ya sea el item o el nombre si pides el item te dara la posicon
for item, name in enumerate(nombres2):
    if name.startswith('A'):
        print(item)

