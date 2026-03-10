"""
Docstring for Dia5.ArgumentosIndefinidos.kwargs.kwargs
kwargsk key word args

se usa para darle un nombre a cada argumento a traves de un diccionario
y se pueden mezclar ambos
"""

def suma(**kwargs):

    kwargs = input("Aigna un nombre seguido de un numero")

    total = 0

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(m=30, u=1, r=200, i=3))

