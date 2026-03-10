from pathlib import Path, PureWindowsPath

carpeta= Path('C:/Users/diegu/OneDrive/Documentos/muris.txt')


ruta =PureWindowsPath(carpeta)

print(ruta)


if not carpeta.exists():
    print("Esta carpeta o archivo no existe")
else:
    print("Nice todo good ")