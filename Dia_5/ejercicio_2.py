"""
Escribe una función
(puedes ponerle cualquier nombre quequieras)
que reciba cualquier palabra como parámetro, y quedevuelva todas sus letras únicas
(sin repetir)
pero en orden alfabético.
Por ejemplo si al invocar esta función pasamos la palabra"entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']
"""

def ordenar_unicas(palabra):
    set_palabra = list(set(palabra))
    set_palabra.sort()
    return set_palabra

print(ordenar_unicas("entretenido"))

# Versión más corta:
def ordenar_unicas(palabra: str) -> list:
    letras_unicas = set(palabra)
    return sorted(letras_unicas)


print(ordenar_unicas("entretenido"))
