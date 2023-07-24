class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuu")


class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")


vaca_1 = Vaca("Aurora")
oveja_1 = Oveja("Nube")


animales = [vaca_1, oveja_1]

for animal in animales:
    animal.hablar()

def animal_habla(animal):
    animal.hablar()


animal_habla(vaca_1)
animal_habla(oveja_1)
