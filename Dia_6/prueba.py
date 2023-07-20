from pathlib import Path

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

file = open('registro.txt', 'a')

for index, texto in enumerate(registro_ultima_sesion):
    registro_ultima_sesion[index] = texto + "\t"


file.writelines(registro_ultima_sesion)

file.close()

file = open('registro.txt', 'r')

print(file.read())


def abrir_leer(file):
    archivo = open(file)
    contenido = archivo.read()

    return contenido


print(abrir_leer('otro.txt'))

ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
carpeta = ruta.parents[5]
print(carpeta)
