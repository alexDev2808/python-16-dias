
def mi_generador():
    for x in range(1, 6):
        yield x * 10


g = mi_generador()

print(next(g))
print(next(g))
print(next(g))


def generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


gen = generador()
print(next(gen))
print(next(gen))
print(next(gen))

