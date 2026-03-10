"""
Docstring for Dia5.InteraccionEntreFunciones.intera_funciones
Puedes hacer que muncahs funciones interactuen 
entre si, ya que podemos usar funciones como parametros para otras funciones

como hacer que un funcion le pase un objeto a 
otro 
"""
from random import shuffle
#lista inicial 
palitos = ['-','--','---','-----']



#Funcion que mezcla los palitos 
def mezcla(lista):
    shuffle(lista)
    return lista




#pedir al usaurio seleccion
def seleccion():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)




#Comprobacion del intento 
def chequear_intento(lista,intento):
    if lista[intento-1]=='-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")
    print(f"Te ha tocado {lista[intento-1]}")

palitos_mezclados = mezcla(palitos)
selec = seleccion()
chequear_intento(palitos_mezclados,selec)