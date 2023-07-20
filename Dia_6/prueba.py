registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

file = open('registro.txt', 'a')

for index, texto in enumerate(registro_ultima_sesion):
    registro_ultima_sesion[index] = texto + "\t"


file.writelines(registro_ultima_sesion)

file.close()

file = open('registro.txt', 'r')

print(file.read())
