"""
Docstring for Dia5.ArgumentosIndefinidos.ArgIndefinidos
son funciones que reciben varios argumentos o funciones que cuyo numerode argumentos 
son variados en este caso son argumentos 
que quiera pasar el usuario 

y comienza con un *
osea le damos un numero indefinido de parametros

es recomendable usar args pero puede tener cualquier nombre
"""

def suma(*args):
    total = 0

    for arg in args:
        total += arg
    return total

print (suma(11,2003,30,1))

"""
Si quieres hacerlo mas facil pudes usar 
directamente una sum 
"""


def suma1(*argumentos):
    return sum(argumentos)

print (suma1(2002,12,10))