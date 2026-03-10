
"""hahs
slicing a esto asi se le llama a la extraccion de strings 
en este caso la primera parte nos dice de donde empieza a tomar y la segunda nos dice hasta donde tomara 
y si colocamos un tercer numero este ira salteando de letra a letra en base al numero especificado
[3:40:2] y si la colocas en negativo ira tomando de izquierda a derecha 
"""

texto = ("Benditos sean los que no tiene memoria porque a ellos petence el mundo de los olvidos")
extraer = texto[3:50:2]
invertida = texto[::-1]
print(f"la primera cadena queda\n {extraer}\n y la segunda cadena queda\n {invertida}")