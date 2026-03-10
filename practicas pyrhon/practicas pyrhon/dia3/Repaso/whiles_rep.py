
name = input("Enter your names ")
monedas = 2500
respuesta = ("s")



while monedas > 0:
    print(f"{name}  tu tienes {monedas} monedas ")
    if respuesta == "s":
        respuesta = input("Quieres seguir jugando s/n ")
        monedas-=500
        if monedas == 0:
            print("Ya no tienes monedas ya no puedes jugar ")
    
    