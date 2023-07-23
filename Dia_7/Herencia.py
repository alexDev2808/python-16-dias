class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Hola " * 4)


class Pajaro(Animal):

    def __init__(self,edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("Pio " * 4)

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")


print(Animal.__subclasses__())
print(Pajaro.__bases__)

piolin = Pajaro(4, "Amarillo", 30)

piolin.nacer()

print(piolin.color)


class Madre:
    def reir(self):
        print("jaja")

    def hablar(self):
        print("Que tal???")


class Padre:
    def hablar(self):
        print("Hola")


class Hijo(Madre, Padre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()

# Method Orden Resolution
print(Nieto.__mro__)
