# -*- coding: utf-8 -*-
from pathlib import Path

"""Abrir y manipular archivos"""

def leer_archivo():
    # Obtener la ruta del archivo en la misma carpeta que este script
    archivo_path = Path(__file__).parent / "file_1.txt"
    mi_archivo = open(archivo_path, "r", encoding="utf-8")  # Abre con encoding UTF-8
    # print(type(mi_archivo))
    #print("Contenido completo del archivo:")
    #print(mi_archivo.read())  # Lee el contenido del archivo

    print("\nContenido del archivo línea por línea:")
    for linea in mi_archivo.readlines():  # Lee el archivo línea por línea
        print(linea.strip())  # Imprime cada línea sin espacios adicionales


    mi_archivo.close()  # Cierra el archivo

def escribir_archivo(texto:str | None = None):
    archivo_path = Path(__file__).parent / "file_2.txt"
    # "w" para escribir (sobrescribe el archivo), "a" para agregar al final del archivo
    mi_archivo = open(archivo_path, "a", encoding="utf-8")  # Abre el archivo en modo de escritura (append)
    if texto:
        mi_archivo.write(texto)
    else:
        mi_archivo.write("Hola Mundo!")
        mi_archivo.write("\n... desde Python!")

    mi_archivo.close()
    
def main():
    leer_archivo()
    escribir_archivo()
    escribir_archivo("Me encanta Python, es genial!")  # Agrega texto al archivo


if __name__ == "__main__":
    main()