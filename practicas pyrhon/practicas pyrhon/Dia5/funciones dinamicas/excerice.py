"""
Docstring for Dia5.funciones dinamicas.excerice
Aca lo hacemos de manera metodica o segmentada

"""


def todos_positivos(lista):
    for numero in lista:
        if numero < 0:
            return False
        else:
            pass
    return True

valor = todos_positivos([30,-2,5])
print(valor)

#Pero si quieres hacerlo usando ALL
"""
Compara toda la lista bajo una determinada condicion
y si no se cumple alguna entonces nos da un falso 
"""

def all_positives(list):
    return all(number > 0 for number in list)


lista1 = all_positives([20,90,100,3])
print(lista1)