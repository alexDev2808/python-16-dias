from random import choice

lista_palabras_secretas = ["elefante", "leon", "jirafa", "panda", "avestruz", "perro", "tigre", "zebra"]
palabra_elegida = choice(lista_palabras_secretas)
longitud_palabra_elegida = len(palabra_elegida)

guiones = "-" * longitud_palabra_elegida
arr = list(guiones)

print(guiones)


def mostrar_guiones(indices):
    for indice in indices:
        arr[indice] = palabra_elegida[indice]

    arr_palabra = "".join(arr)

    return arr_palabra


def comprobar_letra(letra_elegida):
    indices_letra = []
    for index, letra in enumerate(palabra_elegida):
        if letra == letra_elegida:
            indices_letra.append(index)

    if len(indices_letra) > 0:
        return mostrar_guiones(indices_letra)
    else:
        return 1


def pedir_letra():
    letra_ingresada = input("Ingresa una letra: ").lower()
    palabra_completa = comprobar_letra(letra_ingresada)

    if palabra_completa == 1:
        return 1
    else:
        print(palabra_completa)
        return palabra_completa


def verificador():
    vidas = 6

    while vidas >= 1:
        palabra_completa = pedir_letra()
        if palabra_completa == 1:
            vidas -= 1
            print(f"Te quedan {vidas} restantes...")

        if palabra_completa == palabra_elegida:
            print(f"Felicitaciones!!!. Lo lograste")
            break


verificador()
