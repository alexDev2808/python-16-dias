'''
Comentario multilinea
def para crear funciones
puede recibir parametros
'''

def saludar_persona(nombre):
    print(f"Hola {nombre}")

def multiplicar(simbolo, veces):
    return simbolo * veces

def chequear_3_cifras(lista):

    lista_num_3_cifras = []
    for elem in lista:
        if int(elem) in range(100, 1000):
            lista_num_3_cifras.append(elem)
        else:
            pass

    return lista_num_3_cifras

nombre = saludar_persona(input("Escribe tu nombre: "))

print(multiplicar('#',  40))

lista_numeros = input("Escribe una lista de numeros separados por un espacio: ").split(" ")

lista_3_cifras = chequear_3_cifras(lista_numeros)

if lista_3_cifras:
    print(f"Si hay un numero de 3 cifras es {lista_3_cifras[0]}")
else:
    print("No hay :( ")
