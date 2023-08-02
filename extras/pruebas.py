def generador_infinito():
    num = 7
    while True:
        yield num
        num += 7


generador = generador_infinito()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))


def restar_vidas():
    vidas = 3
    yield f"Te quedan {vidas} vidas"

    vidas -= 1
    yield f"Te quedan {vidas} vidas"

    vidas -= 1
    yield f"Te quedan {vidas} vidas"

    yield "Game Over"


perder_vida = restar_vidas()

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))

