class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("El animal ha nacido")
    
    def hablar(self):
        print("El animal emite un sonido")

class Ave:
    def volar(self):
        print("Puedo volar")

    def hablar(self):
        print("Pio pio")

class Perro(Animal):
    def hablar(self):
        print("Guau guau!")

class Gato(Animal):

    def __init__(self, edad, color, altura_brinco):
        super().__init__(edad, color)
        self.altura_brinco = altura_brinco
    def hablar(self):
        print("Miau miau")

    def brincar(self):
        print(f"el gato puede brincar {self.altura_brinco} metros")
    
    def escalar(self, metros):
        print(f"El gato ha escalado {metros} metros")

class AveDomestica(Ave, Animal):
    pass

class Pajaro(AveDomestica):
    pass

# Ver quienes heredan
print(Animal.__subclasses__())

tom = Gato(2, "Gris", 2)
tom.nacer()
tom.hablar()
tom.brincar()
tom.escalar(10)


jerry = Pajaro(1, "Verde")
jerry.hablar()

print(Pajaro.__mro__)