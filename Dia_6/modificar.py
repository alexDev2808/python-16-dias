# a agrega los cambios al archivo al final
file = open('texto.txt', 'w') # w sobreescribe el archivo completo
file.write("Nuevo texto\n")
file.write('''Hola
Mundo
Aqui 
estoy
 ''')

file.writelines(["Alexis", "Hola", "Python"])
file.close()
