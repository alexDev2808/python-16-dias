def comprobar_0(*args):

    for indice, num in enumerate(args):
        if args[indice] == 0 and args[indice + 1] == 0:
            return True

    return False

print(comprobar_0(0, 3,5,0, 2,64,21))
