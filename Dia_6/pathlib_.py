from pathlib import Path, PureWindowsPath

carpeta = Path('/home/alexth/PycharmProjects/PythonTotal_16_Dias/Dia_6/texto.txt')

ruta_windows = PureWindowsPath(carpeta)

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print("El directorio no existe")
else:
    print("Genial, existe!!")

print(ruta_windows)
