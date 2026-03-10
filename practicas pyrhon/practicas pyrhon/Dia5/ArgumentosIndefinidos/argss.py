def suma_cuadrados(*args):
    cuadrado = [numero **2 for numero in args]
    suma = sum(numero for numero in cuadrado)
    return suma

print(suma_cuadrados(2,4,6))



"""Para tomar valores absolutos es decir
que no importa el signo que tengan usamos abs"""
def suma_absolutos(*args2):
    positivos = (abs(numero) for numero in args2)
    suma = sum(numero for numero in positivos)
    return suma

print(suma_absolutos(2,-4,6,-2))


""" Vamos a usar isinstance
nos a ayuda a verificar si un objeto o variable es de un tipo 
en especifico"""
def numeros_persona(*args):
    nombre = []
    numeros = []
    for elemento in args:
        if isinstance(elemento, str):
            nombre.append(elemento)
        elif isinstance(elemento, int):
            numeros.append(elemento)
    
    suma = sum(numero for numero in numeros)
    return f"{nombre}, la suma de tus números es {suma}"

print(numeros_persona('Diego',30,1,2003))

"""
Osea este codigo esta bien solo que nos complica mucho 
en este caso en una funcion puedes usar varias variables
incluyendo args 

que es algo que no sabia asi que como ya sabemos que la 
primervariable siempre va a ser un nombre la asiganamos de una vez 
en lugar de buscarla
"""
def numeros_persona(nombre, *numeros):
    suma = sum(numeros)
    return f"{nombre}, la suma de tus números es {suma}"

print(numeros_persona('Diego', 30, 1, 2003))