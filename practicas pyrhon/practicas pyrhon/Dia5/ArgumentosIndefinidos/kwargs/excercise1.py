"""Ten en cuemta que tambien pudimos haber usado min y max 
en una lista y despues usar sort """

def devolver_distintos(*numeros):
    suma = 0
    ordenados = sorted(numeros)
    menor = ordenados[0]
    mediano = ordenados[1]
    grande = ordenados[2]
    for numero in numeros:
       suma += numero
    if suma > 15:
        return grande
    elif suma <10:
        return menor
    else:
        return mediano
        
print(devolver_distintos(5,8,2))