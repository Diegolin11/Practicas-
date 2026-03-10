"""
Docstring for Dia5.funciones dinamicas.ejerciciofun
Hay qu etener cuidado en donde colocamos los returno 
o las variables en general ya que si no estan en el orden en el que deben 
hacemos que el ciclo termine 

un range no es la mejor validacion de numeros en cuanto a 
valores numericos a definir 
"""


def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero > 0 and numero<1000:
            suma += numero
    return suma

        

excercise = suma_menores([20,26,33,1564])

print(excercise)

"""
Acuerdate como inicializas un contador 
"""
def cantidad_pares(lista_numeros1):
    contador = 0
    for numero in lista_numeros1:
        if numero%2 == 0:
            contador += 1
    return contador

pares = cantidad_pares([20,4,8,9])

print(pares)