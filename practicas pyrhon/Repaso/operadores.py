
"""
Vamos a ver los operadores ya sabemos los basicos ahora vamos con el modulo 
que se representa de esta forma // y lo que hace es darnos el sobrante de una division osea que 
no toma en cuenta los decimales
    """
    
x = 8
y = 3

acount = float(input("how much was the bill "))
Friends = int(input("how many friends are going to pay "))
account_friends=(round(acount/Friends,2))

#se usa mas para saber cuando un numero es par si sobra 0 es par
print(f"el modulo de  {x} entre {y} es igual a {x%y}")
print(f"la cuuenta ya divida entres los {Friends} es de {account_friends}")
#Para elevar un numero al cuadrado se usa ** puedes elevarlo al numero que quieras
#y si quieres sacar las raiz cuadrada usas el **0.5
