from random import randint

num_secreto = randint(1, 100)
vidas = 8
ganador = False

print("Adivina el numero. Tienes 8 intentos para lograrlo!")
nombre = input("Escribe tu nombre: ")


while vidas > 0:
    num_elegido = int(input(f"{nombre}, elige un numero entre 1 - 100: "))
    vidas -= 1

    if num_elegido not in range(1, 101):
        print("Eleccion no valida :(")
    elif num_elegido > num_secreto:
        print("Elegiste un numero mayor")
    elif num_elegido < num_secreto:
        print("Elegiste un numero menor")
    else:
        print(f"Felicidades has adivinado!! :) con {vidas} vidas restantes")
        ganador = True
        break

    print(f"Tienes {vidas} vidas restantes")


if (not ganador):
    print("Game Over")
