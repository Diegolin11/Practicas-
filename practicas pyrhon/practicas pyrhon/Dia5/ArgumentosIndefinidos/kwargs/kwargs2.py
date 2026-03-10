def cantidad_atributos(**kwargs):
    return len(kwargs)

def lista_atributos(**kwargs2):
    return list(kwargs2.values())
    
print (lista_atributos(ca = 33, te=10, du=1))
