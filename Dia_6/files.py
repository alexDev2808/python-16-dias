mi_archivo = open('texto.txt')


# print(mi_archivo.read())
# una_linea = mi_archivo.readline()
#
# print(una_linea.upper())

for linea in mi_archivo:
    print(f"Aqui dice: {linea}")

mi_archivo.close()
