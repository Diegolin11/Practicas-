"""
Ayuda contextual y documentacion oficial 


Metodos son pertenecientes  a los objetos que modifican su contenido o nos dan 
su contenido

"""

dic = {'c1':"Diego",'c2':"Musiala"}

valor = dic.popitem()

print(F"{dic}\n{valor}")

palabra =(""",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#""")
words = palabra.removeprefix(",:_#,,,,,,:::____##")
letters = palabra.lstrip(",:_%#")

print(words)
print(letters)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 

frutas.insert(4,"naranja")


print (frutas)

"""
Verifica si los sets a continuación forman conjuntos aislados
 (es decir, que no tienen elementos en común) metodos de los objetos 
 https://docs.python.org/es/3.13/library/stdtypes.html#set.isdisjoint
"""

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print (f"Hay conjuntos aislados {conjuntos_aislados}")

