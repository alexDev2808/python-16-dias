
class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("mu")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        for n in range(0, 3):
            print(f"Bee {n + 1}")

# Polimorfismo: la misma funcion hablar() se comporta diferente dependiendo del objeto que la llame
vaca1 = Vaca("Lola")
oveja1 = Oveja("Nube")

animales_granja = [vaca1, oveja1]
for animal in animales_granja:
    animal.hablar()