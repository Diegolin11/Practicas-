from pathlib import Path
"""
*.txt
si usas ese comando solo que mostrara las carpetas o archivos 
que esten dentro de tu ruta 

"**/*.txt" si usas los dos asteriscos diagonal 
otro asterico te mostrara todo lo que tiene la carpeta
incluyendo las subcarpetas
"""
guia3 = Path(Path.home())
guia = Path(Path.home(),"Europa")

guia2 = Path("Europa", "españa","Barcelona", "Sagrada_Familia.txt")

en_europa = guia2.relative_to(Path("Europa"))
en_espania = guia2.relative_to(Path("Europa","españa"))


for txt in Path(guia).glob("**/*.txt"):
    print(txt)