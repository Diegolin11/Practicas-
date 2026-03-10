def ceros_vecinos(*args):

    contador = 0
    for numero in args:
        if contador + 1 == len(args):
            return False
        elif args[contador]== 0 and args[contador + 1]==0:
            return True
        else:
            contador += 1
    return False

print(ceros_vecinos(3,5,6,4,2,56,2,63,35,0))