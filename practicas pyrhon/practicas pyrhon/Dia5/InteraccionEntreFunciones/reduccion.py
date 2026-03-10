
lista_numero = ([10,12,2003,30,1,2003])

def reducir_lista(lista_numero):
    lista1=[]
    for numero in lista_numero:
        if numero not in lista1:
            lista1.append(numero)
    
    maximo = max(lista1)
    lista1.remove(maximo)
    return lista1


def promedio(lista1):
    prom = 0
    largo = len(lista1)
    #Siempre que se va a sumar se coloca la vairable a la que se acumula
    #y despues que va a sumar o restar o sea de donde va a sumar
    for elemento in lista1:
        prom += elemento
    
    division = prom/largo
    return division

        