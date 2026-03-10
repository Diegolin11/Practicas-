from random import *

def lanzar_moneda():
    moneda = ['Cara','Cruz']
    aleatorio = choice(moneda)
    return aleatorio

lista_numero = [1,2,3,4]
def probar_suerte(aleatorio,lista_numero):
    if aleatorio == 'Cara':
        lista_numero.clear()
        return (f"La lista se autodestruira {lista_numero}")
    elif aleatorio == 'Cruz':
        return (f"La lista fue salvada {lista_numero}")
    
resultado_moneda = lanzar_moneda()
resultado = probar_suerte(resultado_moneda,lista_numero)

print(f"La moneda cayo {resultado_moneda} {resultado}")