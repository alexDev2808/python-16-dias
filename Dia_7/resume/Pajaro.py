
class Pajaro:
    alas = True
    cantidad_alas = 2

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # metodos de instancia
    def piar(self):
        return f"pio pio. Soy un {self.especie} de color {self.color}"
    
    def volar(self, metros):
        print(self.piar())
        return f"El pajaro ha volado {metros} metros\n{self.piar()}"
    
    def cambiar_color(self, color="Negro"):
        self.color = color
        print(f"Ahora el color del pajaro es {self.color}")


    # metodos de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"El pajaro pone {cantidad} huevos!")
    
    @classmethod
    def contar_alas(cls):
        # no se puede acceder a las propiedades o metodos de instancia
        if cls.alas:
            print(f"El pajaro tiene {cls.cantidad_alas} alas")
            cls.alas = False
        else:
            print("El pajaro no tiene alas")

    @staticmethod
    def mirar():
        print("El pajaro ha comenzado a mirar!")

    

# metodos de instancia
pajaro1 = Pajaro("rojo", "cardenal")
print(pajaro1.volar(10))
pajaro1.cambiar_color()


# metodos de clase
Pajaro.poner_huevos(3)
Pajaro.contar_alas()
Pajaro.contar_alas()

Pajaro.mirar()



# metodos estaticos


