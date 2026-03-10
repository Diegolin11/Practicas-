def devolver_distintos(palabra):
    words =""


    for  letra in palabra:
        if letra not in words:
            words += letra

    return sorted(words)
    
print (devolver_distintos("entretenido"))

def letters_unique(palabras):
    
    #los sets guardan valores unicos
    mi_set = set()

    for letter in palabras:
        mi_set.add(letter)

    mi_lista = list(mi_set)
    mi_lista.sort()

    return mi_lista

print(letters_unique("entretenido"))