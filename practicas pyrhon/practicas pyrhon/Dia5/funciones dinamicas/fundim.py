"""
Docstring for Dia5.funciones dinamicas.fundim
Aca lo unico que hace es comparar uno de los numero no compara 
en si los tres numeros
"""


def chequear(lista):
    for n in lista:
        if n in range(100,1001):
            return True
    
        else:
            pass 
    return False




resultado =  chequear([25,333,1011])
print (resultado)


#Si queremos que compare uno por uno 

def revisar(lista1):
    lista_all_numbers = []


    for numero in lista1:
        if numero in range(100,1001):
            lista_all_numbers.append(numero)
    
        else:
            pass 
    return lista_all_numbers

resultados = revisar([55,115,333])
print(resultados)