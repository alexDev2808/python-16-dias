"""
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
"""

def comprobar_0(*args):

    for indice, num in enumerate(args):
        if args[indice] == 0 and args[indice + 1] == 0:
            return True

    return False

print(comprobar_0(6,0,5,1,0,3,0,1))

def se_repite(*args):
    for index, item in enumerate(args):
        if len(args) > index + 1 and item + args[index + 1] == 0:
            return True
    return False

print(se_repite(6,0,5,1,0,3,0,1))