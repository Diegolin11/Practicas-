
"""
enumarate nos ayuda a como acceder a los indices de una lista 
en este caso enumera una lista 
"""

lista=('a','b','c')


for item in enumerate(lista):
    print(item)

"""
O puedes enumerar un rango de donde a donde quieras que  vaya esto es un loop
"""
for numero in enumerate(range(1,26)):
    print(numero)

mis_tuples = list(enumerate(lista))
print(mis_tuples[1][1])

    