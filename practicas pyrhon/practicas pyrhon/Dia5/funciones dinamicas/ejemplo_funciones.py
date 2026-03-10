precios_cafe = [('Capuccino',75),('Frappe',89),('Americano',55)]

def cafe_caro(lista_precios):
    precio_mayor = 0
    cafe_caro = ''

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor=precio
            cafe_caro = cafe
        else:
            pass
    return(cafe_caro,precio_mayor)

coffe = cafe_caro(precios_cafe)
print(coffe)