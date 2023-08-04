import os
import shutil
import send2trash

archivo = open('curso.txt', 'w')
archivo.write("Texto de Prueba")
archivo.close()

print(os.listdir())
# shutil.move('curso.txt', "/home/alexth/PycharmProjects/PythonTotal_16_Dias/extras")

# shutil.rmtree()
send2trash.send2trash('curso.txt')

ruta = '/home/alexth/PycharmProjects/PythonTotal_16_Dias/Dia_6'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {ruta}")
    print(f"Las subcarpetas son:")

    for sub in subcarpeta:
        print(f"\t{sub}")

    print("Los archivos son:")
    for arch in archivo:
        print(f"\t{arch}")

    print('\n')


