def describir_persona (nombre,**kwargs):
    print(f"Caracteristicas de {nombre}:")
    for clave,valor in kwargs.items():
        print(f"{clave}: {valor}")


print(describir_persona('Diego',Color_ojos = "Verdes", Color_de_Pelo = "Rubio"))