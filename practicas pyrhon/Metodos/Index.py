
"""index nos ayuda a saber donde esta determiando caracter o palabras 
pero si no esta lo que buscas nos dara error y puedes poner de donde a donde va a buscar de 
esta manera ("a",1,30)en las comillas va lo que buscaras y en las comas especifico de donde a donde 
buscara 

lo mismo hace rindex solo que ahora busca de izquierda a derecha
    """
    
frase =("Posdata te busque en todos los lugares a los que soliamos ir esperando que tu tambien me buscaras en alguno de ellos")
busqueda = frase.index("n",0,50)
print(busqueda)