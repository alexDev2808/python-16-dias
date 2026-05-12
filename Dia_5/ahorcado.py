from random import choice

categorias_palabras = {
    "Animales": ["Elefante", "Leon", "Jirafa", "Panda", "Avestruz", "Perro", "Tigre", "Zebra"],
    "Frutas": ["Manzana", "Banana", "Naranja", "Pera", "Uva", "Sandia", "Melon", "Kiwi"],
    "Paises": ["Argentina", "Brasil", "Chile", "Colombia", "Ecuador", "Peru", "Uruguay", "Venezuela"],
    "Series": ["Stranger Things", "Game of Thrones", "Breaking Bad", "The Crown", "The Mandalorian", "Friends", "The Office", "Black Mirror"]
}

def mostrar_palabra(palabra, letras_elegidas):
    for letra in palabra:
        if letra in letras_elegidas:
            print(f"{letra} ", end="")
        else:
            print("__ ", end="")

print("Bienvenido al juego del ahorcado, para comenzar elige una categoria de las siguientes:")
nom_categorias = list(categorias_palabras.keys())
for i, categoria in enumerate(nom_categorias):
    print(f"\t{i + 1}. {categoria}")
categoria_elegida = input("Ingresa el número de tu elección: ")
while not categoria_elegida.isdigit() or int(categoria_elegida) < 1 or int(categoria_elegida) > len(nom_categorias):
    print("Opción inválida. Por favor, ingresa un número válido.")
    categoria_elegida = input("Ingresa el número de tu elección: ")

categoria_elegida = int(categoria_elegida)
palabra_elegida = choice(categorias_palabras[nom_categorias[categoria_elegida - 1]]).lower()
letras_elegidas = []
vidas = 5
adivino = False

print(f"La palabra elegida tiene {len(palabra_elegida)} letras. Suerte!")
mostrar_palabra(palabra_elegida, letras_elegidas)

print("\n\nAhora, ingresa una letra para intentar adivinar la palabra:")
letra_elegida = input("Ingresa una letra: ").lower()

while vidas > 0 and not adivino:
    if letra_elegida in palabra_elegida:
        letras_elegidas.append(letra_elegida)
        mostrar_palabra(palabra_elegida, letras_elegidas)
        print(f"\nBien hecho!. Continua así...")
    else:
        vidas -= 1
        print(f"Letra incorrecta :( Te quedan {vidas} vidas restantes...")
        if vidas == 1:
            print("¡Cuidado! Es tu última oportunidad!!!!.")
        if vidas == 0:
            break
    if all(letra in letras_elegidas for letra in palabra_elegida):
        adivino = True
        print("Felicitaciones!!!. Lo lograste")
    else:
        letra_elegida = input("Ingresa una letra: ").lower()

if not adivino:
    print(f"Game Over. La palabra era: {palabra_elegida.capitalize()}")