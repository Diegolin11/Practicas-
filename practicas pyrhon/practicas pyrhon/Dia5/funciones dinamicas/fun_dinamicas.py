"""
Docstring for Dia5.funciones dinamicas.fun_dinamicas


tambien puedes pasar variables por una funcion 
siempre y cuando no exceda el numero o los parametros 
que ya se han sido establecidos 
"""

def chequear(numero):
    return numero in range(100,1000)


suma = 30+20+11

result2 = chequear(suma)
print (result2)


resultado = chequear(333)
print (resultado)