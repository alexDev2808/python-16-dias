from random import *

aleatorio = randint(1, 50)
print(aleatorio)

aleatorio2 = round(uniform(1, 5), 1)
print(aleatorio2)

aleatorio3 = random()
print(aleatorio3)

colores = ["azul", "rojo", "verde", "morado"]

eleccion = choice(colores)
print(eleccion)

numeros = list(range(1,51, 5))
shuffle(numeros)

print(numeros)
