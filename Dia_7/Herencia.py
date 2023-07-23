class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print("Este animal ha nacido")


class Pajaro(Animal):
    pass


print(Animal.__subclasses__())
print(Pajaro.__bases__)

piolin = Pajaro(4, "Amarillo")

piolin.nacer()

print(piolin.color)
