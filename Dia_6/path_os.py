import os
from pathlib import Path

# ruta = os.getcwd() # obtener el directorio actual
# os.chdir("/home/alexth/PycharmProjects/PythonTotal_16_Dias/extras") #cambiar a otro directorio
# os.makedirs("/home/alexth/PycharmProjects/PythonTotal_16_Dias/extras/archivos") # crear carpetas nuevas

# archivo = open('nuevo.txt')
# print(archivo.read())

# ruta = '/home/alexth/PycharmProjects/PythonTotal_16_Dias/Dia_6/otro.txt'
#
# elem = os.path.dirname(ruta) # obtener dir del archivo
# elemento = os.path.split(ruta) # obtener tupla para separar el dir y el archivo
# print(elem)
# print(elemento)

# os.rmdir('/home/alexth/PycharmProjects/PythonTotal_16_Dias/extras/archivos')

carpeta = Path('/home/alexth/PycharmProjects/PythonTotal_16_Dias/extras/')
archivo = carpeta / 'nuevo.txt'

mi_archivo = open(archivo)

print(mi_archivo.read())

print(os.path.basename('/home/alexth/PycharmProjects/PythonTotal_16_Dias/extras/nuevo.txt'))
