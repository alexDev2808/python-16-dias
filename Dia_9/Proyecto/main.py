import os
import re
import time
import math
from datetime import datetime


def busqueda(patron, ruta):
    coincidencias = []
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arch in archivo:
            archivo_completo = open(f"{carpeta}/{arch}")
            coincidencia = re.search(patron, archivo_completo.read())
            if coincidencia:
                coincidencias.append([arch, coincidencia.group()])
            archivo_completo.close()

    return coincidencias


def imprimir_resultados(lista_resultados, duracion):
    fecha = datetime.now()
    print("-" * 50)
    print(f'Fecha de búsqueda: [{fecha.strftime("%A, %d %B, %Y")}]')
    print(f'''
    ARCHIVO		    NRO. SERIE
    -------------	----------
    ''')
    for arch, num_serie in lista_resultados:
        print(f"\t{arch}\t{num_serie}")

    print(f"\nNúmeros encontrados: {len(lista_resultados)}")
    print(f"Duración de la búsqueda: {math.ceil(duracion)} segundos")
    print("-" * 50)


def resultados():
    ruta = os.getcwd() + "/Mi_Gran_Directorio"
    patron = r'N\D{3}-\d{5}'
    inicio = time.time()
    resultados_busqueda = busqueda(patron, ruta)
    final = time.time()
    duracion = final - inicio

    imprimir_resultados(resultados_busqueda, duracion)


resultados()
