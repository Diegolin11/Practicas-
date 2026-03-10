
"""Podemos usar split paraa volver una cadena de texto en una lista de palabras """
texto = ("Pd:Muri Te busque en todos los lugares en los que soliamos platicar para ver si algun día tu tambien me buscabas")

#De igual manera si usas los corchetes de bsuqueda antes del .upper o lower puedes colocar
#de donde a donde toma las letras que hara en mayusculas o minusculas 

mayus = texto.upper()
minus = texto.lower()

#la diferencia de index con find es que si la letra o palabra a buscar no esta no arrojara error solo dira -1
encontrar = texto.find("Muri")

print(f"la linea de texto en mayusculas queda como\n {mayus}\n y la cadena en mminisculas queda\n {minus}\n y la palabra a encontras es\n {encontrar}")


#la separacion en la lista split es los espacios aunque pudes usar una letra como separador ("t")
lista = texto.split()
print(lista)

#Ahora vamos con Join que lo que hace es unir cadenas de texto a partir de convertirlo en una lista
a = ("Hola")
b = ("Como estas")
c = ("Karo")
#En este caso como es una lista tenemos que usar los corchetes
d = " ".join([a,b,c])

print(type(d))
print(d)

#Por ultimo esta replace que lo que hace es remplazar una cadena de texto o solo letras 
remplaza = texto.replace("Muri","Muriel Gomez").replace("Pd","Posdata")
print(f"El texto remplazado queda asi\n {remplaza}")
print(type(lista))

