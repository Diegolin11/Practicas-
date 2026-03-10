frase = (input("Ingres un pequeño poema en el que tu quieras "))
frase2 = frase.split()
poema = frase.index("n",0,50)
encuentra = frase.find("Jade")
extraer = frase[2:20:]
#Metodo de extraer partes de texto

a = "Jade"
b = "Morales"
c = "Quiero"
d = "Espera un poco mas solo un instante"
e = " ".join([a,b,c,d]).replace("Jade","Niña").replace("Morales","Te")
print(f"{e}")
print(f"{frase2}\n")
print(f"la letra N se encuntra en el lugar {poema}\n Y la palbra Jade se encuntra apartir de {encuentra}")
print(extraer)
print("Muriel" in frase)