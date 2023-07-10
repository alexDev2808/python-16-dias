def ordenar_unicas(palabra):
    set_palabra = list(set(palabra))
    set_palabra.sort()
    return set_palabra


print(ordenar_unicas("entretenido"))
